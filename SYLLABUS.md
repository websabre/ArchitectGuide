# Solution Architect Master Program — Full Syllabus

## Navigation

| Resource | Link |
|----------|------|
| **Start here** | [docs/getting-started/how-to-use-this-guide.md](docs/getting-started/how-to-use-this-guide.md) |
| Documentation hub | [docs/README.md](docs/README.md) |
| Cross-cutting topics | [docs/cross-cutting/README.md](docs/cross-cutting/README.md) |
| Glossary | [docs/reference/glossary.md](docs/reference/glossary.md) |
| Decision frameworks | [docs/reference/decision-frameworks.md](docs/reference/decision-frameworks.md) |
| 52-week map | [CURRICULUM-MAP.md](CURRICULUM-MAP.md) |
| Study plan | [STUDY-PLAN-12-MONTHS.md](STUDY-PLAN-12-MONTHS.md) |
| Week 1 | [weeks/week-01/README.md](weeks/week-01/README.md) |
| Interview prep | [interview-prep/README.md](interview-prep/README.md) |

## Program Levels

| Level | Description | Outcome |
|-------|-------------|---------|
| **Fundamentals** | Core concepts, terminology, basic patterns | Can explain and apply in simple scenarios |
| **Intermediate** | Production patterns, trade-offs, tooling | Can design components independently |
| **Advanced** | Distributed systems, cloud-native, scale | Can design multi-service systems |
| **Expert** | Enterprise governance, cost, DR, leadership | Can lead architecture decisions org-wide |

---

## Phase 1 — Month 1: .NET Foundation & Design Excellence

**Weeks [1–4](weeks/week-01/README.md)** | Phase: [program/phase-01-month-01](program/phase-01-month-01/README.md) | Module: [csharp-dotnet](modules/csharp-dotnet/README.md), [design-patterns-solid](modules/design-patterns-solid/README.md)

### [Week 1](weeks/week-01/README.md): C# Language Mastery for Architects
- Modern C# (12–13): records, pattern matching, nullable reference types
- Memory model, GC, Span/Memory, async/await internals
- Performance implications of language choices
- **Interview focus:** 120 questions on C# internals & design

### [Week 2](weeks/week-02/README.md): .NET Core / .NET 8+ Runtime & Ecosystem
- CLR, BCL, hosting models (Kestrel, IIS, containers)
- Dependency injection, configuration, options pattern
- Minimal APIs vs MVC vs gRPC trade-offs
- **Interview focus:** 150 questions on .NET architecture

### [Week 3](weeks/week-03/README.md): SOLID Principles & Clean Architecture
- SOLID in enterprise .NET codebases
- Clean Architecture, Onion, Hexagonal, Vertical Slice
- CQRS, MediatR, domain boundaries
- **Interview focus:** 130 scenario-based SOLID questions

### [Week 4](weeks/week-04/README.md): Design Patterns (GoF + Enterprise)
- Creational, Structural, Behavioral patterns in C#
- Enterprise patterns: Repository, UoW, Specification, Strategy
- Anti-patterns architects must recognize
- **Capstone:** Refactor a monolith module using patterns

---

## Phase 2 — Month 2: Data & Algorithms

**Weeks [5–8](weeks/week-05/README.md)** | Phase: [program/phase-02-month-02](program/phase-02-month-02/README.md) | Module: [dsa](modules/dsa/README.md), [sql-server](modules/sql-server/README.md), [postgresql](modules/postgresql/README.md) | **Premium Q&A:** [Month 2 Top 50](interview-prep/month-02-top-50-index.md)

### [Week 5](weeks/week-05/README.md): Data Structures for System Design
### [Week 6](weeks/week-06/README.md): Algorithms & Complexity Analysis
### [Week 7](weeks/week-07/README.md): Microsoft SQL Server — Architecture & Tuning
### [Week 8](weeks/week-08/README.md): PostgreSQL & Polyglot Persistence

---

## Phase 3 — Month 3: Azure Fundamentals & Core Services

**Weeks [9–12](weeks/week-09/README.md)** | Phase: [program/phase-03-month-03](program/phase-03-month-03/README.md) | Module: [azure-fundamentals](modules/azure-fundamentals/README.md), [azure-services](modules/azure-services/README.md) | **Premium Q&A:** [Azure Top 50](interview-prep/azure-top-50-index.md)

### [Week 9](weeks/week-09/README.md): Azure Fundamentals & Well-Architected Framework
### [Week 10](weeks/week-10/README.md): Azure Compute & App Services
### [Week 11](weeks/week-11/README.md): Azure Data Platform
### [Week 12](weeks/week-12/README.md): Azure Identity & Key Services Integration — see also [Security](docs/cross-cutting/security/README.md)

---

## Phase 4 — Month 4: Azure Architecture Deep Dive

**Weeks [13–16](weeks/week-13/README.md)** | Phase: [program/phase-04-month-04](program/phase-04-month-04/README.md) | Module: [azure-architecture](modules/azure-architecture/README.md)

### [Week 13](weeks/week-13/README.md): Azure Networking — [Networking fundamentals](docs/cross-cutting/networking-fundamentals/README.md)
### [Week 14](weeks/week-14/README.md): Azure Security Architecture
### [Week 15](weeks/week-15/README.md): Azure Integration & Messaging — [Messaging](docs/cross-cutting/messaging-systems/README.md), [EIP](docs/cross-cutting/enterprise-integration-patterns/README.md)
### [Week 16](weeks/week-16/README.md): Azure Production Capstone — [DR & BCP](docs/cross-cutting/disaster-recovery-bcp/README.md)

---

## Phase 5 — Month 5: AWS Fundamentals & Architecture

**Weeks [17–20](weeks/week-17/README.md)** | Phase: [program/phase-05-month-05](program/phase-05-month-05/README.md) | Module: [aws-fundamentals](modules/aws-fundamentals/README.md), [aws-architecture](modules/aws-architecture/README.md) | **Premium Q&A:** [AWS Top 50](interview-prep/aws-top-50-index.md)

### [Week 17](weeks/week-17/README.md): AWS Fundamentals & Well-Architected Framework
### [Week 18](weeks/week-18/README.md): AWS Compute & Serverless
### [Week 19](weeks/week-19/README.md): AWS Data, Storage & Networking
### [Week 20](weeks/week-20/README.md): Multi-Cloud & Azure vs AWS — [FinOps](docs/cross-cutting/finops-cost-optimization/README.md)

---

## Phase 6 — Month 6: Distributed Systems & Microservices

**Weeks [21–24](weeks/week-21/README.md)** | Phase: [program/phase-06-month-06](program/phase-06-month-06/README.md) | Module: [microservices-distributed-systems](modules/microservices-distributed-systems/README.md), [ddd](modules/ddd/README.md)

### [Week 21](weeks/week-21/README.md): Distributed Systems Fundamentals
### [Week 22](weeks/week-22/README.md): Microservices Architecture
### [Week 23](weeks/week-23/README.md): Domain-Driven Design (DDD)
### [Week 24](weeks/week-24/README.md): Microservices Capstone

---

## Phase 7 — Month 7: Containers, Kubernetes & Linux

**Weeks [25–28](weeks/week-25/README.md)** | Phase: [program/phase-07-month-07](program/phase-07-month-07/README.md) | Module: [docker-kubernetes](modules/docker-kubernetes/README.md), [linux](modules/linux/README.md)

### [Week 25](weeks/week-25/README.md): Docker & Container Architecture
### [Week 26](weeks/week-26/README.md): Kubernetes Fundamentals
### [Week 27](weeks/week-27/README.md): Kubernetes Advanced & Production
### [Week 28](weeks/week-28/README.md): Linux for Architects

---

## Phase 8 — Month 8: DevOps, CI/CD, IaC & Observability

**Weeks [29–32](weeks/week-29/README.md)** | Phase: [program/phase-08-month-08](program/phase-08-month-08/README.md) | Module: [devops-cicd](modules/devops-cicd/README.md), [iac-terraform-bicep](modules/iac-terraform-bicep/README.md), [observability](modules/observability/README.md) | **Premium Q&A:** [DevOps Top 50](interview-prep/devops-top-50-index.md) | **Capstone:** [Month 8 lab](weeks/week-32/labs/lab-32-month8-capstone.md)

### [Week 29](weeks/week-29/README.md): DevOps Culture & Practices
### [Week 30](weeks/week-30/README.md): CI/CD Pipelines
### [Week 31](weeks/week-31/README.md): Infrastructure as Code
### [Week 32](weeks/week-32/README.md): Observability & PowerShell

---

## Phase 9 — Month 9: System Design & Scalability

**Weeks [33–36](weeks/week-33/README.md)** | Phase: [program/phase-09-month-09](program/phase-09-month-09/README.md) | Module: [system-design](modules/system-design/README.md), [caching-messaging](modules/caching-messaging/README.md)

### [Week 33](weeks/week-33/README.md): High-Level System Design Methodology
### [Week 34](weeks/week-34/README.md): Scalability, Caching & CDN — [Performance](docs/cross-cutting/performance-capacity-planning/README.md)
### [Week 35](weeks/week-35/README.md): Messaging & Event-Driven Architecture
### [Week 36](weeks/week-36/README.md): System Design Capstone

---

## Phase 10 — Month 10: AI Architecture & Cloud AI

**Weeks [37–40](weeks/week-37/README.md)** | Phase: [program/phase-10-month-10](program/phase-10-month-10/README.md) | Module: [ai-architecture-rag-llmops](modules/ai-architecture-rag-llmops/README.md)

### [Week 37](weeks/week-37/README.md): AI/ML Architecture Fundamentals
### [Week 38](weeks/week-38/README.md): RAG, Vector Search & LLM Integration
### [Week 39](weeks/week-39/README.md): LLMOps & Responsible AI
### [Week 40](weeks/week-40/README.md): AI Architecture Capstone

---

## Phase 11 — Month 11: Enterprise Case Studies

**Weeks [41–44](weeks/week-41/README.md)** | Phase: [program/phase-11-month-11](program/phase-11-month-11/README.md) | Module: [architecture-documentation](modules/architecture-documentation/README.md), [case-studies](modules/case-studies/README.md)

### [Week 41](weeks/week-41/README.md): Architecture Reviews & ADRs — [C4 & ADRs](docs/cross-cutting/architecture-documentation/README.md)
### [Week 42](weeks/week-42/README.md): FinOps, DR & Performance Engineering
### [Week 43](weeks/week-43/README.md): Frontend Architecture — [React](modules/react/README.md), [Angular](modules/angular/README.md)
### [Week 44](weeks/week-44/README.md): Enterprise Case Study Marathon

---

## Phase 12 — Month 12: Interview Mastery

**Weeks [45–52](weeks/week-45/README.md)** | Phase: [program/phase-12-month-12](program/phase-12-month-12/README.md) | [Interview prep hub](interview-prep/README.md)

### [Weeks 45–47](weeks/week-45/README.md): Technical Interview Intensive
### [Weeks 48–49](weeks/week-48/README.md): Whiteboard & System Design Mock — [whiteboard/](interview-prep/whiteboard/README.md)
### [Weeks 50–51](weeks/week-50/README.md): Leadership & Behavioral — [leadership-governance](docs/cross-cutting/leadership-governance/README.md)
### [Week 52](weeks/week-52/README.md): Final Capstone & Graduation

---

## Interview Question Bank Targets

| Module | Target Q&A Count |
|--------|------------------|
| C# & .NET | 300+ |
| SOLID & Design Patterns | 250+ |
| DSA | 200+ |
| SQL Server & PostgreSQL | 200+ |
| Azure (all) | 400+ |
| AWS (all) | 300+ |
| Microservices & DDD | 250+ |
| Docker & Kubernetes | 200+ |
| DevOps & CI/CD | 150+ |
| System Design | 300+ |
| AI Architecture | 150+ |
| Cross-cutting topics | 200+ |
| Behavioral & Leadership | 100+ |
| **Total** | **3000+** |

**Premium detailed banks:** [Azure Top 50](interview-prep/azure-top-50-index.md) · [AWS Top 50](interview-prep/aws-top-50-index.md) · [Month 2 Top 50](interview-prep/month-02-top-50-index.md) · [DevOps Top 50](interview-prep/devops-top-50-index.md)

---

## Assessment Rubric

Each weekly assessment scores across:

1. **Conceptual understanding** (30%)
2. **Architecture diagram quality** (20%)
3. **Trade-off articulation** (25%)
4. **Production realism** (15%)
5. **Interview communication** (10%)

Pass threshold: **70%** | Expert threshold: **90%**

---

Next: [STUDY-PLAN-12-MONTHS.md](STUDY-PLAN-12-MONTHS.md) | [CURRICULUM-MAP.md](CURRICULUM-MAP.md) | [docs/README.md](docs/README.md)
