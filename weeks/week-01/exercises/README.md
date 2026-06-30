# Week 01 — Exercises

## Exercise 1: Type Modeling (30 min)

Design types for a library management system:

- `Book` — has ISBN (identity), title, author, copies available
- `Loan` — links a patron to a book for a date range
- `Fine` — monetary penalty for late return

**Deliverable:** C# type definitions with justification for each `class` vs `record` vs `struct` choice. Write 1 paragraph per type.

---

## Exercise 2: Async Refactoring (45 min)

Given this problematic code:

```csharp
[HttpGet("{id}")]
public OrderDto GetOrder(Guid id)
{
    var order = _orderService.GetOrderAsync(id).Result;
    var customer = _customerService.GetCustomerAsync(order.CustomerId).Result;
    var payments = _paymentService.GetPaymentsAsync(id).Result;
    return new OrderDto(order, customer, payments);
}
```

**Tasks:**
1. Identify all problems (list at least 5)
2. Refactor to proper async with parallel I/O where possible
3. Add `CancellationToken` support
4. Explain expected latency improvement if each call takes 50ms

---

## Exercise 3: Architecture Diagram (30 min)

Draw from memory (paper or Excalidraw):
1. Async request flow through ASP.NET Core pipeline
2. GC generation lifecycle for a single request
3. Type selection decision tree (struct vs class vs record)

Time limit: 15 minutes total. Compare with [diagrams/README.md](../diagrams/README.md).

---

## Exercise 4: ADR Writing (30 min)

Write an ADR for this decision:

> "Should we use `record` or `class` for our API response DTOs in the new Order Service?"

Use [templates/adr-template.md](../../../templates/adr-template.md).

---

## Exercise 5: Interview Practice (30 min)

Answer aloud (record yourself if possible):

1. Q001 from [interview-questions/01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md)
2. Q005 from same file
3. "A junior dev asks why we use `async` everywhere. Explain in 2 minutes."

Score yourself: clarity (1-5), accuracy (1-5), trade-offs mentioned (1-5). Target: 12+/15.

---

[← Back to Week 01](../README.md)
