# Domain-Driven Design (DDD) — Strategic & Tactical

> **Week 23** | **Module:** [ddd](../../../modules/ddd/README.md)

## Learning Objectives
- Apply strategic DDD: bounded contexts, context mapping
- Apply tactical DDD: aggregates, entities, value objects
- Connect DDD to microservice boundaries

---

## 1. Strategic DDD

### Ubiquitous Language
Shared vocabulary between developers and domain experts. "Order" means the same thing in code and in meetings.

### Bounded Context
Explicit boundary where a domain model applies. **One bounded context = candidate for one microservice.**

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Sales     │  │  Shipping   │  │  Billing    │
│  Context    │  │  Context    │  │  Context    │
│ "Customer"  │  │ "Recipient" │  │ "Account"   │
└─────────────┘  └─────────────┘  └─────────────┘
```

Same term, different meaning per context — that's OK. Don't force one enterprise model.

### Context Mapping

| Relationship | Meaning | Integration |
|--------------|---------|-------------|
| **Partnership** | Mutual dependency | Coordinated releases |
| **Shared Kernel** | Shared subset of model | Shared library (careful) |
| **Customer-Supplier** | Upstream/downstream | Upstream serves downstream |
| **Conformist** | Downstream adopts upstream model | No translation |
| **Anti-corruption Layer** | Translate at boundary | Adapter pattern |
| **Open Host Service** | Published API | REST/gRPC contract |
| **Published Language** | Shared interchange format | Events, DTOs |

---

## 2. Tactical DDD Building Blocks

### Entity
Has identity (Id). Equality by Id, not attributes.

```csharp
public class Order
{
    public Guid Id { get; private set; }  // identity
    public void Confirm() { /* business rule */ }
}
```

### Value Object
No identity. Immutable. Equality by all attributes.

```csharp
public record Money(decimal Amount, string Currency)
{
    public Money Add(Money other) => new(Amount + other.Amount, Currency);
}
public record Address(string Line1, string City, string PostalCode);
```

### Aggregate
Cluster of entities/VOs with one **aggregate root**. External references only to root Id.

**Rules:**
- One transaction = one aggregate
- Invariants enforced within aggregate boundary
- Small aggregates (prefer small)

```csharp
// Aggregate Root
public class Order  // Root
{
    private readonly List<OrderLine> _lines = new();  // internal entities
    public void AddLine(ProductId product, int qty, Money price) { /* invariant: min 1 line */ }
}
```

### Domain Events
Something happened in the domain.

```csharp
public record OrderConfirmed(Guid OrderId, DateTime ConfirmedAt) : IDomainEvent;
```

### Repository
Persistence abstraction per aggregate root (not per table).

---

## 3. Aggregate Design Rules

1. **Model true invariants** — what must be consistent in one transaction
2. **Small aggregates** — large aggregates = contention
3. **Reference by Id** — `CustomerId`, not `Customer` object across aggregates
4. **Eventual consistency** between aggregates via domain events

**Example:** Order aggregate includes OrderLines. Customer is separate aggregate — reference `CustomerId` only.

---

## 4. DDD → Microservices Mapping

| DDD Concept | Microservice |
|-------------|--------------|
| Bounded Context | Service boundary |
| Aggregate | Transaction boundary within service |
| Domain Event | Integration event on message bus |
| ACL | Anti-corruption layer at service API |

---

## 5. Event Storming (Workshop Technique)

Facilitated workshop: domain experts + developers map:
- **Domain events** (orange) — "Order Placed"
- **Commands** (blue) — "Place Order"
- **Aggregates** (yellow) — Order
- **Policies** (lilac) — "When X then Y"
- **Read models** (green) — projections

**Architect use:** Discover bounded contexts before writing code.

---

## Common Mistakes
1. Anemic domain model (no behavior in entities)
2. Giant aggregates (whole order + customer + payment in one)
3. One enterprise data model for all contexts
4. Skipping domain expert collaboration
5. DDD ceremony on simple CRUD

**Next:** Week 24 Capstone
