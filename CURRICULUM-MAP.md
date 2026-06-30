# 52-Week Curriculum Map

Quick-reference mapping of every week to topics, phase, and primary module.

| Week | Phase | Month | Topic | Module | Difficulty |
|------|-------|-------|-------|--------|------------|
| 01 | 1 | 1 | C# Language Mastery | csharp-dotnet | Fundamentals → Advanced |
| 02 | 1 | 1 | .NET Runtime & Ecosystem | csharp-dotnet | Intermediate |
| 03 | 1 | 1 | SOLID & Clean Architecture | design-patterns-solid | Intermediate → Advanced |
| 04 | 1 | 1 | Design Patterns (GoF + Enterprise) | design-patterns-solid | Advanced |
| 05 | 2 | 2 | Data Structures for System Design | dsa | Fundamentals → Intermediate |
| 06 | 2 | 2 | Algorithms & Complexity | dsa | Intermediate → Advanced |
| 07 | 2 | 2 | SQL Server Architecture & Tuning | sql-server | Intermediate → Advanced |
| 08 | 2 | 2 | PostgreSQL & Polyglot Persistence | postgresql | Intermediate |
| 09 | 3 | 3 | Azure Fundamentals & WAF | azure-fundamentals | Fundamentals |
| 10 | 3 | 3 | Azure Compute & App Services | azure-services | Intermediate |
| 11 | 3 | 3 | Azure Data Platform | azure-services | Intermediate |
| 12 | 3 | 3 | Azure Identity & Integration | azure-fundamentals | Intermediate |
| 13 | 4 | 4 | Azure Networking Architecture | azure-architecture | Advanced |
| 14 | 4 | 4 | Azure Security Architecture | azure-architecture | Advanced |
| 15 | 4 | 4 | Azure Integration & Messaging | azure-architecture | Advanced |
| 16 | 4 | 4 | Azure Production Capstone | azure-architecture | Expert |
| 17 | 5 | 5 | AWS Fundamentals & WAF | aws-fundamentals | Fundamentals |
| 18 | 5 | 5 | AWS Compute & Serverless | aws-fundamentals | Intermediate |
| 19 | 5 | 5 | AWS Data, Storage & Networking | aws-architecture | Intermediate → Advanced |
| 20 | 5 | 5 | Multi-Cloud Architecture | aws-architecture | Expert |
| 21 | 6 | 6 | Distributed Systems Fundamentals | microservices-distributed-systems | Advanced |
| 22 | 6 | 6 | Microservices Architecture | microservices-distributed-systems | Advanced |
| 23 | 6 | 6 | Domain-Driven Design (DDD) | ddd | Advanced |
| 24 | 6 | 6 | Microservices Capstone | microservices-distributed-systems | Expert |
| 25 | 7 | 7 | Docker & Container Architecture | docker-kubernetes | Intermediate |
| 26 | 7 | 7 | Kubernetes Fundamentals | docker-kubernetes | Intermediate → Advanced |
| 27 | 7 | 7 | Kubernetes Advanced & Production | docker-kubernetes | Advanced → Expert |
| 28 | 7 | 7 | Linux for Architects | linux | Intermediate |
| 29 | 8 | 8 | DevOps Culture & Practices | devops-cicd | Intermediate |
| 30 | 8 | 8 | CI/CD Pipelines | devops-cicd | Advanced |
| 31 | 8 | 8 | Infrastructure as Code | iac-terraform-bicep | Advanced |
| 32 | 8 | 8 | Observability & PowerShell | observability | Advanced |
| 33 | 9 | 9 | System Design Methodology | system-design | Advanced |
| 34 | 9 | 9 | Scalability, Caching & CDN | caching-messaging | Advanced |
| 35 | 9 | 9 | Messaging & Event-Driven Architecture | caching-messaging | Advanced → Expert |
| 36 | 9 | 9 | System Design Capstone | system-design | Expert |
| 37 | 10 | 10 | AI/ML Architecture Fundamentals | ai-architecture-rag-llmops | Intermediate |
| 38 | 10 | 10 | RAG, Vector Search & LLM Integration | ai-architecture-rag-llmops | Advanced |
| 39 | 10 | 10 | LLMOps & Responsible AI | ai-architecture-rag-llmops | Advanced |
| 40 | 10 | 10 | AI Architecture Capstone | ai-architecture-rag-llmops | Expert |
| 41 | 11 | 11 | Architecture Reviews & ADRs | architecture-documentation | Expert |
| 42 | 11 | 11 | FinOps, DR & Performance Engineering | finops / DR / performance | Expert |
| 43 | 11 | 11 | Frontend Architecture (React & Angular) | react / angular | Intermediate |
| 44 | 11 | 11 | Enterprise Case Study Marathon | case-studies | Expert |
| 45 | 12 | 12 | Technical Interview Intensive I | interview-prep | Review |
| 46 | 12 | 12 | Technical Interview Intensive II | interview-prep | Review |
| 47 | 12 | 12 | Technical Interview Intensive III | interview-prep | Review |
| 48 | 12 | 12 | Whiteboard Mock Sessions I | interview-prep | Practice |
| 49 | 12 | 12 | Whiteboard Mock Sessions II | interview-prep | Practice |
| 50 | 12 | 12 | Leadership & Behavioral I | leadership-governance | Practice |
| 51 | 12 | 12 | Leadership & Behavioral II | leadership-governance | Practice |
| 52 | 12 | 12 | Final Capstone & Graduation | all | Expert |

---

## Cross-Cutting Topic Integration

Topics that appear across multiple weeks:

| Topic | Primary Weeks | Also Referenced In | Deep-dive |
|-------|---------------|-------------------|-----------|
| Networking (TCP/IP, DNS, TLS) | 13, 19, 28 | 09, 16, 20, 33 | [docs/cross-cutting/networking-fundamentals](docs/cross-cutting/networking-fundamentals/README.md) |
| Security (OAuth, JWT, Zero Trust) | 12, 14, 32 | 03, 16, 20, 41 | [docs/cross-cutting/security](docs/cross-cutting/security/README.md) |
| Enterprise Integration Patterns | 15, 35 | 11, 22, 24 | [docs/cross-cutting/enterprise-integration-patterns](docs/cross-cutting/enterprise-integration-patterns/README.md) |
| Messaging (Kafka, Service Bus, SQS) | 15, 35 | 22, 24, 36 | [docs/cross-cutting/messaging-systems](docs/cross-cutting/messaging-systems/README.md) |
| Performance & Capacity Planning | 06, 34, 42 | 07, 16, 33 | [docs/cross-cutting/performance-capacity-planning](docs/cross-cutting/performance-capacity-planning/README.md) |
| Disaster Recovery & BCP | 16, 42 | 07, 13, 20 | [docs/cross-cutting/disaster-recovery-bcp](docs/cross-cutting/disaster-recovery-bcp/README.md) |
| FinOps & Cost Optimization | 20, 42 | 09, 16, 39 | [docs/cross-cutting/finops-cost-optimization](docs/cross-cutting/finops-cost-optimization/README.md) |
| Architecture Documentation (C4, ADR) | 41 | 03, 16, 24, 44 | [docs/cross-cutting/architecture-documentation](docs/cross-cutting/architecture-documentation/README.md) |
| Leadership & Governance | 50, 51 | 41, 44, 52 | [docs/cross-cutting/leadership-governance](docs/cross-cutting/leadership-governance/README.md) |

---

## Difficulty Progression

```
Weeks 01-08   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Fundamentals + Intermediate
Weeks 09-16   ████████████████░░░░░░░░░░░░░░░░░░░░░░░░  Azure (Fund → Expert)
Weeks 17-24   ████████████████████████░░░░░░░░░░░░░░░░  AWS + Distributed (Adv → Expert)
Weeks 25-32   ████████████████████████████████░░░░░░░░░░  Platform + DevOps (Adv)
Weeks 33-40   ████████████████████████████████████████░░  System Design + AI (Expert)
Weeks 41-52   ██████████████████████████████████████████  Enterprise + Interview
```

---

## Navigation

- [Week 01](weeks/week-01/README.md) → Start here
- [docs/README.md](docs/README.md) → Documentation hub
- [SYLLABUS.md](SYLLABUS.md) → Full topic breakdown
- [STUDY-PLAN-12-MONTHS.md](STUDY-PLAN-12-MONTHS.md) → Monthly deliverables
