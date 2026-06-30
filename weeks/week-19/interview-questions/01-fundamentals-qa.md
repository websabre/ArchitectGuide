# Week 19 — Fundamentals Q&A

> Q001–Q030: Premium format (Week 1 quality).
> Cross-reference: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: VPC Design (Public/Private Subnets)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q002: S3 Storage Classes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q003: RDS vs Aurora vs DynamoDB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q004: NAT Gateway vs VPC Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q005: Route 53 Routing Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q006: DynamoDB Partition Key Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q007: S3 Event Notifications

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q008: RDS Multi-AZ vs Read Replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q009: VPC Peering vs Transit Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q010: EBS vs Instance Store

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q011: VPC Flow Logs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Common |

### Question

VPC Flow Logs for security and debugging?

### Short Answer (30 seconds)

Capture accepted/rejected traffic to S3 or CloudWatch. Analyze rejected flows for SG misconfiguration.

### Detailed Answer (3–5 minutes)

**Architect:** Enable on all prod VPCs. Athena queries on S3 parquet flow logs.

**Cost:** Log volume — sample or filter if needed.

### Architecture Perspective

Flow logs prove network debugging skill.

### Follow-up Questions

1. **Custom format fields? — pkt-srcaddr,pkt-dstaddr,action.**
2. **Traffic Mirroring? — Deep packet inspection niche.**

### Common Mistakes in Interviews

- No flow logs prod
- Ignore REJECT patterns
- Overly broad 0.0.0.0/0 undetected

---

## Q012: PrivateLink Interface Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Interface endpoint for SaaS and AWS services?

### Short Answer (30 seconds)

Private connectivity without internet — other AWS accounts publish endpoint service; consumers create interface endpoint in VPC.

### Detailed Answer (3–5 minutes)

**Architect:** Cost per AZ endpoint + data processing — model in TCO.

**Security:** Endpoint policy restricts principals.

### Architecture Perspective

PrivateLink is enterprise connectivity pattern.

### Follow-up Questions

1. **Gateway vs Interface? — S3/Dynamo gateway; most others interface.**
2. **Cross-region endpoint? — PrivateLink limitations apply.**

### Common Mistakes in Interviews

- All traffic over internet to SaaS
- No endpoint policy
- Forget endpoint per-AZ cost

---

## Q013: AWS WAF on ALB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

AWS WAF rules for public API?

### Short Answer (30 seconds)

Managed rule groups (Core, KnownBadInputs), rate-based rule, geo block if needed, custom SQLi/XSS.

### Detailed Answer (3–5 minutes)

**Architect:** WAF in front of ALB/API GW. Log to S3/CloudWatch. Tune false positives in count mode first.

### Architecture Perspective

WAF is edge defense layer.

### Follow-up Questions

1. **WAF vs Shield? — WAF app layer; Shield DDoS.**
2. **Bot Control rule? — Extra cost bot management.**

### Common Mistakes in Interviews

- WAF disabled cost saving
- Block mode day one no tune
- No WAF logs

---

## Q014: Shield Standard vs Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Shield Advanced when justify cost?

### Short Answer (30 seconds)

Standard free DDoS protection all customers. Advanced: cost protection, DRT access, detailed metrics — high revenue sites.

### Detailed Answer (3–5 minutes)

**Architect:** Advanced for DDoS risk business case — ecommerce, fintech. Standard sufficient many B2B APIs.

### Architecture Perspective

DDoS protection is availability topic.

### Follow-up Questions

1. **Route 53 Shield? — DNS layer protection.**
2. **CloudFront + Shield? — Edge combined.**

### Common Mistakes in Interviews

- Assume impossible to DDoS
- Advanced without DRT runbook
- No game day DDoS sim

---

## Q015: S3 Pre-Signed URLs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

Secure large file upload/download with pre-signed URLs?

### Short Answer (30 seconds)

Client requests URL from API; API generates PUT/GET pre-signed with expiry; client uploads direct to S3 — offloads API bandwidth.

### Detailed Answer (3–5 minutes)

**Architect:** Short expiry (15 min). Limit content-type and size. Virus scan on S3 event post-upload.

### Architecture Perspective

Pre-signed pattern is scalable file transfer.

### Follow-up Questions

1. **SSE-KMS pre-signed? — KMS permissions on signer role.**
2. **POST policy alternative? — Browser form upload.**

### Common Mistakes in Interviews

- Public bucket upload
- Long expiry 7 days
- No malware scan user upload

---

## Q016: S3 Cross-Region Replication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DR |
| **Frequency** | Common |

### Question

CRR for compliance and DR?

### Short Answer (30 seconds)

Async replicate objects to second region bucket. Requires versioning both sides. RTC option for tighter RPO.

### Detailed Answer (3–5 minutes)

**Architect:** Replicate encrypted with KMS multi-Region keys plan. Lifecycle on replica bucket.

**Cost:** Replication + storage + egress.

### Architecture Perspective

CRR is DR building block not full failover alone.

### Follow-up Questions

1. **Bidirectional replication? — Conflict handling needed.**
2. **S3 RTC? — 15 min RPO guarantee extra cost.**

### Common Mistakes in Interviews

- Single region prod no backup
- CRR without failover runbook
- Ignore replication lag RPO

---

## Q017: RDS Proxy Connection Pooling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

RDS Proxy for Lambda → RDS connection storm?

### Short Answer (30 seconds)

Proxy pools DB connections; Lambda scales without exhausting max_connections on RDS.

### Detailed Answer (3–5 minutes)

**Architect:** IAM auth through proxy optional. Pin proxy in same VPC private subnets.

**Not for:** All apps — adds latency slight — use when connection count problem proven.

### Architecture Perspective

Connection pooling is serverless + RDS pattern.

### Follow-up Questions

1. **Proxy vs PgBouncer? — AWS managed vs self.**
2. **Read/write splitting proxy? — RDS Proxy targets single cluster.**

### Common Mistakes in Interviews

- 1000 Lambda max connections RDS
- No proxy IAM auth
- Proxy public subnet

---

## Q018: Aurora Global Database

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Common |

### Question

Aurora Global for cross-region DR?

### Short Answer (30 seconds)

Primary region read/write; secondary regions read replica <1s lag typical; promote secondary for DR.

### Detailed Answer (3–5 minutes)

**Architect:** RPO sub-second typical; RTO minutes for promoted cluster. Application DNS failover required.

**Cost:** Secondary cluster running always.

### Architecture Perspective

Global database is premium DR option.

### Follow-up Questions

1. **Write forwarding? — Secondary can forward writes to primary.**
2. **Backtrack? — Rewind cluster mistake — not global.**

### Common Mistakes in Interviews

- Cross-region async only manual
- No promote drill
- App hardcoded primary endpoint

---

## Q019: DynamoDB DAX

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | NoSQL |
| **Frequency** | Occasional |

### Question

When DynamoDB Accelerator (DAX)?

### Short Answer (30 seconds)

Microsecond read cache for DynamoDB hot keys — session store, read-heavy leaderboard.

### Detailed Answer (3–5 minutes)

**Architect:** App must use DAX SDK cluster endpoint. Eventually consistent reads from cache.

**Skip:** If ElastiCache Redis already standard team skill.

### Architecture Perspective

DAX is specialized performance tool.

### Follow-up Questions

1. **DAX vs CloudFront? — Different layers.**
2. **Item cache TTL? — DAX manages invalidation on write.**

### Common Mistakes in Interviews

- DAX for write-heavy workload
- Cache stale reads surprise
- DAX without TLS

---

## Q020: DynamoDB Streams

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Integration |
| **Frequency** | Common |

### Question

DynamoDB Streams use cases?

### Short Answer (30 seconds)

CDC from table — Lambda consumer updates search index, triggers audit, materialized view sync.

### Detailed Answer (3–5 minutes)

**Architect:** Exactly-once processing with idempotent Lambda. Parallelization factor tune.

**Ordering:** Per partition key sequence preserved.

### Architecture Perspective

Streams enable event-driven on NoSQL.

### Follow-up Questions

1. **Stream vs Kinesis? — DynamoDB native vs custom stream.**
2. **TTL deletes in stream? — Yes records appear.**

### Common Mistakes in Interviews

- Poll table scan instead stream
- Non-idempotent consumer
- Ignore iterator age alarm

---

## Q021: ElastiCache Redis Cluster

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Common |

### Question

ElastiCache Redis cluster mode vs single node?

### Short Answer (30 seconds)

Cluster mode: horizontal scale, sharding. Single node: simple session cache small scale.

### Detailed Answer (3–5 minutes)

**Architect:** Multi-AZ with automatic failover production. Auth token enabled. Encryption in transit and at rest.

### Architecture Perspective

Redis architecture affects HA and scale.

### Follow-up Questions

1. **Redis vs Memcached ElastiCache? — Redis data structures richer.**
2. **Global datastore? — Cross-region Redis DR.**

### Common Mistakes in Interviews

- Single node prod cache
- No AUTH token
- Cache as primary database

---

## Q022: Amazon MQ vs MSK

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

ActiveMQ/RabbitMQ (Amazon MQ) vs MSK (Kafka)?

### Short Answer (30 seconds)

Amazon MQ: traditional brokers, JMS, small teams migrating on-prem. MSK: Kafka ecosystem, high throughput event streaming.

### Detailed Answer (3–5 minutes)

**Architect:** MSK for event backbone scale. MQ for legacy JMS integration short term.

### Architecture Perspective

Broker choice is long-term commitment.

### Follow-up Questions

1. **MSK Serverless? — Simpler ops Kafka.**
2. **MQ maintenance? — AWS patches broker.**

### Common Mistakes in Interviews

- Kafka for 10 msgs/day
- MQ for greenfield streaming
- No topic governance MSK

---

## Q023: Direct Connect vs Site-to-Site VPN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

Direct Connect vs VPN for hybrid cloud?

### Short Answer (30 seconds)

DX: dedicated private link, predictable latency, higher setup time/cost. VPN: IPsec over internet, quick, backup path.

### Detailed Answer (3–5 minutes)

**Architect:** DX primary + VPN backup standard enterprise. VIF virtual interfaces routing BGP.

### Architecture Perspective

Hybrid connectivity is architect interview staple.

### Follow-up Questions

1. **DX Gateway? — Connect DX to multi-VPC.**
2. **MACsec encryption? — Line encryption DX.**

### Common Mistakes in Interviews

- VPN only production no redundancy
- DX single location
- No BGP failover test

---

## Q024: Route 53 Health Checks Deep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DNS |
| **Frequency** | Common |

### Question

Route 53 health check types and failover?

### Short Answer (30 seconds)

HTTP/HTTPS, TCP, CloudWatch alarm, calculated health checks combine children.

### Detailed Answer (3–5 minutes)

**Architect:** Health check every 30s; insufficient data handling define. Latency charts for routing decisions.

### Architecture Perspective

DNS health drives failover automation.

### Follow-up Questions

1. **Private health checks? — Internal resources VPC.**
2. **Health check regions? — Multiple probe locations.**

### Common Mistakes in Interviews

- Health check wrong path /
- Failover untested 6 months
- TTL 86400 during migration

---

## Q025: AWS Network Firewall

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Network Firewall vs NACL vs SG?

### Short Answer (30 seconds)

SG: stateful instance level. NACL: stateless subnet edge. Network Firewall: deep inspection, IDS/IPS, domain filtering centralized.

### Detailed Answer (3–5 minutes)

**Architect:** Network Firewall in centralized egress VPC — domain allowlist outbound.

### Architecture Perspective

Layered network security model.

### Follow-up Questions

1. **Suricata rules? — Custom IDS signatures.**
2. **TLS inspection? — Complex compliance need.**

### Common Mistakes in Interviews

- Only SG no defense in depth
- 0.0.0.0/0 egress all
- Firewall misrule blocks prod

---

## Q026: Gateway Load Balancer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Occasional |

### Question

GWLB for inline security appliances?

### Short Answer (30 seconds)

Transparent bump-in-wire scaling third-party firewalls/IDS across VPC.

### Detailed Answer (3–5 minutes)

**Architect:** Niche — regulated industries. Consumer endpoint routes to GWLB endpoint ENI.

### Architecture Perspective

Know GWLB exists for security architecture interviews.

### Follow-up Questions

1. **Endpoint fail open? — Risk if appliance down.**
2. **Vendor appliance AMI? — Partner integrations.**

### Common Mistakes in Interviews

- GWLB for simple API
- Single appliance SPOF
- No health check appliance

---

## Q027: AWS Backup Centralized

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DR |
| **Frequency** | Common |

### Question

AWS Backup for cross-service policy?

### Short Answer (30 seconds)

Central backup plans: EBS, RDS, DynamoDB, EFS, S3 — vault lock immutability, cross-region copy.

### Detailed Answer (3–5 minutes)

**Architect:** Tag-based backup selection `Backup=daily`. Separate vault prod/nonprod.

**Restore drill:** Quarterly restore test documented.

### Architecture Perspective

Unified backup beats per-service scripts.

### Follow-up Questions

1. **Backup Audit Manager? — Compliance reporting.**
2. **Legal hold? — WORM vault lock.**

### Common Mistakes in Interviews

- Manual snapshots only
- Never tested restore
- Backup vault same account delete risk

---

## Q028: EFS vs FSx

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Storage |
| **Frequency** | Occasional |

### Question

EFS vs FSx for Windows/Lustre?

### Short Answer (30 seconds)

EFS: NFS Linux shared files. FSx Windows: SMB .NET legacy shared files. FSx Lustre: HPC ML high throughput.

### Detailed Answer (3–5 minutes)

**Architect:** EFS for container shared config rare cases. FSx when Windows file share required.

### Architecture Perspective

File storage choice by protocol and performance.

### Follow-up Questions

1. **EFS Infrequent Access? — Cost tier lifecycle.**
2. **FSx backup? — AWS Backup support.**

### Common Mistakes in Interviews

- EFS for database files
- FSx overkill static assets
- No performance mode plan

---

## Q029: Data Transfer Pricing Traps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Hidden AWS data transfer costs?

### Short Answer (30 seconds)

Cross-AZ traffic, NAT Gateway processing, cross-region replication, internet egress, inter-AZ ELB to targets.

### Detailed Answer (3–5 minutes)

**Architect:** Model in architecture review — same-AZ placement where possible; endpoints reduce NAT.

**Calculator:** Pricing calculator before design sign-off.

### Architecture Perspective

Egress ignorance kills cloud budget.

### Follow-up Questions

1. **CloudFront reduce origin egress? — Cache hit ratio.**
2. **PrivateLink data processing? — Still charged.**

### Common Mistakes in Interviews

- Chatty cross-AZ microservices
- No cost allocation tags
- Surprise NAT GB bill

---

## Q030: Network Architecture Review Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Process |
| **Frequency** | Common |

### Question

Network architecture review checklist?

### Short Answer (30 seconds)

CIDR plan, subnet tiers, SG least privilege, NACL defense, endpoints vs NAT, flow logs, WAF, hybrid connectivity, DR DNS.

### Detailed Answer (3–5 minutes)

**Architect deliverable:** Diagram + table of every ingress/egress path with justification.

**Security:** No 0.0.0.0/0 on admin ports.

### Architecture Perspective

Checklist shows thorough senior review.

### Follow-up Questions

1. **IPAM integration? — Prevent overlap multi-VPC.**
2. **Network segmentation test? — Pen test validation.**

### Common Mistakes in Interviews

- Flat network all public
- Diagram outdated
- Review once never again

---
