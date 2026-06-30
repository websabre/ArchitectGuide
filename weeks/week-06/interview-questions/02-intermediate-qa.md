# Week 06 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Big O analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Complexity |
| **Frequency** | Very Common |

### Question

What is Big O analysis and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Big O analysis when predict scaling breakpoints. Avoid when premature micro-optimization. Production example: O(n) table scan fails at 500M rows.

### Detailed Answer (3–5 minutes)

**Concept:** Big O analysis

**When to use:** Predict scaling breakpoints

**When to avoid:** Premature micro-optimization

**Production example:** O(n) table scan fails at 500M rows

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Big O analysis to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Big O analysis with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Big O analysis overkill? — Premature micro-optimization**
2. **How measure success after adopting Big O analysis? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Big O analysis without production example
- Using Big O analysis when premature micro-optimization
- No rollback plan when Big O analysis misconfigured

---

## Q032: Binary search

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Common |

### Question

What is Binary search and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Binary search when sorted data o(log n) lookup. Avoid when unsorted datasets. Production example: B-tree index search on disk.

### Detailed Answer (3–5 minutes)

**Concept:** Binary search

**When to use:** Sorted data O(log n) lookup

**When to avoid:** Unsorted datasets

**Production example:** B-tree index search on disk

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Binary search to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Binary search with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Binary search overkill? — Unsorted datasets**
2. **How measure success after adopting Binary search? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Binary search without production example
- Using Binary search when unsorted datasets
- No rollback plan when Binary search misconfigured

---

## Q033: Merge sort external

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Occasional |

### Question

What is Merge sort external and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Merge sort external when large disk-backed sorts. Avoid when small in-memory arrays. Production example: MapReduce shuffle sort phase.

### Detailed Answer (3–5 minutes)

**Concept:** Merge sort external

**When to use:** Large disk-backed sorts

**When to avoid:** Small in-memory arrays

**Production example:** MapReduce shuffle sort phase

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Merge sort external to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Merge sort external with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Merge sort external overkill? — Small in-memory arrays**
2. **How measure success after adopting Merge sort external? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Merge sort external without production example
- Using Merge sort external when small in-memory arrays
- No rollback plan when Merge sort external misconfigured

---

## Q034: Dijkstra shortest path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Very Common |

### Question

What is Dijkstra shortest path and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Dijkstra shortest path when weighted routing decisions. Avoid when unweighted simple bfs enough. Production example: CDN edge path selection concept.

### Detailed Answer (3–5 minutes)

**Concept:** Dijkstra shortest path

**When to use:** Weighted routing decisions

**When to avoid:** Unweighted simple BFS enough

**Production example:** CDN edge path selection concept

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Dijkstra shortest path to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Dijkstra shortest path with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Dijkstra shortest path overkill? — Unweighted simple BFS enough**
2. **How measure success after adopting Dijkstra shortest path? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Dijkstra shortest path without production example
- Using Dijkstra shortest path when unweighted simple bfs enough
- No rollback plan when Dijkstra shortest path misconfigured

---

## Q035: Topological sort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is Topological sort and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Topological sort when build/deploy dependency ordering. Avoid when cyclic workflows. Production example: CI pipeline task DAG ordering.

### Detailed Answer (3–5 minutes)

**Concept:** Topological sort

**When to use:** Build/deploy dependency ordering

**When to avoid:** Cyclic workflows

**Production example:** CI pipeline task DAG ordering

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Topological sort to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Topological sort with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Topological sort overkill? — Cyclic workflows**
2. **How measure success after adopting Topological sort? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Topological sort without production example
- Using Topological sort when cyclic workflows
- No rollback plan when Topological sort misconfigured

---

## Q036: Dynamic programming memoization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DP |
| **Frequency** | Occasional |

### Question

What is Dynamic programming memoization and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Dynamic programming memoization when avoid redundant expensive computation. Avoid when simple linear workflows. Production example: Precomputed shipping rate matrix lookup.

### Detailed Answer (3–5 minutes)

**Concept:** Dynamic programming memoization

**When to use:** Avoid redundant expensive computation

**When to avoid:** Simple linear workflows

**Production example:** Precomputed shipping rate matrix lookup

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Dynamic programming memoization to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Dynamic programming memoization with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Dynamic programming memoization overkill? — Simple linear workflows**
2. **How measure success after adopting Dynamic programming memoization? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Dynamic programming memoization without production example
- Using Dynamic programming memoization when simple linear workflows
- No rollback plan when Dynamic programming memoization misconfigured

---

## Q037: Greedy heuristics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Optimization |
| **Frequency** | Very Common |

### Question

What is Greedy heuristics and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Greedy heuristics when fast near-optimal routing/scheduling. Avoid when proven global optimum required. Production example: Bin packing for container placement.

### Detailed Answer (3–5 minutes)

**Concept:** Greedy heuristics

**When to use:** Fast near-optimal routing/scheduling

**When to avoid:** Proven global optimum required

**Production example:** Bin packing for container placement

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Greedy heuristics to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Greedy heuristics with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Greedy heuristics overkill? — Proven global optimum required**
2. **How measure success after adopting Greedy heuristics? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Greedy heuristics without production example
- Using Greedy heuristics when proven global optimum required
- No rollback plan when Greedy heuristics misconfigured

---

## Q038: Amortized analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Complexity |
| **Frequency** | Common |

### Question

What is Amortized analysis and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Amortized analysis when explain rare latency spikes. Avoid when average-only thinking. Production example: Gen2 GC and log compaction spikes.

### Detailed Answer (3–5 minutes)

**Concept:** Amortized analysis

**When to use:** Explain rare latency spikes

**When to avoid:** Average-only thinking

**Production example:** Gen2 GC and log compaction spikes

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Amortized analysis to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Amortized analysis with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Amortized analysis overkill? — Average-only thinking**
2. **How measure success after adopting Amortized analysis? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Amortized analysis without production example
- Using Amortized analysis when average-only thinking
- No rollback plan when Amortized analysis misconfigured

---

## Q039: Two pointers technique

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Occasional |

### Question

What is Two pointers technique and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Two pointers technique when sorted array pair problems. Avoid when unsorted random access. Production example: Merge two sorted audit log streams.

### Detailed Answer (3–5 minutes)

**Concept:** Two pointers technique

**When to use:** Sorted array pair problems

**When to avoid:** Unsorted random access

**Production example:** Merge two sorted audit log streams

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Two pointers technique to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Two pointers technique with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Two pointers technique overkill? — Unsorted random access**
2. **How measure success after adopting Two pointers technique? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Two pointers technique without production example
- Using Two pointers technique when unsorted random access
- No rollback plan when Two pointers technique misconfigured

---

## Q040: Sliding window

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

What is Sliding window and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Sliding window when streaming metrics and rate limits. Avoid when batch offline only. Production example: 5-minute error rate rolling alert.

### Detailed Answer (3–5 minutes)

**Concept:** Sliding window

**When to use:** Streaming metrics and rate limits

**When to avoid:** Batch offline only

**Production example:** 5-minute error rate rolling alert

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Sliding window to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Sliding window with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Sliding window overkill? — Batch offline only**
2. **How measure success after adopting Sliding window? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Sliding window without production example
- Using Sliding window when batch offline only
- No rollback plan when Sliding window misconfigured

---

## Q041: BFS vs DFS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is BFS vs DFS and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use BFS vs DFS when shortest path vs cycle detection. Avoid when same algorithm for everything. Production example: BFS blast radius from failed payment service.

### Detailed Answer (3–5 minutes)

**Concept:** BFS vs DFS

**When to use:** Shortest path vs cycle detection

**When to avoid:** Same algorithm for everything

**Production example:** BFS blast radius from failed payment service

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect BFS vs DFS to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify BFS vs DFS with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is BFS vs DFS overkill? — Same algorithm for everything**
2. **How measure success after adopting BFS vs DFS? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting BFS vs DFS without production example
- Using BFS vs DFS when same algorithm for everything
- No rollback plan when BFS vs DFS misconfigured

---

## Q042: Backtracking with pruning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Occasional |

### Question

What is Backtracking with pruning and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Backtracking with pruning when constraint satisfaction exploration. Avoid when polynomial greedy sufficient. Production example: Configuration validation with early exit.

### Detailed Answer (3–5 minutes)

**Concept:** Backtracking with pruning

**When to use:** Constraint satisfaction exploration

**When to avoid:** Polynomial greedy sufficient

**Production example:** Configuration validation with early exit

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Backtracking with pruning to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Backtracking with pruning with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Backtracking with pruning overkill? — Polynomial greedy sufficient**
2. **How measure success after adopting Backtracking with pruning? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Backtracking with pruning without production example
- Using Backtracking with pruning when polynomial greedy sufficient
- No rollback plan when Backtracking with pruning misconfigured

---

## Q043: NP-hard heuristics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Optimization |
| **Frequency** | Very Common |

### Question

What is NP-hard heuristics and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use NP-hard heuristics when vrp and scheduling at scale. Avoid when small n exact solve. Production example: Delivery route OR-Tools heuristic.

### Detailed Answer (3–5 minutes)

**Concept:** NP-hard heuristics

**When to use:** VRP and scheduling at scale

**When to avoid:** Small n exact solve

**Production example:** Delivery route OR-Tools heuristic

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect NP-hard heuristics to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify NP-hard heuristics with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is NP-hard heuristics overkill? — Small n exact solve**
2. **How measure success after adopting NP-hard heuristics? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting NP-hard heuristics without production example
- Using NP-hard heuristics when small n exact solve
- No rollback plan when NP-hard heuristics misconfigured

---

## Q044: Recursion depth limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Recursion |
| **Frequency** | Common |

### Question

What is Recursion depth limits and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Recursion depth limits when hierarchy and tree traversal. Avoid when deep unbounded chains. Production example: Org chart materialized path instead of deep recursion.

### Detailed Answer (3–5 minutes)

**Concept:** Recursion depth limits

**When to use:** Hierarchy and tree traversal

**When to avoid:** Deep unbounded chains

**Production example:** Org chart materialized path instead of deep recursion

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Recursion depth limits to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Recursion depth limits with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Recursion depth limits overkill? — Deep unbounded chains**
2. **How measure success after adopting Recursion depth limits? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Recursion depth limits without production example
- Using Recursion depth limits when deep unbounded chains
- No rollback plan when Recursion depth limits misconfigured

---

## Q045: Parallel algorithm decomposition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Parallel |
| **Frequency** | Occasional |

### Question

What is Parallel algorithm decomposition and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Parallel algorithm decomposition when cpu-bound batch processing. Avoid when tiny datasets. Production example: Parallel LINQ on large batch validation.

### Detailed Answer (3–5 minutes)

**Concept:** Parallel algorithm decomposition

**When to use:** CPU-bound batch processing

**When to avoid:** Tiny datasets

**Production example:** Parallel LINQ on large batch validation

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Parallel algorithm decomposition to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Parallel algorithm decomposition with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Parallel algorithm decomposition overkill? — Tiny datasets**
2. **How measure success after adopting Parallel algorithm decomposition? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Parallel algorithm decomposition without production example
- Using Parallel algorithm decomposition when tiny datasets
- No rollback plan when Parallel algorithm decomposition misconfigured

---

## Q046: Quickselect kth element

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Selection |
| **Frequency** | Very Common |

### Question

What is Quickselect kth element and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Quickselect kth element when o(n) average kth. Avoid when sort for kth. Production example: Median quickselect.

### Detailed Answer (3–5 minutes)

**Concept:** Quickselect kth element

**When to use:** O(n) average kth

**When to avoid:** Sort for kth

**Production example:** Median quickselect

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Quickselect kth element to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Quickselect kth element with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Quickselect kth element overkill? — Sort for kth**
2. **How measure success after adopting Quickselect kth element? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Quickselect kth element without production example
- Using Quickselect kth element when sort for kth
- No rollback plan when Quickselect kth element misconfigured

---

## Q047: Median of medians

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Selection |
| **Frequency** | Common |

### Question

What is Median of medians and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Median of medians when worst case linear. Avoid when mom overkill. Production example: Theory guaranteed median.

### Detailed Answer (3–5 minutes)

**Concept:** Median of medians

**When to use:** Worst case linear

**When to avoid:** MoM overkill

**Production example:** Theory guaranteed median

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Median of medians to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Median of medians with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Median of medians overkill? — MoM overkill**
2. **How measure success after adopting Median of medians? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Median of medians without production example
- Using Median of medians when mom overkill
- No rollback plan when Median of medians misconfigured

---

## Q048: Introselect hybrid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Selection |
| **Frequency** | Occasional |

### Question

What is Introselect hybrid and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Introselect hybrid when practical kth. Avoid when introselect api. Production example: Hybrid select algorithm.

### Detailed Answer (3–5 minutes)

**Concept:** Introselect hybrid

**When to use:** Practical kth

**When to avoid:** Introselect API

**Production example:** Hybrid select algorithm

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Introselect hybrid to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Introselect hybrid with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Introselect hybrid overkill? — Introselect API**
2. **How measure success after adopting Introselect hybrid? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Introselect hybrid without production example
- Using Introselect hybrid when introselect api
- No rollback plan when Introselect hybrid misconfigured

---

## Q049: Timsort hybrid sort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Very Common |

### Question

What is Timsort hybrid sort and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Timsort hybrid sort when real world data. Avoid when timsort custom. Production example: Python Java default sort.

### Detailed Answer (3–5 minutes)

**Concept:** Timsort hybrid sort

**When to use:** Real world data

**When to avoid:** Timsort custom

**Production example:** Python Java default sort

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Timsort hybrid sort to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Timsort hybrid sort with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Timsort hybrid sort overkill? — Timsort custom**
2. **How measure success after adopting Timsort hybrid sort? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Timsort hybrid sort without production example
- Using Timsort hybrid sort when timsort custom
- No rollback plan when Timsort hybrid sort misconfigured

---

## Q050: Stable sort requirement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Common |

### Question

What is Stable sort requirement and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Stable sort requirement when preserve order. Avoid when unstable when need stable. Production example: Sort orders by date stable.

### Detailed Answer (3–5 minutes)

**Concept:** Stable sort requirement

**When to use:** Preserve order

**When to avoid:** Unstable when need stable

**Production example:** Sort orders by date stable

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Stable sort requirement to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Stable sort requirement with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Stable sort requirement overkill? — Unstable when need stable**
2. **How measure success after adopting Stable sort requirement? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Stable sort requirement without production example
- Using Stable sort requirement when unstable when need stable
- No rollback plan when Stable sort requirement misconfigured

---

## Q051: External merge sort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Occasional |

### Question

What is External merge sort and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use External merge sort when disk large sort. Avoid when in-memory sort 1tb. Production example: MapReduce shuffle sort.

### Detailed Answer (3–5 minutes)

**Concept:** External merge sort

**When to use:** Disk large sort

**When to avoid:** In-memory sort 1TB

**Production example:** MapReduce shuffle sort

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect External merge sort to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify External merge sort with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is External merge sort overkill? — In-memory sort 1TB**
2. **How measure success after adopting External merge sort? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting External merge sort without production example
- Using External merge sort when in-memory sort 1tb
- No rollback plan when External merge sort misconfigured

---

## Q052: Radix sort strings

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Very Common |

### Question

What is Radix sort strings and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Radix sort strings when fixed width keys. Avoid when radix variable unicode. Production example: IP address radix sort.

### Detailed Answer (3–5 minutes)

**Concept:** Radix sort strings

**When to use:** Fixed width keys

**When to avoid:** Radix variable unicode

**Production example:** IP address radix sort

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Radix sort strings to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Radix sort strings with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Radix sort strings overkill? — Radix variable unicode**
2. **How measure success after adopting Radix sort strings? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Radix sort strings without production example
- Using Radix sort strings when radix variable unicode
- No rollback plan when Radix sort strings misconfigured

---

## Q053: Counting sort frequency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Common |

### Question

What is Counting sort frequency and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Counting sort frequency when small range keys. Avoid when counting sort general. Production example: Age bucket counting.

### Detailed Answer (3–5 minutes)

**Concept:** Counting sort frequency

**When to use:** Small range keys

**When to avoid:** Counting sort general

**Production example:** Age bucket counting

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Counting sort frequency to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Counting sort frequency with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Counting sort frequency overkill? — Counting sort general**
2. **How measure success after adopting Counting sort frequency? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Counting sort frequency without production example
- Using Counting sort frequency when counting sort general
- No rollback plan when Counting sort frequency misconfigured

---

## Q054: Bucket sort uniform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Occasional |

### Question

What is Bucket sort uniform and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Bucket sort uniform when uniform distribution. Avoid when bucket sort skewed. Production example: Hash bucket sort.

### Detailed Answer (3–5 minutes)

**Concept:** Bucket sort uniform

**When to use:** Uniform distribution

**When to avoid:** Bucket sort skewed

**Production example:** Hash bucket sort

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bucket sort uniform to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bucket sort uniform with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Bucket sort uniform overkill? — Bucket sort skewed**
2. **How measure success after adopting Bucket sort uniform? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bucket sort uniform without production example
- Using Bucket sort uniform when bucket sort skewed
- No rollback plan when Bucket sort uniform misconfigured

---

## Q055: Shell sort gap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Very Common |

### Question

What is Shell sort gap and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Shell sort gap when in-place medium. Avoid when shell production. Production example: Embedded sort shell.

### Detailed Answer (3–5 minutes)

**Concept:** Shell sort gap

**When to use:** In-place medium

**When to avoid:** Shell production

**Production example:** Embedded sort shell

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Shell sort gap to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Shell sort gap with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Shell sort gap overkill? — Shell production**
2. **How measure success after adopting Shell sort gap? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Shell sort gap without production example
- Using Shell sort gap when shell production
- No rollback plan when Shell sort gap misconfigured

---

## Q056: Insertion sort nearly sorted

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sorting |
| **Frequency** | Common |

### Question

What is Insertion sort nearly sorted and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Insertion sort nearly sorted when small nearly sorted. Avoid when insertion large random. Production example: Timsort run insertion.

### Detailed Answer (3–5 minutes)

**Concept:** Insertion sort nearly sorted

**When to use:** Small nearly sorted

**When to avoid:** Insertion large random

**Production example:** Timsort run insertion

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Insertion sort nearly sorted to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Insertion sort nearly sorted with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Insertion sort nearly sorted overkill? — Insertion large random**
2. **How measure success after adopting Insertion sort nearly sorted? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Insertion sort nearly sorted without production example
- Using Insertion sort nearly sorted when insertion large random
- No rollback plan when Insertion sort nearly sorted misconfigured

---

## Q057: Binary search bounds

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Occasional |

### Question

What is Binary search bounds and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Binary search bounds when lower upper bound. Avoid when binary search exact only. Production example: bisect_left bisect_right.

### Detailed Answer (3–5 minutes)

**Concept:** Binary search bounds

**When to use:** Lower upper bound

**When to avoid:** Binary search exact only

**Production example:** bisect_left bisect_right

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Binary search bounds to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Binary search bounds with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Binary search bounds overkill? — Binary search exact only**
2. **How measure success after adopting Binary search bounds? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Binary search bounds without production example
- Using Binary search bounds when binary search exact only
- No rollback plan when Binary search bounds misconfigured

---

## Q058: Exponential search unbounded

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Very Common |

### Question

What is Exponential search unbounded and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Exponential search unbounded when unbounded array. Avoid when exponential bounded. Production example: Infinite list search.

### Detailed Answer (3–5 minutes)

**Concept:** Exponential search unbounded

**When to use:** Unbounded array

**When to avoid:** Exponential bounded

**Production example:** Infinite list search

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Exponential search unbounded to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Exponential search unbounded with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Exponential search unbounded overkill? — Exponential bounded**
2. **How measure success after adopting Exponential search unbounded? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Exponential search unbounded without production example
- Using Exponential search unbounded when exponential bounded
- No rollback plan when Exponential search unbounded misconfigured

---

## Q059: Interpolation search uniform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Common |

### Question

What is Interpolation search uniform and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Interpolation search uniform when uniform sorted. Avoid when interpolation skewed. Production example: Phone book interpolation.

### Detailed Answer (3–5 minutes)

**Concept:** Interpolation search uniform

**When to use:** Uniform sorted

**When to avoid:** Interpolation skewed

**Production example:** Phone book interpolation

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Interpolation search uniform to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Interpolation search uniform with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Interpolation search uniform overkill? — Interpolation skewed**
2. **How measure success after adopting Interpolation search uniform? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Interpolation search uniform without production example
- Using Interpolation search uniform when interpolation skewed
- No rollback plan when Interpolation search uniform misconfigured

---

## Q060: Ternary search unimodal

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Occasional |

### Question

What is Ternary search unimodal and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Ternary search unimodal when unimodal function. Avoid when ternary general search. Production example: Peak finding ternary.

### Detailed Answer (3–5 minutes)

**Concept:** Ternary search unimodal

**When to use:** Unimodal function

**When to avoid:** Ternary general search

**Production example:** Peak finding ternary

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Ternary search unimodal to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Ternary search unimodal with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Ternary search unimodal overkill? — Ternary general search**
2. **How measure success after adopting Ternary search unimodal? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Ternary search unimodal without production example
- Using Ternary search unimodal when ternary general search
- No rollback plan when Ternary search unimodal misconfigured

---

## Q061: BFS shortest unweighted

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Very Common |

### Question

What is BFS shortest unweighted and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use BFS shortest unweighted when shortest path unweighted. Avoid when dfs shortest path. Production example: Service blast BFS.

### Detailed Answer (3–5 minutes)

**Concept:** BFS shortest unweighted

**When to use:** Shortest path unweighted

**When to avoid:** DFS shortest path

**Production example:** Service blast BFS

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect BFS shortest unweighted to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify BFS shortest unweighted with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is BFS shortest unweighted overkill? — DFS shortest path**
2. **How measure success after adopting BFS shortest unweighted? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting BFS shortest unweighted without production example
- Using BFS shortest unweighted when dfs shortest path
- No rollback plan when BFS shortest unweighted misconfigured

---

## Q062: DFS cycle detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is DFS cycle detection and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use DFS cycle detection when detect cycles. Avoid when bfs cycle only. Production example: Dependency cycle DFS.

### Detailed Answer (3–5 minutes)

**Concept:** DFS cycle detection

**When to use:** Detect cycles

**When to avoid:** BFS cycle only

**Production example:** Dependency cycle DFS

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect DFS cycle detection to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify DFS cycle detection with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is DFS cycle detection overkill? — BFS cycle only**
2. **How measure success after adopting DFS cycle detection? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting DFS cycle detection without production example
- Using DFS cycle detection when bfs cycle only
- No rollback plan when DFS cycle detection misconfigured

---

## Q063: Kahn topological sort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Occasional |

### Question

What is Kahn topological sort and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Kahn topological sort when dag ordering. Avoid when topo sort cyclic. Production example: Build pipeline Kahn.

### Detailed Answer (3–5 minutes)

**Concept:** Kahn topological sort

**When to use:** DAG ordering

**When to avoid:** Topo sort cyclic

**Production example:** Build pipeline Kahn

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Kahn topological sort to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Kahn topological sort with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Kahn topological sort overkill? — Topo sort cyclic**
2. **How measure success after adopting Kahn topological sort? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Kahn topological sort without production example
- Using Kahn topological sort when topo sort cyclic
- No rollback plan when Kahn topological sort misconfigured

---

## Q064: Floyd Warshall all pairs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Very Common |

### Question

What is Floyd Warshall all pairs and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Floyd Warshall all pairs when all pairs shortest. Avoid when floyd large sparse. Production example: Dense graph Floyd.

### Detailed Answer (3–5 minutes)

**Concept:** Floyd Warshall all pairs

**When to use:** All pairs shortest

**When to avoid:** Floyd large sparse

**Production example:** Dense graph Floyd

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Floyd Warshall all pairs to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Floyd Warshall all pairs with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Floyd Warshall all pairs overkill? — Floyd large sparse**
2. **How measure success after adopting Floyd Warshall all pairs? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Floyd Warshall all pairs without production example
- Using Floyd Warshall all pairs when floyd large sparse
- No rollback plan when Floyd Warshall all pairs misconfigured

---

## Q065: Johnson all pairs sparse

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is Johnson all pairs sparse and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Johnson all pairs sparse when sparse all pairs. Avoid when johnson dense. Production example: Sparse APSP Johnson.

### Detailed Answer (3–5 minutes)

**Concept:** Johnson all pairs sparse

**When to use:** Sparse all pairs

**When to avoid:** Johnson dense

**Production example:** Sparse APSP Johnson

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Johnson all pairs sparse to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Johnson all pairs sparse with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Johnson all pairs sparse overkill? — Johnson dense**
2. **How measure success after adopting Johnson all pairs sparse? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Johnson all pairs sparse without production example
- Using Johnson all pairs sparse when johnson dense
- No rollback plan when Johnson all pairs sparse misconfigured

---

## Q066: A* heuristic search

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Occasional |

### Question

What is A* heuristic search and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use A* heuristic search when path with heuristic. Avoid when a* no heuristic. Production example: Navigation A*.

### Detailed Answer (3–5 minutes)

**Concept:** A* heuristic search

**When to use:** Path with heuristic

**When to avoid:** A* no heuristic

**Production example:** Navigation A*

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect A* heuristic search to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify A* heuristic search with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is A* heuristic search overkill? — A* no heuristic**
2. **How measure success after adopting A* heuristic search? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting A* heuristic search without production example
- Using A* heuristic search when a* no heuristic
- No rollback plan when A* heuristic search misconfigured

---

## Q067: Bidirectional Dijkstra

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Very Common |

### Question

What is Bidirectional Dijkstra and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Bidirectional Dijkstra when faster shortest path. Avoid when unidirectional enough. Production example: Large graph bidirectional.

### Detailed Answer (3–5 minutes)

**Concept:** Bidirectional Dijkstra

**When to use:** Faster shortest path

**When to avoid:** Unidirectional enough

**Production example:** Large graph bidirectional

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bidirectional Dijkstra to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bidirectional Dijkstra with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Bidirectional Dijkstra overkill? — Unidirectional enough**
2. **How measure success after adopting Bidirectional Dijkstra? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bidirectional Dijkstra without production example
- Using Bidirectional Dijkstra when unidirectional enough
- No rollback plan when Bidirectional Dijkstra misconfigured

---

## Q068: Bellman Ford negative

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is Bellman Ford negative and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Bellman Ford negative when negative edge weights. Avoid when bellman no negative. Production example: Currency arbitrage Bellman.

### Detailed Answer (3–5 minutes)

**Concept:** Bellman Ford negative

**When to use:** Negative edge weights

**When to avoid:** Bellman no negative

**Production example:** Currency arbitrage Bellman

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bellman Ford negative to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bellman Ford negative with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Bellman Ford negative overkill? — Bellman no negative**
2. **How measure success after adopting Bellman Ford negative? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bellman Ford negative without production example
- Using Bellman Ford negative when bellman no negative
- No rollback plan when Bellman Ford negative misconfigured

---

## Q069: SPFA queue Bellman

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Occasional |

### Question

What is SPFA queue Bellman and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use SPFA queue Bellman when bellman optimized. Avoid when spfa adversarial. Production example: Contest SPFA.

### Detailed Answer (3–5 minutes)

**Concept:** SPFA queue Bellman

**When to use:** Bellman optimized

**When to avoid:** SPFA adversarial

**Production example:** Contest SPFA

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect SPFA queue Bellman to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify SPFA queue Bellman with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is SPFA queue Bellman overkill? — SPFA adversarial**
2. **How measure success after adopting SPFA queue Bellman? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting SPFA queue Bellman without production example
- Using SPFA queue Bellman when spfa adversarial
- No rollback plan when SPFA queue Bellman misconfigured

---

## Q070: Prim MST algorithm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Very Common |

### Question

What is Prim MST algorithm and when would you apply it in Algorithms & Complexity?

### Short Answer (30 seconds)

Use Prim MST algorithm when minimum spanning tree. Avoid when prim dense graph. Production example: Network Prim MST.

### Detailed Answer (3–5 minutes)

**Concept:** Prim MST algorithm

**When to use:** Minimum spanning tree

**When to avoid:** Prim dense graph

**Production example:** Network Prim MST

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Prim MST algorithm to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Prim MST algorithm with production trade-offs in Algorithms & Complexity.

### Follow-up Questions

1. **When is Prim MST algorithm overkill? — Prim dense graph**
2. **How measure success after adopting Prim MST algorithm? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Prim MST algorithm without production example
- Using Prim MST algorithm when prim dense graph
- No rollback plan when Prim MST algorithm misconfigured

---
