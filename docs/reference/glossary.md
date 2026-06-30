# Architecture Glossary

> Quick reference for terms used across the program. Expand as you study.

## A

**ADR (Architecture Decision Record)** — Document capturing a significant architecture decision, its context, and consequences.

**AKS (Azure Kubernetes Service)** — Managed Kubernetes on Azure.

**Always On** — SQL Server high-availability feature with readable secondaries.

## B

**BFF (Backend for Frontend)** — API layer tailored to a specific client (web, mobile).

**Bounded Context** — DDD term for explicit boundary within which a domain model applies.

## C

**CAP Theorem** — In a partition, choose Consistency or Availability (not both).

**C4 Model** — Context, Container, Component, Code — architecture documentation hierarchy.

**CQRS** — Command Query Responsibility Segregation — separate read and write models.

## D

**DDD (Domain-Driven Design)** — Approach aligning software design with business domain.

**DR (Disaster Recovery)** — Processes and infrastructure for recovering from failures.

## E

**EF Core** — Entity Framework Core — .NET ORM.

**Event Sourcing** — Store state changes as a sequence of events.

## F

**FinOps** — Cloud financial management practice.

## G

**GC (Garbage Collection)** — .NET memory management — reclaims unused heap objects.

## H

**HPA (Horizontal Pod Autoscaler)** — Kubernetes auto-scaling based on metrics.

## I

**IaC (Infrastructure as Code)** — Managing infrastructure via code (Terraform, Bicep).

**Idempotency** — Operation produces same result regardless of how many times executed.

## J

**JWT (JSON Web Token)** — Compact, self-contained token for claims transmission.

## K

**Kafka** — Distributed event streaming platform.

## L

**LOH (Large Object Heap)** — .NET heap for objects ≥ 85,000 bytes.

**LLMOps** — Operational practices for LLM applications in production.

## M

**mTLS** — Mutual TLS — both client and server authenticate via certificates.

## N

**NRT (Nullable Reference Types)** — C# compile-time null safety feature.

## O

**OIDC (OpenID Connect)** — Identity layer on top of OAuth 2.0.

**OWASP Top 10** — Most critical web application security risks.

## P

**PACELC** — Extension of CAP: else (normal operation), choose Latency or Consistency.

## R

**RAG (Retrieval-Augmented Generation)** — LLM pattern combining retrieval with generation.

**RPO (Recovery Point Objective)** — Max acceptable data loss in time.

**RTO (Recovery Time Objective)** — Max acceptable downtime.

## S

**Saga** — Distributed transaction pattern with compensating actions.

**SLA** — Service Level Agreement.

**SOLID** — OOP design principles (SRP, OCP, LSP, ISP, DIP).

## T

**TLS** — Transport Layer Security — encryption for data in transit.

## V

**VNet** — Azure Virtual Network.

**VPC** — AWS Virtual Private Cloud.

## W

**WAF (Well-Architected Framework)** — Cloud best practices (Azure/AWS/GCP).

**WebSocket** — Full-duplex communication protocol over TCP.

## Z

**Zero Trust** — Security model: never trust, always verify.

---

Add terms as you encounter them. Link to relevant week/module.

---

**Navigation:** [Docs hub](../README.md) | [Decision frameworks](decision-frameworks.md) | [SYLLABUS](../../SYLLABUS.md)
