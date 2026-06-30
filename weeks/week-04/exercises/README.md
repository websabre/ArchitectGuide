# Week 04 — Exercises

> Theory: [theory/](../theory/README.md) · Lab: [lab-04-pattern-refactoring](../labs/lab-04-pattern-refactoring.md) · Interview: [interview-questions/](../interview-questions/README.md)

## Exercise 1: Strategy Pattern Refactor (60 min)

Given this shipping calculator:

```csharp
public decimal Calculate(string method, decimal weight)
{
    return method switch
    {
        "standard" => weight * 2.5m,
        "express"  => weight * 5.0m + 10m,
        "overnight"=> weight * 8.0m + 25m,
        _ => throw new ArgumentException("Unknown method")
    };
}
```

**Tasks:**
1. Refactor to Strategy pattern with `IShippingStrategy`
2. Add a fourth method (`freight`) without modifying existing strategies (OCP)
3. Register strategies in DI; resolve by method name
4. Write one unit test per strategy

**Deliverable:** Refactored code. Extend [lab-04](../labs/lab-04-pattern-refactoring.md) if already done.

---

## Exercise 2: Factory vs Abstract Factory (45 min)

Scenario: a document export feature supports PDF, Excel, and Word. Each format needs a `Writer`, `Formatter`, and `Validator` that must stay consistent per format.

**Tasks:**
1. Sketch a Simple Factory solution — when is it enough?
2. Sketch an Abstract Factory solution — what extra flexibility does it buy?
3. Choose one for a multi-tenant SaaS with per-tenant format packs

**Deliverable:** Two UML-style diagrams + 1-paragraph decision rationale.

---

## Exercise 3: Decorator for Logging (45 min)

Wrap an existing `IOrderRepository` with a logging decorator:

```csharp
public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(Guid id, CancellationToken ct);
    Task SaveAsync(Order order, CancellationToken ct);
}
```

Log method name, duration, and correlation ID. Do not modify the concrete repository.

**Deliverable:** `LoggingOrderRepositoryDecorator` + DI registration. No cross-cutting logic in the concrete class.

---

## Exercise 4: Anti-Pattern Identification (30 min)

For each snippet, name the anti-pattern and the preferred pattern:

1. God class `OrderManager` with 40 methods spanning validation, DB, email, PDF
2. `new SqlOrderRepository()` inside every service constructor
3. Singleton `Configuration.Instance` accessed from 50 classes
4. Deep inheritance: `Animal → Mammal → Pet → Dog → ServiceDog`

**Deliverable:** Table with columns: Snippet | Anti-pattern | Refactor | GoF pattern (if any). See [common-mistakes.md](../common-mistakes.md).

---

## Exercise 5: Interview Drill (30 min)

Practice aloud from [01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md):

1. Q001 (Singleton vs DI Singleton)
2. Q005 (Facade Pattern)
3. Q010 (Saga Pattern Introduction)

Target: explain *when not* to use each pattern. Score 12+/15.

---

[← Back to Week 04](../README.md)
