# Clean Architecture & Related Patterns

> **Week 03** | **Level:** Intermediate → Advanced

## Learning Objectives

- Design solutions using Clean Architecture layers
- Compare Clean, Onion, Hexagonal, and Vertical Slice
- Apply CQRS where appropriate

---

## 1. Clean Architecture (Uncle Bob)

```
┌─────────────────────────────────────────────┐
│              Frameworks & Drivers            │
│  (UI, DB, External APIs, EF Core)           │
│  ┌─────────────────────────────────────┐    │
│  │         Interface Adapters           │    │
│  │  (Controllers, Repositories, DTOs)   │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │      Application Rules       │    │    │
│  │  │  (Use Cases, Commands)       │    │    │
│  │  │  ┌─────────────────────┐    │    │    │
│  │  │  │  Enterprise Rules    │    │    │    │
│  │  │  │  (Entities, VOs)     │    │    │    │
│  │  │  └─────────────────────┘    │    │    │
│  │  └─────────────────────────────┘    │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
         Dependency direction: INWARD ONLY
```

**Dependency Rule:** Source code dependencies point inward. Domain knows nothing about EF, ASP.NET, or SQL.

### .NET Project Structure

```
OrderService/
├── OrderService.Domain/           # Entities, Value Objects, Domain Events
├── OrderService.Application/      # Commands, Queries, Handlers, Interfaces
├── OrderService.Infrastructure/   # EF, external APIs, messaging
└── OrderService.Api/              # Minimal APIs, DI composition root
```

---

## 2. Onion Architecture

Similar to Clean Architecture — concentric layers:

| Layer | Contents |
|-------|----------|
| Core (center) | Domain model |
| Domain Services | Domain logic spanning entities |
| Application Services | Use cases, orchestration |
| Infrastructure | Persistence, messaging |
| UI/API | Entry points |

**Difference from Clean:** Onion explicitly includes Domain Services layer. Practically interchangeable in .NET projects.

---

## 3. Hexagonal Architecture (Ports & Adapters)

```
                    ┌──────────────┐
    REST API ──────►│              │──────► SQL DB
                    │   Domain     │
    gRPC ──────────►│   (Ports)    │──────► Redis
                    │              │
    CLI ───────────►│              │──────► Message Queue
                    └──────────────┘
                      Adapters
```

**Ports:** Interfaces defined by domain (e.g., `IOrderRepository`, `IPaymentPort`)
**Adapters:** Implementations (EF repository, Stripe adapter)

**Architect benefit:** Swap infrastructure without touching domain. Test domain with in-memory adapters.

---

## 4. Vertical Slice Architecture

Organize by **feature**, not layer:

```
Features/
├── Orders/
│   ├── CreateOrder/
│   │   ├── CreateOrderCommand.cs
│   │   ├── CreateOrderHandler.cs
│   │   ├── CreateOrderValidator.cs
│   │   └── CreateOrderEndpoint.cs
│   └── GetOrder/
│       └── ...
├── Payments/
│   └── ...
```

**Choose Vertical Slice when:**
- Small to medium teams
- Feature velocity more important than strict layering
- Microservices within a monolith

**Choose Clean/Onion when:**
- Large teams need strict boundaries
- Complex domain with rich business rules
- Multiple entry points (API, worker, CLI)

---

## 5. CQRS (Command Query Responsibility Segregation)

Separate models for reads and writes:

```csharp
// Command
public record CreateOrderCommand(Guid CustomerId, List<OrderLine> Lines);
public class CreateOrderHandler(IOrderRepository repo) : IRequestHandler<CreateOrderCommand, Guid>
{
    public async Task<Guid> Handle(CreateOrderCommand cmd, CancellationToken ct) { ... }
}

// Query
public record GetOrderQuery(Guid OrderId);
public class GetOrderHandler(IOrderReadDb readDb) : IRequestHandler<GetOrderQuery, OrderDto?>
{
    public async Task<OrderDto?> Handle(GetOrderQuery query, CancellationToken ct) { ... }
}
```

| Aspect | Traditional | CQRS |
|--------|------------|------|
| Read model | Same as write | Optimized projection |
| Complexity | Lower | Higher |
| Scale reads | Limited | Independent read DB/cache |
| Consistency | Immediate | May be eventual |

**Use CQRS when:** Read/write ratio extreme, different optimization needs, event sourcing in play.
**Skip CQRS when:** Simple CRUD, small team, no scaling pain.

---

## 6. MediatR Pattern

```csharp
builder.Services.AddMediatR(cfg => cfg.RegisterServicesFromAssembly(typeof(CreateOrderCommand).Assembly));

// Endpoint
orders.MapPost("/", async (CreateOrderCommand cmd, IMediator mediator) =>
{
    var id = await mediator.Send(cmd);
    return Results.Created($"/orders/{id}", new { id });
});
```

**Pros:** Thin controllers/endpoints, pipeline behaviors (validation, logging, transactions).
**Cons:** Indirection — harder to navigate for new developers. "MediatR for everything" anti-pattern.

---

## 7. Architecture Selection Decision Matrix

| Factor | Clean/Onion | Vertical Slice | Simple Layered |
|--------|------------|----------------|----------------|
| Team size | 10+ | 3–15 | 1–5 |
| Domain complexity | High | Medium | Low |
| Change frequency | Moderate | High (features) | Low |
| Testability need | High | Medium | Low |
| Time to market | Slower initial | Faster | Fastest |

---

## Production Example

**Insurance claims system** — 200 developers, 15-year domain rules.

- **Choice:** Clean Architecture + CQRS + event sourcing for claims
- **Why:** Complex domain, audit requirements, read/write scale differs 10:1
- **Result:** 40% faster feature delivery in claims module after 6-month migration

**Startup MVP** — 3 developers, 6-week deadline.

- **Choice:** Vertical Slice + Minimal APIs, single PostgreSQL
- **Why:** Speed over purity; refactor when product-market fit proven

---

## Common Mistakes

1. **Clean Architecture ceremony for CRUD** — 4 projects for 5 endpoints
2. **Anemic domain model** — entities are data bags, logic in services
3. **CQRS without scaling need** — complexity tax
4. **Leaky abstractions** — EF entities in domain layer
5. **MediatR for 3 commands** — over-engineering

**Next:** [03-advanced-expert.md](03-advanced-expert.md)
