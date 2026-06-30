#!/usr/bin/env python3
"""Deepen diagrams/README.md for weeks 5-20 to week-01 quality."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DIAGRAMS = {
    5: """# Week 05 — Data Structures for System Design Diagrams

## 1. Structure Selection for Hot Paths

```mermaid
flowchart TD
    A[Need fast lookup?] --> B{Ordered keys?}
    B -->|Yes| C{Range scans?}
    B -->|No| D[HashMap / Dictionary]
    C -->|Yes| E[B-Tree / Sorted Dictionary]
    C -->|No| F[HashSet]
    D --> G[O1 average get/put]
    E --> H[O log n + ordered iteration]
```

> **Architect note:** In .NET, `Dictionary<K,V>` for general purpose; `SortedDictionary` when you need ordered keys; `ImmutableDictionary` for read-heavy config snapshots.

## 2. Leaderboard — Skip List vs Heap vs Sorted Set

```mermaid
flowchart LR
    subgraph Writes["Score Updates"]
        U[Update score] --> R[Redis ZSET]
    end
    subgraph Reads["Top-N Query"]
        R --> Z[ZRANGEBYSCORE]
        Z --> API[API Response]
    end
```

## 3. Consistent Hashing — Cache Ring

```mermaid
flowchart TB
    subgraph Ring["Hash Ring"]
        N1[Node A]
        N2[Node B]
        N3[Node C]
    end
  Key[cache key hash] --> Ring
  Ring --> N2
```

> **Architect note:** Use virtual nodes (vnodes) to reduce rebalance churn when adding/removing cache nodes.

## 4. Bloom Filter — Duplicate Detection

```mermaid
sequenceDiagram
    participant API
    participant BF as Bloom Filter
    participant DB

    API->>BF: Might exist?
    alt Probably not
        BF-->>API: No
        API->>DB: Insert
    else Maybe yes
        BF-->>API: Yes
        API->>DB: Confirm exists
    end
```

## 5. LRU Cache Eviction

```mermaid
flowchart LR
    Get[Get key] --> Move[Move to MRU]
    Put[Put key] --> Full{At capacity?}
    Full -->|Yes| Evict[Evict LRU]
    Full -->|No| Insert[Insert]
```

## Practice Exercise

Redraw diagrams 1 and 3 from memory. For a 10M-key session store, justify HashMap vs Redis cluster.

---

[← Back to Week 05](../README.md)
""",
    6: """# Week 06 — Algorithms for Architects Diagrams

## 1. Big-O Comparison — API Operations

```mermaid
flowchart LR
    O1[O1 Hash lookup] --> Fast[Cache hit]
    On[O n linear scan] --> Slow[List filter]
    Onlog[O n log n sort] --> Med[Report generation]
    On2[O n² nested loops] --> Bad[Anti-pattern in hot path]
```

## 2. Graph Traversal — Service Dependency Map

```mermaid
flowchart TD
    GW[API Gateway] --> O[Order Svc]
    GW --> C[Catalog Svc]
    O --> P[Payment Svc]
    O --> I[Inventory Svc]
    P --> Ext[Stripe]
```

> **Architect note:** BFS finds shortest dependency path for blast-radius analysis; DFS for cycle detection in build graphs.

## 3. Topological Sort — Deployment Order

```mermaid
flowchart LR
    DB[(Database)] --> Svc[Services]
    Svc --> GW[Gateway]
```

## 4. Sliding Window Rate Limiter

```mermaid
sequenceDiagram
    participant C as Client
    participant RL as Rate Limiter
    participant API

    C->>RL: Request + timestamp
    RL->>RL: Prune window older than 60s
    alt Under limit
        RL->>API: Forward
        API-->>C: 200 OK
    else Over limit
        RL-->>C: 429 Too Many Requests
    end
```

## 5. Sorting Choice Decision Tree

```mermaid
flowchart TD
    A[Need sorted data?] --> B{Dataset fits in memory?}
    B -->|Yes| C{Stable sort needed?}
    B -->|No| D[External sort / DB ORDER BY]
    C -->|Yes| E[Merge sort / TimSort]
    C -->|No| F[QuickSort in-process]
```

## Practice Exercise

Given 3 nested loops over order lines, estimate complexity and propose one O(n) optimization.

---

[← Back to Week 06](../README.md)
""",
    7: """# Week 07 — SQL Server Architecture Diagrams

## 1. Query Execution Path

```mermaid
flowchart LR
    SQL[SQL Query] --> Parser
    Parser --> Optimizer
    Optimizer --> Plan[Execution Plan]
    Plan --> Engine[Storage Engine]
    Engine --> Idx{Index seek?}
    Idx -->|Yes| Fast[Seek + Key Lookup]
    Idx -->|No| Scan[Table Scan]
```

## 2. Index Design — Covering Index

```mermaid
flowchart TB
    Q[SELECT OrderId Status Total WHERE CustomerId = @id]
    Q --> NC[Nonclustered Index on CustomerId INCLUDE Status Total]
    NC --> NoLookup[Key lookup avoided]
```

## 3. Isolation Levels Trade-off

```mermaid
flowchart TD
    RU[READ UNCOMMITTED] --> Dirty[Dirty reads]
    RC[READ COMMITTED] --> Default[Default - blocking writes]
    RR[REPEATABLE READ] --> Phantom[Phantom risk reduced]
    SN[SNAPSHOT] --> Version[Row versioning - readers no block]
```

## 4. Always On Availability Group

```mermaid
flowchart LR
    subgraph Primary["Primary Replica"]
        P[(SQL Primary)]
    end
    subgraph Secondary["Secondary Replicas"]
        S1[(Sync Replica)]
        S2[(Async Replica)]
    end
    App[.NET App] --> Listener[AG Listener]
    Listener --> P
    P -->|sync| S1
    P -->|async| S2
```

## 5. Partitioning Large Tables

```mermaid
flowchart TB
    Orders[Orders Table] --> P2024[Partition 2024]
    Orders --> P2025[Partition 2025]
    Orders --> P2026[Partition 2026]
```

> **Architect note:** Partition elimination requires query filter on partition key (e.g., `OrderDate`).

## Practice Exercise

Draw AG failover flow. When would you choose SNAPSHOT isolation for a reporting API?

---

[← Back to Week 07](../README.md)
""",
    8: """# Week 08 — PostgreSQL Architecture Diagrams

## 1. MVCC Read Consistency

```mermaid
sequenceDiagram
    participant T1 as Txn A
    participant T2 as Txn B
    participant Heap

    T1->>Heap: UPDATE row v1 to v2
    Note over Heap: v1 kept until Txn A commits
    T2->>Heap: SELECT sees v1
    T1->>Heap: COMMIT
    T2->>Heap: SELECT still v1 snapshot
```

## 2. Streaming Replication

```mermaid
flowchart LR
    Primary[(Primary PG)] -->|WAL stream| Replica1[(Hot Standby)]
    Primary -->|async| Replica2[(Read Replica)]
    App[.NET Npgsql] --> PgBouncer[PgBouncer]
    PgBouncer --> Primary
    Reader[Report Svc] --> Replica2
```

## 3. JSONB Document Model

```mermaid
flowchart TB
    Table[products] --> Col[id uuid]
    Table --> Json[attributes jsonb]
    Json --> GIN[GIN Index on attributes]
```

## 4. Vacuum / Bloat Lifecycle

```mermaid
flowchart TD
    Update[UPDATE creates new row version] --> Dead[Dead tuples accumulate]
    Dead --> Autovac[Autovacuum]
    Autovac --> Reclaim[Space reclaim + freeze xid]
```

## 5. Migration from SQL Server

```mermaid
flowchart LR
    SS[SQL Server] --> DMS[Azure DMS / pgloader]
    DMS --> PG[(PostgreSQL)]
    App[EF Core] --> Dual[Dual-write window]
    Dual --> Cutover[DNS cutover]
```

## Practice Exercise

Explain why long-running transactions block vacuum. Design read/write split for 500 RPS API.

---

[← Back to Week 08](../README.md)
""",
    9: """# Week 09 — Azure Fundamentals & WAF Diagrams

## 1. Well-Architected Pillars

```mermaid
flowchart TB
    WAF[Azure WAF] --> R[Reliability]
    WAF --> S[Security]
    WAF --> CO[Cost Optimization]
    WAF --> OP[Operational Excellence]
    WAF --> P[Performance Efficiency]
```

## 2. Landing Zone — Management Groups

```mermaid
flowchart TD
    MG[Management Group Root] --> Prod[Production]
    MG --> NonProd[Non-Production]
    Prod --> SubProd[Subscription: Prod Workloads]
    NonProd --> SubDev[Subscription: Dev/Test]
```

## 3. Hub-Spoke (Intro)

```mermaid
flowchart TB
    Hub[Hub VNet - Firewall VPN] --> Spoke1[Spoke: App]
    Hub --> Spoke2[Spoke: Data]
```

## 4. .NET App on Azure — Baseline

```mermaid
flowchart LR
    User --> FD[Front Door]
    FD --> App[App Service]
    App --> MI[Managed Identity]
    MI --> SQL[(Azure SQL)]
    App --> AI[App Insights]
```

## 5. Resilience — Availability Zones

```mermaid
flowchart TB
    subgraph Region["Azure Region"]
        Z1[Zone 1]
        Z2[Zone 2]
        Z3[Zone 3]
    end
    LB[Load Balancer] --> Z1
    LB --> Z2
    LB --> Z3
```

> **Architect note:** Zone-redundant ≠ region-redundant. Document RTO/RPO per tier.

## Practice Exercise

Sketch a 3-subscription landing zone for a 50-person startup scaling to enterprise.

---

[← Back to Week 09](../README.md)
""",
    10: """# Week 10 — Azure Compute & App Services Diagrams

## 1. App Service vs AKS Decision

```mermaid
flowchart TD
    A[.NET workload] --> B{Need K8s ecosystem?}
    B -->|No| AS[App Service / Container Apps]
    B -->|Yes| AKS[AKS]
    AS --> C[PaaS ops - faster ship]
    AKS --> D[Fine-grained control - more ops]
```

## 2. App Service Scaling

```mermaid
flowchart LR
    Monitor[CPU / Queue Depth] --> Rule[Autoscale Rule]
    Rule --> ScaleOut[Add instances]
    Rule --> ScaleIn[Remove instances]
    ScaleOut --> Plan[App Service Plan]
```

## 3. Deployment Slots

```mermaid
sequenceDiagram
    participant Dev
    participant Staging as Staging Slot
    participant Prod as Production Slot

    Dev->>Staging: Deploy v2
    Dev->>Staging: Warm-up / smoke tests
    Dev->>Prod: Swap slots
    Note over Prod: Instant cutover + rollback via swap back
```

## 4. Container Apps — Dapr Sidecar

```mermaid
flowchart LR
    subgraph Pod
        App[.NET API]
        Dapr[Dapr Sidecar]
    end
    App <--> Dapr
    Dapr --> SB[Service Bus]
    Dapr --> State[State Store]
```

## 5. AKS Ingress Path

```mermaid
flowchart LR
    Internet --> AGIC[App Gateway Ingress]
    AGIC --> Svc[Kubernetes Service]
    Svc --> Pod1[Pod]
    Svc --> Pod2[Pod]
```

## Practice Exercise

When would you choose Container Apps over App Service for a .NET 8 microservice with KEDA scaling on Service Bus queue depth?

---

[← Back to Week 10](../README.md)
""",
    11: """# Week 11 — Azure Data Platform Diagrams

## 1. Polyglot Persistence

```mermaid
flowchart TB
    API[.NET API] --> SQL[(Azure SQL - transactional)]
    API --> Cosmos[(Cosmos DB - session/catalog)]
    API --> Blob[Blob Storage - documents]
    API --> Cache[Redis - hot reads]
```

## 2. Cosmos DB Partition Strategy

```mermaid
flowchart LR
    Doc[Document] --> PK[Partition Key: tenantId]
    PK --> P1[Physical Partition 1]
    PK --> P2[Physical Partition 2]
```

> **Architect note:** Avoid hot partitions — shard high-traffic tenants.

## 3. Event Ingestion to Lake

```mermaid
flowchart LR
    Apps[.NET Services] --> EH[Event Hubs]
    EH --> ADLS[Data Lake Gen2]
    ADLS --> Synapse[Synapse Analytics]
```

## 4. CQRS Read/Write Split

```mermaid
flowchart LR
    Write[Write API] --> SQLW[(SQL Primary)]
    SQLW -->|CDC| Proj[Projection Worker]
    Proj --> CosmosR[(Cosmos Read Model)]
    Read[Read API] --> CosmosR
```

## 5. Backup & DR for Data Tier

```mermaid
flowchart TB
    Primary[(Primary Region DB)] --> Geo[Geo-Replica]
    Primary --> PITR[Point-in-Time Restore]
```

## Practice Exercise

Design partition keys for multi-tenant SaaS orders in Cosmos DB (10K tenants, uneven sizes).

---

[← Back to Week 11](../README.md)
""",
    12: """# Week 12 — Azure Identity & Integration Diagrams

## 1. Entra ID — OAuth Flow for .NET API

```mermaid
sequenceDiagram
    participant User
    participant SPA as Blazor SPA
    participant Entra as Entra ID
    participant API as .NET API

    User->>SPA: Login
    SPA->>Entra: Authorization Code + PKCE
    Entra-->>SPA: Access Token
    SPA->>API: Bearer token
    API->>API: Validate JWT + scopes
```

## 2. Managed Identity to Key Vault

```mermaid
flowchart LR
    App[App Service] --> MI[System-Assigned MI]
    MI --> KV[Key Vault Secrets]
    App --> SQL[(Azure SQL)]
    MI --> SQL
```

## 3. RBAC Layers

```mermaid
flowchart TB
    Sub[Subscription] --> RG[Resource Group]
    RG --> Res[App Service]
    Entra[Entra Group: App-Admins] -->|Role: Contributor| RG
```

## 4. Service Bus — Topics & Subscriptions

```mermaid
flowchart LR
    Pub[Order Service] --> Topic[order-events]
    Topic --> Sub1[inventory-sub]
    Topic --> Sub2[notification-sub]
    Sub1 --> Inv[Inventory Worker]
    Sub2 --> Email[Email Worker]
```

## 5. Event Grid vs Service Bus

```mermaid
flowchart TD
    A[Event type?] --> B{Ordering required?}
    B -->|Yes| SB[Service Bus Queue/Topic]
    B -->|No| EG[Event Grid fan-out]
```

## Practice Exercise

Draw identity flow for a multi-tenant API using `tenantId` claim + per-tenant Key Vault references.

---

[← Back to Week 12](../README.md)
""",
    13: """# Week 13 — Azure Networking Diagrams

## 1. Hub-Spoke Topology

```mermaid
flowchart TB
    subgraph Hub["Hub VNet"]
        FW[Azure Firewall]
        VPN[VPN Gateway]
        DNS[Private DNS Zone]
    end
    subgraph SpokeApp["Spoke: Application"]
        App[App Service VNet Integration]
    end
    subgraph SpokeData["Spoke: Data"]
        SQL[(Private Endpoint SQL)]
    end
    Hub --> SpokeApp
    Hub --> SpokeData
    OnPrem[On-Prem] --> VPN
```

## 2. Private Link Data Path

```mermaid
flowchart LR
    App[App in VNet] --> PE[Private Endpoint]
    PE --> PLS[Private Link Service]
    PLS --> SQL[(Azure SQL)]
    Note[Traffic stays on Microsoft backbone]
```

## 3. NSG Flow — Allow/Deny

```mermaid
flowchart TD
    Req[Inbound 443] --> NSG[NSG Rules]
    NSG -->|Allow AppSubnet| App[App Tier]
    NSG -->|Deny*| Block[Blocked]
```

## 4. Application Gateway + WAF

```mermaid
flowchart LR
    User --> FD[Front Door optional]
    FD --> AGW[App Gateway WAF]
    AGW --> App[Internal App Service]
```

## 5. DNS Private Resolution

```mermaid
flowchart LR
    VM[VM in Spoke] --> DNS[Azure Private DNS]
    DNS --> Name[sql.database.windows.net resolves to private IP]
```

> **Architect note:** Hub owns centralized egress via Firewall — avoid spoke-to-internet bypass.

## Practice Exercise

Compare hub-spoke vs virtual WAN for 15 spokes across 3 regions.

---

[← Back to Week 13](../README.md)
""",
    14: """# Week 14 — Azure Security Architecture Diagrams

## 1. Defense in Depth

```mermaid
flowchart TB
    Edge[WAF / Front Door] --> Id[Entra ID + MFA]
    Id --> Net[NSG + Private Link]
    Net --> App[App Hardening]
    App --> Data[Encryption CMK]
    Data --> Monitor[Defender + Sentinel]
```

## 2. Key Vault — CMK for SQL

```mermaid
sequenceDiagram
    participant SQL as Azure SQL
    participant KV as Key Vault
    participant MI as Managed Identity

    SQL->>MI: Authenticate
    MI->>KV: Wrap/unwrap DEK
    KV-->>SQL: Key material
```

## 3. Zero Trust Request Flow

```mermaid
flowchart LR
    User --> MFA[MFA Verified]
    MFA --> CA[Conditional Access]
    CA --> Token[JWT with risk score]
    Token --> API[API Policy Check]
```

## 4. Secret Rotation

```mermaid
flowchart LR
    KV[Key Vault] --> App[App Service Refs]
    Rot[Rotation Function] --> KV
    App -->|reload on next access| KV
```

## 5. Threat Detection Pipeline

```mermaid
flowchart LR
    Logs[App Insights / Activity Log] --> Sentinel[Microsoft Sentinel]
    Sentinel --> Playbook[Logic App Playbook]
    Playbook --> Ticket[ServiceNow]
```

## Practice Exercise

Map OWASP API Top 10 controls to Azure services for a public .NET API.

---

[← Back to Week 14](../README.md)
""",
    15: """# Week 15 — Azure Integration Patterns Diagrams

## 1. Async Messaging — Outbox

```mermaid
sequenceDiagram
    participant API
    participant DB
    participant Outbox as Outbox Worker
    participant SB as Service Bus

    API->>DB: Commit order + outbox row
    Outbox->>DB: Poll outbox
    Outbox->>SB: Publish event
    Outbox->>DB: Mark sent
```

## 2. Event Grid Fan-Out

```mermaid
flowchart LR
    Blob[Blob Upload] --> EG[Event Grid]
    EG --> Fn1[Function: Virus Scan]
    EG --> Fn2[Function: Thumbnail]
    EG --> LA[Logic App: Notify]
```

## 3. Logic Apps — Enterprise Integration

```mermaid
flowchart LR
    SB[Service Bus] --> LA[Logic App]
    LA --> SAP[SAP Connector]
    LA --> SQL[(SQL)]
```

## 4. API Management Gateway

```mermaid
flowchart LR
    Client --> APIM[API Management]
    APIM -->|rate limit JWT validate| API[Backend .NET API]
```

## 5. Saga via Service Bus Sessions

```mermaid
sequenceDiagram
    participant Orch as Orchestrator
    participant SB as Service Bus Session

    Orch->>SB: Command Reserve
    SB-->>Orch: Reply OK
    Orch->>SB: Command Charge
    SB-->>Orch: Reply FAIL
    Orch->>SB: Compensate Release
```

## Practice Exercise

Choose Event Grid vs Service Bus for order-created notifications to 5 downstream systems.

---

[← Back to Week 15](../README.md)
""",
    16: """# Week 16 — Azure Capstone Architecture Diagrams

## 1. Reference 3-Tier .NET SaaS on Azure

```mermaid
flowchart TB
    User --> FD[Azure Front Door + WAF]
    FD --> App[App Service / AKS]
    App --> MI[Managed Identity]
    MI --> SQL[(Azure SQL)]
    App --> Redis[Azure Cache for Redis]
    App --> SB[Service Bus]
    App --> AI[App Insights]
    App --> KV[Key Vault]
```

## 2. Multi-Region Active-Passive

```mermaid
flowchart LR
    subgraph Primary["East US"]
        PApp[App]
        PDB[(SQL Primary)]
    end
    subgraph DR["West US"]
        DApp[App standby]
        DDB[(SQL Geo-Replica)]
    end
    FD[Front Door] --> PApp
    FD -.->|failover| DApp
    PDB --> DDB
```

## 3. Observability — End to End

```mermaid
flowchart LR
    OTel[OpenTelemetry SDK] --> AI[Application Insights]
    AI --> WB[Workbooks + Alerts]
    AI --> AM[Azure Monitor Action Groups]
```

## 4. CI/CD to Azure

```mermaid
flowchart LR
    GH[GitHub] --> GHA[Actions]
    GHA --> ACR[Container Registry]
    ACR --> AS[App Service Slot]
    GHA --> IaC[Bicep Deploy]
```

## 5. Cost Governance

```mermaid
flowchart TB
    Tags[Resource Tags] --> Cost[Cost Management]
    Budget[Budget Alerts] --> Action[Auto-shutdown dev]
```

## Practice Exercise

Produce a single-page architecture for Week 16 capstone: 3-tier SaaS with DR and observability.

---

[← Back to Week 16](../README.md)
""",
    17: """# Week 17 — AWS Fundamentals Diagrams

## 1. AWS Well-Architected Framework

```mermaid
flowchart TB
    WAF[AWS WAF] --> OPS[Operational Excellence]
    WAF --> SEC[Security]
    WAF --> REL[Reliability]
    WAF --> PERF[Performance]
    WAF --> COST[Cost Optimization]
    WAF --> SUS[Sustainability]
```

## 2. Account Structure

```mermaid
flowchart TD
    Org[AWS Organization] --> Prod[Prod Account]
    Org --> Dev[Dev Account]
    Org --> Sec[Security / Log Archive]
```

## 3. IAM — Least Privilege for .NET on ECS

```mermaid
flowchart LR
    Task[ECS Task Role] --> S3[S3 Read]
    Task --> SM[Secrets Manager]
    Exec[Execution Role] --> ECR[ECR Pull]
```

## 4. Regional Services Layout

```mermaid
flowchart TB
    subgraph Region["us-east-1"]
        ALB[ALB]
        ECS[ECS Fargate]
        RDS[(RDS SQL Server)]
    end
    R53[Route 53] --> ALB
```

## 5. Azure vs AWS Concept Map

```mermaid
flowchart LR
    AS[App Service] --- EB[Elastic Beanstalk / ECS]
    AKS[AKS] --- EKS[EKS]
    SQL[Azure SQL] --- RDS[RDS]
    SB[Service Bus] --- SQS[SQS/SNS]
```

## Practice Exercise

Map Week 9 Azure landing zone to equivalent AWS Organization OU structure.

---

[← Back to Week 17](../README.md)
""",
    18: """# Week 18 — AWS Compute Diagrams

## 1. ECS Fargate — .NET API

```mermaid
flowchart LR
    User --> ALB[Application Load Balancer]
    ALB --> TG[Target Group]
    TG --> Task1[Fargate Task]
    TG --> Task2[Fargate Task]
    Task1 --> RDS[(RDS)]
```

## 2. EKS Ingress

```mermaid
flowchart LR
    Internet --> ALB[AWS LB Controller]
    ALB --> Ing[Ingress]
    Ing --> Svc[Service]
    Svc --> Pod[.NET Pod]
```

## 3. Lambda — Event-Driven

```mermaid
flowchart LR
    S3[S3 Upload] --> SQS[SQS]
    SQS --> Lambda[Lambda .NET 8]
    Lambda --> DDB[(DynamoDB)]
```

## 4. Auto Scaling

```mermaid
flowchart TD
    CW[CloudWatch CPU] --> ASG[Auto Scaling Group]
    ASG --> Add[Scale Out]
    ASG --> Rem[Scale In]
```

## 5. Blue/Green on ECS

```mermaid
sequenceDiagram
    participant CICD
    participant Blue as Blue Service
    participant Green as Green Service
    participant ALB

    CICD->>Green: Deploy new task def
    CICD->>ALB: Shift traffic to Green
    Note over Blue: Drain then decommission
```

## Practice Exercise

When is Lambda wrong for a .NET order API with 200ms p99 SLA and 2K RPS steady state?

---

[← Back to Week 18](../README.md)
""",
    19: """# Week 19 — AWS Data & VPC Diagrams

## 1. VPC — 3-Tier Subnets

```mermaid
flowchart TB
    subgraph VPC
        Pub[Public Subnet - ALB]
        App[Private App Subnet - ECS]
        Data[Private Data Subnet - RDS]
    end
    IGW[Internet Gateway] --> Pub
    NAT[NAT Gateway] --> App
    App --> Data
```

## 2. RDS Multi-AZ

```mermaid
flowchart LR
    Primary[(RDS Primary AZ-a)] --> Standby[(Standby AZ-b)]
    App[.NET App] --> Primary
```

## 3. S3 + CloudFront Static Assets

```mermaid
flowchart LR
    User --> CF[CloudFront]
    CF --> S3[S3 Bucket OAI/OAC]
    User --> ALB[ALB API]
```

## 4. Read Replica Scaling

```mermaid
flowchart LR
    W[Write API] --> Primary[(RDS Primary)]
    Primary --> RR1[(Read Replica)]
    Primary --> RR2[(Read Replica)]
    R[Read API] --> RR1
```

## 5. VPC Endpoints — Private AWS API Access

```mermaid
flowchart LR
    App[Private Subnet] --> VPCE[VPC Endpoint]
    VPCE --> S3[S3 / DynamoDB]
```

> **Architect note:** NAT Gateway egress costs — use VPC endpoints for S3/Dynamo to reduce NAT traffic.

## Practice Exercise

Design VPC CIDR plan for 3 AZs with room for 4 environment expansions.

---

[← Back to Week 19](../README.md)
""",
    20: """# Week 20 — Multi-Cloud Architecture Diagrams

## 1. Active-Active Multi-Cloud (Conceptual)

```mermaid
flowchart TB
    GSLB[Global Load Balancer / Traffic Manager] --> Azure[Azure Region]
    GSLB --> AWS[AWS Region]
    Azure --> DB1[(Azure SQL)]
    AWS --> DB2[(RDS)]
    DB1 <-.->|async repl conflict mgmt| DB2
```

## 2. Cloud-Agnostic Abstraction

```mermaid
flowchart LR
    App[.NET Core API] --> Abs[IStorage IMessaging ICache]
    Abs --> AzureAdp[Azure Adapters]
    Abs --> AWSAdp[AWS Adapters]
```

## 3. DR — Primary Azure, DR AWS

```mermaid
flowchart LR
    Prod[Azure Primary] -->|replicate| DR[AWS DR Warm]
    TM[Traffic Manager] --> Prod
    TM -.->|failover| DR
```

## 4. Observability Across Clouds

```mermaid
flowchart LR
    AzureAI[App Insights] --> OTel[OpenTelemetry Collector]
    AWSXRay[X-Ray / CloudWatch] --> OTel
    OTel --> Grafana[Grafana / Datadog]
```

## 5. Decision — Single vs Multi-Cloud

```mermaid
flowchart TD
    A[Workload] --> B{Regulatory multi-cloud?}
    B -->|No| C[Single cloud + DR region]
    B -->|Yes| D[Multi-cloud with explicit TCO]
    D --> E[Avoid lowest-common-denominator trap]
```

## Practice Exercise

Build a comparison table (5 rows) for the same .NET API on Azure App Service vs AWS ECS Fargate.

---

[← Back to Week 20](../README.md)
""",
}


def main():
    for week, content in DIAGRAMS.items():
        path = ROOT / f"weeks/week-{week:02d}/diagrams/README.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)} ({len(content.splitlines())} lines)")


if __name__ == "__main__":
    main()
