# Week 06 — Exercises

> Theory: [theory/](../theory/README.md) · Lab: [lab-06-complexity-analysis](../labs/lab-06-complexity-analysis.md) · Interview: [interview-questions/](../interview-questions/README.md)

## Exercise 1: Big O Analysis of Code Snippet (45 min)

Analyze this nested-loop service method:

```csharp
public List<DuplicatePair> FindDuplicates(List<Order> orders)
{
    var result = new List<DuplicatePair>();
    for (int i = 0; i < orders.Count; i++)
        for (int j = i + 1; j < orders.Count; j++)
            if (orders[i].CustomerId == orders[j].CustomerId
                && orders[i].Total == orders[j].Total)
                result.Add(new DuplicatePair(orders[i], orders[j]));
    return result;
}
```

**Tasks:**
1. State time and space complexity
2. Refactor to O(n) average using a hash map
3. At what input size does the refactor matter on a 4-core API? (show math)

**Deliverable:** Before/after code + complexity comparison table.

---

## Exercise 2: Graph Traversal for Dependency Map (60 min)

Given microservice call edges: `Gateway → Order → Inventory`, `Order → Payment`, `Payment → Fraud`, `Inventory → Catalog`:

**Tasks:**
1. Build adjacency list representation
2. Run BFS from `Gateway` — list services by hop distance
3. Run DFS — detect if `Catalog` can reach `Gateway` (circular dependency?)
4. Identify critical path for order placement latency

**Deliverable:** Traversal outputs + Mermaid diagram. Extend [lab-06](../labs/lab-06-complexity-analysis.md).

---

## Exercise 3: Sorting Choice ADR (30 min)

Write an ADR for:

> "Should the analytics dashboard pre-sort 50M event rows nightly (external sort) or maintain a sorted index on `(timestamp, user_id)`?"

Constraints: 90-day retention, p95 query &lt; 200ms, batch window 2 hours.

Use [templates/adr-template.md](../../../templates/adr-template.md). Compare merge sort, B-tree index, and columnstore.

---

## Exercise 4: Sliding Window Rate Limiter Design (45 min)

Design a rate limiter: 1000 requests/minute per API key, distributed across 4 API instances.

**Tasks:**
1. Compare fixed window, sliding window log, and token bucket
2. Choose one; describe Redis or in-memory data structures
3. State space complexity per key and failure mode if Redis is down

**Deliverable:** Sequence diagram + pseudocode for `IsAllowed(apiKey)`. See [theory/](../theory/README.md).

---

## Exercise 5: Interview Drill (30 min)

Practice aloud from [01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md):

1. Q001 (Big O for Architects)
2. Q005 (Dynamic Programming in Architecture)
3. Q010 (Algorithm Choice Decision Framework)

Explain when architects should *stop* optimizing. Score 12+/15.

---

[← Back to Week 06](../README.md)
