# Algorithms & Complexity — Architect Lens

> **Week 06** | **Module:** [dsa](../../../modules/dsa/README.md)

## Learning Objectives
- Analyze Big-O for architecture decisions
- Know when algorithmic complexity matters in production
- Estimate system capacity using complexity awareness

---

## 1. Big-O Notation

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash lookup, array index |
| O(log n) | Logarithmic | Binary search, B-Tree index |
| O(n) | Linear | Scan all rows, single loop |
| O(n log n) | Linearithmic | Merge sort, efficient sorting |
| O(n²) | Quadratic | Nested loops, naive all-pairs |
| O(2ⁿ) | Exponential | Brute force combinatorics |

**Architect rule:** At 1M records, O(n²) is unacceptable. O(n log n) may need batching. O(log n) is production-grade for lookups.

---

## 2. When Architects Need Algorithms vs When They Don't

**Need deep algorithms:**
- Designing search, recommendation, routing systems
- Capacity planning for sort/aggregation at scale
- Evaluating database query plans
- Technical interviews

**Don't need to implement:**
- Business CRUD — use framework/ORM
- Standard sorting — use `OrderBy`
- Graph traversal — use graph DB or pre-built library

**Architect role:** Recognize when team proposes O(n²) solution at scale. Ask "what's n at peak?"

---

## 3. Sorting in Production

| Algorithm | Average | Stable | Use |
|-----------|---------|--------|-----|
| Quick sort | O(n log n) | No | General in-memory |
| Merge sort | O(n log n) | Yes | External sort, linked lists |
| Tim sort | O(n log n) | Yes | .NET `Array.Sort`, Python default |

**Database:** `ORDER BY` uses index (O(n) scan of index) or sort operator (O(n log n)) — **architect ensures query uses index.**

---

## 4. Search Algorithms

- **Binary search:** O(log n) on sorted data — binary search on indexed column
- **Full table scan:** O(n) — missing index
- **Index seek + key lookup:** O(log n + k) — optimal

---

## 5. Graph Algorithms in Systems

| Problem | Algorithm | Application |
|---------|-----------|-------------|
| Shortest path | Dijkstra, A* | Maps, network routing |
| Minimum spanning tree | Kruskal, Prim | Network design |
| Topological sort | DFS/Kahn | Build order, task dependencies |
| Cycle detection | DFS | Deadlock detection, dependency graphs |

---

## 6. Amortized Analysis

Dynamic array doubling: individual insert O(n) worst case, O(1) amortized.

**Architect relevance:** Understand burst vs sustained — amortized cost matters for auto-scaling decisions.

---

## 7. Space-Time Trade-offs

| Trade-off | Example |
|-----------|---------|
| More memory, faster lookup | Caching, materialized views |
| Precompute, faster read | Denormalization, read replicas |
| Less memory, slower | Streaming processing vs load all |

---

## Capacity Estimation Example

**Problem:** Sort 10M records daily for report.

- O(n log n) ≈ 10M × 23 ≈ 230M operations
- At 1M ops/sec → ~4 minutes CPU
- **Decision:** Batch job on separate worker, not in API request path

---

## Common Mistakes
1. Premature algorithm optimization on CRUD apps
2. Ignoring database index impact (biggest real-world gain)
3. Not estimating n at peak scale
4. Using nested loops on joined tables (N+1 queries)

**Next:** [diagrams/](../diagrams/) | Week 07 SQL Server
