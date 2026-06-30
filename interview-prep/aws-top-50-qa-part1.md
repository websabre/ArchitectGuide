# AWS Top 50 Interview Q&A — Detailed Answers (Part 1)

> **Premium bank** — Mirrors [Azure Top 50](azure-top-50-index.md) quality.  
> Covers Weeks 17–20 topics.

| Section | Questions | Topics |
|---------|-----------|--------|
| [Fundamentals & WAF](#section-1-fundamentals--waf) | Q001–Q008 | Organizations, IAM, WAF pillars |
| [Compute](#section-2-compute) | Q009–Q014 | EC2, Lambda, ECS, EKS |
| [Data & Storage](#section-3-data--storage) | Q015–Q020 | S3, RDS, DynamoDB |

**Navigation:** [Part 2](aws-top-50-qa-part2.md) | [Part 3](aws-top-50-qa-part3.md) | [Index](aws-top-50-index.md)

---

## Section 1: Fundamentals & WAF

## Q001: AWS Well-Architected Framework Pillars

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS WAF |
| **Frequency** | Very Common |
| **Week** | 17 |

### Question

What are the six pillars of the AWS Well-Architected Framework? How do they differ from Azure WAF?

### Short Answer (30 seconds)

Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability. AWS adds Sustainability as a sixth pillar; Azure WAF has five. Apply all pillars as a review scorecard for every architecture.

### Detailed Answer (3–5 minutes)

**AWS WAF Six Pillars:**

1. **Operational Excellence** — Run and monitor systems: IaC, CI/CD, runbooks, blameless postmortems, evolve procedures.

2. **Security** — IAM least privilege, encryption, detective controls (GuardDuty, CloudTrail), infrastructure and data protection.

3. **Reliability** — Recover from failures: multi-AZ, auto-scaling, change management, backup, test recovery.

4. **Performance Efficiency** — Right resource types, serverless, global scaling, experiments, remove bottlenecks.

5. **Cost Optimization** — Eliminate waste: right-sizing, Reserved Instances, Savings Plans, Spot for fault-tolerant workloads.

6. **Sustainability** — Minimize environmental impact: efficient resources, serverless, Graviton instances, data transfer reduction.

**Azure comparison:** Azure has Reliability, Security, Cost, Operational Excellence, Performance — no explicit Sustainability pillar (though implied in efficiency).

**Architect application:** Score proposed design 1-5 per pillar. Document accepted trade-offs: "We score lower on Cost due to multi-AZ requirement for 99.99% SLA (Reliability)."

### Architecture Perspective

Multi-cloud architects must know both frameworks — interviewers test breadth. Map pillars when comparing Azure vs AWS designs.

### Follow-up Questions

1. **Well-Architected Review?** AWS offers free WAFR with SA — structured questionnaire per pillar.
2. **Which pillar first for migration?** Security + Operational Excellence (IAM, logging) before Performance optimization.

### Common Mistakes in Interviews

- Listing pillars without application example
- Ignoring Sustainability (AWS-specific question trap)
- Confusing WAFR with AWS Support tiers

---

## Q002: AWS Organizations and Account Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Governance |
| **Frequency** | Common |
| **Week** | 17 |

### Question

How do you structure AWS Organizations for an enterprise with multiple product teams?

### Short Answer

Management account for billing/governance only. OUs for Production, Non-Production, Security. Separate accounts per team/environment. SCPs for guardrails. Control Tower for landing zone automation.

### Detailed Answer

```
Management Account (no workloads)
├── OU: Security
│   ├── Log Archive account (CloudTrail, Config)
│   └── Audit account (GuardDuty admin)
├── OU: Infrastructure
│   ├── Network account (Transit Gateway, VPN)
│   └── Shared Services (CI/CD, ECR)
└── OU: Workloads
    ├── OU: Production
    │   ├── account-prod-payments
    │   └── account-prod-catalog
    └── OU: Non-Production
        ├── account-dev-payments
        └── account-staging-payments
```

**Service Control Policies (SCPs):** IAM permission boundaries at OU level — "deny all except us-east-1 and eu-west-1", "deny root user actions".

**AWS Control Tower:** Automated landing zone — account vending, guardrails, dashboard.

**vs Azure:** Management Groups + Subscriptions — same concepts, different names.

### Follow-up Questions

1. **Account vs VPC isolation?** Account = stronger security boundary. VPC = network isolation within account.
2. **Consolidated billing?** Organizations enables single bill, RI sharing across accounts.

### Common Mistakes

- Running production workloads in management account
- One account for everything — blast radius and cost allocation failure

---

## Q003: IAM Users vs Roles vs Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS IAM |
| **Frequency** | Very Common |
| **Week** | 17 |

### Question

Explain IAM users, roles, and policies. What should you use for an EC2 instance accessing S3?

### Short Answer

Policies define permissions (JSON). Roles are assumable identities with policies attached. Users are long-lived identities — avoid for apps. EC2 uses IAM Role via instance profile — never access keys on disk.

### Detailed Answer

**Policy:** JSON document defining Allow/Deny on actions/resources.
```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

**Role:** Assumed by AWS services or federated users. Temporary credentials via STS.

**User:** Permanent identity with access keys — use for humans only (and prefer SSO). **Never** embed access keys in application code.

**EC2 → S3 pattern:**
1. Create IAM Role with S3 read policy
2. Attach instance profile to EC2
3. SDK uses instance metadata for temporary credentials — auto-rotated

**Lambda:** Execution role. **EKS:** IRSA (IAM Roles for Service Accounts). **Azure equivalent:** Managed Identity.

### Common Mistakes

- Long-lived access keys in Lambda environment variables
- `AdministratorAccess` role for application services
- Not using permission boundaries for human admins

---

## Q004: AWS Shared Responsibility Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS Security |
| **Frequency** | Common |
| **Week** | 17 |

### Question

Explain AWS shared responsibility model for EC2 vs Lambda vs RDS.

### Short Answer

You're always responsible for your data and IAM. EC2: you patch OS. Lambda: AWS patches runtime, you manage code. RDS: AWS patches database engine, you manage schema and access.

### Detailed Answer

| Layer | EC2 | Lambda | RDS |
|-------|-----|--------|-----|
| Physical security | AWS | AWS | AWS |
| Hypervisor | AWS | AWS | AWS |
| OS patching | **You** | AWS | AWS |
| Runtime/App | **You** | **You** (code) | **You** (queries) |
| Network config | **You** | Shared | Shared |
| Data encryption | **You** | **You** | Shared |

**Architect implication:** EC2 = more control, more ops burden. Lambda/RDS = less patching, faster to production.

---

## Q005: AWS Region and AZ Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Infrastructure |
| **Frequency** | Common |
| **Week** | 17 |

### Question

How do you choose AWS regions and Availability Zones?

### Short Answer

Choose region for: latency to users, data residency, service availability, and cost. Deploy across minimum 2 AZs for production HA. Use 3 AZs for critical workloads.

### Detailed Answer

**Region factors:**
- User proximity (eu-west-1 for EU users)
- Compliance (data must stay in EU)
- Service availability (not all services in all regions — check first)
- Cost (us-east-1 often cheapest)

**AZ rules:**
- Minimum 2 AZs for RDS Multi-AZ, ALB, EKS
- AZ failure is real — design for single AZ loss
- AZ names are account-specific (us-east-1a ≠ same physical AZ across accounts)

**Azure mapping:** Region = Azure Region. AZ = Availability Zone. AWS has more regions globally.

---

## Q006: CloudTrail vs CloudWatch vs Config

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Operations |
| **Frequency** | Common |
| **Week** | 17, 32 |

### Question

What's the difference between CloudTrail, CloudWatch, and AWS Config?

### Short Answer

CloudTrail: API audit log (who did what). CloudWatch: metrics, logs, alarms (how system performs). Config: resource configuration history and compliance rules.

### Detailed Answer

| Service | Question Answered | Example |
|---------|-------------------|---------|
| **CloudTrail** | Who deleted that S3 bucket? | API call audit |
| **CloudWatch Logs** | What did app log on error? | Application logs |
| **CloudWatch Metrics** | Is CPU > 80%? | Alarms, dashboards |
| **Config** | Was this SG ever open to 0.0.0.0/0? | Compliance timeline |

**Architect:** Enable CloudTrail org-wide in log archive account. Centralize logs. Config rules for compliance (encrypted volumes, no public S3).

---

## Q007: SCP vs IAM Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Governance |
| **Frequency** | Occasional |
| **Week** | 17 |

### Question

Service Control Policy vs IAM Policy — when each?

### Short Answer

IAM Policy: grants permissions to identities. SCP: sets maximum permissions for entire OU/account — cannot grant, only deny/limit. SCPs don't affect management account or service-linked roles.

### Detailed Answer

**Use SCP:** "No one in this OU can launch EC2 outside us-east-1", "Deny deletion of CloudTrail", "Require IMDSv2 on EC2".

**Use IAM:** "This Lambda role can read from this S3 bucket."

**Together:** SCP is guardrail ceiling. IAM grants within ceiling.

**Azure equivalent:** SCP ≈ Azure Policy at management group (deny effect). IAM ≈ RBAC.

---

## Q008: AWS Pricing Models Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |
| **Week** | 17, 20 |

### Question

Explain AWS on-demand, Reserved, Savings Plans, and Spot pricing.

### Short Answer

On-demand: pay per hour, no commitment. Reserved: 1-3 year commit, ~40% off. Savings Plans: commit to $/hour compute spend, flexible instance families. Spot: spare capacity, ~70-90% off, can be interrupted.

### Detailed Answer

| Model | Commitment | Interruption | Best For |
|-------|------------|--------------|----------|
| On-Demand | None | No | Dev, unpredictable |
| Reserved Instances | 1-3 yr, specific type | No | Stable prod workloads |
| Savings Plans | $/hr commit, flexible | No | Mixed compute |
| Spot | None | Yes (2 min notice) | Batch, CI, stateless workers |

**Architect:** Model 12-month steady-state cost with RI/SP. Use Spot for EKS node groups running fault-tolerant jobs. **Never** Spot for primary user-facing API without interruption handling.

---

*Continued in [Part 2](aws-top-50-qa-part2.md)*
