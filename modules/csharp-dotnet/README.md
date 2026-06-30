# C# & .NET Module

| Attribute | Value |
|-----------|-------|
| **Module ID** | `csharp-dotnet` |
| **Weeks** | 1–2 |
| **Level** | Fundamentals → Expert |
| **Prerequisites** | 3+ years C# development |
| **Interview Q&A Target** | 300+ |

## Overview

C# and .NET are the foundation for architects coming from a Microsoft stack. This module goes beyond syntax — it teaches how language and runtime decisions affect **scalability**, **latency**, **memory**, **deployment**, and **team velocity**.

Senior developers know how to write C#. Architects know **when and why** to choose specific C# constructs for a given system's non-functional requirements.

## Learning Objectives

- [ ] Explain CLR, GC, and async internals and their architectural impact
- [ ] Select appropriate type strategies (struct/class/record) for domain models
- [ ] Evaluate .NET hosting models for deployment scenarios
- [ ] Compare API styles (Minimal APIs, MVC, gRPC) with trade-offs
- [ ] Make language/platform decisions in architecture reviews

## Topic Map

| # | Topic | Level | Week |
|---|-------|-------|------|
| 1 | Type system, NRT, records | Fundamentals | 1 |
| 2 | Memory model, GC, Span/Memory | Intermediate | 1 |
| 3 | Async/await internals | Advanced | 1 |
| 4 | Performance engineering | Advanced | 1 |
| 5 | CLR, hosting, DI | Intermediate | 2 |
| 6 | Minimal APIs vs MVC vs gRPC | Advanced | 2 |
| 7 | Configuration & options pattern | Intermediate | 2 |
| 8 | Native AOT, trimming | Expert | 2 |

## Key Trade-offs

| Decision | Option A | Option B | Choose A When | Choose B When |
|----------|----------|----------|---------------|---------------|
| DTO type | `record` | `class` | Immutable API models | EF Core entities |
| Hot path data | `record struct` | `class` | Small, high-throughput | Large, identity-bearing |
| API style | Minimal APIs | MVC Controllers | Microservices, simple APIs | Complex routing, filters |
| Inter-service | gRPC | REST JSON | Internal, performance-critical | Public, browser clients |
| Serialization | Source-generated JSON | Reflection JSON | High throughput, AOT | Rapid development |

## Week Content

| Week | Focus | Path |
|------|-------|------|
| 1 | C# Language Mastery | [weeks/week-01](../../weeks/week-01/README.md) |
| 2 | .NET Runtime & Ecosystem | [weeks/week-02](../../weeks/week-02/README.md) |

## Interview Questions Index

| Source | Count | Status |
|--------|-------|--------|
| Week 01 fundamentals | 30 | 🔄 Sample (10 complete) |
| Week 01 intermediate | 40 | 📝 Planned |
| Week 01 advanced | 30 | 📝 Planned |
| Week 02 all levels | 200+ | 📝 Planned |

## Related Modules

- [design-patterns-solid](../design-patterns-solid/README.md) — Week 3–4
- [microservices-distributed-systems](../microservices-distributed-systems/README.md) — Week 21+

## Further Reading

- [CLR via C# — Jeffrey Richter](https://www.amazon.com/CLR-via-C-Jeffrey-Richter/dp/0735667454)
- [.NET Microservices Architecture — Microsoft eBook](https://dotnet.microsoft.com/en-us/learn/aspnet/microservices-architecture)
