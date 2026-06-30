# Week 06 — Algorithms for Architects Diagrams

## 1. Big-O Comparison — API Operations

```mermaid
flowchart LR
    O1[O1 Hash lookup] --> Fast[Cache hit]
    On[O n linear scan] --> Slow[List filter]
    Onlog[O n log n sort] --> Med[Report generation]
    On2[O n² nested loops] --> Bad[Anti-pattern in hot path]
```

## 2. Graph Traversal — Service Dependency Map

```mermaid
flowchart TD
    GW[API Gateway] --> O[Order Svc]
    GW --> C[Catalog Svc]
    O --> P[Payment Svc]
    O --> I[Inventory Svc]
    P --> Ext[Stripe]
```

> **Architect note:** BFS finds shortest dependency path for blast-radius analysis; DFS for cycle detection in build graphs.

## 3. Topological Sort — Deployment Order

```mermaid
flowchart LR
    DB[(Database)] --> Svc[Services]
    Svc --> GW[Gateway]
```

## 4. Sliding Window Rate Limiter

```mermaid
sequenceDiagram
    participant C as Client
    participant RL as Rate Limiter
    participant API

    C->>RL: Request + timestamp
    RL->>RL: Prune window older than 60s
    alt Under limit
        RL->>API: Forward
        API-->>C: 200 OK
    else Over limit
        RL-->>C: 429 Too Many Requests
    end
```

## 5. Sorting Choice Decision Tree

```mermaid
flowchart TD
    A[Need sorted data?] --> B{Dataset fits in memory?}
    B -->|Yes| C{Stable sort needed?}
    B -->|No| D[External sort / DB ORDER BY]
    C -->|Yes| E[Merge sort / TimSort]
    C -->|No| F[QuickSort in-process]
```

## Practice Exercise

Given 3 nested loops over order lines, estimate complexity and propose one O(n) optimization.

---

[← Back to Week 06](../README.md)
