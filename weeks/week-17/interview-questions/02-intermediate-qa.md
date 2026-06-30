# Week 17 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: AWS Well-Architected Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q032: AWS Organizations and OU Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q033: IAM Policies vs SCPs vs Permission Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q034: AWS Regions and Availability Zones

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q035: AWS Migration and CAF

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q036: AWS Cost Allocation Tags

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q037: AWS Landing Zone (Control Tower)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q038: IAM Custom Policies and Roles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q039: AWS Budgets and Cost Explorer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q040: Choose AWS vs On-Premises

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q041: IAM Policy Evaluation Logic Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What must architects know about IAM Policy Evaluation Logic?

### Short Answer (30 seconds)

Explicit deny wins; intersection of SCP, identity, resource, and session policies

### Detailed Answer (3–5 minutes)

**Topic:** IAM Policy Evaluation Logic
**Focus:** Explicit deny wins; intersection of SCP, identity, resource, and session policies

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about IAM Policy Evaluation Logic?

### Architecture Perspective

IAM Policy Evaluation Logic is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IAM Policy Evaluation Logic?**
2. **Common production mistake with IAM Policy Evaluation Logic?**

### Common Mistakes in Interviews

- Confusing IAM Policy Evaluation Logic with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IAM Policy Evaluation Logic failures

---

## Q042: IAM Policy Evaluation Logic Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How deploy IAM Policy Evaluation Logic in production enterprise workloads?

### Short Answer (30 seconds)

Explicit deny wins; intersection of SCP, identity, resource, and session policies

### Detailed Answer (3–5 minutes)

**Topic:** IAM Policy Evaluation Logic
**Focus:** Explicit deny wins; intersection of SCP, identity, resource, and session policies

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy IAM Policy Evaluation Logic in production enterprise workloads?

### Architecture Perspective

IAM Policy Evaluation Logic is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IAM Policy Evaluation Logic?**
2. **Common production mistake with IAM Policy Evaluation Logic?**

### Common Mistakes in Interviews

- Confusing IAM Policy Evaluation Logic with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IAM Policy Evaluation Logic failures

---

## Q043: IAM Policy Evaluation Logic Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Advanced IAM Policy Evaluation Logic tuning and edge cases?

### Short Answer (30 seconds)

Explicit deny wins; intersection of SCP, identity, resource, and session policies

### Detailed Answer (3–5 minutes)

**Topic:** IAM Policy Evaluation Logic
**Focus:** Explicit deny wins; intersection of SCP, identity, resource, and session policies

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced IAM Policy Evaluation Logic tuning and edge cases?

### Architecture Perspective

IAM Policy Evaluation Logic is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IAM Policy Evaluation Logic?**
2. **Common production mistake with IAM Policy Evaluation Logic?**

### Common Mistakes in Interviews

- Confusing IAM Policy Evaluation Logic with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IAM Policy Evaluation Logic failures

---

## Q044: IAM Policy Evaluation Logic Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Architecture trade-offs for IAM Policy Evaluation Logic?

### Short Answer (30 seconds)

Explicit deny wins; intersection of SCP, identity, resource, and session policies

### Detailed Answer (3–5 minutes)

**Topic:** IAM Policy Evaluation Logic
**Focus:** Explicit deny wins; intersection of SCP, identity, resource, and session policies

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for IAM Policy Evaluation Logic?

### Architecture Perspective

IAM Policy Evaluation Logic is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IAM Policy Evaluation Logic?**
2. **Common production mistake with IAM Policy Evaluation Logic?**

### Common Mistakes in Interviews

- Confusing IAM Policy Evaluation Logic with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IAM Policy Evaluation Logic failures

---

## Q045: STS AssumeRole Chain Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What must architects know about STS AssumeRole Chain?

### Short Answer (30 seconds)

Temporary credential chaining and external ID for third parties

### Detailed Answer (3–5 minutes)

**Topic:** STS AssumeRole Chain
**Focus:** Temporary credential chaining and external ID for third parties

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about STS AssumeRole Chain?

### Architecture Perspective

STS AssumeRole Chain is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of STS AssumeRole Chain?**
2. **Common production mistake with STS AssumeRole Chain?**

### Common Mistakes in Interviews

- Confusing STS AssumeRole Chain with adjacent service
- Console-only knowledge without design rationale
- No monitoring for STS AssumeRole Chain failures

---

## Q046: STS AssumeRole Chain Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How deploy STS AssumeRole Chain in production enterprise workloads?

### Short Answer (30 seconds)

Temporary credential chaining and external ID for third parties

### Detailed Answer (3–5 minutes)

**Topic:** STS AssumeRole Chain
**Focus:** Temporary credential chaining and external ID for third parties

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy STS AssumeRole Chain in production enterprise workloads?

### Architecture Perspective

STS AssumeRole Chain is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of STS AssumeRole Chain?**
2. **Common production mistake with STS AssumeRole Chain?**

### Common Mistakes in Interviews

- Confusing STS AssumeRole Chain with adjacent service
- Console-only knowledge without design rationale
- No monitoring for STS AssumeRole Chain failures

---

## Q047: STS AssumeRole Chain Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Advanced STS AssumeRole Chain tuning and edge cases?

### Short Answer (30 seconds)

Temporary credential chaining and external ID for third parties

### Detailed Answer (3–5 minutes)

**Topic:** STS AssumeRole Chain
**Focus:** Temporary credential chaining and external ID for third parties

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced STS AssumeRole Chain tuning and edge cases?

### Architecture Perspective

STS AssumeRole Chain is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of STS AssumeRole Chain?**
2. **Common production mistake with STS AssumeRole Chain?**

### Common Mistakes in Interviews

- Confusing STS AssumeRole Chain with adjacent service
- Console-only knowledge without design rationale
- No monitoring for STS AssumeRole Chain failures

---

## Q048: STS AssumeRole Chain Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Architecture trade-offs for STS AssumeRole Chain?

### Short Answer (30 seconds)

Temporary credential chaining and external ID for third parties

### Detailed Answer (3–5 minutes)

**Topic:** STS AssumeRole Chain
**Focus:** Temporary credential chaining and external ID for third parties

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for STS AssumeRole Chain?

### Architecture Perspective

STS AssumeRole Chain is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of STS AssumeRole Chain?**
2. **Common production mistake with STS AssumeRole Chain?**

### Common Mistakes in Interviews

- Confusing STS AssumeRole Chain with adjacent service
- Console-only knowledge without design rationale
- No monitoring for STS AssumeRole Chain failures

---

## Q049: Control Tower Customizations Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Landing Zone |
| **Frequency** | Very Common |

### Question

What must architects know about Control Tower Customizations?

### Short Answer (30 seconds)

CfCT manifest extending Account Factory baselines

### Detailed Answer (3–5 minutes)

**Topic:** Control Tower Customizations
**Focus:** CfCT manifest extending Account Factory baselines

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about Control Tower Customizations?

### Architecture Perspective

Control Tower Customizations is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Control Tower Customizations?**
2. **Common production mistake with Control Tower Customizations?**

### Common Mistakes in Interviews

- Confusing Control Tower Customizations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Control Tower Customizations failures

---

## Q050: Control Tower Customizations Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Landing Zone |
| **Frequency** | Very Common |

### Question

How deploy Control Tower Customizations in production enterprise workloads?

### Short Answer (30 seconds)

CfCT manifest extending Account Factory baselines

### Detailed Answer (3–5 minutes)

**Topic:** Control Tower Customizations
**Focus:** CfCT manifest extending Account Factory baselines

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy Control Tower Customizations in production enterprise workloads?

### Architecture Perspective

Control Tower Customizations is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Control Tower Customizations?**
2. **Common production mistake with Control Tower Customizations?**

### Common Mistakes in Interviews

- Confusing Control Tower Customizations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Control Tower Customizations failures

---

## Q051: Control Tower Customizations Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Landing Zone |
| **Frequency** | Common |

### Question

Advanced Control Tower Customizations tuning and edge cases?

### Short Answer (30 seconds)

CfCT manifest extending Account Factory baselines

### Detailed Answer (3–5 minutes)

**Topic:** Control Tower Customizations
**Focus:** CfCT manifest extending Account Factory baselines

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced Control Tower Customizations tuning and edge cases?

### Architecture Perspective

Control Tower Customizations is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Control Tower Customizations?**
2. **Common production mistake with Control Tower Customizations?**

### Common Mistakes in Interviews

- Confusing Control Tower Customizations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Control Tower Customizations failures

---

## Q052: Control Tower Customizations Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Landing Zone |
| **Frequency** | Common |

### Question

Architecture trade-offs for Control Tower Customizations?

### Short Answer (30 seconds)

CfCT manifest extending Account Factory baselines

### Detailed Answer (3–5 minutes)

**Topic:** Control Tower Customizations
**Focus:** CfCT manifest extending Account Factory baselines

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for Control Tower Customizations?

### Architecture Perspective

Control Tower Customizations is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Control Tower Customizations?**
2. **Common production mistake with Control Tower Customizations?**

### Common Mistakes in Interviews

- Confusing Control Tower Customizations with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Control Tower Customizations failures

---

## Q053: AWS Artifact Compliance Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

What must architects know about AWS Artifact Compliance?

### Short Answer (30 seconds)

SOC and ISO report access for customer audits

### Detailed Answer (3–5 minutes)

**Topic:** AWS Artifact Compliance
**Focus:** SOC and ISO report access for customer audits

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about AWS Artifact Compliance?

### Architecture Perspective

AWS Artifact Compliance is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Artifact Compliance?**
2. **Common production mistake with AWS Artifact Compliance?**

### Common Mistakes in Interviews

- Confusing AWS Artifact Compliance with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Artifact Compliance failures

---

## Q054: AWS Artifact Compliance Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

How deploy AWS Artifact Compliance in production enterprise workloads?

### Short Answer (30 seconds)

SOC and ISO report access for customer audits

### Detailed Answer (3–5 minutes)

**Topic:** AWS Artifact Compliance
**Focus:** SOC and ISO report access for customer audits

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy AWS Artifact Compliance in production enterprise workloads?

### Architecture Perspective

AWS Artifact Compliance is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Artifact Compliance?**
2. **Common production mistake with AWS Artifact Compliance?**

### Common Mistakes in Interviews

- Confusing AWS Artifact Compliance with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Artifact Compliance failures

---

## Q055: AWS Artifact Compliance Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Advanced AWS Artifact Compliance tuning and edge cases?

### Short Answer (30 seconds)

SOC and ISO report access for customer audits

### Detailed Answer (3–5 minutes)

**Topic:** AWS Artifact Compliance
**Focus:** SOC and ISO report access for customer audits

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced AWS Artifact Compliance tuning and edge cases?

### Architecture Perspective

AWS Artifact Compliance is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Artifact Compliance?**
2. **Common production mistake with AWS Artifact Compliance?**

### Common Mistakes in Interviews

- Confusing AWS Artifact Compliance with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Artifact Compliance failures

---

## Q056: AWS Artifact Compliance Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Architecture trade-offs for AWS Artifact Compliance?

### Short Answer (30 seconds)

SOC and ISO report access for customer audits

### Detailed Answer (3–5 minutes)

**Topic:** AWS Artifact Compliance
**Focus:** SOC and ISO report access for customer audits

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for AWS Artifact Compliance?

### Architecture Perspective

AWS Artifact Compliance is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Artifact Compliance?**
2. **Common production mistake with AWS Artifact Compliance?**

### Common Mistakes in Interviews

- Confusing AWS Artifact Compliance with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Artifact Compliance failures

---

## Q057: Service Quotas Management Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

What must architects know about Service Quotas Management?

### Short Answer (30 seconds)

Quota monitoring and increase requests before scale events

### Detailed Answer (3–5 minutes)

**Topic:** Service Quotas Management
**Focus:** Quota monitoring and increase requests before scale events

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about Service Quotas Management?

### Architecture Perspective

Service Quotas Management is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Service Quotas Management?**
2. **Common production mistake with Service Quotas Management?**

### Common Mistakes in Interviews

- Confusing Service Quotas Management with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Service Quotas Management failures

---

## Q058: Service Quotas Management Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

How deploy Service Quotas Management in production enterprise workloads?

### Short Answer (30 seconds)

Quota monitoring and increase requests before scale events

### Detailed Answer (3–5 minutes)

**Topic:** Service Quotas Management
**Focus:** Quota monitoring and increase requests before scale events

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy Service Quotas Management in production enterprise workloads?

### Architecture Perspective

Service Quotas Management is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Service Quotas Management?**
2. **Common production mistake with Service Quotas Management?**

### Common Mistakes in Interviews

- Confusing Service Quotas Management with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Service Quotas Management failures

---

## Q059: Service Quotas Management Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Advanced Service Quotas Management tuning and edge cases?

### Short Answer (30 seconds)

Quota monitoring and increase requests before scale events

### Detailed Answer (3–5 minutes)

**Topic:** Service Quotas Management
**Focus:** Quota monitoring and increase requests before scale events

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced Service Quotas Management tuning and edge cases?

### Architecture Perspective

Service Quotas Management is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Service Quotas Management?**
2. **Common production mistake with Service Quotas Management?**

### Common Mistakes in Interviews

- Confusing Service Quotas Management with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Service Quotas Management failures

---

## Q060: Service Quotas Management Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Architecture trade-offs for Service Quotas Management?

### Short Answer (30 seconds)

Quota monitoring and increase requests before scale events

### Detailed Answer (3–5 minutes)

**Topic:** Service Quotas Management
**Focus:** Quota monitoring and increase requests before scale events

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for Service Quotas Management?

### Architecture Perspective

Service Quotas Management is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Service Quotas Management?**
2. **Common production mistake with Service Quotas Management?**

### Common Mistakes in Interviews

- Confusing Service Quotas Management with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Service Quotas Management failures

---

## Q061: RAM Resource Access Manager Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

What must architects know about RAM Resource Access Manager?

### Short Answer (30 seconds)

Share subnets and Transit Gateway across accounts

### Detailed Answer (3–5 minutes)

**Topic:** RAM Resource Access Manager
**Focus:** Share subnets and Transit Gateway across accounts

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about RAM Resource Access Manager?

### Architecture Perspective

RAM Resource Access Manager is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of RAM Resource Access Manager?**
2. **Common production mistake with RAM Resource Access Manager?**

### Common Mistakes in Interviews

- Confusing RAM Resource Access Manager with adjacent service
- Console-only knowledge without design rationale
- No monitoring for RAM Resource Access Manager failures

---

## Q062: RAM Resource Access Manager Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

How deploy RAM Resource Access Manager in production enterprise workloads?

### Short Answer (30 seconds)

Share subnets and Transit Gateway across accounts

### Detailed Answer (3–5 minutes)

**Topic:** RAM Resource Access Manager
**Focus:** Share subnets and Transit Gateway across accounts

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy RAM Resource Access Manager in production enterprise workloads?

### Architecture Perspective

RAM Resource Access Manager is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of RAM Resource Access Manager?**
2. **Common production mistake with RAM Resource Access Manager?**

### Common Mistakes in Interviews

- Confusing RAM Resource Access Manager with adjacent service
- Console-only knowledge without design rationale
- No monitoring for RAM Resource Access Manager failures

---

## Q063: RAM Resource Access Manager Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Advanced RAM Resource Access Manager tuning and edge cases?

### Short Answer (30 seconds)

Share subnets and Transit Gateway across accounts

### Detailed Answer (3–5 minutes)

**Topic:** RAM Resource Access Manager
**Focus:** Share subnets and Transit Gateway across accounts

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced RAM Resource Access Manager tuning and edge cases?

### Architecture Perspective

RAM Resource Access Manager is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of RAM Resource Access Manager?**
2. **Common production mistake with RAM Resource Access Manager?**

### Common Mistakes in Interviews

- Confusing RAM Resource Access Manager with adjacent service
- Console-only knowledge without design rationale
- No monitoring for RAM Resource Access Manager failures

---

## Q064: RAM Resource Access Manager Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Architecture trade-offs for RAM Resource Access Manager?

### Short Answer (30 seconds)

Share subnets and Transit Gateway across accounts

### Detailed Answer (3–5 minutes)

**Topic:** RAM Resource Access Manager
**Focus:** Share subnets and Transit Gateway across accounts

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for RAM Resource Access Manager?

### Architecture Perspective

RAM Resource Access Manager is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of RAM Resource Access Manager?**
2. **Common production mistake with RAM Resource Access Manager?**

### Common Mistakes in Interviews

- Confusing RAM Resource Access Manager with adjacent service
- Console-only knowledge without design rationale
- No monitoring for RAM Resource Access Manager failures

---

## Q065: IMDSv2 Instance Metadata Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What must architects know about IMDSv2 Instance Metadata?

### Short Answer (30 seconds)

Require session token preventing SSRF credential theft

### Detailed Answer (3–5 minutes)

**Topic:** IMDSv2 Instance Metadata
**Focus:** Require session token preventing SSRF credential theft

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about IMDSv2 Instance Metadata?

### Architecture Perspective

IMDSv2 Instance Metadata is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IMDSv2 Instance Metadata?**
2. **Common production mistake with IMDSv2 Instance Metadata?**

### Common Mistakes in Interviews

- Confusing IMDSv2 Instance Metadata with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IMDSv2 Instance Metadata failures

---

## Q066: IMDSv2 Instance Metadata Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How deploy IMDSv2 Instance Metadata in production enterprise workloads?

### Short Answer (30 seconds)

Require session token preventing SSRF credential theft

### Detailed Answer (3–5 minutes)

**Topic:** IMDSv2 Instance Metadata
**Focus:** Require session token preventing SSRF credential theft

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy IMDSv2 Instance Metadata in production enterprise workloads?

### Architecture Perspective

IMDSv2 Instance Metadata is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IMDSv2 Instance Metadata?**
2. **Common production mistake with IMDSv2 Instance Metadata?**

### Common Mistakes in Interviews

- Confusing IMDSv2 Instance Metadata with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IMDSv2 Instance Metadata failures

---

## Q067: IMDSv2 Instance Metadata Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Advanced IMDSv2 Instance Metadata tuning and edge cases?

### Short Answer (30 seconds)

Require session token preventing SSRF credential theft

### Detailed Answer (3–5 minutes)

**Topic:** IMDSv2 Instance Metadata
**Focus:** Require session token preventing SSRF credential theft

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Advanced IMDSv2 Instance Metadata tuning and edge cases?

### Architecture Perspective

IMDSv2 Instance Metadata is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IMDSv2 Instance Metadata?**
2. **Common production mistake with IMDSv2 Instance Metadata?**

### Common Mistakes in Interviews

- Confusing IMDSv2 Instance Metadata with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IMDSv2 Instance Metadata failures

---

## Q068: IMDSv2 Instance Metadata Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Architecture trade-offs for IMDSv2 Instance Metadata?

### Short Answer (30 seconds)

Require session token preventing SSRF credential theft

### Detailed Answer (3–5 minutes)

**Topic:** IMDSv2 Instance Metadata
**Focus:** Require session token preventing SSRF credential theft

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** Architecture trade-offs for IMDSv2 Instance Metadata?

### Architecture Perspective

IMDSv2 Instance Metadata is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of IMDSv2 Instance Metadata?**
2. **Common production mistake with IMDSv2 Instance Metadata?**

### Common Mistakes in Interviews

- Confusing IMDSv2 Instance Metadata with adjacent service
- Console-only knowledge without design rationale
- No monitoring for IMDSv2 Instance Metadata failures

---

## Q069: GuardDuty Threat Detection Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What must architects know about GuardDuty Threat Detection?

### Short Answer (30 seconds)

ML-based threat findings integrated with Security Hub

### Detailed Answer (3–5 minutes)

**Topic:** GuardDuty Threat Detection
**Focus:** ML-based threat findings integrated with Security Hub

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** What must architects know about GuardDuty Threat Detection?

### Architecture Perspective

GuardDuty Threat Detection is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of GuardDuty Threat Detection?**
2. **Common production mistake with GuardDuty Threat Detection?**

### Common Mistakes in Interviews

- Confusing GuardDuty Threat Detection with adjacent service
- Console-only knowledge without design rationale
- No monitoring for GuardDuty Threat Detection failures

---

## Q070: GuardDuty Threat Detection Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How deploy GuardDuty Threat Detection in production enterprise workloads?

### Short Answer (30 seconds)

ML-based threat findings integrated with Security Hub

### Detailed Answer (3–5 minutes)

**Topic:** GuardDuty Threat Detection
**Focus:** ML-based threat findings integrated with Security Hub

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 17 context:** How deploy GuardDuty Threat Detection in production enterprise workloads?

### Architecture Perspective

GuardDuty Threat Detection is essential Week 17 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of GuardDuty Threat Detection?**
2. **Common production mistake with GuardDuty Threat Detection?**

### Common Mistakes in Interviews

- Confusing GuardDuty Threat Detection with adjacent service
- Console-only knowledge without design rationale
- No monitoring for GuardDuty Threat Detection failures

---
