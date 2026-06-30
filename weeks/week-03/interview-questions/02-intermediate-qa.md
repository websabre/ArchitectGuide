# Week 03 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Single Responsibility Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

What is Single Responsibility Principle and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Single Responsibility Principle when one reason to change per module. Avoid when god classes with 20 methods. Production example: Separate OrderPricing from OrderPersistence.

### Detailed Answer (3–5 minutes)

**Concept:** Single Responsibility Principle

**When to use:** One reason to change per module

**When to avoid:** God classes with 20 methods

**Production example:** Separate OrderPricing from OrderPersistence

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Single Responsibility Principle to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Single Responsibility Principle with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Single Responsibility Principle overkill? — God classes with 20 methods**
2. **How measure success after adopting Single Responsibility Principle? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Single Responsibility Principle without production example
- Using Single Responsibility Principle when god classes with 20 methods
- No rollback plan when Single Responsibility Principle misconfigured

---

## Q032: Open/Closed Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

What is Open/Closed Principle and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Open/Closed Principle when extend via new types not edits. Avoid when modify switch for every new discount. Production example: IDiscountStrategy implementations.

### Detailed Answer (3–5 minutes)

**Concept:** Open/Closed Principle

**When to use:** Extend via new types not edits

**When to avoid:** Modify switch for every new discount

**Production example:** IDiscountStrategy implementations

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Open/Closed Principle to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Open/Closed Principle with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Open/Closed Principle overkill? — Modify switch for every new discount**
2. **How measure success after adopting Open/Closed Principle? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Open/Closed Principle without production example
- Using Open/Closed Principle when modify switch for every new discount
- No rollback plan when Open/Closed Principle misconfigured

---

## Q033: Liskov Substitution Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Occasional |

### Question

What is Liskov Substitution Principle and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Liskov Substitution Principle when subtypes honor contracts. Avoid when square inherits rectangle incorrectly. Production example: NotSupportedException in override = smell.

### Detailed Answer (3–5 minutes)

**Concept:** Liskov Substitution Principle

**When to use:** Subtypes honor contracts

**When to avoid:** Square inherits Rectangle incorrectly

**Production example:** NotSupportedException in override = smell

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Liskov Substitution Principle to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Liskov Substitution Principle with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Liskov Substitution Principle overkill? — Square inherits Rectangle incorrectly**
2. **How measure success after adopting Liskov Substitution Principle? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Liskov Substitution Principle without production example
- Using Liskov Substitution Principle when square inherits rectangle incorrectly
- No rollback plan when Liskov Substitution Principle misconfigured

---

## Q034: Interface Segregation Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

What is Interface Segregation Principle and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Interface Segregation Principle when small focused interfaces. Avoid when ifatinterface with 30 methods. Production example: IReadOrder vs IWriteOrder split.

### Detailed Answer (3–5 minutes)

**Concept:** Interface Segregation Principle

**When to use:** Small focused interfaces

**When to avoid:** IFatInterface with 30 methods

**Production example:** IReadOrder vs IWriteOrder split

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Interface Segregation Principle to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Interface Segregation Principle with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Interface Segregation Principle overkill? — IFatInterface with 30 methods**
2. **How measure success after adopting Interface Segregation Principle? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Interface Segregation Principle without production example
- Using Interface Segregation Principle when ifatinterface with 30 methods
- No rollback plan when Interface Segregation Principle misconfigured

---

## Q035: Dependency Inversion Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

What is Dependency Inversion Principle and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Dependency Inversion Principle when depend on abstractions. Avoid when new sqlorderrepository in service. Production example: Inject IOrderRepository interface.

### Detailed Answer (3–5 minutes)

**Concept:** Dependency Inversion Principle

**When to use:** Depend on abstractions

**When to avoid:** new SqlOrderRepository in service

**Production example:** Inject IOrderRepository interface

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Dependency Inversion Principle to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Dependency Inversion Principle with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Dependency Inversion Principle overkill? — new SqlOrderRepository in service**
2. **How measure success after adopting Dependency Inversion Principle? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Dependency Inversion Principle without production example
- Using Dependency Inversion Principle when new sqlorderrepository in service
- No rollback plan when Dependency Inversion Principle misconfigured

---

## Q036: Clean Architecture layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Clean Arch |
| **Frequency** | Occasional |

### Question

What is Clean Architecture layers and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Clean Architecture layers when domain-centric dependency rule. Avoid when domain references ef core. Production example: Domain has zero infrastructure refs.

### Detailed Answer (3–5 minutes)

**Concept:** Clean Architecture layers

**When to use:** Domain-centric dependency rule

**When to avoid:** Domain references EF Core

**Production example:** Domain has zero infrastructure refs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Clean Architecture layers to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Clean Architecture layers with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Clean Architecture layers overkill? — Domain references EF Core**
2. **How measure success after adopting Clean Architecture layers? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Clean Architecture layers without production example
- Using Clean Architecture layers when domain references ef core
- No rollback plan when Clean Architecture layers misconfigured

---

## Q037: Vertical Slice Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

What is Vertical Slice Architecture and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Vertical Slice Architecture when feature-based folders. Avoid when layer folders for 3 features. Production example: Features/Orders/CreateOrder handler.

### Detailed Answer (3–5 minutes)

**Concept:** Vertical Slice Architecture

**When to use:** Feature-based folders

**When to avoid:** Layer folders for 3 features

**Production example:** Features/Orders/CreateOrder handler

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Vertical Slice Architecture to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Vertical Slice Architecture with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Vertical Slice Architecture overkill? — Layer folders for 3 features**
2. **How measure success after adopting Vertical Slice Architecture? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Vertical Slice Architecture without production example
- Using Vertical Slice Architecture when layer folders for 3 features
- No rollback plan when Vertical Slice Architecture misconfigured

---

## Q038: CQRS logical separation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

What is CQRS logical separation and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use CQRS logical separation when different read/write models. Avoid when cqrs on day-one crud. Production example: MediatR commands vs queries.

### Detailed Answer (3–5 minutes)

**Concept:** CQRS logical separation

**When to use:** Different read/write models

**When to avoid:** CQRS on day-one CRUD

**Production example:** MediatR commands vs queries

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect CQRS logical separation to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify CQRS logical separation with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is CQRS logical separation overkill? — CQRS on day-one CRUD**
2. **How measure success after adopting CQRS logical separation? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting CQRS logical separation without production example
- Using CQRS logical separation when cqrs on day-one crud
- No rollback plan when CQRS logical separation misconfigured

---

## Q039: MediatR pipeline behaviors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Occasional |

### Question

What is MediatR pipeline behaviors and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use MediatR pipeline behaviors when cross-cutting in pipeline. Avoid when duplicate validation per handler. Production example: ValidationBehavior before handler.

### Detailed Answer (3–5 minutes)

**Concept:** MediatR pipeline behaviors

**When to use:** Cross-cutting in pipeline

**When to avoid:** Duplicate validation per handler

**Production example:** ValidationBehavior before handler

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect MediatR pipeline behaviors to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify MediatR pipeline behaviors with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is MediatR pipeline behaviors overkill? — Duplicate validation per handler**
2. **How measure success after adopting MediatR pipeline behaviors? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting MediatR pipeline behaviors without production example
- Using MediatR pipeline behaviors when duplicate validation per handler
- No rollback plan when MediatR pipeline behaviors misconfigured

---

## Q040: Anemic domain model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Anti-Pattern |
| **Frequency** | Very Common |

### Question

What is Anemic domain model and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Anemic domain model when rich entities with behavior. Avoid when all logic in orderservice. Production example: order.Confirm() on aggregate.

### Detailed Answer (3–5 minutes)

**Concept:** Anemic domain model

**When to use:** Rich entities with behavior

**When to avoid:** All logic in OrderService

**Production example:** order.Confirm() on aggregate

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Anemic domain model to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Anemic domain model with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Anemic domain model overkill? — All logic in OrderService**
2. **How measure success after adopting Anemic domain model? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Anemic domain model without production example
- Using Anemic domain model when all logic in orderservice
- No rollback plan when Anemic domain model misconfigured

---

## Q041: Ports and Adapters

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hexagonal |
| **Frequency** | Common |

### Question

What is Ports and Adapters and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Ports and Adapters when isolate infrastructure. Avoid when ef entities in domain. Production example: IOrderPort implemented by SqlAdapter.

### Detailed Answer (3–5 minutes)

**Concept:** Ports and Adapters

**When to use:** Isolate infrastructure

**When to avoid:** EF entities in domain

**Production example:** IOrderPort implemented by SqlAdapter

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Ports and Adapters to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Ports and Adapters with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Ports and Adapters overkill? — EF entities in domain**
2. **How measure success after adopting Ports and Adapters? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Ports and Adapters without production example
- Using Ports and Adapters when ef entities in domain
- No rollback plan when Ports and Adapters misconfigured

---

## Q042: Application layer role

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Clean Arch |
| **Frequency** | Occasional |

### Question

What is Application layer role and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Application layer role when orchestrate use cases. Avoid when business rules in controllers. Production example: CreateOrderHandler coordinates.

### Detailed Answer (3–5 minutes)

**Concept:** Application layer role

**When to use:** Orchestrate use cases

**When to avoid:** Business rules in controllers

**Production example:** CreateOrderHandler coordinates

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Application layer role to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Application layer role with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Application layer role overkill? — Business rules in controllers**
2. **How measure success after adopting Application layer role? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Application layer role without production example
- Using Application layer role when business rules in controllers
- No rollback plan when Application layer role misconfigured

---

## Q043: Domain events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

What is Domain events and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Domain events when capture business facts. Avoid when integration events in domain. Production example: OrderPlaced raised from aggregate.

### Detailed Answer (3–5 minutes)

**Concept:** Domain events

**When to use:** Capture business facts

**When to avoid:** Integration events in domain

**Production example:** OrderPlaced raised from aggregate

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Domain events to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Domain events with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Domain events overkill? — Integration events in domain**
2. **How measure success after adopting Domain events? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Domain events without production example
- Using Domain events when integration events in domain
- No rollback plan when Domain events misconfigured

---

## Q044: Validation placement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design |
| **Frequency** | Common |

### Question

What is Validation placement and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Validation placement when input validation at boundary. Avoid when validation scattered everywhere. Production example: FluentValidation on commands.

### Detailed Answer (3–5 minutes)

**Concept:** Validation placement

**When to use:** Input validation at boundary

**When to avoid:** Validation scattered everywhere

**Production example:** FluentValidation on commands

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Validation placement to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Validation placement with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Validation placement overkill? — Validation scattered everywhere**
2. **How measure success after adopting Validation placement? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Validation placement without production example
- Using Validation placement when validation scattered everywhere
- No rollback plan when Validation placement misconfigured

---

## Q045: Exception handling strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design |
| **Frequency** | Occasional |

### Question

What is Exception handling strategy and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Exception handling strategy when consistent error responses. Avoid when try/catch per controller. Production example: Global exception middleware + ProblemDetails.

### Detailed Answer (3–5 minutes)

**Concept:** Exception handling strategy

**When to use:** Consistent error responses

**When to avoid:** try/catch per controller

**Production example:** Global exception middleware + ProblemDetails

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Exception handling strategy to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Exception handling strategy with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Exception handling strategy overkill? — try/catch per controller**
2. **How measure success after adopting Exception handling strategy? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Exception handling strategy without production example
- Using Exception handling strategy when try/catch per controller
- No rollback plan when Exception handling strategy misconfigured

---

## Q046: Mapping strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design |
| **Frequency** | Very Common |

### Question

What is Mapping strategies and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Mapping strategies when dto to domain mapping. Avoid when automapper magic everywhere. Production example: Explicit mapper for complex aggregates.

### Detailed Answer (3–5 minutes)

**Concept:** Mapping strategies

**When to use:** DTO to domain mapping

**When to avoid:** AutoMapper magic everywhere

**Production example:** Explicit mapper for complex aggregates

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Mapping strategies to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Mapping strategies with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Mapping strategies overkill? — AutoMapper magic everywhere**
2. **How measure success after adopting Mapping strategies? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Mapping strategies without production example
- Using Mapping strategies when automapper magic everywhere
- No rollback plan when Mapping strategies misconfigured

---

## Q047: Feature folders

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Organization |
| **Frequency** | Common |

### Question

What is Feature folders and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Feature folders when co-locate feature code. Avoid when giant services folder. Production example: Orders/Create/CreateOrder.cs.

### Detailed Answer (3–5 minutes)

**Concept:** Feature folders

**When to use:** Co-locate feature code

**When to avoid:** Giant Services folder

**Production example:** Orders/Create/CreateOrder.cs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Feature folders to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Feature folders with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Feature folders overkill? — Giant Services folder**
2. **How measure success after adopting Feature folders? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Feature folders without production example
- Using Feature folders when giant services folder
- No rollback plan when Feature folders misconfigured

---

## Q048: Modular monolith

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Occasional |

### Question

What is Modular monolith and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Modular monolith when bounded modules in one deploy. Avoid when microservices too early. Production example: Separate modules with clear APIs.

### Detailed Answer (3–5 minutes)

**Concept:** Modular monolith

**When to use:** Bounded modules in one deploy

**When to avoid:** Microservices too early

**Production example:** Separate modules with clear APIs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Modular monolith to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Modular monolith with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Modular monolith overkill? — Microservices too early**
2. **How measure success after adopting Modular monolith? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Modular monolith without production example
- Using Modular monolith when microservices too early
- No rollback plan when Modular monolith misconfigured

---

## Q049: Testing pyramid in clean arch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Very Common |

### Question

What is Testing pyramid in clean arch and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Testing pyramid in clean arch when unit domain, integration infra. Avoid when e2e only. Production example: Domain unit tests without DB.

### Detailed Answer (3–5 minutes)

**Concept:** Testing pyramid in clean arch

**When to use:** Unit domain, integration infra

**When to avoid:** E2E only

**Production example:** Domain unit tests without DB

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Testing pyramid in clean arch to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Testing pyramid in clean arch with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Testing pyramid in clean arch overkill? — E2E only**
2. **How measure success after adopting Testing pyramid in clean arch? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Testing pyramid in clean arch without production example
- Using Testing pyramid in clean arch when e2e only
- No rollback plan when Testing pyramid in clean arch misconfigured

---

## Q050: EF Core in infrastructure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Persistence |
| **Frequency** | Common |

### Question

What is EF Core in infrastructure and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use EF Core in infrastructure when dbcontext outside domain. Avoid when dbcontext in domain layer. Production example: Infrastructure project owns EF.

### Detailed Answer (3–5 minutes)

**Concept:** EF Core in infrastructure

**When to use:** DbContext outside domain

**When to avoid:** DbContext in domain layer

**Production example:** Infrastructure project owns EF

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect EF Core in infrastructure to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify EF Core in infrastructure with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is EF Core in infrastructure overkill? — DbContext in domain layer**
2. **How measure success after adopting EF Core in infrastructure? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting EF Core in infrastructure without production example
- Using EF Core in infrastructure when dbcontext in domain layer
- No rollback plan when EF Core in infrastructure misconfigured

---

## Q051: Specification pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Occasional |

### Question

What is Specification pattern and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Specification pattern when composable query logic. Avoid when copy-paste linq filters. Production example: ActiveOrdersSpec for repository.

### Detailed Answer (3–5 minutes)

**Concept:** Specification pattern

**When to use:** Composable query logic

**When to avoid:** Copy-paste LINQ filters

**Production example:** ActiveOrdersSpec for repository

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Specification pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Specification pattern with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Specification pattern overkill? — Copy-paste LINQ filters**
2. **How measure success after adopting Specification pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Specification pattern without production example
- Using Specification pattern when copy-paste linq filters
- No rollback plan when Specification pattern misconfigured

---

## Q052: Unit of Work

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

What is Unit of Work and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Unit of Work when atomic transaction boundary. Avoid when multiple savechanges per request. Production example: One UoW per request scope.

### Detailed Answer (3–5 minutes)

**Concept:** Unit of Work

**When to use:** Atomic transaction boundary

**When to avoid:** Multiple SaveChanges per request

**Production example:** One UoW per request scope

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Unit of Work to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Unit of Work with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Unit of Work overkill? — Multiple SaveChanges per request**
2. **How measure success after adopting Unit of Work? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Unit of Work without production example
- Using Unit of Work when multiple savechanges per request
- No rollback plan when Unit of Work misconfigured

---

## Q053: Options pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Common |

### Question

What is Options pattern and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Options pattern when strongly typed settings. Avoid when magic strings for config. Production example: IOptions<PaymentSettings>.

### Detailed Answer (3–5 minutes)

**Concept:** Options pattern

**When to use:** Strongly typed settings

**When to avoid:** magic strings for config

**Production example:** IOptions<PaymentSettings>

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Options pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Options pattern with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Options pattern overkill? — magic strings for config**
2. **How measure success after adopting Options pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Options pattern without production example
- Using Options pattern when magic strings for config
- No rollback plan when Options pattern misconfigured

---

## Q054: Cross-cutting logging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Occasional |

### Question

What is Cross-cutting logging and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Cross-cutting logging when structured logging pipeline. Avoid when console.writeline debug. Production example: Serilog with correlation ID.

### Detailed Answer (3–5 minutes)

**Concept:** Cross-cutting logging

**When to use:** Structured logging pipeline

**When to avoid:** Console.WriteLine debug

**Production example:** Serilog with correlation ID

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Cross-cutting logging to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Cross-cutting logging with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Cross-cutting logging overkill? — Console.WriteLine debug**
2. **How measure success after adopting Cross-cutting logging? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Cross-cutting logging without production example
- Using Cross-cutting logging when console.writeline debug
- No rollback plan when Cross-cutting logging misconfigured

---

## Q055: Health checks design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

What is Health checks design and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Health checks design when liveness vs readiness. Avoid when db check in liveness. Production example: Separate /health/live and /ready.

### Detailed Answer (3–5 minutes)

**Concept:** Health checks design

**When to use:** Liveness vs readiness

**When to avoid:** DB check in liveness

**Production example:** Separate /health/live and /ready

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Health checks design to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Health checks design with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Health checks design overkill? — DB check in liveness**
2. **How measure success after adopting Health checks design? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Health checks design without production example
- Using Health checks design when db check in liveness
- No rollback plan when Health checks design misconfigured

---

## Q056: API versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

What is API versioning and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use API versioning when stable public contracts. Avoid when breaking changes without version. Production example: URL path versioning /v2/.

### Detailed Answer (3–5 minutes)

**Concept:** API versioning

**When to use:** Stable public contracts

**When to avoid:** Breaking changes without version

**Production example:** URL path versioning /v2/

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect API versioning to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify API versioning with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is API versioning overkill? — Breaking changes without version**
2. **How measure success after adopting API versioning? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting API versioning without production example
- Using API versioning when breaking changes without version
- No rollback plan when API versioning misconfigured

---

## Q057: Authorization vs authentication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

What is Authorization vs authentication and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Authorization vs authentication when authn identity authz permissions. Avoid when confuse the two. Production example: Policy-based authorization on handlers.

### Detailed Answer (3–5 minutes)

**Concept:** Authorization vs authentication

**When to use:** AuthN identity AuthZ permissions

**When to avoid:** Confuse the two

**Production example:** Policy-based authorization on handlers

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Authorization vs authentication to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Authorization vs authentication with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Authorization vs authentication overkill? — Confuse the two**
2. **How measure success after adopting Authorization vs authentication? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Authorization vs authentication without production example
- Using Authorization vs authentication when confuse the two
- No rollback plan when Authorization vs authentication misconfigured

---

## Q058: When NOT Clean Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Pragmatism |
| **Frequency** | Very Common |

### Question

What is When NOT Clean Architecture and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use When NOT Clean Architecture when simple crud internal tools. Avoid when ca for 5-endpoint admin. Production example: Pragmatic layering for low complexity.

### Detailed Answer (3–5 minutes)

**Concept:** When NOT Clean Architecture

**When to use:** Simple CRUD internal tools

**When to avoid:** CA for 5-endpoint admin

**Production example:** Pragmatic layering for low complexity

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect When NOT Clean Architecture to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify When NOT Clean Architecture with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is When NOT Clean Architecture overkill? — CA for 5-endpoint admin**
2. **How measure success after adopting When NOT Clean Architecture? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting When NOT Clean Architecture without production example
- Using When NOT Clean Architecture when ca for 5-endpoint admin
- No rollback plan when When NOT Clean Architecture misconfigured

---

## Q059: Onion vs Clean Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Terminology |
| **Frequency** | Common |

### Question

What is Onion vs Clean Architecture and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Onion vs Clean Architecture when same dependency rule. Avoid when religious naming debates. Production example: Focus dependency direction not name.

### Detailed Answer (3–5 minutes)

**Concept:** Onion vs Clean Architecture

**When to use:** Same dependency rule

**When to avoid:** Religious naming debates

**Production example:** Focus dependency direction not name

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Onion vs Clean Architecture to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Onion vs Clean Architecture with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Onion vs Clean Architecture overkill? — Religious naming debates**
2. **How measure success after adopting Onion vs Clean Architecture? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Onion vs Clean Architecture without production example
- Using Onion vs Clean Architecture when religious naming debates
- No rollback plan when Onion vs Clean Architecture misconfigured

---

## Q060: Request response vs domain model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design |
| **Frequency** | Occasional |

### Question

What is Request response vs domain model and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Request response vs domain model when separate api contracts. Avoid when expose ef entities on api. Production example: OrderDto vs Order entity.

### Detailed Answer (3–5 minutes)

**Concept:** Request response vs domain model

**When to use:** Separate API contracts

**When to avoid:** Expose EF entities on API

**Production example:** OrderDto vs Order entity

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Request response vs domain model to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Request response vs domain model with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Request response vs domain model overkill? — Expose EF entities on API**
2. **How measure success after adopting Request response vs domain model? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Request response vs domain model without production example
- Using Request response vs domain model when expose ef entities on api
- No rollback plan when Request response vs domain model misconfigured

---

## Q061: Onion architecture layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Clean Arch |
| **Frequency** | Very Common |

### Question

What is Onion architecture layers and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Onion architecture layers when same dependency rule. Avoid when religious layer count. Production example: Domain core with adapters.

### Detailed Answer (3–5 minutes)

**Concept:** Onion architecture layers

**When to use:** Same dependency rule

**When to avoid:** Religious layer count

**Production example:** Domain core with adapters

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Onion architecture layers to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Onion architecture layers with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Onion architecture layers overkill? — Religious layer count**
2. **How measure success after adopting Onion architecture layers? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Onion architecture layers without production example
- Using Onion architecture layers when religious layer count
- No rollback plan when Onion architecture layers misconfigured

---

## Q062: Bounded context boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Common |

### Question

What is Bounded context boundaries and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Bounded context boundaries when team and model alignment. Avoid when one enterprise model. Production example: Billing vs Support Customer types.

### Detailed Answer (3–5 minutes)

**Concept:** Bounded context boundaries

**When to use:** Team and model alignment

**When to avoid:** One enterprise model

**Production example:** Billing vs Support Customer types

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bounded context boundaries to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bounded context boundaries with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Bounded context boundaries overkill? — One enterprise model**
2. **How measure success after adopting Bounded context boundaries? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bounded context boundaries without production example
- Using Bounded context boundaries when one enterprise model
- No rollback plan when Bounded context boundaries misconfigured

---

## Q063: Aggregate consistency boundary

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Occasional |

### Question

What is Aggregate consistency boundary and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Aggregate consistency boundary when transaction per aggregate. Avoid when cross-aggregate single tx. Production example: Order root owns lines.

### Detailed Answer (3–5 minutes)

**Concept:** Aggregate consistency boundary

**When to use:** Transaction per aggregate

**When to avoid:** Cross-aggregate single TX

**Production example:** Order root owns lines

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Aggregate consistency boundary to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Aggregate consistency boundary with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Aggregate consistency boundary overkill? — Cross-aggregate single TX**
2. **How measure success after adopting Aggregate consistency boundary? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Aggregate consistency boundary without production example
- Using Aggregate consistency boundary when cross-aggregate single tx
- No rollback plan when Aggregate consistency boundary misconfigured

---

## Q064: Value object immutability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

What is Value object immutability and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Value object immutability when money address types. Avoid when primitive obsession. Production example: record Money with currency.

### Detailed Answer (3–5 minutes)

**Concept:** Value object immutability

**When to use:** Money Address types

**When to avoid:** Primitive obsession

**Production example:** record Money with currency

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Value object immutability to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Value object immutability with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Value object immutability overkill? — Primitive obsession**
2. **How measure success after adopting Value object immutability? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Value object immutability without production example
- Using Value object immutability when primitive obsession
- No rollback plan when Value object immutability misconfigured

---

## Q065: Domain service when

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Common |

### Question

What is Domain service when and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Domain service when when logic across entities. Avoid when anemic everything in service. Production example: PricingService for cross-line discount.

### Detailed Answer (3–5 minutes)

**Concept:** Domain service when

**When to use:** Logic across entities

**When to avoid:** Anemic everything in service

**Production example:** PricingService for cross-line discount

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Domain service when to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Domain service when with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Domain service when overkill? — Anemic everything in service**
2. **How measure success after adopting Domain service when? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Domain service when without production example
- Using Domain service when when anemic everything in service
- No rollback plan when Domain service when misconfigured

---

## Q066: Repository interface placement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Clean Arch |
| **Frequency** | Occasional |

### Question

What is Repository interface placement and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Repository interface placement when domain or application debate. Avoid when ef in domain. Production example: IOrderRepository in application layer.

### Detailed Answer (3–5 minutes)

**Concept:** Repository interface placement

**When to use:** Domain or application debate

**When to avoid:** EF in domain

**Production example:** IOrderRepository in application layer

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Repository interface placement to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Repository interface placement with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Repository interface placement overkill? — EF in domain**
2. **How measure success after adopting Repository interface placement? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Repository interface placement without production example
- Using Repository interface placement when ef in domain
- No rollback plan when Repository interface placement misconfigured

---

## Q067: CQRS without event sourcing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CQRS |
| **Frequency** | Very Common |

### Question

What is CQRS without event sourcing and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use CQRS without event sourcing when read write separation. Avoid when cqrs day one two tables. Production example: Separate query handlers same DB.

### Detailed Answer (3–5 minutes)

**Concept:** CQRS without event sourcing

**When to use:** Read write separation

**When to avoid:** CQRS day one two tables

**Production example:** Separate query handlers same DB

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect CQRS without event sourcing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify CQRS without event sourcing with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is CQRS without event sourcing overkill? — CQRS day one two tables**
2. **How measure success after adopting CQRS without event sourcing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting CQRS without event sourcing without production example
- Using CQRS without event sourcing when cqrs day one two tables
- No rollback plan when CQRS without event sourcing misconfigured

---

## Q068: Read model projection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CQRS |
| **Frequency** | Common |

### Question

What is Read model projection and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Read model projection when optimized queries. Avoid when join 12 tables on read. Production example: OrderListDto projection table.

### Detailed Answer (3–5 minutes)

**Concept:** Read model projection

**When to use:** Optimized queries

**When to avoid:** Join 12 tables on read

**Production example:** OrderListDto projection table

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Read model projection to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Read model projection with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Read model projection overkill? — Join 12 tables on read**
2. **How measure success after adopting Read model projection? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Read model projection without production example
- Using Read model projection when join 12 tables on read
- No rollback plan when Read model projection misconfigured

---

## Q069: Anti-corruption layer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Occasional |

### Question

What is Anti-corruption layer and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Anti-corruption layer when legacy system isolation. Avoid when erp dtos in domain. Production example: ErpOrderAdapter maps legacy.

### Detailed Answer (3–5 minutes)

**Concept:** Anti-corruption layer

**When to use:** Legacy system isolation

**When to avoid:** ERP DTOs in domain

**Production example:** ErpOrderAdapter maps legacy

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Anti-corruption layer to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Anti-corruption layer with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Anti-corruption layer overkill? — ERP DTOs in domain**
2. **How measure success after adopting Anti-corruption layer? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Anti-corruption layer without production example
- Using Anti-corruption layer when erp dtos in domain
- No rollback plan when Anti-corruption layer misconfigured

---

## Q070: Strangler fig migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

What is Strangler fig migration and when would you apply it in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Use Strangler fig migration when incremental replacement. Avoid when big bang rewrite. Production example: Route new features to new module.

### Detailed Answer (3–5 minutes)

**Concept:** Strangler fig migration

**When to use:** Incremental replacement

**When to avoid:** Big bang rewrite

**Production example:** Route new features to new module

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Strangler fig migration to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Strangler fig migration with production trade-offs in SOLID & Clean Architecture.

### Follow-up Questions

1. **When is Strangler fig migration overkill? — Big bang rewrite**
2. **How measure success after adopting Strangler fig migration? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Strangler fig migration without production example
- Using Strangler fig migration when big bang rewrite
- No rollback plan when Strangler fig migration misconfigured

---
