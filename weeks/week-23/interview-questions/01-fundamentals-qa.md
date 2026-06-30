# Week 23 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Bounded Context

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

What is a bounded context? Example in e-commerce.

### Short Answer (30 seconds)

'Customer' differs in Sales (buyer), Support (ticket submitter), Shipping (recipient). Separate models, integrate via events or ACL.

### Detailed Answer (3–5 minutes)

Bounded context = linguistic boundary where domain terms have precise meaning. Map to microservice or module boundary.

Context map documents relationships: upstream/downstream, conformist, anti-corruption layer.

### Architecture Perspective

DDD vocabulary is architect interview language.

### Follow-up Questions

1. **Ubiquitous language? — Same terms in code, docs, and conversation with domain experts.**
2. **Shared kernel? — Small shared model between contexts — use sparingly.**

### Common Mistakes in Interviews

- One enterprise data model for everything
- Anemic domain — logic in services not entities
- Context boundaries follow org chart only

---

## Q002: Aggregate and Consistency Boundary

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

What is an aggregate root? Why one transaction per aggregate?

### Short Answer (30 seconds)

Cluster of entities updated atomically — Order + OrderLines. Root (Order) is only entry point. One transaction per aggregate — cross-aggregate eventual consistency.

### Detailed Answer (3–5 minutes)

Order aggregate: add line, recalculate total, raise OrderLineAdded domain event — all in one transaction.

Reference other aggregates by ID only — not object reference across boundaries.

### Architecture Perspective

Aggregate rules prevent distributed lock nightmares.

### Follow-up Questions

1. **Aggregate size? — Small — large aggregates cause contention — split if needed.**
2. **Domain events from aggregate? — Raise on state change — persist in same transaction (outbox).**

### Common Mistakes in Interviews

- Transaction spanning Order and Customer aggregates
- Direct entity references across aggregates
- God aggregate with 50 child entities

---

## Q003: Ubiquitous Language

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

How do architects enforce ubiquitous language?

### Short Answer (30 seconds)

Code names match business terms. Glossary in wiki. PR reviews reject technical jargon replacing domain terms. Event names = business language.

### Detailed Answer (3–5 minutes)

`PlaceOrder` not `ProcessOrderDto`. `Money` not `decimal amount`.

Workshop with domain experts quarterly — refine language.

### Architecture Perspective

Language alignment reduces bugs between business and engineering.

### Follow-up Questions

1. **Anti-corruption layer naming? — Translate external terms at boundary only.**
2. **Bounded context glossary? — Per-context wiki page linked from repo.**

### Common Mistakes in Interviews

- Database column `fld_amt_1`
- Different terms in UI vs API vs database
- Developers never talk to domain experts

---

## Q004: Domain Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Domain event vs integration event?

### Short Answer (30 seconds)

Domain event: something happened in model (OrderPlaced) — in-process first. Integration event: cross-service message on bus — published after commit via outbox.

### Detailed Answer (3–5 minutes)

OrderPlaced → handler sends email (in-process). Same event → outbox → Service Bus → Inventory service (integration).

Don't leak integration concerns into domain layer.

### Architecture Perspective

Event distinction keeps domain pure.

### Follow-up Questions

1. **Event sourcing? — Store events as source of truth — different pattern — high complexity.**
2. **Event version evolution? — Additive schema — `version` field.**

### Common Mistakes in Interviews

- Synchronous email in same transaction as order
- Domain event with HTTP call inside handler
- No distinction domain vs integration events

---

## Q005: Anti-Corruption Layer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Integrate legacy ERP with new order service using ACL.

### Short Answer (30 seconds)

ACL translates ERP XML/API to domain commands. New service never imports ERP models.

### Detailed Answer (3–5 minutes)

Adapter module: `ErpOrderAdapter` maps `ERP_SALES_ORDER_42` → `PlaceOrderCommand`.

Isolate legacy ugliness — replace ERP without rewriting domain.

### Architecture Perspective

ACL is migration pattern architects specify.

### Follow-up Questions

1. **When skip ACL? — Greenfield with no legacy — direct API.**
2. **ACL testing? — Contract tests against ERP sandbox responses.**

### Common Mistakes in Interviews

- ERP DTOs in domain layer
- Direct SQL to legacy DB from new service
- No translation layer documented

---

## Q006: CQRS in DDD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

When apply CQRS in bounded context?

### Short Answer (30 seconds)

Read model differs from write model — different scale, shape, or optimization. Commands mutate aggregates; queries hit read DB or projection.

### Detailed Answer (3–5 minutes)

Write: Order aggregate in SQL. Read: denormalized OrderSummary in Redis or read replica optimized for list screens.

Start logical CQRS (separate handlers) before separate databases.

### Architecture Perspective

CQRS solves read/write mismatch — not default pattern.

### Follow-up Questions

1. **Eventual consistency on read model? — Accept lag — show 'updating' in UI.**
2. **Projection rebuild? — Replay events from event store — disaster recovery.**

### Common Mistakes in Interviews

- CQRS on day one for CRUD admin
- Separate DB without migration plan
- Write model returned on complex read query

---

## Q007: Context Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Explain upstream/downstream and conformist in context map.

### Short Answer (30 seconds)

Downstream conforms to upstream model or uses ACL. Upstream has power — downstream adapts.

### Detailed Answer (3–5 minutes)

Payment (upstream) publishes PaymentCompleted — Order (downstream) conforms or translates via ACL.

Document on context map diagram — prevents implicit coupling.

### Architecture Perspective

Context maps are architect deliverables in DDD initiatives.

### Follow-up Questions

1. **Partnership? — Two contexts evolve together — rare — needs coordination.**
2. **Open host service? — Published language for integrators — API as product.**

### Common Mistakes in Interviews

- No documented context relationships
- Downstream forces upstream model change
- Shared database between contexts

---

## Q008: Event Storming

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

What is event storming and what artifacts does it produce?

### Short Answer (30 seconds)

Workshop: domain experts + engineers stick orange (events), blue (commands), yellow (aggregates) on wall. Produces bounded contexts, process flows, hot spots.

### Detailed Answer (3–5 minutes)

Run before microservice split. Output: candidate services, integration events, unresolved policy questions.

Architect facilitates — not passive attendee.

### Architecture Perspective

Event storming is discovery — not design silver bullet.

### Follow-up Questions

1. **Remote event storming? — Miro boards — works with facilitation discipline.**
2. **Hot spot (pink)? — Unclear policy or contention — resolve before coding.**

### Common Mistakes in Interviews

- Skip discovery — code first
- Only developers in room
- No follow-up ADR from storming

---

## Q009: Anemic Domain Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Anti-Pattern |
| **Frequency** | Common |

### Question

Detect and fix anemic domain model.

### Short Answer (30 seconds)

Entities are data bags; all logic in `OrderService` 2000 lines. Fix: move behavior to entities/value objects; application layer orchestrates.

### Detailed Answer (3–5 minutes)

`order.Confirm()` not `orderService.SetStatus(order, Confirmed)`. Rich domain catches invalid transitions inside aggregate.

### Architecture Perspective

Anemic model leads to god services — architect review red flag.

### Follow-up Questions

1. **When anemic OK? — Integration DTOs and read models — not core domain.**
2. **DDD tactical patterns effort? — Worth it in core domain only — not CRUD edges.**

### Common Mistakes in Interviews

- Public setters on all entity properties
- Validation only in API controller
- OrderService knows all other domains

---

## Q010: DDD and Microservices Alignment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

Does every bounded context become a microservice?

### Short Answer (30 seconds)

No — modular monolith with clear boundaries first. Microservice when independent deploy, scale, or team need justifies ops cost.

### Detailed Answer (3–5 minutes)

Start: bounded contexts as .NET projects in one solution. Extract when pain real.

Conway's Law: service boundaries should align with team boundaries.

### Architecture Perspective

Pragmatic DDD — not distributed everything.

### Follow-up Questions

1. **Monolith modular structure? — `Ordering.Domain`, `Billing.Domain` projects.**
2. **Team topologies? — Stream-aligned team per core context.**

### Common Mistakes in Interviews

- 10 microservices for 4 developers
- Bounded context = database table
- No integration strategy between contexts

---

## Q011: Value Objects Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Design value objects for Money and Address in an order domain. What rules apply?

### Short Answer (30 seconds)

Value objects are immutable, compared by value, no identity. Money: amount + currency; operations return new instances. Address: street, city, postal — validate on construction.

### Detailed Answer (3–5 minutes)

**Money:** Never use `decimal` alone — `new Money(10.50m, Currency.USD)`. Addition only when currencies match; otherwise convert via domain service.

**Address:** `ShippingAddress.Create(...)` validates postal format; equality via all fields.

**Architect:** Value objects encapsulate validation — invalid states unrepresentable. EF Core: owned types or complex type mapping.

### Architecture Perspective

Value objects are where domain invariants hide — interviewers probe immutability and equality.

### Follow-up Questions

1. **Record types in C# for value objects? — Good fit if no inheritance — still validate in constructor.**
2. **When value object vs entity? — Entity has lifecycle and ID; value object replaces wholesale.**

### Common Mistakes in Interviews

- Mutable value object with setters
- Money as bare decimal without currency
- Reference equality on value objects

---

## Q012: Entities vs Value Objects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Order is an entity; OrderLine quantity — entity or value object? How decide?

### Short Answer (30 seconds)

Entity: identity persists through attribute changes (OrderId). Value object: defined entirely by attributes; replace don't mutate (Quantity as int primitive OK; Money as VO).

### Detailed Answer (3–5 minutes)

**Decision tree:**
1. Need to track *same thing* over time with changing state? → Entity
2. Concept defined only by current values? → Value object
3. Child within aggregate with no external reference? → Often value object or entity inside aggregate only

OrderLine may be entity *inside* Order aggregate (line ID for updates) but external world references Order only.

### Architecture Perspective

Entity vs VO classification drives aggregate design.

### Follow-up Questions

1. **OrderLineId inside aggregate? — Entity within aggregate — still no direct external reference.**
2. **Primitive obsession? — Wrap primitives in VOs when rules exist (Email, SKU).**

### Common Mistakes in Interviews

- Every table row is entity
- Value object with database-generated ID
- External service holds reference to OrderLine entity

---

## Q013: Aggregate Invariants

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Enforce 'order cannot ship until paid' inside the Order aggregate.

### Short Answer (30 seconds)

Invariant enforced in domain methods — `order.MarkShipped()` checks `Status == Paid` and throws domain exception if violated. No setter bypass.

### Detailed Answer (3–5 minutes)

**Pattern:**
```csharp
public void MarkShipped() {
  if (Status != OrderStatus.Paid)
    throw new DomainException("Cannot ship unpaid order");
  Status = OrderStatus.Shipped;
  RaiseDomainEvent(new OrderShipped(Id));
}
```

**Architect:** Invariants live in aggregate root methods — not application service `if` chains. Unit test every illegal transition.

### Architecture Perspective

Aggregate invariants are consistency guarantees — core DDD interview topic.

### Follow-up Questions

1. **Invariant vs validation? — Invariant always true in aggregate; validation at boundary may reject input.**
2. **Cross-aggregate invariant? — Eventual consistency — saga or process manager.**

### Common Mistakes in Interviews

- Public Status setter bypasses rules
- Invariant enforced only in API controller
- Database CHECK constraint as only guard

---

## Q014: Domain Services When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

When use a domain service instead of entity method?

### Short Answer (30 seconds)

Domain service when operation doesn't naturally belong to one entity — e.g. `TransferFunds(from, to, amount)` spanning two accounts, or pricing requiring external rate table owned by domain.

### Detailed Answer (3–5 minutes)

**Use entity method when:** operation concerns single aggregate root.

**Use domain service when:**
- Multi-aggregate coordination (prefer events/saga if cross-transaction)
- Stateless domain calculation (ShippingCostCalculator)
- Domain concept not an entity/VO (RoutingPolicy)

**Architect:** Keep domain services stateless; inject via DI in application layer — domain layer defines interface.

### Architecture Perspective

Domain services fill gaps — not a dumping ground for god logic.

### Follow-up Questions

1. **Application service vs domain service? — Application orchestrates; domain service holds domain logic that isn't on one entity.**
2. **Infrastructure in domain service? — Interface in domain; implementation in infrastructure.**

### Common Mistakes in Interviews

- OrderService 3000-line god class
- Domain service with DbContext dependency
- Every operation through domain service bypassing entities

---

## Q015: Repositories in DDD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

What belongs in a DDD repository interface? Where does querying live?

### Short Answer (30 seconds)

Repository: load/save aggregate by ID — `GetById`, `Add`, `Remove`. Collection-like per aggregate root. Complex queries → specification or read model — not repository returning DTO lists.

### Detailed Answer (3–5 minutes)

**Interface in domain layer:** `IOrderRepository : IRepository<Order, OrderId>`.

**Implementation:** EF Core in infrastructure — maps persistence to aggregate reconstitution.

**Architect:** One repository per aggregate root. `GetOrdersByCustomerForDashboard` belongs in read side (CQRS) or query service — not bloated repository.

### Architecture Perspective

Repository abstraction protects domain from ORM leakage.

### Follow-up Questions

1. **Unit of Work pattern? — Single transaction boundary — EF DbContext is UoW.**
2. **Generic repository anti-pattern? — `IRepository<T>` for all entities loses aggregate focus.**

### Common Mistakes in Interviews

- Repository returns IQueryable to controllers
- 27 methods on IOrderRepository
- Repository used from domain entities

---

## Q016: Factory in Domain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

When use a factory to create aggregates vs constructor?

### Short Answer (30 seconds)

Factory when creation is complex — multiple steps, optional components, or must ensure invariants before object exists. Constructor for simple aggregates.

### Detailed Answer (3–5 minutes)

**Examples:** `OrderFactory.CreateFromCart(cart, customerId)` validates cart non-empty, applies promotions, assigns ID, raises `OrderCreated`.

**Domain factory** (not GoF abstract factory): encapsulates creation rules. Static `Create` on aggregate acceptable for simple cases.

**Architect:** Ban `new Order()` scattered in application layer — centralize creation.

### Architecture Perspective

Factories hide construction complexity and enforce valid birth state.

### Follow-up Questions

1. **Factory vs builder? — Builder for stepwise optional assembly; factory for domain-valid complete aggregate.**
2. **DI for factories? — Inject `IOrderFactory` when dependencies needed (clock, ID generator).**

### Common Mistakes in Interviews

- new Order() in controller with 15 property assignments
- Factory in infrastructure only — domain can't create aggregates
- No factory tests for illegal creation paths

---

## Q017: Specifications Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Use specification pattern for 'orders eligible for expedited shipping'.

### Short Answer (30 seconds)

Specification encapsulates business rule as composable predicate — `ExpeditedShippingSpec.IsSatisfiedBy(order)`. Combine with AND/OR for complex rules.

### Detailed Answer (3–5 minutes)

**Domain layer:**
```csharp
public class ExpeditedShippingSpec : ISpecification<Order> {
  public bool IsSatisfiedBy(Order o) =>
    o.Total > Money.Usd(100) && o.ShippingAddress.IsDomestic;
}
```

**Infrastructure:** Translate to SQL via expression visitor for EF — or use in-memory for unit tests.

**Architect:** Replaces scattered LINQ `Where` duplicates — single source of truth for business rule.

### Architecture Perspective

Specifications make business rules explicit and testable.

### Follow-up Questions

1. **Specification vs CQRS read query? — Spec for domain rule; read query for projection shape.**
2. **Composable specs? — `AndSpec`, `OrSpec` — DRY complex eligibility.**

### Common Mistakes in Interviews

- Same business rule copy-pasted in 4 queries
- Specification with HTTP call inside
- No unit tests on specification classes

---

## Q018: Anti-Corruption Layer Deep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Design ACL between legacy mainframe inventory and new order service — layers and testing.

### Short Answer (30 seconds)

ACL modules: adapter (protocol), translator (DTO→domain command), facade (single entry to legacy). Order domain never sees COBOL copybook fields.

### Detailed Answer (3–5 minutes)

**Layers:**
1. **Adapter** — calls mainframe MQ/API
2. **Translator** — `LegacyStockResponse` → `ReservationResult`
3. **Facade** — `ILegacyInventoryGateway.Reserve(sku, qty)`

**Testing:** Contract tests against mainframe stub; record/replay fixtures. Canary release ACL changes independently.

**Architect:** ACL is strategic pattern — budget maintenance; plan strangler replacement.

### Architecture Perspective

Deep ACL design shows integration maturity in DDD interviews.

### Follow-up Questions

1. **ACL vs adapter pattern? — ACL adds semantic translation to domain language — not just protocol.**
2. **ACL versioning? — Version translators when legacy changes — parallel translators during migration.**

### Common Mistakes in Interviews

- Legacy field names in domain events
- ACL without integration tests
- Direct mainframe DB access bypassing ACL

---

## Q019: Context Map Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Draw context map relationships for Order, Payment, Catalog, and Legacy ERP.

### Short Answer (30 seconds)

Document: Order downstream of Payment (conformist to PaymentCompleted event); Catalog upstream open host; Legacy ERP upstream — Order uses ACL; Shipping partnership with Order.

### Detailed Answer (3–5 minutes)

**Patterns on map:**
- **Partnership** — joint evolution (rare)
- **Customer/Supplier** — negotiated upstream/downstream
- **Conformist** — downstream accepts upstream model
- **ACL** — downstream translates legacy
- **OHS** — upstream published integration API
- **Shared Kernel** — minimal shared code (dangerous)

**Architect deliverable:** Context map diagram in ADR — updated when relationships change.

### Architecture Perspective

Context maps make integration politics explicit.

### Follow-up Questions

1. **When conformist vs ACL? — Conformist when upstream model acceptable; ACL when legacy toxic.**
2. **Distilled context map? — Subset for one initiative — don't boil ocean.**

### Common Mistakes in Interviews

- No context map in microservice split
- Every relationship conformist — no ACL where needed
- Context map never updated after year one

---

## Q020: Published Language

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Define published language for integration events across bounded contexts.

### Short Answer (30 seconds)

Published language = stable, documented vocabulary for cross-context messages. `OrderPlacedV1` schema in schema registry — business terms, not internal entity names.

### Detailed Answer (3–5 minutes)

**Rules:**
- Event names past tense business facts
- Payload fields match ubiquitous language of *consuming* contexts
- Version in schema name or header
- Wiki page: glossary + example JSON

**Architect:** Integration team owns published language — breaking change = major version + consumer notice.

### Architecture Perspective

Published language prevents implicit coupling via ad hoc JSON.

### Follow-up Questions

1. **Integration event naming convention? — `{Context}{Fact}V{n}` — e.g. `BillingPaymentCapturedV1`.**
2. **Schema registry? — Confluent/Azure Schema Registry — enforce compatibility.**

### Common Mistakes in Interviews

- Internal entity serialized directly to bus
- Renamed field without version bump
- No glossary for integration terms

---

## Q021: Open Host Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Catalog context exposes product data to Order and Search — design as open host.

### Short Answer (30 seconds)

Open Host Service: Catalog publishes well-defined API/events (published language) — multiple downstream consumers adapt. Catalog doesn't know each consumer's model.

### Detailed Answer (3–5 minutes)

**Implementation:**
- REST `GET /products/{id}` + `ProductUpdated` integration event
- Rate limits, API keys per consumer team
- SLA documented — 99.9% read availability

**Contrast conformist:** OHS puts burden on host to maintain stable contract — host team is platform for integrators.

### Architecture Perspective

OHS is upstream pattern for shared reference data.

### Follow-up Questions

1. **OHS vs shared database? — OHS replaces shared DB anti-pattern.**
2. **GraphQL as OHS? — Federation supergraph can be OHS — governance critical.**

### Common Mistakes in Interviews

- Catalog team custom endpoint per consumer
- Breaking API change without notice
- No SLA on integration API

---

## Q022: Customer Supplier Relationship

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Order team needs faster changes from Payment team — customer/supplier negotiation.

### Short Answer (30 seconds)

Downstream (Order) is customer; upstream (Payment) is supplier. Customer requests features/SLAs; supplier prioritizes roadmap. Formalize in context map + integration SLA.

### Detailed Answer (3–5 minutes)

**Negotiation artifacts:**
- Consumer-driven contract tests (Pact) — customer defines expectations
- Joint planning for new event types
- Escalation when supplier breaking change threatens customer

**Architect role:** Facilitate — not let downstream hack upstream DB.

### Architecture Perspective

Customer/supplier models real organizational dynamics in DDD.

### Follow-up Questions

1. **Supplier driven by downstream? — Rare inversion — supplier usually upstream.**
2. **SLA for event delivery latency? — e.g. PaymentCompleted within 5s p99.**

### Common Mistakes in Interviews

- Downstream reads upstream database directly
- No contract tests between teams
- Assuming unlimited supplier capacity

---

## Q023: Conformist vs ACL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Payment service uses Stripe's API model directly in domain — conformist or fix?

### Short Answer (30 seconds)

Stripe model in domain = conformist (acceptable at boundary if Stripe is industry standard). If Stripe shapes corrupt ubiquitous language, use ACL to translate to `PaymentCapture` domain concept.

### Detailed Answer (3–5 minutes)

**Conformist when:** upstream model is industry standard and stable (ISO codes, Stripe statuses).

**ACL when:** legacy ERP, toxic nomenclature, or frequent upstream changes you must isolate.

**Architect decision:** Document in ADR — cost of ACL maintenance vs conformist coupling.

### Architecture Perspective

Conformist vs ACL is strategic trade-off — not moral choice.

### Follow-up Questions

1. **Two conformist hops? — Coupling accumulates — consider ACL at outer boundary.**
2. **Test conformist boundary? — Contract tests against Stripe sandbox.**

### Common Mistakes in Interviews

- ACL everywhere including stable standards
- Conformist to legacy ERP in core domain
- Undocumented conformist decision

---

## Q024: Event Storming Facilitation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

You facilitate event storming for checkout redesign — agenda and outputs?

### Short Answer (30 seconds)

Agenda: 90m — domain narrative (15m), big picture events (30m), commands/policies (20m), aggregates (15m), context boundaries (10m). Output: event flow, candidate aggregates, bounded contexts, pink hot spots.

### Detailed Answer (3–5 minutes)

**Facilitation tips:**
- Domain experts stick orange events — developers don't dominate
- Timebox — park debates in hot spots
- Read events chronologically aloud — gaps surface
- Photo/Miro export → ADR input

**Architect:** Run storming *before* service boundaries locked. Follow-up workshop resolves hot spots within 2 weeks.

### Architecture Perspective

Facilitation skill separates architects who discover from those who dictate.

### Follow-up Questions

1. **Remote facilitation? — Miro + breakout pairs for commands/aggregates.**
2. **Process modeling level? — Second workshop — swimlanes per actor/system.**

### Common Mistakes in Interviews

- Developers-only storming
- No hot spot follow-up
- Storming output never reaches ADRs

---

## Q025: Process Modeling in Event Storming

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Common |

### Question

After big picture storming, model 'place order' as process — steps?

### Short Answer (30 seconds)

Process level: swimlanes per actor (Customer, Order, Payment, Inventory). Connect events → commands → policies (when X then Y). Reveals sync vs async needs and sagas.

### Detailed Answer (3–5 minutes)

**Example flow:**
`SubmitOrder` → `OrderSubmitted` → policy → `ReserveInventory` → `InventoryReserved` → `ChargePayment` → `PaymentFailed` → policy → `ReleaseInventory`.

**Output:** Saga candidate, integration events, timeout policies.

**Architect:** Process model drives orchestration vs choreography decision.

### Architecture Perspective

Process modeling bridges discovery and technical design.

### Follow-up Questions

1. **Policy (lavender sticky)? — Reactive rule — 'Whenever PaymentFailed, CancelOrder'.**
2. **Read model (green)? — UI projection needs from flow.**

### Common Mistakes in Interviews

- Skip process level — jump to microservices
- All policies implemented sync HTTP
- No timeout policy on external steps

---

## Q026: Policy Pattern in Domain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Occasional |

### Question

Implement domain policy 'apply free shipping over $100' — where does it live?

### Short Answer (30 seconds)

Policy as domain object implementing `IShippingPolicy` — `FreeShippingOverThresholdPolicy`. Order aggregate or domain service evaluates policies collection — not hardcoded in application layer.

### Detailed Answer (3–5 minutes)

**Design:**
```csharp
public interface IShippingPolicy {
  Money AdjustShipping(Order order, Money baseShipping);
}
```

Policies composable — run in defined order. Configuration may load policy set per tenant.

**Architect:** Distinguish domain policy (business rule) from infrastructure policy (Polly retry).

### Architecture Perspective

Policy pattern keeps conditional business rules extensible.

### Follow-up Questions

1. **Strategy vs policy? — Similar — policy often event-triggered (when X then Y).**
2. **Policy in event storming vs code? — Lavender sticky → `IPolicy` implementation.**

### Common Mistakes in Interviews

- if (total > 100) in controller
- Policy with database call in domain
- Non-composable monolithic policy method

---

## Q027: Domain Events vs Integration Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

OrderPlaced raised in aggregate — trace path to Service Bus message.

### Short Answer (30 seconds)

In aggregate: raise `OrderPlaced` domain event (in-memory). On `SaveChanges`: persist to outbox table same transaction. Outbox worker publishes `OrderPlacedIntegrationEventV1` to bus — translated payload, schema version.

### Detailed Answer (3–5 minutes)

**Layers:**
1. Domain event — internal, rich domain objects OK in handler (same process)
2. Outbox — transactional guarantee
3. Integration event — public contract, primitive/DTO payload

**Architect:** Never publish domain entity JSON to bus. Handlers in application layer map domain → integration.

### Architecture Perspective

Event layering is frequent senior interview question.

### Follow-up Questions

1. **In-process domain event handlers? — Email, metrics — keep fast; no HTTP.**
2. **Eventual outbox failure? — Retry with idempotent publish key.**

### Common Mistakes in Interviews

- Domain event published directly to Kafka
- Same class for domain and integration event
- Integration event includes EF navigation properties

---

## Q028: Snapshotting Aggregates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Occasional |

### Question

Event-sourced Order aggregate with 10K events — when and how snapshot?

### Short Answer (30 seconds)

Snapshot every N events (e.g. 100) or on schedule — store current state blob + version. Load: latest snapshot + events since snapshot version.

### Detailed Answer (3–5 minutes)

**Trade-offs:**
- Faster load — O(events since snapshot) not O(all)
- Snapshot storage cost
- Snapshot invalidation on schema change — migration strategy needed

**Architect:** Snapshot async after commit — don't block write path. Version snapshot schema.

### Architecture Perspective

Snapshotting is event sourcing performance tool.

### Follow-up Questions

1. **Snapshot per aggregate type? — Order yes; small Cart maybe never.**
2. **Delete events after snapshot? — No — events are audit source — archive old.**

### Common Mistakes in Interviews

- Load replay 10K events every request
- Snapshot without version field
- Blocking write on snapshot creation

---

## Q029: CQRS in Bounded Context

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Apply CQRS inside Ordering context — write model vs read model design.

### Short Answer (30 seconds)

Write: Order aggregate, normalized tables, business invariants. Read: `OrderListItem` denormalized projection — customer name, line count, status badge — optimized for UI queries.

### Detailed Answer (3–5 minutes)

**Start logical:** separate command/query handlers, same DB. **Physical split** when read RPS >> write or schemas diverge.

**Projection:** OrderPlaced/OrderShipped events update read store — eventual consistency acceptable for list screen (show stale 2s).

**Architect:** CQRS per bounded context — not global mandate.

### Architecture Perspective

CQRS scope is context-local — interviewers check you don't over-apply.

### Follow-up Questions

1. **Read your own writes? — Synchronous projection or client polling for detail view.**
2. **Separate read DB migration? — Projections versioned — rebuild from events.**

### Common Mistakes in Interviews

- Global CQRS day one
- Write model returned for complex grid
- No projection lag documentation

---

## Q030: Modular Monolith DDD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Structure modular monolith with DDD bounded contexts before microservices.

### Short Answer (30 seconds)

Solution folders: `Ordering.Domain`, `Ordering.Application`, `Ordering.Infrastructure`, `Billing.Domain`, etc. No project reference from Ordering.Domain → Billing.Domain — integration via events or ACL interface.

### Detailed Answer (3–5 minutes)

**Rules:**
- Domain projects reference nothing infrastructure
- Cross-context only via integration events or explicit ACL project
- Single deploy initially — module boundaries enforced by architecture tests (NetArchTest)

**Architect:** Modular monolith is valid end state for many products — extract services when independent scale/deploy justified.

### Architecture Perspective

Modular monolith is disciplined default — not failure to microservice.

### Follow-up Questions

1. **Architecture tests? — `DomainShouldNotReferenceInfrastructure` — CI enforced.**
2. **Shared database modular monolith? — Schema per context minimum — table cross-join forbidden.**

### Common Mistakes in Interviews

- All contexts in one Domain project
- Cross-context entity references
- Microservices without modular monolith trial

---
