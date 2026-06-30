# Week 19 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: VPC Design (Public/Private Subnets)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Design VPC for 3-tier .NET app (web, API, database)?

### Short Answer (30 seconds)

Public subnets: ALB only. Private subnets: ECS/EC2 app tier. Isolated subnets: RDS. NAT Gateway per AZ (or NAT instance for cost at scale). VPC endpoints for S3/DynamoDB to avoid NAT egress.

### Detailed Answer (3–5 minutes)

**CIDR planning:** /16 VPC, /24 per AZ per tier — room for growth.

**Security:** NACLs stateless edge; security groups stateful per tier.

**Architect:** No public IPs on app instances — ALB is sole public entry.

### Architecture Perspective

VPC design is foundational AWS architect skill.

### Follow-up Questions

1. **IPv6 dual-stack? — Consider for future; plan CIDR carefully.**
2. **Subnet calculator mistakes? — Overlap breaks peering.**

### Common Mistakes in Interviews

- RDS in public subnet
- Single NAT Gateway (AZ SPOF)
- 0.0.0.0/0 open on database SG

---

## Q032: S3 Storage Classes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

Choose S3 storage class for backups, logs, and user uploads?

### Short Answer (30 seconds)

Standard for frequent access uploads. Intelligent-Tiering for unknown patterns. Glacier Instant/Flexible for backups per RTO. Lifecycle policies automate transition.

### Detailed Answer (3–5 minutes)

**Lifecycle example:** Logs → IA after 30d → Glacier after 90d → delete 365d.

**Architect:** Model retrieval cost for Glacier — restore time affects DR drills.

**Security:** Block public access at account level; bucket policies deny insecure transport.

### Architecture Perspective

Storage class choice affects cost and DR.

### Follow-up Questions

1. **S3 Express One Zone? — Ultra-low latency single-AZ — know trade-off.**
2. **Versioning + MFA delete? — Protect against ransomware on critical buckets.**

### Common Mistakes in Interviews

- Standard for all backup data forever
- Public bucket for user uploads
- No lifecycle policy on log buckets

---

## Q033: RDS vs Aurora vs DynamoDB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

When RDS vs Aurora vs DynamoDB for order data?

### Short Answer (30 seconds)

RDS/Aurora: relational orders with joins and transactions. Aurora: higher scale MySQL/Postgres with faster failover. DynamoDB: key-value access patterns at massive scale, not ad-hoc SQL reporting.

### Detailed Answer (3–5 minutes)

**Decision tree:**
- Complex queries + ACID → Aurora PostgreSQL
- Simple key access 100K+ WPS → DynamoDB
- SQL Server requirement → RDS SQL Server

**Architect:** Start relational unless proven access pattern needs NoSQL.

### Architecture Perspective

Database choice is hardest to reverse.

### Follow-up Questions

1. **Aurora Serverless v2? — Variable relational workload.**
2. **DynamoDB single-table design? — Requires access pattern upfront design.**

### Common Mistakes in Interviews

- DynamoDB for reporting-heavy OLTP
- RDS without Multi-AZ in prod
- Ignore connection pool limits on Lambda→RDS

---

## Q034: NAT Gateway vs VPC Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Reduce NAT Gateway costs for S3-heavy workload?

### Short Answer (30 seconds)

Gateway endpoints for S3 and DynamoDB (free). Interface endpoints for other AWS services. Keep NAT only for true internet egress.

### Detailed Answer (3–5 minutes)

**Cost:** NAT Gateway per-AZ hourly + per-GB — adds up at scale.

**Architect:** Endpoint policy least privilege; private DNS for interface endpoints.

**Pattern:** App in private subnet reaches S3 via gateway endpoint — no NAT traversal.

### Architecture Perspective

Egress architecture is FinOps topic.

### Follow-up Questions

1. **Interface endpoint per AZ? — HA vs cost trade-off.**
2. **Egress-only internet gateway? — IPv6 outbound pattern.**

### Common Mistakes in Interviews

- All AWS API traffic through NAT
- No endpoint policies
- Ignore NAT data processing charges

---

## Q035: Route 53 Routing Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Common |

### Question

Route 53 policies for DR failover and geolocation?

### Short Answer (30 seconds)

Failover: primary/secondary health checks. Geolocation: route EU users to eu-west-1. Weighted: canary traffic split. Latency: lowest latency region.

### Detailed Answer (3–5 minutes)

**DR pattern:** Failover record with health check on primary ALB — secondary in passive region.

**Architect:** DNS TTL affects failover speed — lower TTL before migration events.

**Combine with:** Global Accelerator for static anycast entry.

### Architecture Perspective

DNS is architect-level traffic management.

### Follow-up Questions

1. **Alias vs CNAME? — Alias to ALB/CloudFront free.**
2. **Private hosted zones? — Internal service discovery.**

### Common Mistakes in Interviews

- Geolocation without compliance review
- Health check on wrong endpoint
- TTL 86400 during migration weekend

---

## Q036: DynamoDB Partition Key Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | NoSQL |
| **Frequency** | Very Common |

### Question

Design DynamoDB keys for orders table at 50K WPS?

### Short Answer (30 seconds)

Partition key with high cardinality — `orderId` or composite `tenantId#orderId`. Avoid hot partitions (celebrity tenant). GSI for alternate access patterns.

### Detailed Answer (3–5 minutes)

**Anti-pattern:** `status` as partition key — throttling on `PENDING`.

**Patterns:** Write sharding with suffix, GSI for customerId lookup.

**Architect:** Access patterns first — single-table design workshop before schema.

### Architecture Perspective

DynamoDB failures are design failures.

### Follow-up Questions

1. **On-demand vs provisioned? — On-demand for unknown; provisioned + auto scaling for predictable.**
2. **DAX? — Microsecond cache for read-heavy hot keys.**

### Common Mistakes in Interviews

- Low-cardinality partition key
- Scan for reporting in production
- No GSI for secondary access pattern

---

## Q037: S3 Event Notifications

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

User uploads to S3 trigger virus scan and thumbnail. Architecture?

### Short Answer (30 seconds)

S3 event → SQS (buffer) → Lambda scan → second Lambda thumbnail → metadata in DynamoDB. Idempotent consumers; DLQ on failure.

### Detailed Answer (3–5 minutes)

**Why SQS:** Decouple burst uploads from Lambda concurrency.

**Architect:** EventBridge for multi-subscriber; S3 notifications simpler for single consumer.

**Security:** Pre-signed URLs for upload; block public read.

### Architecture Perspective

Event-driven S3 is common interview scenario.

### Follow-up Questions

1. **S3 Event Notifications vs EventBridge? — EventBridge richer filtering.**
2. **Lambda timeout on large files? — Step Functions or ECS for big objects.**

### Common Mistakes in Interviews

- Synchronous Lambda chain on every upload
- No virus scan on user content
- Public read on upload bucket

---

## Q038: RDS Multi-AZ vs Read Replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

RDS Multi-AZ vs read replica — when each?

### Short Answer (30 seconds)

Multi-AZ: synchronous standby for HA failover (same region). Read replicas: async read scale and DR copy (can cross-region).

### Detailed Answer (3–5 minutes)

**HA:** Multi-AZ automatic failover ~60-120s.

**Scale reads:** Replicas with connection router aware of lag.

**Architect:** Multi-AZ for prod OLTP; replicas when read:write > 3:1 and lag tolerable.

### Architecture Perspective

Confusing Multi-AZ with read scaling fails interviews.

### Follow-up Questions

1. **Aurora replicas? — Up to 15; faster failover than RDS.**
2. **Replica lag monitoring? — CloudWatch `ReplicaLag`.**

### Common Mistakes in Interviews

- Read replica for HA instead of Multi-AZ
- Strong consistency reads on replica
- No failover drill documented

---

## Q039: VPC Peering vs Transit Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Connect 8 VPCs across 3 regions. Peering or Transit Gateway?

### Short Answer (30 seconds)

Transit Gateway — full mesh peering doesn't scale (n(n-1)/2 connections). TGW hub-spoke with route tables per environment.

### Detailed Answer (3–5 minutes)

**TGW benefits:** Centralized routing, cross-region peering via TGW peering, shared services VPC attachment.

**Peering:** OK for 2-3 VPCs same region simple case.

**Architect:** Document CIDR non-overlap across entire org upfront.

### Architecture Perspective

Network topology scales with hub-spoke.

### Follow-up Questions

1. **TGW route table segmentation? — Isolate prod/nonprod traffic.**
2. **PrivateLink vs peering? — SaaS consumer pattern different.**

### Common Mistakes in Interviews

- Full mesh peering at 10 VPCs
- Overlapping CIDRs discovered late
- No network diagram maintained

---

## Q040: EBS vs Instance Store

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

When use instance store vs EBS for database EC2?

### Short Answer (30 seconds)

EBS: persistent, snapshots, most workloads. Instance store: ephemeral, highest IOPS local NVMe — cache layers only, data lost on stop.

### Detailed Answer (3–5 minutes)

**Architect:** RDS/Aurora preferred over self-managed DB on EC2 unless extreme customization.

**gp3 vs io2:** gp3 baseline for most; io2 for sustained high IOPS.

**Encryption:** EBS encryption by default — KMS CMK for compliance.

### Architecture Perspective

Storage durability is architect concern.

### Follow-up Questions

1. **EBS Multi-Attach? — io2 only — clustered file systems niche.**
2. **Snapshot lifecycle? — Automate via Data Lifecycle Manager.**

### Common Mistakes in Interviews

- Instance store for production database
- No EBS snapshot DR plan
- Unencrypted volumes in prod

---

## Q041: VPC Lattice Service Network Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about VPC Lattice Service Network?

### Short Answer (30 seconds)

Application-layer service-to-service connectivity

### Detailed Answer (3–5 minutes)

**Topic:** VPC Lattice Service Network
**Focus:** Application-layer service-to-service connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about VPC Lattice Service Network?

### Architecture Perspective

VPC Lattice Service Network is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of VPC Lattice Service Network?**
2. **Common production mistake with VPC Lattice Service Network?**

### Common Mistakes in Interviews

- Confusing VPC Lattice Service Network with adjacent service
- Console-only knowledge without design rationale
- No monitoring for VPC Lattice Service Network failures

---

## Q042: VPC Lattice Service Network Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy VPC Lattice Service Network in production enterprise workloads?

### Short Answer (30 seconds)

Application-layer service-to-service connectivity

### Detailed Answer (3–5 minutes)

**Topic:** VPC Lattice Service Network
**Focus:** Application-layer service-to-service connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy VPC Lattice Service Network in production enterprise workloads?

### Architecture Perspective

VPC Lattice Service Network is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of VPC Lattice Service Network?**
2. **Common production mistake with VPC Lattice Service Network?**

### Common Mistakes in Interviews

- Confusing VPC Lattice Service Network with adjacent service
- Console-only knowledge without design rationale
- No monitoring for VPC Lattice Service Network failures

---

## Q043: VPC Lattice Service Network Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Advanced VPC Lattice Service Network tuning and edge cases?

### Short Answer (30 seconds)

Application-layer service-to-service connectivity

### Detailed Answer (3–5 minutes)

**Topic:** VPC Lattice Service Network
**Focus:** Application-layer service-to-service connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced VPC Lattice Service Network tuning and edge cases?

### Architecture Perspective

VPC Lattice Service Network is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of VPC Lattice Service Network?**
2. **Common production mistake with VPC Lattice Service Network?**

### Common Mistakes in Interviews

- Confusing VPC Lattice Service Network with adjacent service
- Console-only knowledge without design rationale
- No monitoring for VPC Lattice Service Network failures

---

## Q044: VPC Lattice Service Network Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Architecture trade-offs for VPC Lattice Service Network?

### Short Answer (30 seconds)

Application-layer service-to-service connectivity

### Detailed Answer (3–5 minutes)

**Topic:** VPC Lattice Service Network
**Focus:** Application-layer service-to-service connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for VPC Lattice Service Network?

### Architecture Perspective

VPC Lattice Service Network is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of VPC Lattice Service Network?**
2. **Common production mistake with VPC Lattice Service Network?**

### Common Mistakes in Interviews

- Confusing VPC Lattice Service Network with adjacent service
- Console-only knowledge without design rationale
- No monitoring for VPC Lattice Service Network failures

---

## Q045: AWS Network Firewall Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about AWS Network Firewall?

### Short Answer (30 seconds)

Stateful network inspection and domain filtering

### Detailed Answer (3–5 minutes)

**Topic:** AWS Network Firewall
**Focus:** Stateful network inspection and domain filtering

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about AWS Network Firewall?

### Architecture Perspective

AWS Network Firewall is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Network Firewall?**
2. **Common production mistake with AWS Network Firewall?**

### Common Mistakes in Interviews

- Confusing AWS Network Firewall with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Network Firewall failures

---

## Q046: AWS Network Firewall Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy AWS Network Firewall in production enterprise workloads?

### Short Answer (30 seconds)

Stateful network inspection and domain filtering

### Detailed Answer (3–5 minutes)

**Topic:** AWS Network Firewall
**Focus:** Stateful network inspection and domain filtering

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy AWS Network Firewall in production enterprise workloads?

### Architecture Perspective

AWS Network Firewall is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Network Firewall?**
2. **Common production mistake with AWS Network Firewall?**

### Common Mistakes in Interviews

- Confusing AWS Network Firewall with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Network Firewall failures

---

## Q047: AWS Network Firewall Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Advanced AWS Network Firewall tuning and edge cases?

### Short Answer (30 seconds)

Stateful network inspection and domain filtering

### Detailed Answer (3–5 minutes)

**Topic:** AWS Network Firewall
**Focus:** Stateful network inspection and domain filtering

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced AWS Network Firewall tuning and edge cases?

### Architecture Perspective

AWS Network Firewall is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Network Firewall?**
2. **Common production mistake with AWS Network Firewall?**

### Common Mistakes in Interviews

- Confusing AWS Network Firewall with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Network Firewall failures

---

## Q048: AWS Network Firewall Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Architecture trade-offs for AWS Network Firewall?

### Short Answer (30 seconds)

Stateful network inspection and domain filtering

### Detailed Answer (3–5 minutes)

**Topic:** AWS Network Firewall
**Focus:** Stateful network inspection and domain filtering

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for AWS Network Firewall?

### Architecture Perspective

AWS Network Firewall is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of AWS Network Firewall?**
2. **Common production mistake with AWS Network Firewall?**

### Common Mistakes in Interviews

- Confusing AWS Network Firewall with adjacent service
- Console-only knowledge without design rationale
- No monitoring for AWS Network Firewall failures

---

## Q049: Shield Advanced DDoS Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What must architects know about Shield Advanced DDoS?

### Short Answer (30 seconds)

DDoS Response Team and cost protection for scale attacks

### Detailed Answer (3–5 minutes)

**Topic:** Shield Advanced DDoS
**Focus:** DDoS Response Team and cost protection for scale attacks

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about Shield Advanced DDoS?

### Architecture Perspective

Shield Advanced DDoS is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Shield Advanced DDoS?**
2. **Common production mistake with Shield Advanced DDoS?**

### Common Mistakes in Interviews

- Confusing Shield Advanced DDoS with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Shield Advanced DDoS failures

---

## Q050: Shield Advanced DDoS Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How deploy Shield Advanced DDoS in production enterprise workloads?

### Short Answer (30 seconds)

DDoS Response Team and cost protection for scale attacks

### Detailed Answer (3–5 minutes)

**Topic:** Shield Advanced DDoS
**Focus:** DDoS Response Team and cost protection for scale attacks

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy Shield Advanced DDoS in production enterprise workloads?

### Architecture Perspective

Shield Advanced DDoS is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Shield Advanced DDoS?**
2. **Common production mistake with Shield Advanced DDoS?**

### Common Mistakes in Interviews

- Confusing Shield Advanced DDoS with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Shield Advanced DDoS failures

---

## Q051: Shield Advanced DDoS Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Advanced Shield Advanced DDoS tuning and edge cases?

### Short Answer (30 seconds)

DDoS Response Team and cost protection for scale attacks

### Detailed Answer (3–5 minutes)

**Topic:** Shield Advanced DDoS
**Focus:** DDoS Response Team and cost protection for scale attacks

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced Shield Advanced DDoS tuning and edge cases?

### Architecture Perspective

Shield Advanced DDoS is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Shield Advanced DDoS?**
2. **Common production mistake with Shield Advanced DDoS?**

### Common Mistakes in Interviews

- Confusing Shield Advanced DDoS with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Shield Advanced DDoS failures

---

## Q052: Shield Advanced DDoS Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Architecture trade-offs for Shield Advanced DDoS?

### Short Answer (30 seconds)

DDoS Response Team and cost protection for scale attacks

### Detailed Answer (3–5 minutes)

**Topic:** Shield Advanced DDoS
**Focus:** DDoS Response Team and cost protection for scale attacks

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for Shield Advanced DDoS?

### Architecture Perspective

Shield Advanced DDoS is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Shield Advanced DDoS?**
2. **Common production mistake with Shield Advanced DDoS?**

### Common Mistakes in Interviews

- Confusing Shield Advanced DDoS with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Shield Advanced DDoS failures

---

## Q053: Gateway Load Balancer Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about Gateway Load Balancer?

### Short Answer (30 seconds)

Inline third-party security appliance insertion

### Detailed Answer (3–5 minutes)

**Topic:** Gateway Load Balancer
**Focus:** Inline third-party security appliance insertion

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about Gateway Load Balancer?

### Architecture Perspective

Gateway Load Balancer is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Gateway Load Balancer?**
2. **Common production mistake with Gateway Load Balancer?**

### Common Mistakes in Interviews

- Confusing Gateway Load Balancer with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Gateway Load Balancer failures

---

## Q054: Gateway Load Balancer Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy Gateway Load Balancer in production enterprise workloads?

### Short Answer (30 seconds)

Inline third-party security appliance insertion

### Detailed Answer (3–5 minutes)

**Topic:** Gateway Load Balancer
**Focus:** Inline third-party security appliance insertion

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy Gateway Load Balancer in production enterprise workloads?

### Architecture Perspective

Gateway Load Balancer is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Gateway Load Balancer?**
2. **Common production mistake with Gateway Load Balancer?**

### Common Mistakes in Interviews

- Confusing Gateway Load Balancer with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Gateway Load Balancer failures

---

## Q055: Gateway Load Balancer Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Advanced Gateway Load Balancer tuning and edge cases?

### Short Answer (30 seconds)

Inline third-party security appliance insertion

### Detailed Answer (3–5 minutes)

**Topic:** Gateway Load Balancer
**Focus:** Inline third-party security appliance insertion

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced Gateway Load Balancer tuning and edge cases?

### Architecture Perspective

Gateway Load Balancer is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Gateway Load Balancer?**
2. **Common production mistake with Gateway Load Balancer?**

### Common Mistakes in Interviews

- Confusing Gateway Load Balancer with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Gateway Load Balancer failures

---

## Q056: Gateway Load Balancer Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Architecture trade-offs for Gateway Load Balancer?

### Short Answer (30 seconds)

Inline third-party security appliance insertion

### Detailed Answer (3–5 minutes)

**Topic:** Gateway Load Balancer
**Focus:** Inline third-party security appliance insertion

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for Gateway Load Balancer?

### Architecture Perspective

Gateway Load Balancer is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Gateway Load Balancer?**
2. **Common production mistake with Gateway Load Balancer?**

### Common Mistakes in Interviews

- Confusing Gateway Load Balancer with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Gateway Load Balancer failures

---

## Q057: Direct Connect Dedicated Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about Direct Connect Dedicated?

### Short Answer (30 seconds)

Private dedicated hybrid connectivity bypassing internet

### Detailed Answer (3–5 minutes)

**Topic:** Direct Connect Dedicated
**Focus:** Private dedicated hybrid connectivity bypassing internet

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about Direct Connect Dedicated?

### Architecture Perspective

Direct Connect Dedicated is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Direct Connect Dedicated?**
2. **Common production mistake with Direct Connect Dedicated?**

### Common Mistakes in Interviews

- Confusing Direct Connect Dedicated with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Direct Connect Dedicated failures

---

## Q058: Direct Connect Dedicated Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy Direct Connect Dedicated in production enterprise workloads?

### Short Answer (30 seconds)

Private dedicated hybrid connectivity bypassing internet

### Detailed Answer (3–5 minutes)

**Topic:** Direct Connect Dedicated
**Focus:** Private dedicated hybrid connectivity bypassing internet

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy Direct Connect Dedicated in production enterprise workloads?

### Architecture Perspective

Direct Connect Dedicated is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Direct Connect Dedicated?**
2. **Common production mistake with Direct Connect Dedicated?**

### Common Mistakes in Interviews

- Confusing Direct Connect Dedicated with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Direct Connect Dedicated failures

---

## Q059: Direct Connect Dedicated Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Advanced Direct Connect Dedicated tuning and edge cases?

### Short Answer (30 seconds)

Private dedicated hybrid connectivity bypassing internet

### Detailed Answer (3–5 minutes)

**Topic:** Direct Connect Dedicated
**Focus:** Private dedicated hybrid connectivity bypassing internet

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced Direct Connect Dedicated tuning and edge cases?

### Architecture Perspective

Direct Connect Dedicated is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Direct Connect Dedicated?**
2. **Common production mistake with Direct Connect Dedicated?**

### Common Mistakes in Interviews

- Confusing Direct Connect Dedicated with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Direct Connect Dedicated failures

---

## Q060: Direct Connect Dedicated Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Architecture trade-offs for Direct Connect Dedicated?

### Short Answer (30 seconds)

Private dedicated hybrid connectivity bypassing internet

### Detailed Answer (3–5 minutes)

**Topic:** Direct Connect Dedicated
**Focus:** Private dedicated hybrid connectivity bypassing internet

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for Direct Connect Dedicated?

### Architecture Perspective

Direct Connect Dedicated is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Direct Connect Dedicated?**
2. **Common production mistake with Direct Connect Dedicated?**

### Common Mistakes in Interviews

- Confusing Direct Connect Dedicated with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Direct Connect Dedicated failures

---

## Q061: Site-to-Site VPN Backup Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about Site-to-Site VPN Backup?

### Short Answer (30 seconds)

IPsec VPN failover path for hybrid connectivity

### Detailed Answer (3–5 minutes)

**Topic:** Site-to-Site VPN Backup
**Focus:** IPsec VPN failover path for hybrid connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about Site-to-Site VPN Backup?

### Architecture Perspective

Site-to-Site VPN Backup is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Site-to-Site VPN Backup?**
2. **Common production mistake with Site-to-Site VPN Backup?**

### Common Mistakes in Interviews

- Confusing Site-to-Site VPN Backup with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Site-to-Site VPN Backup failures

---

## Q062: Site-to-Site VPN Backup Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy Site-to-Site VPN Backup in production enterprise workloads?

### Short Answer (30 seconds)

IPsec VPN failover path for hybrid connectivity

### Detailed Answer (3–5 minutes)

**Topic:** Site-to-Site VPN Backup
**Focus:** IPsec VPN failover path for hybrid connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy Site-to-Site VPN Backup in production enterprise workloads?

### Architecture Perspective

Site-to-Site VPN Backup is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Site-to-Site VPN Backup?**
2. **Common production mistake with Site-to-Site VPN Backup?**

### Common Mistakes in Interviews

- Confusing Site-to-Site VPN Backup with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Site-to-Site VPN Backup failures

---

## Q063: Site-to-Site VPN Backup Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Advanced Site-to-Site VPN Backup tuning and edge cases?

### Short Answer (30 seconds)

IPsec VPN failover path for hybrid connectivity

### Detailed Answer (3–5 minutes)

**Topic:** Site-to-Site VPN Backup
**Focus:** IPsec VPN failover path for hybrid connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced Site-to-Site VPN Backup tuning and edge cases?

### Architecture Perspective

Site-to-Site VPN Backup is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Site-to-Site VPN Backup?**
2. **Common production mistake with Site-to-Site VPN Backup?**

### Common Mistakes in Interviews

- Confusing Site-to-Site VPN Backup with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Site-to-Site VPN Backup failures

---

## Q064: Site-to-Site VPN Backup Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Architecture trade-offs for Site-to-Site VPN Backup?

### Short Answer (30 seconds)

IPsec VPN failover path for hybrid connectivity

### Detailed Answer (3–5 minutes)

**Topic:** Site-to-Site VPN Backup
**Focus:** IPsec VPN failover path for hybrid connectivity

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for Site-to-Site VPN Backup?

### Architecture Perspective

Site-to-Site VPN Backup is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Site-to-Site VPN Backup?**
2. **Common production mistake with Site-to-Site VPN Backup?**

### Common Mistakes in Interviews

- Confusing Site-to-Site VPN Backup with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Site-to-Site VPN Backup failures

---

## Q065: Global Accelerator Anycast Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about Global Accelerator Anycast?

### Short Answer (30 seconds)

Static anycast IP with health-aware regional routing

### Detailed Answer (3–5 minutes)

**Topic:** Global Accelerator Anycast
**Focus:** Static anycast IP with health-aware regional routing

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about Global Accelerator Anycast?

### Architecture Perspective

Global Accelerator Anycast is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Global Accelerator Anycast?**
2. **Common production mistake with Global Accelerator Anycast?**

### Common Mistakes in Interviews

- Confusing Global Accelerator Anycast with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Global Accelerator Anycast failures

---

## Q066: Global Accelerator Anycast Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy Global Accelerator Anycast in production enterprise workloads?

### Short Answer (30 seconds)

Static anycast IP with health-aware regional routing

### Detailed Answer (3–5 minutes)

**Topic:** Global Accelerator Anycast
**Focus:** Static anycast IP with health-aware regional routing

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy Global Accelerator Anycast in production enterprise workloads?

### Architecture Perspective

Global Accelerator Anycast is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Global Accelerator Anycast?**
2. **Common production mistake with Global Accelerator Anycast?**

### Common Mistakes in Interviews

- Confusing Global Accelerator Anycast with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Global Accelerator Anycast failures

---

## Q067: Global Accelerator Anycast Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Advanced Global Accelerator Anycast tuning and edge cases?

### Short Answer (30 seconds)

Static anycast IP with health-aware regional routing

### Detailed Answer (3–5 minutes)

**Topic:** Global Accelerator Anycast
**Focus:** Static anycast IP with health-aware regional routing

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Advanced Global Accelerator Anycast tuning and edge cases?

### Architecture Perspective

Global Accelerator Anycast is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Global Accelerator Anycast?**
2. **Common production mistake with Global Accelerator Anycast?**

### Common Mistakes in Interviews

- Confusing Global Accelerator Anycast with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Global Accelerator Anycast failures

---

## Q068: Global Accelerator Anycast Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Architecture trade-offs for Global Accelerator Anycast?

### Short Answer (30 seconds)

Static anycast IP with health-aware regional routing

### Detailed Answer (3–5 minutes)

**Topic:** Global Accelerator Anycast
**Focus:** Static anycast IP with health-aware regional routing

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** Architecture trade-offs for Global Accelerator Anycast?

### Architecture Perspective

Global Accelerator Anycast is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Global Accelerator Anycast?**
2. **Common production mistake with Global Accelerator Anycast?**

### Common Mistakes in Interviews

- Confusing Global Accelerator Anycast with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Global Accelerator Anycast failures

---

## Q069: CloudFront Edge Caching Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

What must architects know about CloudFront Edge Caching?

### Short Answer (30 seconds)

CDN TLS termination and origin shield patterns

### Detailed Answer (3–5 minutes)

**Topic:** CloudFront Edge Caching
**Focus:** CDN TLS termination and origin shield patterns

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** What must architects know about CloudFront Edge Caching?

### Architecture Perspective

CloudFront Edge Caching is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of CloudFront Edge Caching?**
2. **Common production mistake with CloudFront Edge Caching?**

### Common Mistakes in Interviews

- Confusing CloudFront Edge Caching with adjacent service
- Console-only knowledge without design rationale
- No monitoring for CloudFront Edge Caching failures

---

## Q070: CloudFront Edge Caching Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

How deploy CloudFront Edge Caching in production enterprise workloads?

### Short Answer (30 seconds)

CDN TLS termination and origin shield patterns

### Detailed Answer (3–5 minutes)

**Topic:** CloudFront Edge Caching
**Focus:** CDN TLS termination and origin shield patterns

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 19 context:** How deploy CloudFront Edge Caching in production enterprise workloads?

### Architecture Perspective

CloudFront Edge Caching is essential Week 19 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of CloudFront Edge Caching?**
2. **Common production mistake with CloudFront Edge Caching?**

### Common Mistakes in Interviews

- Confusing CloudFront Edge Caching with adjacent service
- Console-only knowledge without design rationale
- No monitoring for CloudFront Edge Caching failures

---
