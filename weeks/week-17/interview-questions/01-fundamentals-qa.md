# Week 17 — Fundamentals Q&A

> Q001–Q030: Premium format (Week 1 quality).
> Cross-reference: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: AWS Well-Architected Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS WAF |
| **Frequency** | Very Common |

### Question

What are the six AWS WAF pillars and how do you use them in reviews?

### Short Answer (30 seconds)

Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability. Score each design decision; prioritize by business risk.

### Detailed Answer (3–5 minutes)

AWS WAF adds **Sustainability** as a sixth pillar vs Azure's five.

1. **Operational Excellence** — IaC, runbooks, CI/CD, observability
2. **Security** — IAM least privilege, encryption, GuardDuty
3. **Reliability** — Multi-AZ, auto scaling, backup/DR
4. **Performance Efficiency** — Right instance types, caching, serverless where fit
5. **Cost Optimization** — Reserved/Savings Plans, rightsizing, lifecycle policies
6. **Sustainability** — Graviton, efficient regions, workload scheduling

**Review process:** Map each component to pillars; payment API leads Security + Reliability.

### Architecture Perspective

Structured WAF reviews beat listing service names.

### Follow-up Questions

1. **AWS WAF vs Azure WAF? — Same philosophy; sustainability explicit on AWS.**
2. **Well-Architected Tool? — Free workload review in console — document findings.**

### Common Mistakes in Interviews

- Security-only reviews
- Ignoring cost pillar on prod estates
- No remediation priorities

---

## Q002: AWS Organizations and OU Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Design AWS Organizations for 5 product teams with SOC 2 requirements.

### Short Answer (30 seconds)

Root org → Security OU (audit/logging) + Workloads OU. Per team: prod and nonprod accounts. SCPs at OU level. Central security account for CloudTrail/Config.

### Detailed Answer (3–5 minutes)

**Structure:**
```
Organization
├── Security OU (audit, log archive, security tooling)
└── Workloads OU
    ├── Team A (prod + nonprod accounts)
    └── Team B (prod + nonprod accounts)
```

**SOC 2:** Consolidated billing, SCP deny root API keys, mandatory CloudTrail to log archive, break-glass separate from daily IAM users.

**Architect:** Account = blast radius + billing boundary — not one account per microservice.

### Architecture Perspective

Organizations design is foundational — painful to retrofit.

### Follow-up Questions

1. **Control Tower vs manual org? — Control Tower accelerates landing zone — customize guardrails.**
2. **How many accounts? — Enough isolation; not hundreds unmanaged.**

### Common Mistakes in Interviews

- Single prod account for all teams
- No centralized audit logging
- SCPs only on root without testing

---

## Q003: IAM Policies vs SCPs vs Permission Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Difference between IAM policy, SCP, and permission boundary?

### Short Answer (30 seconds)

IAM policy: what identity can do. SCP: max permissions for accounts/OUs (guardrail). Permission boundary: max permissions for IAM user/role.

### Detailed Answer (3–5 minutes)

**IAM policy** on role `DeployRole`: allows `ecs:UpdateService` on specific cluster.

**SCP** on Workloads OU: denies `ec2:RunInstances` without tag `Environment` — applies to all identities including admin.

**Permission boundary** on developer role: caps even if admin attaches broader policy.

**Architect:** SCPs for org-wide guardrails; IAM for workload least privilege; boundaries for delegated admin scenarios.

### Architecture Perspective

Confusing IAM layers fails senior AWS interviews.

### Follow-up Questions

1. **Resource-based policies? — S3 bucket policy — different axis — know cross-account access.**
2. **IAM Access Analyzer? — Finds unintended external access.**

### Common Mistakes in Interviews

- SCP as only security control
- Admin users without MFA
- Overly broad `*` actions on roles

---

## Q004: AWS Regions and Availability Zones

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

When deploy multi-AZ vs single-AZ? Cost trade-off?

### Short Answer (30 seconds)

Multi-AZ for production RDS, ALB, ECS/EKS across AZs. Single-AZ for dev. Multi-AZ RDS ~2x database cost — worth for revenue workloads.

### Detailed Answer (3–5 minutes)

**AZ:** isolated datacenters within region.

**Region:** geographic — choose for latency, compliance (eu-west-1 for GDPR).

**SLA math:** Single-AZ RDS has lower SLA than Multi-AZ.

**Architect:** Document RTO/RPO per tier; Multi-AZ protects AZ failure not region failure — DR is separate.

### Architecture Perspective

AZ vs region confusion is common failure mode.

### Follow-up Questions

1. **Local Zones / Wavelength? — Edge extensions — latency-sensitive use cases.**
2. **Opt-in regions? — Enable before deploy — automation must handle.**

### Common Mistakes in Interviews

- Single-AZ RDS for payment prod
- No cross-region DR plan
- Random region without compliance check

---

## Q005: AWS Migration and CAF

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CAF |
| **Frequency** | Common |

### Question

Summarize AWS Cloud Adoption Framework for enterprise migration.

### Short Answer (30 seconds)

Envision → Align → Map → Migrate → Optimize → Scale. Architects lead Map/Migrate waves; platform team owns landing zone.

### Detailed Answer (3–5 minutes)

**Map:** Application Portfolio Service (APS), 7 Rs (rehost, replatform, refactor...).

**Migrate:** Waves by risk and dependency — not big-bang.

**Architect deliverable:** Migration plan with TCO, wave schedule, rollback criteria per workload.

### Architecture Perspective

CAF shows enterprise adoption beyond single-app deploy.

### Follow-up Questions

1. **Migration Hub / Application Discovery Service? — Discovery and tracking.**
2. **Rehost vs refactor decision? — Document per workload in ADR.**

### Common Mistakes in Interviews

- Lift-and-shift everything without assessment
- No wave prioritization
- Skip landing zone

---

## Q006: AWS Cost Allocation Tags

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Mandatory tags for enterprise AWS? How enforce?

### Short Answer (30 seconds)

Environment, CostCenter, Owner, Application. Enforce via SCP + Config rules + tag-on-create IAM condition keys. Cost Explorer allocation reports.

### Detailed Answer (3–5 minutes)

**Enforcement:**
- SCP: require tags on resource creation
- AWS Config: noncompliant resource report
- Lambda remediation for drift

**Architect:** Tags drive chargeback, Instance Scheduler shutdown, and incident routing.

### Architecture Perspective

Tags are FinOps foundation on AWS.

### Follow-up Questions

1. **Tag propagation from org? — Tag policies in Organizations.**
2. **Cost anomaly detection? — Cost Anomaly Detection alerts.**

### Common Mistakes in Interviews

- Optional tags nobody uses
- No SCP tag enforcement
- Untagged prod resources after 30 days

---

## Q007: AWS Landing Zone (Control Tower)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Landing Zone |
| **Frequency** | Very Common |

### Question

Platform landing zone vs application account in AWS?

### Short Answer (30 seconds)

Platform: shared networking (Transit Gateway), security tooling, logging — central team. Application accounts: workload deploy with guardrails from Control Tower.

### Detailed Answer (3–5 minutes)

**Control Tower provides:** Account Factory, guardrails (SCPs), centralized logging account.

**Application team gets:** Account with VPC from blueprint, deploy ECS/RDS within guardrails.

**Architect:** Start from Control Tower + customize — don't reinvent org structure.

### Architecture Perspective

Landing zone vocabulary expected in AWS architect interviews.

### Follow-up Questions

1. **Terraform vs CloudFormation for LZ? — Team skill; CloudFormation native.**
2. **Brownfield? — Import accounts into org; retrofit SCPs carefully.**

### Common Mistakes in Interviews

- Every team builds own Transit Gateway
- No centralized CloudTrail
- Landing zone never updated post-launch

---

## Q008: IAM Custom Policies and Roles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

When create custom IAM policy vs AWS managed policy?

### Short Answer (30 seconds)

Custom when managed too broad. CI/CD role: `ecs:UpdateService` + `ecr:GetAuthorizationToken` only — not PowerUserAccess.

### Detailed Answer (3–5 minutes)

**Pattern:** `GitHubActionsDeployRole` with OIDC trust + minimal policy on one cluster.

**Principle:** Least privilege per workload. Prefer roles over long-lived access keys.

**Architect:** IAM Access Analyzer in CI; no access keys in repos.

### Architecture Perspective

Custom IAM shows production governance experience.

### Follow-up Questions

1. **IAM Roles Anywhere? — On-prem workloads need AWS creds — certificate-based.**
2. **Cross-account roles? — Hub account assumption pattern for centralized ops.**

### Common Mistakes in Interviews

- PowerUserAccess for CI/CD
- Long-lived IAM user access keys
- Root account for daily operations

---

## Q009: AWS Budgets and Cost Explorer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Prevent surprise AWS bill for new product team?

### Short Answer (30 seconds)

AWS Budgets at 80%/100%, Cost Anomaly Detection, Instance Scheduler for dev, Savings Plans for baseline, weekly rightsizing review.

### Detailed Answer (3–5 minutes)

**Onboarding checklist:**
- Budget per linked account
- SCP deny expensive instance types in nonprod
- CloudWatch log retention limits
- Compute Optimizer recommendations monthly

**Unit economics:** Track $/transaction as feature scales.

### Architecture Perspective

FinOps is architect responsibility from day one.

### Follow-up Questions

1. **CUR vs Cost Explorer? — Cost and Usage Report for detailed analysis.**
2. **RI vs Savings Plans? — SP more flexible for mixed compute.**

### Common Mistakes in Interviews

- No budget alerts
- m5.24xlarge in dev accounts
- Unbounded CloudWatch Logs retention

---

## Q010: Choose AWS vs On-Premises

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Stakeholder asks 'why AWS?' — architect response framework?

### Short Answer (30 seconds)

Agility, global reach, managed services reduce undifferentiated ops, pay-as-you-go for variable load. Honest TCO including egress, support, and ops labor — not 'always cheaper'.

### Detailed Answer (3–5 minutes)

**When AWS wins:** Elastic scale, global footprint, serverless/event-driven, rapid experimentation.

**When hybrid/on-prem:** Factory floor latency, sunk datacenter, strict data sovereignty without approved region.

**Architect:** Hybrid common — Outposts or Direct Connect for extension.

### Architecture Perspective

Balanced advocacy impresses executives.

### Follow-up Questions

1. **Repatriation? — Some workloads return on-prem — stay workload-driven.**
2. **Egress in TCO? — Cross-AZ and internet egress often underestimated.**

### Common Mistakes in Interviews

- Cloud lift without ops model change
- Ignoring data transfer costs
- 100% cloud mandate without exceptions

---

## Q011: CloudTrail Organization Trail

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design organization-wide CloudTrail for SOC 2?

### Short Answer (30 seconds)

Org trail in all regions, log file validation, centralized S3 bucket in log-archive account, SSE-KMS, Object Lock for immutability.

### Detailed Answer (3–5 minutes)

**Architect:** Separate account for logs — developers can't delete audit trail.

**Integration:** CloudTrail → EventBridge → Security Hub for alerts on root login, IAM changes.

**Retention:** Match compliance — 1 year minimum many frameworks.

### Architecture Perspective

Audit logging is non-negotiable for enterprise AWS.

### Follow-up Questions

1. **Data events vs management events? — S3 object-level optional extra cost.**
2. **CloudTrail Lake? — SQL analytics on trails.**

### Common Mistakes in Interviews

- Trail only in one region
- Logs in same account as workloads
- No alerting on root usage

---

## Q012: AWS Config Rules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

AWS Config for continuous compliance — key rules?

### Short Answer (30 seconds)

Managed rules: encrypted-volumes, rds-storage-encrypted, s3-bucket-public-read-prohibited, required-tags.

### Detailed Answer (3–5 minutes)

**Architect:** Conformance packs bundle SOC2/PCI rules. Remediation via SSM automation or Lambda.

**Cost:** Config per resource recording — enable where compliance requires.

### Architecture Perspective

Config catches drift not just deploy-time policy.

### Follow-up Questions

1. **Config aggregator? — Multi-account multi-region view.**
2. **Remediation action? — Auto-fix noncompliant SG rule.**

### Common Mistakes in Interviews

- Config enabled no rules
- Ignore noncompliant report
- Manual compliance quarterly only

---

## Q013: KMS Key Management Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

CMK strategy for RDS, S3, and EBS?

### Short Answer (30 seconds)

Customer managed CMK per data classification — separate keys prod vs nonprod. Key policy least privilege. Automatic annual rotation.

### Detailed Answer (3–5 minutes)

**Architect:** Grant IAM roles `kms:Decrypt` not `*` on key. CloudTrail logs KMS API calls.

**Multi-account:** CMK in security account with cross-account grant.

### Architecture Perspective

Key management is shared responsibility core.

### Follow-up Questions

1. **AWS managed vs CMK? — CMK for control and audit.**
2. **KMS multi-Region keys? — DR for encrypted data.**

### Common Mistakes in Interviews

- One CMK wildcard principal *
- No key rotation
- Secrets in plaintext beside encrypted data

---

## Q014: Secrets Manager Rotation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Rotate RDS credentials with Secrets Manager?

### Short Answer (30 seconds)

Secret stores connection string; Lambda rotation function updates DB password and secret version; apps fetch latest via SDK.

### Detailed Answer (3–5 minutes)

**Architect:** No passwords in Parameter Store plaintext for DB. Rotation schedule 30-90 days.

**Apps:** Cache secret with TTL; handle rotation gracefully on auth failure retry.

### Architecture Perspective

Automated rotation beats manual password tickets.

### Follow-up Questions

1. **Rotation vs manual? — Lambda single-user rotation for RDS.**
2. **Cross-account secrets? — Resource policy on secret.**

### Common Mistakes in Interviews

- Password in environment variable forever
- No rotation on prod DB
- App never refreshes cached secret

---

## Q015: CloudWatch Alarms for SLOs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

CloudWatch alarms aligned to SLO error budget?

### Short Answer (30 seconds)

Alarm on ALB 5xx rate, Lambda errors, RDS CPU, custom business metric. Composite alarm reduces noise.

### Detailed Answer (3–5 minutes)

**Architect:** Multi-stage — warning at 50% budget burn, page at 90%. Runbooks linked in alarm description.

**Metric math:** `(errors/requests)*100` over 5 minutes.

### Architecture Perspective

Alarms connect metrics to human response.

### Follow-up Questions

1. **Anomaly detection alarms? — ML baseline for variable traffic.**
2. **Alarm on insufficient data? — Treat missing data as breach for critical.**

### Common Mistakes in Interviews

- Alarm every metric no prioritization
- No runbook in alarm
- PagerDuty on dev environment alarm

---

## Q016: X-Ray Distributed Tracing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Enable X-Ray across API Gateway, Lambda, ECS?

### Short Answer (30 seconds)

Active tracing on API GW, Lambda pass-through, ECS daemon or sidecar. Service map shows latency bottlenecks.

### Detailed Answer (3–5 minutes)

**Architect:** Sample rate tune for cost. Correlate with CloudWatch Logs via trace ID.

**OpenTelemetry:** ADOT collector export to X-Ray — portable instrumentation.

### Architecture Perspective

Tracing is architect debugging superpower.

### Follow-up Questions

1. **X-Ray groups? — Filter traces by service version.**
2. **Service lens? — Health dashboard per service.**

### Common Mistakes in Interviews

- No tracing production
- 100% trace always on
- Trace without log correlation

---

## Q017: Service Control Policy Examples

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Three SCPs every enterprise AWS org needs?

### Short Answer (30 seconds)

Deny root user actions, deny unencrypted S3 upload, restrict regions to approved list.

### Detailed Answer (3–5 minutes)

**Architect:** SCPs don't grant — only filter max permissions. Test in sandbox OU before prod MG.

**Exemption:** Break-glass OU without region deny but heavily monitored.

### Architecture Perspective

SCPs are guardrails not IAM replacement.

### Follow-up Questions

1. **SCP inheritance? — All OUs below inherit.**
2. **FullAWSAccess SCP? — Still need explicit attach.**

### Common Mistakes in Interviews

- SCP on root without testing
- Think SCP grants permissions
- No exemption process

---

## Q018: IAM Access Analyzer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Use IAM Access Analyzer in CI/CD?

### Short Answer (30 seconds)

Identifies resources shared externally — S3 public, KMS keys, IAM roles trust external accounts.

### Detailed Answer (3–5 minutes)

**Architect:** Run in pipeline on Terraform plan — fail PR if unintended public access.

**Unused access analyzer:** Right-size IAM policies — remove stale permissions.

### Architecture Perspective

External access findings prevent breaches.

### Follow-up Questions

1. **Archive rules? — Suppress known intentional findings.**
2. **Zone of trust? — Organization as trust boundary.**

### Common Mistakes in Interviews

- Ignore Access Analyzer findings
- Public S3 discovered at audit
- Overly broad resource * in policy

---

## Q019: AWS Systems Manager

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Systems Manager for patch and session management?

### Short Answer (30 seconds)

SSM Patch Manager baselines for EC2, Session Manager replaces SSH with audited access, Parameter Store for config hierarchy.

### Detailed Answer (3–5 minutes)

**Architect:** No SSH keys on instances — Session Manager IAM-based. Patch windows with maintenance windows.

**Hybrid:** SSM agent on-prem via activation.

### Architecture Perspective

SSM is modern EC2 operations default.

### Follow-up Questions

1. **Run command vs State Manager? — Ad hoc vs desired state.**
2. **Parameter Store vs Secrets Manager? — Secrets for credentials; Param for config.**

### Common Mistakes in Interviews

- SSH port 22 open world
- Manual patching prod fleet
- Secrets in Parameter Store String

---

## Q020: AWS Trusted Advisor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Occasional |

### Question

Trusted Advisor vs Cost Explorer vs Compute Optimizer?

### Short Answer (30 seconds)

Trusted Advisor: high-level checks (support tier). Cost Explorer: spend analysis. Compute Optimizer: ML rightsizing.

### Detailed Answer (3–5 minutes)

**Architect:** Monthly review all three dashboards. Trusted Advisor security checks on Business+ support.

**Automate:** Export recommendations to ticketing.

### Architecture Perspective

Operational excellence uses AWS advisory tools.

### Follow-up Questions

1. **Trusted Advisor API? — Automate report to S3.**
2. **Priority support benefit? — TA full checks.**

### Common Mistakes in Interviews

- Never review recommendations
- Ignore security TA checks
- Rightsizing once never again

---

## Q021: Cost Explorer and CUR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Cost and Usage Report vs Cost Explorer?

### Short Answer (30 seconds)

Cost Explorer: interactive dashboards. CUR: detailed line-item export to Athena/S3 for custom analysis.

### Detailed Answer (3–5 minutes)

**Architect:** CUR with hourly granularity for chargeback. Athena queries by tag CostCenter.

**Unit economics:** Join CUR with application metrics table.

### Architecture Perspective

FinOps needs granular data export.

### Follow-up Questions

1. **CUR parquet? — Efficient Athena queries.**
2. **Data exports new? — Simpler than legacy CUR setup.**

### Common Mistakes in Interviews

- Invoice surprise no CUR
- Untagged resources 40% spend
- No monthly cost review

---

## Q022: Savings Plans vs Reserved Instances

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Savings Plans vs RI for steady .NET on EC2?

### Short Answer (30 seconds)

Compute Savings Plans flexible across instance family/region. Standard RI cheapest for fixed size. Convertible RI for migration flexibility.

### Detailed Answer (3–5 minutes)

**Architect:** 1-year SP baseline after 3 months stable usage. Analyze in Cost Explorer recommendations.

**Don't:** Buy 3-year RI day one of new product.

### Architecture Perspective

Commitment discounts need usage stability proof.

### Follow-up Questions

1. **SP EC2 Instance SP vs Compute SP? — Compute SP broader.**
2. **RI marketplace? — Sell unused RI.**

### Common Mistakes in Interviews

- On-Demand only at scale always
- RI wrong instance family locked
- No utilization monitoring

---

## Q023: AWS Support Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Occasional |

### Question

When upgrade to Business or Enterprise Support?

### Short Answer (30 seconds)

Business: production workloads needing <1hr response on urgent. Enterprise: mission-critical, TAM, concierge routing.

### Detailed Answer (3–5 minutes)

**Architect:** Business minimum for prod accounts with Trusted Advisor full. Enterprise for regulated/large estate.

**Cost:** % of monthly spend — model in TCO.

### Architecture Perspective

Support tier is insurance policy.

### Follow-up Questions

1. **AWS Health Dashboard? — All tiers — personalized events.**
2. **Support case severity? — Know when Sev1 justified.**

### Common Mistakes in Interviews

- Basic support prod outage
- Enterprise without TAM engagement
- No runbook before opening case

---

## Q024: Shared Responsibility Model Depth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Explain shared responsibility for EC2 vs Lambda vs RDS?

### Short Answer (30 seconds)

EC2: you patch OS, AWS patches hypervisor. Lambda: AWS manages runtime, you manage code/IAM. RDS: AWS manages DB engine patch, you manage schema/access.

### Detailed Answer (3–5 minutes)

**Interview:** Map each service to who patches, encrypts, configures network.

**Architect:** Misunderstanding causes compliance gaps — 'AWS is secure' without customer duties.

### Architecture Perspective

Shared responsibility is AWS interview foundation.

### Follow-up Questions

1. **Customer responsibility matrix? — Download per service.**
2. **Compliance inheritance? — You still certify workload config.**

### Common Mistakes in Interviews

- Assume AWS handles all security
- Unpatched EC2 AMI in prod
- Lambda with wild IAM role

---

## Q025: Multi-Account Strategy Pitfalls

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Common mistakes in AWS multi-account design?

### Short Answer (30 seconds)

Too many accounts unmanageable, no centralized logging, inconsistent SCPs, VPC per account without TGW plan, manual account creation.

### Detailed Answer (3–5 minutes)

**Architect:** Landing zone with Control Tower, account vending automation, guardrails at OU level.

**Balance:** Isolation vs operational overhead.

### Architecture Perspective

Account strategy errors are expensive to fix.

### Follow-up Questions

1. **Account per developer? — Usually excessive.**
2. **Consolidated billing? — Required for org benefits.**

### Common Mistakes in Interviews

- 50 accounts no org structure
- Duplicate VPC CIDRs
- No log archive account

---

## Q026: Control Tower Guardrails

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Landing Zone |
| **Frequency** | Common |

### Question

AWS Control Tower guardrails — mandatory vs elective?

### Short Answer (30 seconds)

Mandatory: disallow public RDS, require encryption. Elective: allowed regions, approved instance types.

### Detailed Answer (3–5 minutes)

**Architect:** Enable mandatory set on prod OU; elective customized per workload OU.

**Drift:** Control Tower detects drift from baseline — remediate or document exception.

### Architecture Perspective

Guardrails operationalize governance at scale.

### Follow-up Questions

1. **Custom guardrails? — Lambda-based proactive controls.**
2. **Account Factory baseline? — VPC config per new account.**

### Common Mistakes in Interviews

- Control Tower without guardrail review
- Disable guardrail for convenience
- No drift detection process

---

## Q027: Account Vending Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Platform |
| **Frequency** | Common |

### Question

Automate new AWS account provisioning?

### Short Answer (30 seconds)

Control Tower Account Factory, AFT (Account Factory for Terraform), or Service Catalog — pipeline creates account, applies SCPs, VPC baseline.

### Detailed Answer (3–5 minutes)

**Architect:** Self-service portal for teams with guardrails — not ticket to cloud team for 2 weeks.

**Inputs:** Account email, OU placement, tags, network CIDR from IPAM.

### Architecture Perspective

Vending scales cloud adoption.

### Follow-up Questions

1. **AFT vs CFCT? — Terraform vs Control Tower native customization.**
2. **IPAM integration? — Avoid CIDR collisions.**

### Common Mistakes in Interviews

- Manual console account create
- No baseline applied new account
- Account sprawl untracked

---

## Q028: Break-Glass Account Procedure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Design break-glass emergency access?

### Short Answer (30 seconds)

Separate account or root MFA hardware keys in physical safe; CloudTrail alert on any use; post-incident review mandatory; time-limited credentials.

### Detailed Answer (3–5 minutes)

**Architect:** Break-glass excluded from SCP deny root only with dual control. Runbook documents when authorized.

### Architecture Perspective

Emergency access without procedure is liability.

### Follow-up Questions

1. **PIM equivalent AWS? — No exact — process + monitoring.**
2. **Disable break-glass creds after? — Rotate and audit.**

### Common Mistakes in Interviews

- Daily admin uses break-glass
- No alert on break-glass use
- Shared break-glass password

---

## Q029: AWS Outage Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

During AWS regional outage — architect actions?

### Short Answer (30 seconds)

Check Service Health Dashboard, communicate ETA unknown honestly, fail over if DR ready, disable non-critical jobs, post-mortem after.

### Detailed Answer (3–5 minutes)

**Architect:** Pre-written status comms template. DR drill proves failover works — not first attempt during outage.

**Don't:** Promise recovery time without data.

### Architecture Perspective

Calm communication is leadership skill.

### Follow-up Questions

1. **Personal Health Dashboard? — Subscribe RSS per service.**
2. **Multi-region failover test frequency? — Quarterly minimum critical.**

### Common Mistakes in Interviews

- No DR plan documented
- First failover attempt during outage
- Blame AWS publicly without internal review

---

## Q030: AWS Health Dashboard Subscriptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Personal Health Dashboard and EventBridge integration?

### Short Answer (30 seconds)

Subscribe to service events affecting your account; EventBridge rules trigger SNS/Slack on `AWS Health API` events.

### Detailed Answer (3–5 minutes)

**Architect:** Automated comms to status page internal channel. Runbooks per critical service (RDS, ECS, DynamoDB).

**Proactive:** Plan maintenance windows from scheduled events.

### Architecture Perspective

Health events should drive automated response.

### Follow-up Questions

1. **Organization view health? — Aggregated across accounts.**
2. **Affected entities API? — Identify impacted resources.**

### Common Mistakes in Interviews

- Learn outage from customers first
- No EventBridge health rules
- Ignore scheduled maintenance events

---
