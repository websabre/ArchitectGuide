# Week 18 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: EC2 vs Lambda vs Fargate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q032: ECS vs EKS Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q033: Lambda Cold Starts and Provisioned Concurrency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q034: Auto Scaling Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q035: Elastic Beanstalk When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q036: API Gateway + Lambda Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q037: ALB vs NLB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q038: Graviton (ARM) Instances

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q039: Spot vs On-Demand Instances

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q040: Serverless Anti-Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q041: Lambda Destinations Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

What must architects know about Lambda Destinations?

### Short Answer (30 seconds)

Route async invocation success and failure to SQS, SNS, or Lambda

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Destinations
**Focus:** Route async invocation success and failure to SQS, SNS, or Lambda

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about Lambda Destinations?

### Architecture Perspective

Lambda Destinations is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Destinations?**
2. **Common production mistake with Lambda Destinations?**

### Common Mistakes in Interviews

- Confusing Lambda Destinations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Destinations failures

---

## Q042: Lambda Destinations Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

How deploy Lambda Destinations in production enterprise workloads?

### Short Answer (30 seconds)

Route async invocation success and failure to SQS, SNS, or Lambda

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Destinations
**Focus:** Route async invocation success and failure to SQS, SNS, or Lambda

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy Lambda Destinations in production enterprise workloads?

### Architecture Perspective

Lambda Destinations is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Destinations?**
2. **Common production mistake with Lambda Destinations?**

### Common Mistakes in Interviews

- Confusing Lambda Destinations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Destinations failures

---

## Q043: Lambda Destinations Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Advanced Lambda Destinations tuning and edge cases?

### Short Answer (30 seconds)

Route async invocation success and failure to SQS, SNS, or Lambda

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Destinations
**Focus:** Route async invocation success and failure to SQS, SNS, or Lambda

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced Lambda Destinations tuning and edge cases?

### Architecture Perspective

Lambda Destinations is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Destinations?**
2. **Common production mistake with Lambda Destinations?**

### Common Mistakes in Interviews

- Confusing Lambda Destinations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Destinations failures

---

## Q044: Lambda Destinations Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Architecture trade-offs for Lambda Destinations?

### Short Answer (30 seconds)

Route async invocation success and failure to SQS, SNS, or Lambda

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Destinations
**Focus:** Route async invocation success and failure to SQS, SNS, or Lambda

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for Lambda Destinations?

### Architecture Perspective

Lambda Destinations is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Destinations?**
2. **Common production mistake with Lambda Destinations?**

### Common Mistakes in Interviews

- Confusing Lambda Destinations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Destinations failures

---

## Q045: Lambda Layers Packaging Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

What must architects know about Lambda Layers Packaging?

### Short Answer (30 seconds)

Shared dependencies and runtime extension layers

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Layers Packaging
**Focus:** Shared dependencies and runtime extension layers

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about Lambda Layers Packaging?

### Architecture Perspective

Lambda Layers Packaging is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Layers Packaging?**
2. **Common production mistake with Lambda Layers Packaging?**

### Common Mistakes in Interviews

- Confusing Lambda Layers Packaging with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Layers Packaging failures

---

## Q046: Lambda Layers Packaging Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

How deploy Lambda Layers Packaging in production enterprise workloads?

### Short Answer (30 seconds)

Shared dependencies and runtime extension layers

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Layers Packaging
**Focus:** Shared dependencies and runtime extension layers

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy Lambda Layers Packaging in production enterprise workloads?

### Architecture Perspective

Lambda Layers Packaging is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Layers Packaging?**
2. **Common production mistake with Lambda Layers Packaging?**

### Common Mistakes in Interviews

- Confusing Lambda Layers Packaging with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Layers Packaging failures

---

## Q047: Lambda Layers Packaging Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Advanced Lambda Layers Packaging tuning and edge cases?

### Short Answer (30 seconds)

Shared dependencies and runtime extension layers

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Layers Packaging
**Focus:** Shared dependencies and runtime extension layers

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced Lambda Layers Packaging tuning and edge cases?

### Architecture Perspective

Lambda Layers Packaging is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Layers Packaging?**
2. **Common production mistake with Lambda Layers Packaging?**

### Common Mistakes in Interviews

- Confusing Lambda Layers Packaging with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Layers Packaging failures

---

## Q048: Lambda Layers Packaging Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Architecture trade-offs for Lambda Layers Packaging?

### Short Answer (30 seconds)

Shared dependencies and runtime extension layers

### Detailed Answer (3–5 minutes)

**Topic:** Lambda Layers Packaging
**Focus:** Shared dependencies and runtime extension layers

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for Lambda Layers Packaging?

### Architecture Perspective

Lambda Layers Packaging is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Lambda Layers Packaging?**
2. **Common production mistake with Lambda Layers Packaging?**

### Common Mistakes in Interviews

- Confusing Lambda Layers Packaging with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Lambda Layers Packaging failures

---

## Q049: ECS Capacity Providers Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

What must architects know about ECS Capacity Providers?

### Short Answer (30 seconds)

Mix Fargate and EC2 capacity with managed scaling

### Detailed Answer (3–5 minutes)

**Topic:** ECS Capacity Providers
**Focus:** Mix Fargate and EC2 capacity with managed scaling

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about ECS Capacity Providers?

### Architecture Perspective

ECS Capacity Providers is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Capacity Providers?**
2. **Common production mistake with ECS Capacity Providers?**

### Common Mistakes in Interviews

- Confusing ECS Capacity Providers with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Capacity Providers failures

---

## Q050: ECS Capacity Providers Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

How deploy ECS Capacity Providers in production enterprise workloads?

### Short Answer (30 seconds)

Mix Fargate and EC2 capacity with managed scaling

### Detailed Answer (3–5 minutes)

**Topic:** ECS Capacity Providers
**Focus:** Mix Fargate and EC2 capacity with managed scaling

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy ECS Capacity Providers in production enterprise workloads?

### Architecture Perspective

ECS Capacity Providers is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Capacity Providers?**
2. **Common production mistake with ECS Capacity Providers?**

### Common Mistakes in Interviews

- Confusing ECS Capacity Providers with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Capacity Providers failures

---

## Q051: ECS Capacity Providers Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Advanced ECS Capacity Providers tuning and edge cases?

### Short Answer (30 seconds)

Mix Fargate and EC2 capacity with managed scaling

### Detailed Answer (3–5 minutes)

**Topic:** ECS Capacity Providers
**Focus:** Mix Fargate and EC2 capacity with managed scaling

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced ECS Capacity Providers tuning and edge cases?

### Architecture Perspective

ECS Capacity Providers is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Capacity Providers?**
2. **Common production mistake with ECS Capacity Providers?**

### Common Mistakes in Interviews

- Confusing ECS Capacity Providers with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Capacity Providers failures

---

## Q052: ECS Capacity Providers Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Architecture trade-offs for ECS Capacity Providers?

### Short Answer (30 seconds)

Mix Fargate and EC2 capacity with managed scaling

### Detailed Answer (3–5 minutes)

**Topic:** ECS Capacity Providers
**Focus:** Mix Fargate and EC2 capacity with managed scaling

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for ECS Capacity Providers?

### Architecture Perspective

ECS Capacity Providers is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Capacity Providers?**
2. **Common production mistake with ECS Capacity Providers?**

### Common Mistakes in Interviews

- Confusing ECS Capacity Providers with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Capacity Providers failures

---

## Q053: ECS Blue/Green Deploy Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

What must architects know about ECS Blue/Green Deploy?

### Short Answer (30 seconds)

CodeDeploy controlled traffic shift between task sets

### Detailed Answer (3–5 minutes)

**Topic:** ECS Blue/Green Deploy
**Focus:** CodeDeploy controlled traffic shift between task sets

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about ECS Blue/Green Deploy?

### Architecture Perspective

ECS Blue/Green Deploy is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Blue/Green Deploy?**
2. **Common production mistake with ECS Blue/Green Deploy?**

### Common Mistakes in Interviews

- Confusing ECS Blue/Green Deploy with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Blue/Green Deploy failures

---

## Q054: ECS Blue/Green Deploy Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

How deploy ECS Blue/Green Deploy in production enterprise workloads?

### Short Answer (30 seconds)

CodeDeploy controlled traffic shift between task sets

### Detailed Answer (3–5 minutes)

**Topic:** ECS Blue/Green Deploy
**Focus:** CodeDeploy controlled traffic shift between task sets

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy ECS Blue/Green Deploy in production enterprise workloads?

### Architecture Perspective

ECS Blue/Green Deploy is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Blue/Green Deploy?**
2. **Common production mistake with ECS Blue/Green Deploy?**

### Common Mistakes in Interviews

- Confusing ECS Blue/Green Deploy with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Blue/Green Deploy failures

---

## Q055: ECS Blue/Green Deploy Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Advanced ECS Blue/Green Deploy tuning and edge cases?

### Short Answer (30 seconds)

CodeDeploy controlled traffic shift between task sets

### Detailed Answer (3–5 minutes)

**Topic:** ECS Blue/Green Deploy
**Focus:** CodeDeploy controlled traffic shift between task sets

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced ECS Blue/Green Deploy tuning and edge cases?

### Architecture Perspective

ECS Blue/Green Deploy is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Blue/Green Deploy?**
2. **Common production mistake with ECS Blue/Green Deploy?**

### Common Mistakes in Interviews

- Confusing ECS Blue/Green Deploy with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Blue/Green Deploy failures

---

## Q056: ECS Blue/Green Deploy Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Architecture trade-offs for ECS Blue/Green Deploy?

### Short Answer (30 seconds)

CodeDeploy controlled traffic shift between task sets

### Detailed Answer (3–5 minutes)

**Topic:** ECS Blue/Green Deploy
**Focus:** CodeDeploy controlled traffic shift between task sets

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for ECS Blue/Green Deploy?

### Architecture Perspective

ECS Blue/Green Deploy is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of ECS Blue/Green Deploy?**
2. **Common production mistake with ECS Blue/Green Deploy?**

### Common Mistakes in Interviews

- Confusing ECS Blue/Green Deploy with adjacent service
- Console-only knowledge without design rationale
- No monitoring for ECS Blue/Green Deploy failures

---

## Q057: EKS Pod Identity Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

What must architects know about EKS Pod Identity?

### Short Answer (30 seconds)

IAM roles for service accounts without OIDC boilerplate

### Detailed Answer (3–5 minutes)

**Topic:** EKS Pod Identity
**Focus:** IAM roles for service accounts without OIDC boilerplate

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about EKS Pod Identity?

### Architecture Perspective

EKS Pod Identity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of EKS Pod Identity?**
2. **Common production mistake with EKS Pod Identity?**

### Common Mistakes in Interviews

- Confusing EKS Pod Identity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for EKS Pod Identity failures

---

## Q058: EKS Pod Identity Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

How deploy EKS Pod Identity in production enterprise workloads?

### Short Answer (30 seconds)

IAM roles for service accounts without OIDC boilerplate

### Detailed Answer (3–5 minutes)

**Topic:** EKS Pod Identity
**Focus:** IAM roles for service accounts without OIDC boilerplate

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy EKS Pod Identity in production enterprise workloads?

### Architecture Perspective

EKS Pod Identity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of EKS Pod Identity?**
2. **Common production mistake with EKS Pod Identity?**

### Common Mistakes in Interviews

- Confusing EKS Pod Identity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for EKS Pod Identity failures

---

## Q059: EKS Pod Identity Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Advanced EKS Pod Identity tuning and edge cases?

### Short Answer (30 seconds)

IAM roles for service accounts without OIDC boilerplate

### Detailed Answer (3–5 minutes)

**Topic:** EKS Pod Identity
**Focus:** IAM roles for service accounts without OIDC boilerplate

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced EKS Pod Identity tuning and edge cases?

### Architecture Perspective

EKS Pod Identity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of EKS Pod Identity?**
2. **Common production mistake with EKS Pod Identity?**

### Common Mistakes in Interviews

- Confusing EKS Pod Identity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for EKS Pod Identity failures

---

## Q060: EKS Pod Identity Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Architecture trade-offs for EKS Pod Identity?

### Short Answer (30 seconds)

IAM roles for service accounts without OIDC boilerplate

### Detailed Answer (3–5 minutes)

**Topic:** EKS Pod Identity
**Focus:** IAM roles for service accounts without OIDC boilerplate

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for EKS Pod Identity?

### Architecture Perspective

EKS Pod Identity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of EKS Pod Identity?**
2. **Common production mistake with EKS Pod Identity?**

### Common Mistakes in Interviews

- Confusing EKS Pod Identity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for EKS Pod Identity failures

---

## Q061: Karpenter Autoscaling Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

What must architects know about Karpenter Autoscaling?

### Short Answer (30 seconds)

Just-in-time node provisioning for EKS

### Detailed Answer (3–5 minutes)

**Topic:** Karpenter Autoscaling
**Focus:** Just-in-time node provisioning for EKS

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about Karpenter Autoscaling?

### Architecture Perspective

Karpenter Autoscaling is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Karpenter Autoscaling?**
2. **Common production mistake with Karpenter Autoscaling?**

### Common Mistakes in Interviews

- Confusing Karpenter Autoscaling with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Karpenter Autoscaling failures

---

## Q062: Karpenter Autoscaling Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

How deploy Karpenter Autoscaling in production enterprise workloads?

### Short Answer (30 seconds)

Just-in-time node provisioning for EKS

### Detailed Answer (3–5 minutes)

**Topic:** Karpenter Autoscaling
**Focus:** Just-in-time node provisioning for EKS

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy Karpenter Autoscaling in production enterprise workloads?

### Architecture Perspective

Karpenter Autoscaling is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Karpenter Autoscaling?**
2. **Common production mistake with Karpenter Autoscaling?**

### Common Mistakes in Interviews

- Confusing Karpenter Autoscaling with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Karpenter Autoscaling failures

---

## Q063: Karpenter Autoscaling Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Advanced Karpenter Autoscaling tuning and edge cases?

### Short Answer (30 seconds)

Just-in-time node provisioning for EKS

### Detailed Answer (3–5 minutes)

**Topic:** Karpenter Autoscaling
**Focus:** Just-in-time node provisioning for EKS

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced Karpenter Autoscaling tuning and edge cases?

### Architecture Perspective

Karpenter Autoscaling is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Karpenter Autoscaling?**
2. **Common production mistake with Karpenter Autoscaling?**

### Common Mistakes in Interviews

- Confusing Karpenter Autoscaling with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Karpenter Autoscaling failures

---

## Q064: Karpenter Autoscaling Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Architecture trade-offs for Karpenter Autoscaling?

### Short Answer (30 seconds)

Just-in-time node provisioning for EKS

### Detailed Answer (3–5 minutes)

**Topic:** Karpenter Autoscaling
**Focus:** Just-in-time node provisioning for EKS

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for Karpenter Autoscaling?

### Architecture Perspective

Karpenter Autoscaling is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Karpenter Autoscaling?**
2. **Common production mistake with Karpenter Autoscaling?**

### Common Mistakes in Interviews

- Confusing Karpenter Autoscaling with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Karpenter Autoscaling failures

---

## Q065: App Runner Simplicity Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

What must architects know about App Runner Simplicity?

### Short Answer (30 seconds)

Managed container web service without cluster ops

### Detailed Answer (3–5 minutes)

**Topic:** App Runner Simplicity
**Focus:** Managed container web service without cluster ops

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about App Runner Simplicity?

### Architecture Perspective

App Runner Simplicity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of App Runner Simplicity?**
2. **Common production mistake with App Runner Simplicity?**

### Common Mistakes in Interviews

- Confusing App Runner Simplicity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for App Runner Simplicity failures

---

## Q066: App Runner Simplicity Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

How deploy App Runner Simplicity in production enterprise workloads?

### Short Answer (30 seconds)

Managed container web service without cluster ops

### Detailed Answer (3–5 minutes)

**Topic:** App Runner Simplicity
**Focus:** Managed container web service without cluster ops

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy App Runner Simplicity in production enterprise workloads?

### Architecture Perspective

App Runner Simplicity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of App Runner Simplicity?**
2. **Common production mistake with App Runner Simplicity?**

### Common Mistakes in Interviews

- Confusing App Runner Simplicity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for App Runner Simplicity failures

---

## Q067: App Runner Simplicity Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Advanced App Runner Simplicity tuning and edge cases?

### Short Answer (30 seconds)

Managed container web service without cluster ops

### Detailed Answer (3–5 minutes)

**Topic:** App Runner Simplicity
**Focus:** Managed container web service without cluster ops

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Advanced App Runner Simplicity tuning and edge cases?

### Architecture Perspective

App Runner Simplicity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of App Runner Simplicity?**
2. **Common production mistake with App Runner Simplicity?**

### Common Mistakes in Interviews

- Confusing App Runner Simplicity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for App Runner Simplicity failures

---

## Q068: App Runner Simplicity Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Architecture trade-offs for App Runner Simplicity?

### Short Answer (30 seconds)

Managed container web service without cluster ops

### Detailed Answer (3–5 minutes)

**Topic:** App Runner Simplicity
**Focus:** Managed container web service without cluster ops

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** Architecture trade-offs for App Runner Simplicity?

### Architecture Perspective

App Runner Simplicity is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of App Runner Simplicity?**
2. **Common production mistake with App Runner Simplicity?**

### Common Mistakes in Interviews

- Confusing App Runner Simplicity with adjacent service
- Console-only knowledge without design rationale
- No monitoring for App Runner Simplicity failures

---

## Q069: AWS Batch Workloads Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

What must architects know about AWS Batch Workloads?

### Short Answer (30 seconds)

Managed batch job queues and compute environments

### Detailed Answer (3–5 minutes)

**Topic:** AWS Batch Workloads
**Focus:** Managed batch job queues and compute environments

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** What must architects know about AWS Batch Workloads?

### Architecture Perspective

AWS Batch Workloads is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Batch Workloads?**
2. **Common production mistake with AWS Batch Workloads?**

### Common Mistakes in Interviews

- Confusing AWS Batch Workloads with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Batch Workloads failures

---

## Q070: AWS Batch Workloads Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

How deploy AWS Batch Workloads in production enterprise workloads?

### Short Answer (30 seconds)

Managed batch job queues and compute environments

### Detailed Answer (3–5 minutes)

**Topic:** AWS Batch Workloads
**Focus:** Managed batch job queues and compute environments

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 18 context:** How deploy AWS Batch Workloads in production enterprise workloads?

### Architecture Perspective

AWS Batch Workloads is essential Week 18 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Batch Workloads?**
2. **Common production mistake with AWS Batch Workloads?**

### Common Mistakes in Interviews

- Confusing AWS Batch Workloads with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Batch Workloads failures

---
