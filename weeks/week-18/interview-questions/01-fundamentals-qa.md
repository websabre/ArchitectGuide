# Week 18 — Fundamentals Q&A

> Q001–Q030: Premium format (Week 1 quality).
> Cross-reference: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: EC2 vs Lambda vs Fargate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

When EC2 vs Lambda vs Fargate for .NET workload?

### Short Answer (30 seconds)

EC2: full control, steady traffic, Windows/.NET Framework legacy. Lambda: event-driven, spiky, short requests. Fargate: containers without managing EC2 — middle ground for .NET Core APIs.

### Detailed Answer (3–5 minutes)

**Lambda:** API Gateway + Lambda for low-traffic internal APIs; watch cold start and 15min limit.

**Fargate:** ECS/EKS serverless tasks — .NET 8 containers, no EC2 patching.

**EC2:** Always-on high RPS, WebSockets, custom AMIs.

**Architect:** Default Fargate/ECS for containerized .NET Core; Lambda for async processors.

### Architecture Perspective

Compute choice drives ops model and cost.

### Follow-up Questions

1. **Lambda .NET cold start? — Provisioned concurrency for latency-sensitive.**
2. **App Runner? — Simpler than ECS for container web apps.**

### Common Mistakes in Interviews

- Lambda for steady 10K RPS API
- EC2 for every cron job
- Ignoring Lambda concurrency limits

---

## Q002: ECS vs EKS Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

Team wants Kubernetes. You have 3 microservices and 4 developers. Recommendation?

### Short Answer (30 seconds)

ECS Fargate unless team has K8s operational maturity. EKS justified at 10+ services, multi-cloud K8s skill, or service mesh needs.

### Detailed Answer (3–5 minutes)

**ECS pros:** AWS-native, simpler, lower ops overhead.

**EKS pros:** Portable K8s, rich ecosystem, multi-cloud.

**Architect:** Honest assessment — EKS tax is real (control plane cost, upgrades, add-ons). Start ECS; migrate to EKS when triggers hit.

### Architecture Perspective

Right-sizing orchestration is senior architect judgment.

### Follow-up Questions

1. **EKS Fargate vs EC2 nodes? — Fargate reduces node ops; EC2 for GPU/custom.**
2. **ECS Service Connect? — Service discovery without full mesh.**

### Common Mistakes in Interviews

- EKS for 2 services because 'industry standard'
- No cluster upgrade plan
- Developers running kubectl to prod

---

## Q003: Lambda Cold Starts and Provisioned Concurrency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

User-facing API on Lambda has 2s cold starts. Options?

### Short Answer (30 seconds)

Provisioned concurrency (cost), SnapStart for Java (not .NET), reduce package size, ARM Graviton, avoid VPC unless required, API Gateway caching, or move steady traffic to Fargate.

### Detailed Answer (3–5 minutes)

**Architect analysis:** Cold start acceptable for async; not for sync user path at P99.

**Mitigations:** Minimize init code, reuse HttpClient, lazy DI, smaller deployment package.

**Trade-off:** Provisioned concurrency = always-on cost — compare to Fargate baseline.

### Architecture Perspective

Serverless latency requires architect-level trade-offs.

### Follow-up Questions

1. **Lambda in VPC? — Adds ENI cold start — use VPC only when required.**
2. **Lambda vs Lambda@Edge? — Edge for CloudFront-triggered only.**

### Common Mistakes in Interviews

- Provisioned concurrency on all functions blindly
- Heavy DI container in Lambda init
- Ignore P99 latency in SLOs

---

## Q004: Auto Scaling Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Design ASG for variable traffic .NET API on EC2?

### Short Answer (30 seconds)

ALB target tracking on request count or CPU; min 2 across AZs; scale-out fast, scale-in slow with cooldown; health checks on `/health`.

### Detailed Answer (3–5 minutes)

**Policies:** Target tracking preferred over step scaling for web.

**Architect:** Warm pool for faster scale-out on known events (Black Friday).

**Mixed instances:** On-Demand base + Spot for burst capacity.

### Architecture Perspective

ASG design ties to reliability and cost.

### Follow-up Questions

1. **Predictive scaling? — ML-based pre-scale before demand.**
2. **Lifecycle hooks? — Graceful drain before terminate.**

### Common Mistakes in Interviews

- Single instance ASG in prod
- Scale-in kills instances mid-request
- No ALB health check grace period

---

## Q005: Elastic Beanstalk When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Occasional |

### Question

When still recommend Elastic Beanstalk?

### Short Answer (30 seconds)

Rapid .NET deploy without container/K8s ops; small teams; platform handles capacity/provisioning. Declining vs ECS/Fargate for new greenfield.

### Detailed Answer (3–5 minutes)

**Good fit:** Internal tools, prototypes, teams avoiding Docker.

**Avoid:** Complex microservices, custom networking, multi-region active-active.

**Architect:** Honest — Beanstalk is underrated for simple web apps; not default for microservices.

### Architecture Perspective

Knowing when NOT to use K8s shows maturity.

### Follow-up Questions

1. **Beanstalk .NET on Linux? — Supported — prefer over Windows workers for cost.**
2. **Blue/green on Beanstalk? — Swap environment URLs.**

### Common Mistakes in Interviews

- Beanstalk for 20 microservices
- Ignore platform deprecation notices
- No environment separation

---

## Q006: API Gateway + Lambda Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

Design public REST API with API Gateway and Lambda. Key decisions?

### Short Answer (30 seconds)

HTTP API vs REST API (cost/features), JWT authorizer vs Cognito, throttling per client, request validation, Lambda integration timeout 29s, structured logging, X-Ray tracing.

### Detailed Answer (3–5 minutes)

**Architect checklist:**
- WAF on API Gateway for public APIs
- Usage plans + API keys for partners
- Idempotency for POST from clients
- DLQ on async invocations

**Alternative:** ALB + Fargate if WebSockets or long requests.

### Architecture Perspective

API Gateway is edge architecture decision.

### Follow-up Questions

1. **HTTP API vs REST API? — HTTP API cheaper; REST API more features.**
2. **Lambda response streaming? — Large payloads — know limits.**

### Common Mistakes in Interviews

- No throttling on public API
- 29s timeout on long-running sync work
- Secrets in Lambda environment plaintext

---

## Q007: ALB vs NLB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Application Load Balancer vs Network Load Balancer?

### Short Answer (30 seconds)

ALB: Layer 7, path/host routing, HTTP/HTTPS, WebSockets, Lambda targets. NLB: Layer 4, ultra-low latency, static IP, TCP/UDP, millions RPS.

### Detailed Answer (3–5 minutes)

**ALB:** Default for .NET HTTP APIs behind ECS/EC2.

**NLB:** Gaming, IoT, TLS passthrough, extreme performance.

**Architect:** ALB + WAF for public web; NLB for non-HTTP protocols.

### Architecture Perspective

Load balancer choice affects security and routing.

### Follow-up Questions

1. **Gateway Load Balancer? — Inline security appliances — niche.**
2. **Cross-zone load balancing cost? — NLB charges per AZ — model in TCO.**

### Common Mistakes in Interviews

- NLB for standard REST API unnecessarily
- ALB for raw TCP gaming traffic
- No connection draining on deploy

---

## Q008: Graviton (ARM) Instances

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

When recommend Graviton for .NET workloads?

### Short Answer (30 seconds)

.NET 8+ runs well on ARM64. Graviton3 offers better price-performance for Linux containers and Lambda. Validate with load test before migration.

### Detailed Answer (3–5 minutes)

**Benefits:** ~20-40% better price-performance for compatible workloads.

**Caveats:** Native dependencies must support ARM; Windows Graviton limited.

**Architect:** Pilot on nonprod; benchmark P99 latency and cost; Savings Plans after validation.

### Architecture Perspective

Hardware choice is architect cost/perf lever.

### Follow-up Questions

1. **Lambda Graviton? — arm64 architecture flag.**
2. **RDS Graviton? — Supported for many engines.**

### Common Mistakes in Interviews

- Migrate without compatibility testing
- Assume all NuGet packages support ARM
- Ignore performance regression in P99

---

## Q009: Spot vs On-Demand Instances

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cost |
| **Frequency** | Common |

### Question

When use Spot instances in production architecture?

### Short Answer (30 seconds)

Fault-tolerant batch, CI runners, K8s node groups with diversification, render farms — NOT single-instance stateful primary without interruption handling.

### Detailed Answer (3–5 minutes)

**Patterns:** Spot Fleet, mixed On-Demand + Spot ASG, Karpenter Spot provisioning.

**Architect:** 2-minute interruption notice — workloads must checkpoint or drain.

### Architecture Perspective

Spot is cost lever with architect safeguards.

### Follow-up Questions

1. **Spot placement score? — Choose pools with capacity.**
2. **Capacity Rebalancing? — ASG replaces at-risk Spot instances.**

### Common Mistakes in Interviews

- Spot for single-AZ primary database
- No interruption handling
- One instance type only — capacity risk

---

## Q010: Serverless Anti-Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Common serverless anti-patterns you've seen?

### Short Answer (30 seconds)

Lambda for long sync chains, chatty Lambda-to-Lambda without queue, huge deployment packages, VPC everything, no DLQ, treating DynamoDB like SQL, ignoring concurrency account limits.

### Detailed Answer (3–5 minutes)

**Architect remediation:**
- Step Functions for orchestration
- SQS between functions
- Right-size memory (affects CPU)
- Reserved concurrency on critical paths only

**When to exit serverless:** Steady high RPS — Fargate often cheaper.

### Architecture Perspective

Knowing anti-patterns shows production experience.

### Follow-up Questions

1. **Lambda monolith? — 10K lines in one function — split by trigger.**
2. **Serverless framework lock-in? — Prefer SAM/CDK for AWS-native.**

### Common Mistakes in Interviews

- 15-function sync chain for checkout
- No idempotency on SQS consumer
- Ignore account concurrency soft limits

---

## Q011: EC2 Instance Type Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

Choose EC2 family for .NET API workload?

### Short Answer (30 seconds)

General purpose m7g/m7i for APIs. Compute optimized c7 for CPU-heavy. Memory r7 for large in-memory cache. Graviton if ARM-validated.

### Detailed Answer (3–5 minutes)

**Architect:** Start m-family right-sized; benchmark before jumping to xlarge. Burst T-family dev only.

**Rightsizing:** Compute Optimizer recommendations monthly.

### Architecture Perspective

Instance selection drives cost and performance.

### Follow-up Questions

1. **Metal instances? — Bare metal niche compliance.**
2. **Dedicated hosts? — License compliance Oracle/SQL legacy.**

### Common Mistakes in Interviews

- largest instance without profiling
- T3 unlimited prod API surprise bill
- Wrong architecture ARM incompatible

---

## Q012: Launch Templates and AMIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Golden AMI vs launch template user data?

### Short Answer (30 seconds)

Golden AMI: baked dependencies fast boot. Launch template: cloud-init installs latest on boot — more flexible.

### Detailed Answer (3–5 minutes)

**Architect:** Packer builds golden AMI in CI; ASG uses launch template version. Immutable infrastructure pattern.

### Architecture Perspective

Image strategy affects deploy speed and drift.

### Follow-up Questions

1. **EC2 Image Builder? — Managed pipeline for AMIs.**
2. **Launch template versioning? — Rollback ASG to prior version.**

### Common Mistakes in Interviews

- Manual SSH install packages
- No AMI refresh patching
- Mutable servers pet model

---

## Q013: ECS Task Definitions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Containers |
| **Frequency** | Common |

### Question

Design ECS task definition for .NET container?

### Short Answer (30 seconds)

CPU/memory limits, awsvpc networking, secrets from Secrets Manager, health check, logging to awslogs driver.

### Detailed Answer (3–5 minutes)

**Architect:** Task role vs execution role — execution pulls image/secrets; task role app AWS API access.

**Sidecar:** ADOT collector for traces.

### Architecture Perspective

Task definition is container deploy contract.

### Follow-up Questions

1. **Fargate vs EC2 launch type? — Fargate serverless; EC2 more control.**
2. **Task placement constraints? — GPU instance type.**

### Common Mistakes in Interviews

- Secrets in task definition plaintext
- No health check container
- Task role AdministratorAccess

---

## Q014: EKS Cluster Autoscaler

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

EKS cluster autoscaler vs Karpenter?

### Short Answer (30 seconds)

Cluster Autoscaler scales ASG node groups. Karpenter provisions nodes dynamically per pod requirements — faster scale.

### Detailed Answer (3–5 minutes)

**Architect:** Karpenter preferred greenfield EKS .NET workloads. Define NodePool limits for cost cap.

**Watch:** Pod disruption budgets during scale-in.

### Architecture Perspective

Node autoscaling prevents pending pods stuck.

### Follow-up Questions

1. **Karpenter consolidation? — Remove empty nodes.**
2. **Multiple node groups? — Spot + on-demand split.**

### Common Mistakes in Interviews

- Fixed 10 nodes always
- No PDB on critical deployment
- Autoscaler without resource requests

---

## Q015: Lambda Layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

When use Lambda layers for .NET?

### Short Answer (30 seconds)

Share dependencies across functions — common libraries, native deps, ADOT layer — reduce deployment package size.

### Detailed Answer (3–5 minutes)

**Limit:** 5 layers per function, 250MB unzipped total.

**Architect:** Layer for approved internal SDK version — central update.

### Architecture Perspective

Layers manage shared dependency versions.

### Follow-up Questions

1. **Layer versioning? — Pin function to layer version.**
2. **.NET layer custom runtime? — Native deps packaging.**

### Common Mistakes in Interviews

- Duplicate 50MB lib per function
- Unversioned layer breaking change
- Layer exceeds size limit

---

## Q016: Lambda Destinations on Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Lambda failure handling with destinations and DLQ?

### Short Answer (30 seconds)

Async invoke: on-failure destination to SQS/SNS/Lambda. Sync: return error to client. DLQ for event source mapping.

### Detailed Answer (3–5 minutes)

**Architect:** Destinations for observability routing — not silent drop. Idempotent failure handler.

**Retry:** Event source mapping retry policy vs function async retry.

### Architecture Perspective

Failure paths must be designed not accidental.

### Follow-up Questions

1. **On-success destination? — Chain async workflows.**
2. **Bisect batch on failure? — Partial batch response SQS.**

### Common Mistakes in Interviews

- No DLQ on SQS trigger
- Infinite retry poison message
- Lost failed events silent

---

## Q017: Step Functions Orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Step Functions for order saga vs Lambda chain?

### Short Answer (30 seconds)

Step Functions: visual state machine, built-in retry/catch, long-running, human approval steps.

### Detailed Answer (3–5 minutes)

**Architect:** Express workflows high volume short; Standard workflows sagas minutes-days.

**.NET:** Lambda tasks or ECS run task integration.

### Architecture Perspective

Orchestration visibility beats hidden Lambda chains.

### Follow-up Questions

1. **Callback pattern? — Wait for external token.**
2. **Map state parallel? — Bulk processing.**

### Common Mistakes in Interviews

- 15 Lambda sync chain
- Saga state in Lambda memory
- No compensation path defined

---

## Q018: EventBridge vs SNS vs SQS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

Choose EventBridge, SNS, or SQS?

### Short Answer (30 seconds)

SQS: point-to-point queue, pull, ordering option. SNS: fan-out pub/sub push. EventBridge: event bus routing rules, schema registry, SaaS integration.

### Detailed Answer (3–5 minutes)

**Architect:** EventBridge default enterprise event backbone. SNS+SQS fan-out pattern classic. SQS worker queues.

### Architecture Perspective

Wrong messaging choice hurts coupling and scale.

### Follow-up Questions

1. **FIFO vs standard SQS? — FIFO ordering cost.**
2. **EventBridge archive replay? — Debug and reprocess.**

### Common Mistakes in Interviews

- SNS email for critical path
- No DLQ on queue consumer
- EventBridge no schema governance

---

## Q019: Elastic Beanstalk Environments

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Occasional |

### Question

Beanstalk environment tiers and deployment policies?

### Short Answer (30 seconds)

WebServer vs Worker environment. Rolling, rolling with batch, immutable, traffic splitting deployments.

### Detailed Answer (3–5 minutes)

**Architect:** Immutable deploy for zero-downtime config safety. Worker tier for SQS-driven background.

### Architecture Perspective

Beanstalk still valid for simple .NET hosting.

### Follow-up Questions

1. **Platform branch .NET? — Windows vs Linux platform.**
2. **EB CLI vs console? — IaC prefer CloudFormation generated.**

### Common Mistakes in Interviews

- Single instance prod Beanstalk
- AllAtOnce deploy prod
- Ignore health check red

---

## Q020: AWS App Runner

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compute |
| **Frequency** | Occasional |

### Question

App Runner vs ECS Fargate for container API?

### Short Answer (30 seconds)

App Runner: simplest — connect repo/ECR, auto scale, built-in load balancer. ECS: more control, VPC, service mesh.

### Detailed Answer (3–5 minutes)

**Architect:** App Runner internal tools and MVPs. ECS/EKS enterprise microservices.

### Architecture Perspective

Simplicity vs control trade-off.

### Follow-up Questions

1. **App Runner VPC connector? — Reach private RDS.**
2. **Custom domain TLS? — App Runner managed cert.**

### Common Mistakes in Interviews

- App Runner for complex mesh
- ECS for hello-world only
- No VPC connector to private DB

---

## Q021: Fargate Task Networking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Fargate awsvpc networking and security groups?

### Short Answer (30 seconds)

Each task gets ENI — security group per task/service. Private subnets + NAT for outbound internet.

### Detailed Answer (3–5 minutes)

**Architect:** Security group least privilege — ALB SG → task SG only on app port.

**Cost:** NAT Gateway per AZ — use VPC endpoints.

### Architecture Perspective

Fargate networking affects security and cost.

### Follow-up Questions

1. **Service Connect vs Cloud Map? — ECS service discovery.**
2. **Public IP on task? — Avoid — use ALB ingress.**

### Common Mistakes in Interviews

- 0.0.0.0/0 egress task SG
- Tasks in public subnet unnecessary
- No endpoint S3 through NAT

---

## Q022: SSM Session Manager Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Replace SSH with Session Manager?

### Short Answer (30 seconds)

IAM-based shell access, logged to S3/CloudWatch, no bastion host, port 22 closed.

### Detailed Answer (3–5 minutes)

**Architect:** Require MFA for Session Manager IAM policy. Session logs retained for audit.

**Port forwarding:** Tunnel to RDS through instance.

### Architecture Perspective

Bastion elimination reduces attack surface.

### Follow-up Questions

1. **Session Manager preferences? — Log encryption KMS.**
2. **Hybrid activations? — On-prem servers.**

### Common Mistakes in Interviews

- SSH keys on all EC2
- Bastion no patching
- Session logs not retained

---

## Q023: Parameter Store Hierarchy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Config |
| **Frequency** | Common |

### Question

SSM Parameter Store hierarchy design?

### Short Answer (30 seconds)

/app/prod/database/host — path convention per env and service. Standard vs advanced parameters.

### Detailed Answer (3–5 minutes)

**Architect:** Advanced for secrets with policies; Secrets Manager for rotation. IaC references parameters not hardcode.

### Architecture Perspective

Hierarchy prevents config chaos.

### Follow-up Questions

1. **StringList parameters? — Multiple values.**
2. **Policy on parameter? — IAM resource-level.**

### Common Mistakes in Interviews

- Flat parameter names
- Secrets in String not SecureString
- Prod param in dev path typo

---

## Q024: CloudWatch Logs Insights

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Query patterns in Logs Insights for incident?

### Short Answer (30 seconds)

Filter `@message like /Exception/`, stats count by bin(5m), parse JSON fields, correlate traceId.

### Detailed Answer (3–5 minutes)

**Architect:** Structured JSON logging mandatory. Saved queries for common incidents.

**Cost:** Log retention 30-90d hot; archive S3 Glacier.

### Architecture Perspective

Log query skill speeds MTTR.

### Follow-up Questions

1. **Contributor Insights? — Find noisy log sources.**
2. **Metric filters on logs? — Custom metrics from log pattern.**

### Common Mistakes in Interviews

- Unstructured grep only
- Infinite log retention
- No saved queries runbook

---

## Q025: ECR Image Scanning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

ECR vulnerability scanning in CI/CD?

### Short Answer (30 seconds)

Scan on push, fail pipeline on critical CVE, enhance scanning for OS and language deps.

### Detailed Answer (3–5 minutes)

**Architect:** Pin base image digest not `:latest`. Renovate base image updates weekly.

**Lambda:** Container image same scanning discipline.

### Architecture Perspective

Supply chain security includes images.

### Follow-up Questions

1. **Inspector vs basic scan? — Enhanced deeper.**
2. **Private ECR replication? — DR images region.**

### Common Mistakes in Interviews

- latest tag prod deploy
- Ignore critical CVE
- Public Docker Hub prod

---

## Q026: CodeDeploy Blue/Green

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deployment |
| **Frequency** | Common |

### Question

CodeDeploy blue/green for ECS/ASG?

### Short Answer (30 seconds)

Parallel green environment, traffic shift via ALB, automatic rollback on CloudWatch alarm, terminate blue after success.

### Detailed Answer (3–5 minutes)

**Architect:** Hook scripts run integration tests on green before shift. Deployment configuration minimum healthy hosts.

### Architecture Perspective

Blue/green reduces deploy risk.

### Follow-up Questions

1. **Canary traffic shift? — Linear 10% increments.**
2. **CodeDeploy vs Argo? — AWS-native vs K8s GitOps.**

### Common Mistakes in Interviews

- In-place deploy prod only
- No rollback alarm
- Skip validation hook

---

## Q027: CodePipeline Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

Multi-account CodePipeline with OIDC?

### Short Answer (30 seconds)

Source GitHub → build CodeBuild → deploy cross-account via OIDC role assumption — no long-lived keys.

### Detailed Answer (3–5 minutes)

**Architect:** Separate tooling account pipelines; deploy role trust GitHub OIDC subject repo:branch.

**Artifacts:** S3 encrypted between stages.

### Architecture Perspective

Pipeline security is architect CI/CD topic.

### Follow-up Questions

1. **Manual approval stage? — Prod gate.**
2. **Parallel actions? — Build and test split.**

### Common Mistakes in Interviews

- Access keys in CodeBuild env
- Deploy role * on *
- No approval prod deploy

---

## Q028: SAM vs CDK vs Terraform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Choose SAM, CDK, or Terraform for AWS .NET serverless?

### Short Answer (30 seconds)

SAM: Lambda/API GW focused simple. CDK: .NET constructs, L2 abstractions, good for mixed AWS. Terraform: multi-cloud, large community.

### Detailed Answer (3–5 minutes)

**Architect:** Team skill matters. CDK if all .NET shop on AWS. Terraform if multi-cloud standard.

**Testing:** cdk synth in CI; tf plan review.

### Architecture Perspective

IaC choice affects velocity and portability.

### Follow-up Questions

1. **CloudFormation raw? — Verbose — CDK generates.**
2. **SAM local invoke? — Dev Lambda test.**

### Common Mistakes in Interviews

- Console deploy prod
- No plan review CI
- Mixed IaC tools per resource random

---

## Q029: .NET on Lambda Packaging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Package .NET 8 Lambda — best practices?

### Short Answer (30 seconds)

Trimmed publish, ReadyToRun optional, native deps for arm64 Graviton, container image if package >50MB.

### Detailed Answer (3–5 minutes)

**Architect:** Provisioned concurrency for API Lambda after measuring cold start.

**Logging:** Structured JSON to CloudWatch.

### Architecture Perspective

Packaging affects cold start and cost.

### Follow-up Questions

1. **Lambda Annotations framework? — Simplified attribute model.**
2. **AOT Lambda? — Experimental constraints check.**

### Common Mistakes in Interviews

- Full framework self-contained always huge
- Ignore cold start metrics
- x86 only without ARM test

---

## Q030: Compute Selection ADR Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Process |
| **Frequency** | Very Common |

### Question

ADR framework: EC2 vs ECS vs EKS vs Lambda?

### Short Answer (30 seconds)

Forces: team skill, traffic pattern, scale-to-zero need, VPC integration, ops overhead, cost model.

### Detailed Answer (3–5 minutes)

**Decision matrix:** Score 1-5; weight by business priority. Document rejected options.

**Review:** Revisit ADR when traffic 10x or team doubles.

### Architecture Perspective

Structured compute choice impresses interviewers.

### Follow-up Questions

1. **Reversibility? — Note migration cost if wrong.**
2. **PoC spike timebox? — 1 week validate Lambda cold start.**

### Common Mistakes in Interviews

- EKS because trendy
- Lambda for 10K RPS steady
- No documented decision

---
