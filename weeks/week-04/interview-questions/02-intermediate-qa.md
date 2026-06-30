# Week 04 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Singleton vs DI singleton

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Very Common |

### Question

What is Singleton vs DI singleton and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Singleton vs DI singleton when di singleton lifetime. Avoid when static singleton anti-pattern. Production example: Register cache as singleton in DI.

### Detailed Answer (3–5 minutes)

**Concept:** Singleton vs DI singleton

**When to use:** DI singleton lifetime

**When to avoid:** Static singleton anti-pattern

**Production example:** Register cache as singleton in DI

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Singleton vs DI singleton to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Singleton vs DI singleton with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Singleton vs DI singleton overkill? — Static singleton anti-pattern**
2. **How measure success after adopting Singleton vs DI singleton? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Singleton vs DI singleton without production example
- Using Singleton vs DI singleton when static singleton anti-pattern
- No rollback plan when Singleton vs DI singleton misconfigured

---

## Q032: Factory pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Common |

### Question

What is Factory pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Factory pattern when encapsulate object creation. Avoid when new everywhere. Production example: PaymentGatewayFactory by type.

### Detailed Answer (3–5 minutes)

**Concept:** Factory pattern

**When to use:** Encapsulate object creation

**When to avoid:** new everywhere

**Production example:** PaymentGatewayFactory by type

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Factory pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Factory pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Factory pattern overkill? — new everywhere**
2. **How measure success after adopting Factory pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Factory pattern without production example
- Using Factory pattern when new everywhere
- No rollback plan when Factory pattern misconfigured

---

## Q033: Abstract Factory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Occasional |

### Question

What is Abstract Factory and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Abstract Factory when families of related objects. Avoid when one factory for everything. Production example: UI theme factory family.

### Detailed Answer (3–5 minutes)

**Concept:** Abstract Factory

**When to use:** Families of related objects

**When to avoid:** One factory for everything

**Production example:** UI theme factory family

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Abstract Factory to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Abstract Factory with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Abstract Factory overkill? — One factory for everything**
2. **How measure success after adopting Abstract Factory? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Abstract Factory without production example
- Using Abstract Factory when one factory for everything
- No rollback plan when Abstract Factory misconfigured

---

## Q034: Builder pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Very Common |

### Question

What is Builder pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Builder pattern when complex object construction. Avoid when 20-parameter constructor. Production example: OrderBuilder with fluent API.

### Detailed Answer (3–5 minutes)

**Concept:** Builder pattern

**When to use:** Complex object construction

**When to avoid:** 20-parameter constructor

**Production example:** OrderBuilder with fluent API

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Builder pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Builder pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Builder pattern overkill? — 20-parameter constructor**
2. **How measure success after adopting Builder pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Builder pattern without production example
- Using Builder pattern when 20-parameter constructor
- No rollback plan when Builder pattern misconfigured

---

## Q035: Prototype pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Common |

### Question

What is Prototype pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Prototype pattern when clone expensive objects. Avoid when reconstruct from scratch. Production example: Deep clone template document.

### Detailed Answer (3–5 minutes)

**Concept:** Prototype pattern

**When to use:** Clone expensive objects

**When to avoid:** Reconstruct from scratch

**Production example:** Deep clone template document

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Prototype pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Prototype pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Prototype pattern overkill? — Reconstruct from scratch**
2. **How measure success after adopting Prototype pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Prototype pattern without production example
- Using Prototype pattern when reconstruct from scratch
- No rollback plan when Prototype pattern misconfigured

---

## Q036: Adapter pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

What is Adapter pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Adapter pattern when legacy interface wrapper. Avoid when change legacy api globally. Production example: LegacyErpAdapter implements IOrders.

### Detailed Answer (3–5 minutes)

**Concept:** Adapter pattern

**When to use:** Legacy interface wrapper

**When to avoid:** Change legacy API globally

**Production example:** LegacyErpAdapter implements IOrders

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Adapter pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Adapter pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Adapter pattern overkill? — Change legacy API globally**
2. **How measure success after adopting Adapter pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Adapter pattern without production example
- Using Adapter pattern when change legacy api globally
- No rollback plan when Adapter pattern misconfigured

---

## Q037: Decorator pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Very Common |

### Question

What is Decorator pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Decorator pattern when add behavior dynamically. Avoid when deep inheritance tree. Production example: CachingDecorator on IProductService.

### Detailed Answer (3–5 minutes)

**Concept:** Decorator pattern

**When to use:** Add behavior dynamically

**When to avoid:** Deep inheritance tree

**Production example:** CachingDecorator on IProductService

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Decorator pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Decorator pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Decorator pattern overkill? — Deep inheritance tree**
2. **How measure success after adopting Decorator pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Decorator pattern without production example
- Using Decorator pattern when deep inheritance tree
- No rollback plan when Decorator pattern misconfigured

---

## Q038: Facade pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Common |

### Question

What is Facade pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Facade pattern when simplify complex subsystem. Avoid when controller calls 8 services. Production example: CheckoutFacade orchestrates.

### Detailed Answer (3–5 minutes)

**Concept:** Facade pattern

**When to use:** Simplify complex subsystem

**When to avoid:** Controller calls 8 services

**Production example:** CheckoutFacade orchestrates

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Facade pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Facade pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Facade pattern overkill? — Controller calls 8 services**
2. **How measure success after adopting Facade pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Facade pattern without production example
- Using Facade pattern when controller calls 8 services
- No rollback plan when Facade pattern misconfigured

---

## Q039: Proxy pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

What is Proxy pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Proxy pattern when control access lazy load. Avoid when direct expensive calls. Production example: Lazy loading proxy for report.

### Detailed Answer (3–5 minutes)

**Concept:** Proxy pattern

**When to use:** Control access lazy load

**When to avoid:** Direct expensive calls

**Production example:** Lazy loading proxy for report

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Proxy pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Proxy pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Proxy pattern overkill? — Direct expensive calls**
2. **How measure success after adopting Proxy pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Proxy pattern without production example
- Using Proxy pattern when direct expensive calls
- No rollback plan when Proxy pattern misconfigured

---

## Q040: Composite pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Very Common |

### Question

What is Composite pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Composite pattern when tree structures uniform. Avoid when special case leaf nodes. Production example: Org chart component tree.

### Detailed Answer (3–5 minutes)

**Concept:** Composite pattern

**When to use:** Tree structures uniform

**When to avoid:** Special case leaf nodes

**Production example:** Org chart component tree

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Composite pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Composite pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Composite pattern overkill? — Special case leaf nodes**
2. **How measure success after adopting Composite pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Composite pattern without production example
- Using Composite pattern when special case leaf nodes
- No rollback plan when Composite pattern misconfigured

---

## Q041: Bridge pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Common |

### Question

What is Bridge pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Bridge pattern when decouple abstraction from impl. Avoid when explosion of subclasses. Production example: MessageSender bridge SMS/Email.

### Detailed Answer (3–5 minutes)

**Concept:** Bridge pattern

**When to use:** Decouple abstraction from impl

**When to avoid:** Explosion of subclasses

**Production example:** MessageSender bridge SMS/Email

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bridge pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bridge pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Bridge pattern overkill? — Explosion of subclasses**
2. **How measure success after adopting Bridge pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bridge pattern without production example
- Using Bridge pattern when explosion of subclasses
- No rollback plan when Bridge pattern misconfigured

---

## Q042: Strategy pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Occasional |

### Question

What is Strategy pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Strategy pattern when interchangeable algorithms. Avoid when switch on type string. Production example: IShippingStrategy implementations.

### Detailed Answer (3–5 minutes)

**Concept:** Strategy pattern

**When to use:** Interchangeable algorithms

**When to avoid:** switch on type string

**Production example:** IShippingStrategy implementations

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Strategy pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Strategy pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Strategy pattern overkill? — switch on type string**
2. **How measure success after adopting Strategy pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Strategy pattern without production example
- Using Strategy pattern when switch on type string
- No rollback plan when Strategy pattern misconfigured

---

## Q043: Observer and events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Very Common |

### Question

What is Observer and events and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Observer and events when publish-subscribe decoupling. Avoid when tight callback chains. Production example: Domain events to handlers.

### Detailed Answer (3–5 minutes)

**Concept:** Observer and events

**When to use:** Publish-subscribe decoupling

**When to avoid:** Tight callback chains

**Production example:** Domain events to handlers

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Observer and events to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Observer and events with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Observer and events overkill? — Tight callback chains**
2. **How measure success after adopting Observer and events? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Observer and events without production example
- Using Observer and events when tight callback chains
- No rollback plan when Observer and events misconfigured

---

## Q044: Command pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

What is Command pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Command pattern when encapsulate requests. Avoid when god method doeverything. Production example: PlaceOrderCommand + handler.

### Detailed Answer (3–5 minutes)

**Concept:** Command pattern

**When to use:** Encapsulate requests

**When to avoid:** God method DoEverything

**Production example:** PlaceOrderCommand + handler

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Command pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Command pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Command pattern overkill? — God method DoEverything**
2. **How measure success after adopting Command pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Command pattern without production example
- Using Command pattern when god method doeverything
- No rollback plan when Command pattern misconfigured

---

## Q045: State pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Occasional |

### Question

What is State pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use State pattern when state-specific behavior. Avoid when switch on status everywhere. Production example: IOrderState implementations.

### Detailed Answer (3–5 minutes)

**Concept:** State pattern

**When to use:** State-specific behavior

**When to avoid:** switch on status everywhere

**Production example:** IOrderState implementations

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect State pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify State pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is State pattern overkill? — switch on status everywhere**
2. **How measure success after adopting State pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting State pattern without production example
- Using State pattern when switch on status everywhere
- No rollback plan when State pattern misconfigured

---

## Q046: Template Method

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Very Common |

### Question

What is Template Method and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Template Method when algorithm skeleton subclass steps. Avoid when duplicate algorithm steps. Production example: BaseExporter defines flow.

### Detailed Answer (3–5 minutes)

**Concept:** Template Method

**When to use:** Algorithm skeleton subclass steps

**When to avoid:** Duplicate algorithm steps

**Production example:** BaseExporter defines flow

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Template Method to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Template Method with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Template Method overkill? — Duplicate algorithm steps**
2. **How measure success after adopting Template Method? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Template Method without production example
- Using Template Method when duplicate algorithm steps
- No rollback plan when Template Method misconfigured

---

## Q047: Chain of Responsibility

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

What is Chain of Responsibility and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Chain of Responsibility when pipeline handlers. Avoid when nested if validation. Production example: Validation chain per request.

### Detailed Answer (3–5 minutes)

**Concept:** Chain of Responsibility

**When to use:** Pipeline handlers

**When to avoid:** Nested if validation

**Production example:** Validation chain per request

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Chain of Responsibility to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Chain of Responsibility with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Chain of Responsibility overkill? — Nested if validation**
2. **How measure success after adopting Chain of Responsibility? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Chain of Responsibility without production example
- Using Chain of Responsibility when nested if validation
- No rollback plan when Chain of Responsibility misconfigured

---

## Q048: Mediator pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Occasional |

### Question

What is Mediator pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Mediator pattern when reduce direct dependencies. Avoid when spaghetti service calls. Production example: MediatR as mediator.

### Detailed Answer (3–5 minutes)

**Concept:** Mediator pattern

**When to use:** Reduce direct dependencies

**When to avoid:** Spaghetti service calls

**Production example:** MediatR as mediator

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Mediator pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Mediator pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Mediator pattern overkill? — Spaghetti service calls**
2. **How measure success after adopting Mediator pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Mediator pattern without production example
- Using Mediator pattern when spaghetti service calls
- No rollback plan when Mediator pattern misconfigured

---

## Q049: Memento pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Very Common |

### Question

What is Memento pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Memento pattern when undo state capture. Avoid when expose internal state. Production example: Audit snapshot memento.

### Detailed Answer (3–5 minutes)

**Concept:** Memento pattern

**When to use:** Undo state capture

**When to avoid:** Expose internal state

**Production example:** Audit snapshot memento

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Memento pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Memento pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Memento pattern overkill? — Expose internal state**
2. **How measure success after adopting Memento pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Memento pattern without production example
- Using Memento pattern when expose internal state
- No rollback plan when Memento pattern misconfigured

---

## Q050: Visitor pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

What is Visitor pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Visitor pattern when operations on hierarchy. Avoid when pattern matching sufficient. Production example: Visitor for complex tax calc tree.

### Detailed Answer (3–5 minutes)

**Concept:** Visitor pattern

**When to use:** Operations on hierarchy

**When to avoid:** Pattern matching sufficient

**Production example:** Visitor for complex tax calc tree

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Visitor pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Visitor pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Visitor pattern overkill? — Pattern matching sufficient**
2. **How measure success after adopting Visitor pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Visitor pattern without production example
- Using Visitor pattern when pattern matching sufficient
- No rollback plan when Visitor pattern misconfigured

---

## Q051: Repository pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Enterprise |
| **Frequency** | Occasional |

### Question

What is Repository pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Repository pattern when persistence abstraction. Avoid when repository on everything. Production example: IOrderRepository meaningful aggregate.

### Detailed Answer (3–5 minutes)

**Concept:** Repository pattern

**When to use:** Persistence abstraction

**When to avoid:** Repository on everything

**Production example:** IOrderRepository meaningful aggregate

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Repository pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Repository pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Repository pattern overkill? — Repository on everything**
2. **How measure success after adopting Repository pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Repository pattern without production example
- Using Repository pattern when repository on everything
- No rollback plan when Repository pattern misconfigured

---

## Q052: Unit of Work pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

What is Unit of Work pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Unit of Work pattern when transaction coordination. Avoid when per-repository transactions. Production example: DbContext as UoW.

### Detailed Answer (3–5 minutes)

**Concept:** Unit of Work pattern

**When to use:** Transaction coordination

**When to avoid:** Per-repository transactions

**Production example:** DbContext as UoW

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Unit of Work pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Unit of Work pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Unit of Work pattern overkill? — Per-repository transactions**
2. **How measure success after adopting Unit of Work pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Unit of Work pattern without production example
- Using Unit of Work pattern when per-repository transactions
- No rollback plan when Unit of Work pattern misconfigured

---

## Q053: Outbox pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Enterprise |
| **Frequency** | Common |

### Question

What is Outbox pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Outbox pattern when reliable event publish. Avoid when savechanges then fire event. Production example: Outbox table + relay worker.

### Detailed Answer (3–5 minutes)

**Concept:** Outbox pattern

**When to use:** Reliable event publish

**When to avoid:** SaveChanges then fire event

**Production example:** Outbox table + relay worker

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Outbox pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Outbox pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Outbox pattern overkill? — SaveChanges then fire event**
2. **How measure success after adopting Outbox pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Outbox pattern without production example
- Using Outbox pattern when savechanges then fire event
- No rollback plan when Outbox pattern misconfigured

---

## Q054: Saga orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Enterprise |
| **Frequency** | Occasional |

### Question

What is Saga orchestration and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Saga orchestration when distributed workflow. Avoid when saga for 2-step local tx. Production example: Orchestrator for checkout steps.

### Detailed Answer (3–5 minutes)

**Concept:** Saga orchestration

**When to use:** Distributed workflow

**When to avoid:** Saga for 2-step local TX

**Production example:** Orchestrator for checkout steps

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Saga orchestration to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Saga orchestration with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Saga orchestration overkill? — Saga for 2-step local TX**
2. **How measure success after adopting Saga orchestration? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Saga orchestration without production example
- Using Saga orchestration when saga for 2-step local tx
- No rollback plan when Saga orchestration misconfigured

---

## Q055: CQRS with patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

What is CQRS with patterns and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use CQRS with patterns when separate read write stacks. Avoid when separate dbs day one. Production example: Logical CQRS first.

### Detailed Answer (3–5 minutes)

**Concept:** CQRS with patterns

**When to use:** Separate read write stacks

**When to avoid:** Separate DBs day one

**Production example:** Logical CQRS first

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect CQRS with patterns to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify CQRS with patterns with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is CQRS with patterns overkill? — Separate DBs day one**
2. **How measure success after adopting CQRS with patterns? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting CQRS with patterns without production example
- Using CQRS with patterns when separate dbs day one
- No rollback plan when CQRS with patterns misconfigured

---

## Q056: Anti-pattern God Object

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Anti-Pattern |
| **Frequency** | Common |

### Question

What is Anti-pattern God Object and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Anti-pattern God Object when split responsibilities. Avoid when applicationservice 5000 lines. Production example: Slice by feature command handlers.

### Detailed Answer (3–5 minutes)

**Concept:** Anti-pattern God Object

**When to use:** Split responsibilities

**When to avoid:** ApplicationService 5000 lines

**Production example:** Slice by feature command handlers

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Anti-pattern God Object to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Anti-pattern God Object with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Anti-pattern God Object overkill? — ApplicationService 5000 lines**
2. **How measure success after adopting Anti-pattern God Object? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Anti-pattern God Object without production example
- Using Anti-pattern God Object when applicationservice 5000 lines
- No rollback plan when Anti-pattern God Object misconfigured

---

## Q057: Anti-pattern spaghetti callback

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Anti-Pattern |
| **Frequency** | Occasional |

### Question

What is Anti-pattern spaghetti callback and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Anti-pattern spaghetti callback when events or mediator. Avoid when nested action callbacks. Production example: Async event driven flow.

### Detailed Answer (3–5 minutes)

**Concept:** Anti-pattern spaghetti callback

**When to use:** Events or mediator

**When to avoid:** Nested Action callbacks

**Production example:** Async event driven flow

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Anti-pattern spaghetti callback to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Anti-pattern spaghetti callback with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Anti-pattern spaghetti callback overkill? — Nested Action callbacks**
2. **How measure success after adopting Anti-pattern spaghetti callback? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Anti-pattern spaghetti callback without production example
- Using Anti-pattern spaghetti callback when nested action callbacks
- No rollback plan when Anti-pattern spaghetti callback misconfigured

---

## Q058: Pattern selection framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Process |
| **Frequency** | Very Common |

### Question

What is Pattern selection framework and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Pattern selection framework when simplest pattern that works. Avoid when pattern for every line. Production example: Strategy when algorithms vary.

### Detailed Answer (3–5 minutes)

**Concept:** Pattern selection framework

**When to use:** Simplest pattern that works

**When to avoid:** Pattern for every line

**Production example:** Strategy when algorithms vary

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Pattern selection framework to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Pattern selection framework with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Pattern selection framework overkill? — Pattern for every line**
2. **How measure success after adopting Pattern selection framework? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Pattern selection framework without production example
- Using Pattern selection framework when pattern for every line
- No rollback plan when Pattern selection framework misconfigured

---

## Q059: Visitor vs pattern matching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Modern C# |
| **Frequency** | Common |

### Question

What is Visitor vs pattern matching and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Visitor vs pattern matching when pattern matching for simple. Avoid when visitor for open hierarchy. Production example: switch expression on types.

### Detailed Answer (3–5 minutes)

**Concept:** Visitor vs pattern matching

**When to use:** Pattern matching for simple

**When to avoid:** Visitor for open hierarchy

**Production example:** switch expression on types

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Visitor vs pattern matching to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Visitor vs pattern matching with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Visitor vs pattern matching overkill? — Visitor for open hierarchy**
2. **How measure success after adopting Visitor vs pattern matching? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Visitor vs pattern matching without production example
- Using Visitor vs pattern matching when visitor for open hierarchy
- No rollback plan when Visitor vs pattern matching misconfigured

---

## Q060: Enterprise vs GoF scope

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Terminology |
| **Frequency** | Occasional |

### Question

What is Enterprise vs GoF scope and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Enterprise vs GoF scope when gof tactical enterprise integration. Avoid when confuse categories. Production example: GoF in code Enterprise in architecture.

### Detailed Answer (3–5 minutes)

**Concept:** Enterprise vs GoF scope

**When to use:** GoF tactical Enterprise integration

**When to avoid:** Confuse categories

**Production example:** GoF in code Enterprise in architecture

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Enterprise vs GoF scope to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Enterprise vs GoF scope with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Enterprise vs GoF scope overkill? — Confuse categories**
2. **How measure success after adopting Enterprise vs GoF scope? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Enterprise vs GoF scope without production example
- Using Enterprise vs GoF scope when confuse categories
- No rollback plan when Enterprise vs GoF scope misconfigured

---

## Q061: Object pool pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Very Common |

### Question

What is Object pool pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Object pool pattern when expensive object reuse. Avoid when pool everything. Production example: SqlConnection pool built-in.

### Detailed Answer (3–5 minutes)

**Concept:** Object pool pattern

**When to use:** Expensive object reuse

**When to avoid:** Pool everything

**Production example:** SqlConnection pool built-in

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Object pool pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Object pool pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Object pool pattern overkill? — Pool everything**
2. **How measure success after adopting Object pool pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Object pool pattern without production example
- Using Object pool pattern when pool everything
- No rollback plan when Object pool pattern misconfigured

---

## Q062: Lazy initialization thread-safe

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Creational |
| **Frequency** | Common |

### Question

What is Lazy initialization thread-safe and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Lazy initialization thread-safe when defer cost. Avoid when lazy everywhere. Production example: Lazy<T> for heavy config parse.

### Detailed Answer (3–5 minutes)

**Concept:** Lazy initialization thread-safe

**When to use:** Defer cost

**When to avoid:** Lazy everywhere

**Production example:** Lazy<T> for heavy config parse

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Lazy initialization thread-safe to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Lazy initialization thread-safe with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Lazy initialization thread-safe overkill? — Lazy everywhere**
2. **How measure success after adopting Lazy initialization thread-safe? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Lazy initialization thread-safe without production example
- Using Lazy initialization thread-safe when lazy everywhere
- No rollback plan when Lazy initialization thread-safe misconfigured

---

## Q063: Flyweight pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

What is Flyweight pattern and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Flyweight pattern when shared intrinsic state. Avoid when duplicate data. Production example: Glyph flyweight in text editor.

### Detailed Answer (3–5 minutes)

**Concept:** Flyweight pattern

**When to use:** Shared intrinsic state

**When to avoid:** Duplicate data

**Production example:** Glyph flyweight in text editor

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Flyweight pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Flyweight pattern with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Flyweight pattern overkill? — Duplicate data**
2. **How measure success after adopting Flyweight pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Flyweight pattern without production example
- Using Flyweight pattern when duplicate data
- No rollback plan when Flyweight pattern misconfigured

---

## Q064: Facade vs Mediator

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Very Common |

### Question

What is Facade vs Mediator and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Facade vs Mediator when simplify interactions. Avoid when confuse patterns. Production example: Facade checkout Mediator order events.

### Detailed Answer (3–5 minutes)

**Concept:** Facade vs Mediator

**When to use:** Simplify interactions

**When to avoid:** Confuse patterns

**Production example:** Facade checkout Mediator order events

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Facade vs Mediator to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Facade vs Mediator with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Facade vs Mediator overkill? — Confuse patterns**
2. **How measure success after adopting Facade vs Mediator? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Facade vs Mediator without production example
- Using Facade vs Mediator when confuse patterns
- No rollback plan when Facade vs Mediator misconfigured

---

## Q065: Decorator vs Proxy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Common |

### Question

What is Decorator vs Proxy and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Decorator vs Proxy when add behavior vs control. Avoid when inheritance maze. Production example: CachingDecorator vs SecurityProxy.

### Detailed Answer (3–5 minutes)

**Concept:** Decorator vs Proxy

**When to use:** Add behavior vs control

**When to avoid:** Inheritance maze

**Production example:** CachingDecorator vs SecurityProxy

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Decorator vs Proxy to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Decorator vs Proxy with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Decorator vs Proxy overkill? — Inheritance maze**
2. **How measure success after adopting Decorator vs Proxy? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Decorator vs Proxy without production example
- Using Decorator vs Proxy when inheritance maze
- No rollback plan when Decorator vs Proxy misconfigured

---

## Q066: Adapter for third party SDK

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

What is Adapter for third party SDK and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Adapter for third party SDK when isolate vendor. Avoid when sdk calls in controllers. Production example: StripeAdapter implements IPayment.

### Detailed Answer (3–5 minutes)

**Concept:** Adapter for third party SDK

**When to use:** Isolate vendor

**When to avoid:** SDK calls in controllers

**Production example:** StripeAdapter implements IPayment

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Adapter for third party SDK to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Adapter for third party SDK with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Adapter for third party SDK overkill? — SDK calls in controllers**
2. **How measure success after adopting Adapter for third party SDK? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Adapter for third party SDK without production example
- Using Adapter for third party SDK when sdk calls in controllers
- No rollback plan when Adapter for third party SDK misconfigured

---

## Q067: Bridge for multi-channel notify

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Very Common |

### Question

What is Bridge for multi-channel notify and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Bridge for multi-channel notify when decouple abstraction. Avoid when subclass explosion. Production example: Notification bridge SMS email push.

### Detailed Answer (3–5 minutes)

**Concept:** Bridge for multi-channel notify

**When to use:** Decouple abstraction

**When to avoid:** Subclass explosion

**Production example:** Notification bridge SMS email push

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bridge for multi-channel notify to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bridge for multi-channel notify with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Bridge for multi-channel notify overkill? — Subclass explosion**
2. **How measure success after adopting Bridge for multi-channel notify? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bridge for multi-channel notify without production example
- Using Bridge for multi-channel notify when subclass explosion
- No rollback plan when Bridge for multi-channel notify misconfigured

---

## Q068: Composite menu permissions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Structural |
| **Frequency** | Common |

### Question

What is Composite menu permissions and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Composite menu permissions when tree operations. Avoid when special case leaves. Production example: Permission composite tree.

### Detailed Answer (3–5 minutes)

**Concept:** Composite menu permissions

**When to use:** Tree operations

**When to avoid:** Special case leaves

**Production example:** Permission composite tree

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Composite menu permissions to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Composite menu permissions with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Composite menu permissions overkill? — Special case leaves**
2. **How measure success after adopting Composite menu permissions? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Composite menu permissions without production example
- Using Composite menu permissions when special case leaves
- No rollback plan when Composite menu permissions misconfigured

---

## Q069: Iterator pattern LINQ

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Occasional |

### Question

What is Iterator pattern LINQ and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Iterator pattern LINQ when collection traversal. Avoid when manual index loops. Production example: IEnumerable iterator pattern.

### Detailed Answer (3–5 minutes)

**Concept:** Iterator pattern LINQ

**When to use:** Collection traversal

**When to avoid:** Manual index loops

**Production example:** IEnumerable iterator pattern

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Iterator pattern LINQ to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Iterator pattern LINQ with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Iterator pattern LINQ overkill? — Manual index loops**
2. **How measure success after adopting Iterator pattern LINQ? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Iterator pattern LINQ without production example
- Using Iterator pattern LINQ when manual index loops
- No rollback plan when Iterator pattern LINQ misconfigured

---

## Q070: Interpreter rule engine

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Behavioral |
| **Frequency** | Very Common |

### Question

What is Interpreter rule engine and when would you apply it in Design Patterns?

### Short Answer (30 seconds)

Use Interpreter rule engine when dsl evaluation. Avoid when interpreter for simple if. Production example: Promo rule interpreter.

### Detailed Answer (3–5 minutes)

**Concept:** Interpreter rule engine

**When to use:** DSL evaluation

**When to avoid:** Interpreter for simple if

**Production example:** Promo rule interpreter

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Interpreter rule engine to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Interpreter rule engine with production trade-offs in Design Patterns.

### Follow-up Questions

1. **When is Interpreter rule engine overkill? — Interpreter for simple if**
2. **How measure success after adopting Interpreter rule engine? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Interpreter rule engine without production example
- Using Interpreter rule engine when interpreter for simple if
- No rollback plan when Interpreter rule engine misconfigured

---
