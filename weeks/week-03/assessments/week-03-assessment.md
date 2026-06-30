# Week 03 — Common Mistakes & Assessment

## Common Mistakes

1. **Clean Architecture for every project** — 4 projects for a todo app
2. **Anemic domain** — entities with only getters/setters
3. **Domain depending on EF** — `DbContext` in domain layer
4. **CQRS without read scaling need** — two models, double maintenance
5. **MediatR everywhere** — simple pass-through handlers
6. **Microservices before modular monolith** — skipping intermediate step
7. **Shared database across microservices** — distributed monolith

## Assessment (60 min, pass 70%)

### A1 (10 pts): Identify SOLID violation

```csharp
public class ReportService : IReportService, IEmailService, IDatabaseBackup
```

**Answer:** SRP violation — three reasons to change. Split into separate services.

### A2 (10 pts): Clean vs Vertical Slice for 4-person startup?

**Answer:** Vertical Slice — faster delivery, less ceremony. Refactor to Clean when domain complexity grows.

### A3 (10 pts): When CQRS?

**Answer:** High read/write ratio, different optimization needs, event sourcing, independent read scaling. Not for simple CRUD.

### B (20 pts): Draw Clean Architecture layers with dependency direction.

### C (25 pts): 800K LOC monolith — microservices in 6 months or modular monolith first?

**Answer:** Modular monolith. Team lacks ops maturity. Extract one service after boundaries proven.

### D (15 pts): Rich vs anemic domain — when each?

**Answer:** Rich for complex rules (finance, insurance). Anemic for simple CRUD with little logic.

### E (10 pts): Explain DIP to a developer in 2 minutes.

**Answer:** High-level code depends on interfaces, not concrete SQL/Stripe classes. Enables swapping implementations and testing with mocks.
