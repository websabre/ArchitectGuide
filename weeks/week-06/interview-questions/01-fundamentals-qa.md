# Week 06 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Big O for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Complexity Analysis |
| **Frequency** | Very Common |

### Question

Why must architects understand Big O beyond coding interviews?

### Short Answer (30 seconds)

Big O describes growth rate — architects use it to predict when designs break at 10x scale. O(n) scan on 1M rows is fine; on 1B rows it's an outage.

### Detailed Answer (3–5 minutes)

**Architect applications:**
- **Database:** missing index = O(n) scan → timeout at scale
- **API:** nested loops over cart × products = O(n×m) — breaks on large carts
- **Messaging:** O(n) fan-out to all users — need O(1) per user via push infra

Communicate with numbers: 'Current O(n) search at 10M records = 12s. Inverted index: O(log n) or O(1) — 20ms.'

### Architecture Perspective

Transforms complexity from academic to capacity planning.

### Follow-up Questions

1. **Big O vs real latency? — Constants matter — hash O(1) with disk still slow.**
2. **Worst vs average case? — Attackers target worst case — architects plan for it.**

### Common Mistakes in Interviews

- Quoting O(1) for everything
- Ignoring hidden O(n) in ORM lazy loading
- No measurement before algorithm change

---

## Q002: Sorting at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sorting |
| **Frequency** | Common |

### Question

When does sorting algorithm choice matter in production systems?

### Short Answer (30 seconds)

In-memory sort algorithm (quicksort, mergesort) matters for batch jobs. At scale, external merge sort on disk, distributed sort (MapReduce), or pre-sorted indexes (B-tree) replace in-memory sorts.

### Detailed Answer (3–5 minutes)

**Small data:** `Array.Sort` — Timsort O(n log n) — fine.

**Large batch:** External sort — chunks fit in memory, merge passes on disk.

**Distributed:** MapReduce sort, Spark `orderBy` — shuffle is expensive — architects minimize sorts.

**Database:** `ORDER BY` uses index if available — O(n) scan + sort if not.

**Architect rule:** Push sort to index where possible; avoid sorting millions of rows per request.

### Architecture Perspective

Sorting cost appears in analytics pipelines and SQL — not just coding puzzles.

### Follow-up Questions

1. **Stable sort when needed? — Merge sort stable; quicksort often not — matters for multi-key sort.**
2. **Top-K without full sort? — Heap O(n log k) better than O(n log n) full sort.**

### Common Mistakes in Interviews

- ORDER BY on unindexed column at billions of rows
- Sorting in application when DB index could serve order
- Ignoring shuffle cost in distributed sorts

---

## Q003: Binary Search Beyond Arrays

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Search |
| **Frequency** | Common |

### Question

Where does binary search apply in system architecture?

### Short Answer (30 seconds)

Binary search is O(log n) divide-and-conquer on sorted data. Applies to: B-tree index lookups, finding slot in ring buffer, versioned config rollout, git bisect for incident debugging.

### Detailed Answer (3–5 minutes)

Any monotonic predicate supports binary search: 'find smallest deployment where latency exceeds 200ms.'

**Database:** B-tree is multi-way binary search on disk blocks.

**Load balancing:** Weighted selection sometimes uses binary search on prefix sums.

**Time-series:** Binary search timestamp in sorted log for incident start.

### Architecture Perspective

Generalizes binary search from array index to operational debugging.

### Follow-up Questions

1. **Binary search on rotated array? — Coding detail; architect cares about sorted index equivalence.**
2. **Interpolation search? — When values uniformly distributed — O(log log n).**

### Common Mistakes in Interviews

- Linear scan on sorted billion-row table
- Not using index for range queries
- Binary search without monotonic invariant

---

## Q004: Graph Traversal for Dependencies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graph Algorithms |
| **Frequency** | Common |

### Question

How do BFS and DFS apply to microservice dependency analysis?

### Short Answer (30 seconds)

BFS: level-order — find all services N hops away (blast radius). DFS: deep path — detect circular dependencies, topological build order.

### Detailed Answer (3–5 minutes)

**Incident response:** Payment down → BFS from payment node → list affected services for communication.

**Deployment:** Topological sort (DFS-based) of service build DAG.

**Cycle detection:** DFS with visited set — circular sync calls are architectural bugs.

### Architecture Perspective

Graph algorithms operationalized for platform engineering.

### Follow-up Questions

1. **BFS vs DFS for shortest path? — BFS on unweighted graph; Dijkstra weighted.**
2. **Transitive dependency risk? — A→B→C means A indirectly depends on C.**

### Common Mistakes in Interviews

- No dependency graph for 20+ microservices
- Circular sync call chains undetected
- Manual incident impact analysis without traversal

---

## Q005: Dynamic Programming in Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DP |
| **Frequency** | Occasional |

### Question

Is dynamic programming relevant to architects?

### Short Answer (30 seconds)

DP mindset — optimal substructure, memoization — applies to capacity planning, cost optimization, and caching computed results. Not about coding Fibonacci — about not recomputing expensive work.

### Detailed Answer (3–5 minutes)

**Architectural DP:**
- **Memoization:** Cache expensive aggregation results (dashboard metrics)
- **Optimal substructure:** Shortest path routing — subpaths are optimal
- **Batch precomputation:** Nightly jobs vs real-time — trade storage for CPU

Example: shipping cost table precomputed for all zone pairs — O(1) lookup at checkout vs O(n) calculation per order.

### Architecture Perspective

DP as 'avoid redundant computation' resonates with architects.

### Follow-up Questions

1. **DP vs greedy? — Greedy fails when local optimal ≠ global — need DP or proof.**
2. **When precompute vs realtime? — Precompute when staleness OK and read >> write.**

### Common Mistakes in Interviews

- Recomputing aggregates on every dashboard load
- Greedy algorithm for resource allocation without proof
- DP trivia without architectural mapping

---

## Q006: Amortized Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Complexity |
| **Frequency** | Occasional |

### Question

Explain amortized complexity with a production example.

### Short Answer (30 seconds)

Amortized O(1): occasional expensive operation spread over many cheap ones. Dynamic array resize, append-only log compaction, garbage collection.

### Detailed Answer (3–5 minutes)

**Examples:**
- **ArrayList.Add:** Usually O(1), rare O(n) copy — amortized O(1)
- **Kafka log compaction:** Periodic expensive merge — amortized write cost
- **.NET GC:** Gen0 collections frequent and cheap; Gen2 rare and expensive — design for low Gen2 frequency

Architects care because p99 spikes often come from amortized 'rare' events — log compaction, full GC, resharding.

### Architecture Perspective

Explains latency spikes that averages hide.

### Follow-up Questions

1. **Amortized vs average? — Amortized worst-case bound over sequence; average is probabilistic.**
2. **Linked to p99? — Rare O(n) events cause tail latency spikes.**

### Common Mistakes in Interviews

- Designing only for average latency
- Ignoring compaction/resharding spikes
- Not capacity-planning for worst-case batch jobs

---

## Q007: NP-Hard Problems in Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | NP-Hard |
| **Frequency** | Rare |

### Question

How do architects handle NP-hard optimization problems (routing, scheduling)?

### Short Answer (30 seconds)

Use heuristics, approximation algorithms, or solvers with time limits. Exact optimal routing for 10,000 delivery vehicles is NP-hard — use greedy + local search or specialized OR-Tools.

### Detailed Answer (3–5 minutes)

**Real problems:** VRP (vehicle routing), bin packing (container placement), optimal shard balancing.

**Architect approach:**
1. Can you simplify constraints?
2. Greedy good enough? (often 90% optimal)
3. Offline optimization + online execution
4. Human-in-the-loop for edge cases

Don't block product launch waiting for perfect optimal — ship heuristic, measure gap.

### Architecture Perspective

Shows pragmatic computer science for operations research problems.

### Follow-up Questions

1. **P vs NP interview trap? — Acknowledge; pivot to practical heuristics.**
2. **OR-Tools / constraint solvers? — Use when problem well-defined and offline.**

### Common Mistakes in Interviews

- Claiming exact optimal at massive scale
- No fallback when solver times out
- Over-engineering optimization for 100-item problem

---

## Q008: Recursion and Stack Overflow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Recursion |
| **Frequency** | Common |

### Question

When does recursion become an architectural risk in .NET services?

### Short Answer (30 seconds)

Deep recursion risks stack overflow. Architects prefer iterative processing, trampolining, or workflow engines for deeply nested business logic (approval chains, org hierarchies).

### Detailed Answer (3–5 minutes)

**Risks:** 10,000-level org hierarchy recursive query — stack overflow. **Mitigations:** iterative BFS, materialized path pattern (`/1/5/23/`), closure table, or workflow engine (Durable Functions) for arbitrary depth.

**JSON deserialization** deeply nested objects — configure max depth limits.

### Architecture Perspective

Production recursion limits matter in hierarchical enterprise data.

### Follow-up Questions

1. **Tail recursion in .NET? — JIT may not optimize — don't rely on it.**
2. **Materialized path pattern? — Store `/root/parent/id` for hierarchy queries.**

### Common Mistakes in Interviews

- Unbounded recursive approval workflow
- Recursive SQL CTE without depth limit
- Stack overflow in production hierarchy API

---

## Q009: Sliding Window Algorithms

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

How do sliding window patterns apply to streaming and monitoring?

### Short Answer (30 seconds)

Sliding window: process contiguous subarray/substream in O(n). Used for rate limiting (requests per minute), moving averages in metrics, anomaly detection.

### Detailed Answer (3–5 minutes)

**Rate limiter:** Count requests in last 60 seconds — sliding window log or approximate counter.

**Metrics:** Rolling p99 latency over 5-minute window — streaming algorithms.

**Stream processing:** Flink/Kafka windowed aggregations — tumbling vs sliding vs session windows.

Architect specifies window semantics in NFRs: 'alert when error rate > 5% over 5-minute sliding window.'

### Architecture Perspective

Window semantics are architecture decisions in streaming pipelines.

### Follow-up Questions

1. **Tumbling vs sliding window? — Tumbling non-overlapping; sliding overlapping — different alert sensitivity.**
2. **Count-min sketch? — Approximate frequency in streaming — memory efficient.**

### Common Mistakes in Interviews

- Unbounded event buffer without window
- Wrong window size for seasonality
- Alert on single spike without smoothing

---

## Q010: Algorithm Choice Decision Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Framework |
| **Frequency** | Common |

### Question

Walk through how you select algorithms and data structures for a new feature.

### Short Answer (30 seconds)

Start from access pattern: read/write ratio, range vs point lookup, ordering needs, memory budget, consistency. Map pattern to DS, then to managed service (Redis, SQL index, Elasticsearch).

### Detailed Answer (3–5 minutes)

**Framework:**
1. **Access pattern** — equality, range, prefix, graph traversal?
2. **Scale** — n = ? QPS = ?
3. **Consistency** — strong or eventual?
4. **Managed service** — build vs Redis/SQL/Cosmos
5. **Measure** — prototype, load test, revise

Document in ADR with rejected alternatives.

### Architecture Perspective

Structured selection beats 'we always use X.'

### Follow-up Questions

1. **Build vs buy for search? — Elasticsearch/Azure AI Search when full-text needed.**
2. **When custom DS justified? — Extreme scale or unique constraints only.**

### Common Mistakes in Interviews

- Algorithm before requirements
- Not documenting rejected alternatives in ADR
- Building custom cache when Redis suffices

---

## Q011: Merge Sort vs Quicksort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sorting |
| **Frequency** | Common |

### Question

When choose merge sort over quicksort in production systems?

### Short Answer (30 seconds)

Merge sort: stable O(n log n) worst case, good for external sort and linked lists. Quicksort: faster in practice in-memory, O(n²) worst case, often unstable — typical library default with optimizations.

### Detailed Answer (3–5 minutes)

**Merge sort wins:**
- **External sort** — merge sorted chunks from disk
- **Stability required** — multi-key sort preserving order
- **Linked list sort** — O(1) space merge on lists
- **Parallel sort** — predictable divide for fork-join

**Quicksort wins:**
- **In-memory general sort** — cache-friendly, in-place variants
- **.NET/Java default** — Timsort (hybrid merge+insertion) not pure quicksort

**Architect:** Don't pick algorithm per API request — push ordering to index. Batch ETL: external merge sort. Know tradeoffs for pipeline design.

### Architecture Perspective

Sort choice matters in batch pipelines, not typical CRUD.

### Follow-up Questions

1. **Timsort? — Real-world hybrid — merge + insertion for runs — Python/Java default.**
2. **Introsort? — C++ std::sort — quicksort + heap sort fallback for O(n log n) worst.**

### Common Mistakes in Interviews

- In-memory quicksort on dataset larger than RAM
- Unstable sort breaking secondary key order
- Full sort when partial top-K suffices

---

## Q012: Heap Sort Use Cases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sorting |
| **Frequency** | Occasional |

### Question

When is heap sort the right choice in system design?

### Short Answer (30 seconds)

Heap sort: O(n log n) in-place, not stable. Best when memory is tight and you need guaranteed O(n log n) without merge sort's extra space. Introsort uses heap sort as quicksort worst-case fallback.

### Detailed Answer (3–5 minutes)

**Use cases:**
- **Priority-driven processing** — heap more natural than heap sort on full array
- **Top-K extraction** — min-heap of size K is O(n log k), better than heap sorting entire array
- **Real-time systems** — bounded worst case matters

**Rarely:** Full array heap sort in application code — libraries handle it.

**Architect:** Think heap data structure for scheduling and top-K, not heap sort algorithm for reporting queries. SQL `ORDER BY` with limit uses heap internally in some engines.

### Architecture Perspective

Heap sort matters as worst-case guard; heap structure matters for operations.

### Follow-up Questions

1. **Heap sort vs merge for in-place? — Heap in-place O(1) extra; merge needs O(n).**
2. **Why introsort uses heap? — Guarantees O(n log n) when quicksort pivots degrade.**

### Common Mistakes in Interviews

- Heap sorting 1B rows in app memory
- Using full sort for top-10 leaderboard
- Not knowing library already uses introsort/timsort

---

## Q013: Radix and Counting Sort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sorting |
| **Frequency** | Occasional |

### Question

When do radix sort or counting sort beat comparison sorts?

### Short Answer (30 seconds)

Non-comparison sorts: O(n) when key range is bounded. Counting sort for small integer range; radix sort for fixed-width keys (IDs, IPs). Used in suffix arrays, GPU sorts, specialized indexes.

### Detailed Answer (3–5 minutes)

**Counting sort:** O(n + k) where k = max value — fine when k is small (e.g., ages 0–120).

**Radix sort:** Process digit by digit — O(n × d) for d digits. LSD radix for 32-bit integers, fixed-length strings.

**Production:**
- **IP routing tables** — prefix/suffix sorting patterns
- **GPU batch sorts** — radix on parallel hardware
- **Bucket sort by hash prefix** — shuffle in MapReduce

**Architect:** When user IDs are numeric and range bounded, bucket by radix digit for sharding — related concept. Don't radix sort arbitrary strings in API layer.

### Architecture Perspective

Linear-time sorts exploit key structure — not general purpose.

### Follow-up Questions

1. **Radix vs hash partition? — Radix for ordered buckets; hash for uniform distribution.**
2. **When counting sort fails? — k larger than n — memory explodes.**

### Common Mistakes in Interviews

- Comparison sort on million duplicate small integers
- Radix sort on variable-length UTF-8 without care
- O(n) claim without bounded key assumption

---

## Q014: Binary Search Variants

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Search |
| **Frequency** | Common |

### Question

What binary search variants matter beyond sorted array lookup?

### Short Answer (30 seconds)

Variants: lower_bound (first ≥ target), upper_bound (first > target), search rotated array, binary search on answer (parametric search). B-tree index lookup is multi-way binary search.

### Detailed Answer (3–5 minutes)

**Parametric search:** 'Minimum cache size so p99 < 100ms' — monotonic predicate, binary search on configuration space.

**Production:**
- **Capacity planning** — binary search replica count in load test
- **Feature flags rollout** — bisect percentage until error rate threshold
- **Git bisect** — find introducing commit — operational binary search

**Invariant:** Monotonicity — if predicate true at x, true at all x' > x (or < x).

**Architect:** Binary search on answer is underused — applies to tuning, not just arrays.

### Architecture Perspective

Binary search generalizes to any monotonic decision problem.

### Follow-up Questions

1. **Lower bound vs upper bound? — Range query boundaries; equal_range for duplicates.**
2. **Binary search on floating point? — Careful with precision and iteration limit.**

### Common Mistakes in Interviews

- Linear scan configuration space for tuning
- Binary search without proving monotonic invariant
- Off-by-one in lower_bound implementation

---

## Q015: Master Theorem Intuition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Complexity |
| **Frequency** | Occasional |

### Question

Explain the master theorem intuition for divide-and-conquer recurrences.

### Short Answer (30 seconds)

Master theorem solves T(n) = aT(n/b) + O(n^d). Compare log_b(a) vs d: more subproblems → leaves dominate; equal → balanced; fewer → root work dominates.

### Detailed Answer (3–5 minutes)

**Intuition:**
- **Case 1 (log_b a > d):** Leaf work dominates — O(n^{log_b a}) — merge sort T(n)=2T(n/2)+O(n) → O(n log n)
- **Case 2 (equal):** Balanced — O(n^d log n)
- **Case 3 (log_b a < d):** Root dominates — O(n^d)

**Architect use:** Estimate MapReduce cost — a mappers, b reduction factor, O(n^d) merge cost. Predict when distributed merge becomes bottleneck.

Don't memorize — communicate: 'Recursive halving with linear merge → n log n.'

### Architecture Perspective

Master theorem quantifies distributed divide-and-conquer pipelines.

### Follow-up Questions

1. **Akra-Bazzi? — Generalization when subproblem sizes vary — more accurate for real systems.**
2. **When master theorem fails? — Non-polynomial f(n) or uneven splits — use recursion tree.**

### Common Mistakes in Interviews

- Quoting master theorem without relating to pipeline cost
- Ignoring communication cost in distributed recurrence
- Assuming perfect halving in skewed data partitions

---

## Q016: Topological Sort Algorithm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graph Algorithms |
| **Frequency** | Common |

### Question

Compare Kahn's algorithm and DFS for topological sort. When prefer each?

### Short Answer (30 seconds)

Kahn's: BFS by in-degree — peel nodes with in-degree 0, detect cycles if nodes remain. DFS: post-order finish times — reverse for topo order. Both O(V+E).

### Detailed Answer (3–5 minutes)

**Kahn's advantages:**
- Natural parallelization — all in-degree-0 nodes at same level
- Explicit cycle detection (queue stalls)
- Intuitive for build pipelines

**DFS advantages:**
- Compact recursive code
- Combined with cycle detection (back edge)
- Single pass for connected components + topo

**Production:** Terraform plan uses DFS-style dependency walk. CI systems often Kahn for parallel stage execution.

**Architect:** Expose parallel levels in pipeline UI — Kahn's level structure maps directly.

### Architecture Perspective

Algorithm choice affects parallelization of deploy graphs.

### Follow-up Questions

1. **Lexicographic topo sort? — Priority queue for in-degree-0 — deterministic order.**
2. **Topo sort on cyclic graph? — Impossible — return cycle for engineer fix.**

### Common Mistakes in Interviews

- DFS topo without cycle check on dependency graph
- Serial deploy when parallel levels exist
- O(V²) in-degree scan each iteration instead of queue

---

## Q017: Cycle Detection Algorithms

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graph Algorithms |
| **Frequency** | Common |

### Question

How detect cycles in directed vs undirected graphs in architecture contexts?

### Short Answer (30 seconds)

Directed: DFS with three colors (white/gray/black) — back edge to gray node = cycle. Or Kahn's — nodes left after processing. Undirected: DFS tracking parent — edge to visited non-parent = cycle.

### Detailed Answer (3–5 minutes)

**Architecture mappings:**
- **Microservice sync calls** — directed cycle = deadlock risk
- **Circular FK dependencies** — migration graph cycle
- **Deadlock detection** — wait-for graph cycles
- **Terraform** — cycle prevents apply

**Union-find:** Undirected cycle detection during MST build — adding edge connecting same component.

**Architect:** Run cycle detection in CI on service dependency manifest — fail build before production deadlock.

### Architecture Perspective

Cycle detection prevents class of production failures in dependency graphs.

### Follow-up Questions

1. **Directed vs undirected cycle? — Mutual A↔B sync calls — directed 2-cycle.**
2. **Self-loop? — Trivial cycle — validate in schema.**

### Common Mistakes in Interviews

- No dependency graph validation in CI
- Confusing undirected and directed cycle algorithms
- Ignoring indirect cycles A→B→C→A

---

## Q018: Bellman-Ford vs Dijkstra

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graph Algorithms |
| **Frequency** | Common |

### Question

When use Bellman-Ford over Dijkstra for shortest path problems?

### Short Answer (30 seconds)

Dijkstra: non-negative weights, O((V+E) log V) with heap. Bellman-Ford: handles negative weights, detects negative cycles, O(VE) — slower but more general.

### Detailed Answer (3–5 minutes)

**Bellman-Ford when:**
- Negative edge weights (currency arbitrage detection)
- Need negative cycle detection
- Small sparse graphs where VE acceptable
- Distributed Bellman-Ford variants in distance-vector routing (RIP)

**Dijkstra when:**
- Non-negative weights (latency, distance, cost)
- Large graphs — need efficiency
- Production routing, CDN path selection

**Architect:** Service latency routing = non-negative → Dijkstra or A*. Financial netting with credits/debits — validate sign convention before algorithm choice.

### Architecture Perspective

Shortest path algorithm follows edge weight semantics.

### Follow-up Questions

1. **Floyd-Warshall? — All-pairs O(V³) — small V only (network topology matrix).**
2. **Johnson's algorithm? — All-pairs sparse with reweighting — rare in interviews.**

### Common Mistakes in Interviews

- Dijkstra on graph with negative latency 'boosts'
- Bellman-Ford on million-node graph per request
- Not detecting negative cycle in arbitrage scenario

---

## Q019: Rabin-Karp String Search

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | String Algorithms |
| **Frequency** | Occasional |

### Question

How does Rabin-Karp apply beyond string matching in interviews?

### Short Answer (30 seconds)

Rabin-Karp: rolling hash compares pattern in O(n) average — hash match then verify. Used for plagiarism detection, duplicate file finding, multi-pattern search, DNA sequence matching.

### Detailed Answer (3–5 minutes)

**Rolling hash:** Update hash in O(1) when window slides — remove left char, add right char.

**Production:**
- **Duplicate detection** — hash file chunks, compare hashes before byte compare
- **Git blob identification** — content hash (SHA, not Rabin-Karp, but same rolling concept for diff)
- **IDS signature matching** — multiple patterns via hash buckets

**Collision handling:** Hash match → verify characters — avoid false positive.

**Architect:** Content-defined chunking (rsync, backup dedup) uses rolling hash for boundary detection.

### Architecture Perspective

Rolling hash enables streaming pattern and duplicate detection.

### Follow-up Questions

1. **Rabin-Karp vs KMP? — KMP O(n) worst case single pattern; Rabin-Karp better multiple patterns.**
2. **Polynomial hash modulo prime? — Base and mod chosen to reduce collisions.**

### Common Mistakes in Interviews

- Byte-by-byte compare on GB files for duplicate find
- Ignoring hash collision verification step
- Wrong modulus causing excessive collisions

---

## Q020: Backtracking with Pruning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Backtracking |
| **Frequency** | Occasional |

### Question

Explain backtracking with pruning. Where does it appear in system design?

### Short Answer (30 seconds)

Backtracking explores decision tree, abandons branches when constraints fail (prune). Used in constraint solvers, scheduling, config validation, test case generation — not brute force enumeration.

### Detailed Answer (3–5 minutes)

**Pruning examples:**
- **Resource allocation** — stop branch when budget exceeded
- **Scheduling** — skip assignment violating hard constraints
- **Feature flag matrix** — invalid combinations pruned early

**Production:** OR-Tools, SAT solvers, SQL query optimizer prunes plan search space.

**Architect:** Offline optimization (shift scheduling, capacity planning) uses backtracking/branch-and-bound with time limit — return best-so-far if timeout.

### Architecture Perspective

Pruning is how systems make NP-hard search tractable.

### Follow-up Questions

1. **Branch and bound? — Prune when lower bound exceeds best known solution.**
2. **Time-boxed solver? — Architect specifies max solve time for config generation.**

### Common Mistakes in Interviews

- Brute force all combinations for 40-flag config
- No pruning in custom allocation engine
- Infinite backtracking without memoization on overlapping subproblems

---

## Q021: NP-Hard Recognition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | NP-Hard |
| **Frequency** | Occasional |

### Question

How recognize NP-hard problems in architecture and respond appropriately?

### Short Answer (30 seconds)

NP-hard: no known polynomial exact solution. Recognize: scheduling, routing, bin packing, graph coloring, optimal shard placement. Response: heuristics, approximation, limits, or offline solver.

### Detailed Answer (3–5 minutes)

**Recognition signals:**
- 'Optimal' assignment of N items to M containers minimizing cost
- Traveling salesman / vehicle routing
- Boolean satisfiability for complex rule sets

**Architect playbook:**
1. **Simplify** — reduce constraints
2. **Heuristic** — greedy 90% solution
3. **Approximation algorithm** — proven bound (e.g., 2-approx bin packing)
4. **Offline + cache** — solve nightly, serve lookup
5. **Human override** — edge cases

Don't promise real-time optimal at scale.

### Architecture Perspective

Recognizing NP-hard prevents impossible SLA commitments.

### Follow-up Questions

1. **NP-hard vs NP-complete? — Interview precision; both mean 'don't expect polynomial exact.'**
2. **APX-hard? — Even constant approximation may be hard — set expectations lower.**

### Common Mistakes in Interviews

- Promising optimal real-time routing for 10K vehicles
- Exact solver with no timeout in API path
- Not identifying problem as NP-hard before estimating

---

## Q022: Parallel Algorithm Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Parallelism |
| **Frequency** | Common |

### Question

What parallel algorithm patterns matter for architects designing scalable systems?

### Short Answer (30 seconds)

Patterns: map-reduce, fork-join divide-conquer, pipeline parallelism, data parallelism, scatter-gather. Amdahl's law limits speedup — sequential bottleneck dominates.

### Detailed Answer (3–5 minutes)

**MapReduce:** Map shards process in parallel; shuffle; reduce aggregates. Spark, Hadoop.

**Fork-join:** Parallel merge sort, parallel graph traversal with careful synchronization.

**Pipeline:** Assembly line stages — Kafka consumers per stage.

**Data parallel:** Same operation on array shards — SIMD, GPU batch inference.

**Architect:** Identify sequential fraction — if 5% serial, max 20× speedup regardless of cores. Partition data to minimize shuffle (expensive network).

### Architecture Perspective

Parallel patterns map to Spark, K8s jobs, and stream pipelines.

### Follow-up Questions

1. **Amdahl's law example? — 10% serial → max 10× speedup on infinite cores.**
2. **Straggler problem? — Slowest map task delays reduce — speculative execution.**

### Common Mistakes in Interviews

- Parallelize without measuring sequential bottleneck
- Massive shuffle in every Spark job
- Shared mutable state across parallel workers

---

## Q023: External Merge Sort

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sorting |
| **Frequency** | Common |

### Question

Explain external merge sort for datasets larger than memory.

### Short Answer (30 seconds)

Phase 1: sort chunks in memory, write sorted runs to disk. Phase 2: k-way merge runs using min-heap. O(n log n) comparisons, O(n/B) I/O passes with buffer size B.

### Detailed Answer (3–5 minutes)

**When needed:**
- ETL sorting billion-row warehouse table
- Database ORDER BY spilling to disk
- Log file merge across time partitions

**Optimization:**
- **Larger run size** — match RAM budget
- **k-way merge** — heap of size k, not pairwise merge
- **SSD vs HDD** — I/O dominates; sequential read matters

**Architect:** Design batch jobs with known memory ceiling — external sort built into Spark, SQL Server, not hand-rolled. Hand-roll only embedded/edge constraints.

### Architecture Perspective

External sort is how 'sort everything' works at warehouse scale.

### Follow-up Questions

1. **Replacement selection? — Generate longer initial runs — fewer merge passes.**
2. **Polyphase merge? — Optimize tape/disk drive utilization — classic DB technique.**

### Common Mistakes in Interviews

- Load entire billion-row file into API memory
- Pairwise merge of 1000 runs — inefficient
- Random disk access during merge — kill performance

---

## Q024: Reservoir Sampling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sampling |
| **Frequency** | Common |

### Question

What is reservoir sampling and where is it used in streaming systems?

### Short Answer (30 seconds)

Reservoir sampling: uniform random sample of size k from stream of unknown length in O(n) time, O(k) memory. Each element seen has k/i probability of entering reservoir at step i.

### Detailed Answer (3–5 minutes)

**Use cases:**
- **Log sampling** — retain representative 0.1% for debugging without bias
- **A/B test analysis** — uniform subsample for expensive computation
- **Stream QA** — continuous quality sample from Kafka topic

**Variants:** Weighted reservoir sampling for non-uniform probabilities.

**Architect:** Prefer reservoir over 'every Nth' — Nth is biased if stream has patterns. Document sampling rate in observability ADR.

### Architecture Perspective

Unbiased streaming sample under memory constraints.

### Follow-up Questions

1. **Reservoir size k choice? — Balance storage vs statistical confidence.**
2. **Distributed reservoir? — Per-shard sample then merge — approximate global uniform.**

### Common Mistakes in Interviews

- Take first k events as sample — biased
- Every-1000th event sample on periodic traffic — aliasing
- Reservoir per thread without merge strategy

---

## Q025: Fisher-Yates Shuffle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Randomization |
| **Frequency** | Occasional |

### Question

Why is Fisher-Yates the correct shuffle algorithm for fair randomization?

### Short Answer (30 seconds)

Fisher-Yates (Knuth shuffle): O(n) unbiased permutation. For each i from n-1 down to 1, swap i with random j in [0,i]. Every permutation equally likely.

### Detailed Answer (3–5 minutes)

**Production:**
- **Load balancer** — shuffle backend list for fairness
- **A/B experiment** — randomize cohort assignment
- **Game/matchmaking** — fair random ordering
- **ML training** — shuffle training data each epoch

**Wrong approach:** Sort by random() — biased due to duplicate random keys and sort stability issues.

**Architect:** Use crypto RNG (`RandomNumberGenerator` in .NET) for security-sensitive shuffle; `System.Random` for load distribution.

### Architecture Perspective

Fair shuffle matters for experiments and load distribution integrity.

### Follow-up Questions

1. **Shuffle vs sample? — Shuffle permutes all; reservoir samples subset.**
2. **Seed for reproducibility? — Fixed seed in ML; not for security.**

### Common Mistakes in Interviews

- Sort by Math.random() for shuffle
- Modulo bias when mapping random to index
- Predictable PRNG for lottery or security shuffle

---

## Q026: Reservoir for Streaming Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sampling |
| **Frequency** | Common |

### Question

How combine reservoir sampling with streaming analytics pipelines?

### Short Answer (30 seconds)

Reservoir provides unbiased fixed-size sample stream; downstream aggregates (percentiles, histograms) run on sample with known confidence bounds.

### Detailed Answer (3–5 minutes)

**Pipeline:**
1. Kafka consumer → reservoir buffer size 10K
2. On flush interval → compute metrics on sample
3. Extrapolate with confidence interval to full population

**vs Count-min/HLL:** Reservoir keeps actual events for debugging; sketches aggregate without retention.

**Architect:** Dual path — sketches for real-time dashboard (HLL, count-min), reservoir for drill-down and incident investigation.

### Architecture Perspective

Sampling strategy is observability architecture decision.

### Follow-up Questions

1. **Sample and hold vs reservoir? — Reservoir uniform; sample-and-hold may bias recent.**
2. **Confidence intervals on sample metrics? — Document error bars for stakeholders.**

### Common Mistakes in Interviews

- Store all events for 'just in case' at 1M/sec
- Metrics on biased every-Nth sample
- No sample retention policy — compliance risk

---

## Q027: Meet-in-the-Middle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Algorithm Patterns |
| **Frequency** | Occasional |

### Question

Explain meet-in-the-middle. When does it apply to architecture-scale problems?

### Short Answer (30 seconds)

Meet-in-the-middle: split problem in half, solve each half, combine via hash lookup — reduces O(2^n) to O(2^{n/2}). Applies to subset sum, password cracking partitions, pairing search spaces.

### Detailed Answer (3–5 minutes)

**Architectural analogy:**
- **Distributed join** — partition both sides, hash join on key — same intersection idea
- **Security** — key search space halved per node in distributed crack (ethical pentest)
- **Feature combination testing** — test half-configs on each environment, intersect failures

**Coding:** Subset sum for budget allocation with 40 items — brute force 2^40 impossible; meet-in-the-middle 2^20 + 2^20 feasible.

**Architect:** When exponential search seems needed, ask if problem splits for hash-based intersection.

### Architecture Perspective

Meet-in-the-middle is exponential search made feasible via hashing.

### Follow-up Questions

1. **Hash join similarity? — Build hash on smaller half; probe with larger — SQL optimizer.**
2. **Space-time tradeoff? — Store half results in memory/disk for lookup.**

### Common Mistakes in Interviews

- Brute force exponential without split attempt
- Meet-in-the-middle without hash — O(n²) intersection
- Applying to problem without separable halves

---

## Q028: Bit Manipulation Tricks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Bit Manipulation |
| **Frequency** | Occasional |

### Question

What bit manipulation techniques are useful for architects and performance engineers?

### Short Answer (30 seconds)

Techniques: power-of-two sizing (mask instead of mod), feature flags in bitmask, bloom filter bit array, permission sets, cardinality in bitmap indexes.

### Detailed Answer (3–5 minutes)

**Production:**
- **Feature flags** — `flags & FEATURE_X` — compact permission storage
- **Roaring bitmap** — compressed bitmap indexes in analytics DBs (Druid, Pinot)
- **Bloom filter** — bit array with k hashes
- **Connection pooling bitmap** — track free slots

**Useful ops:** `x & (x-1)` clears lowest set bit (count bits); `x & -x` isolates lowest bit.

**Architect:** Bitmap index for low-cardinality columns (status, country) in OLAP — 100× compression vs naive storage.

### Architecture Perspective

Bits pack state efficiently at scale — flags, indexes, filters.

### Follow-up Questions

1. **Roaring bitmap? — Hybrid array/container — better compression than naive bitmap.**
2. **Bit field in API versioning? — Compact capability negotiation.**

### Common Mistakes in Interviews

- String column index for boolean-like status
- Modulo instead of bitmask on power-of-two ring buffer
- Assuming bit ops are always faster — measure

---

## Q029: Algorithm Interview Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

How should architects communicate algorithm thinking in system design interviews?

### Short Answer (30 seconds)

Structure: clarify constraints → state brute force → optimize with DS/algorithm → analyze complexity → discuss scale limits → map to production service.

### Detailed Answer (3–5 minutes)

**Template:**
1. **Constraints** — n, QPS, memory, latency SLO
2. **Brute force** — 'Scan all rows O(n)' — honest baseline
3. **Optimization** — 'B-tree index → O(log n)' or 'cache → O(1)'
4. **Bottleneck** — 'At 10M QPS, single shard fails — shard by userId'
5. **Production** — 'Redis sorted set, not custom heap'

**Stakeholder version:** Skip Big-O symbols — 'Index cuts query from 30s to 50ms, costs 20% more write I/O.'

**Architect signal:** You connect algorithm to managed service and operational cost.

### Architecture Perspective

Communication separates senior architects from silent coders.

### Follow-up Questions

1. **When to whiteboard code vs boxes? — System design: boxes; coding round: implement.**
2. **Trade-off articulation? — 'We chose eventual consistency for 10× read throughput.'**

### Common Mistakes in Interviews

- Jump to Redis without stating access pattern
- Only Big-O without scale numbers
- Cannot explain why brute force fails at scale

---

## Q030: Complexity Proof Sketch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Complexity |
| **Frequency** | Occasional |

### Question

How sketch a complexity argument in an interview without formal proofs?

### Short Answer (30 seconds)

Use recursion tree, aggregate analysis, or loop invariants. State dominant term; ignore lower-order constants. Show you understand structure, not graduate-level proof.

### Detailed Answer (3–5 minutes)

**Recursion tree:** Merge sort — n levels, n work per level → O(n log n).

**Aggregate:** n inserts into heap of size n → each O(log n) → O(n log n) total.

**Amortized:** n appends to dynamic array — n × O(1) + log(n) resizes × O(n) → O(n) total → O(1) amortized.

**Architect version:** 'Each of n requests does hash lookup O(1) average; worst case O(n) if attacker crafts collisions — we use SipHash.'

Interviewers want structured reasoning, not LaTeX.

### Architecture Perspective

Proof sketch shows depth without academic overhead.

### Follow-up Questions

1. **Loop invariant example? — Binary search — subarray always contains answer.**
2. **When amortized vs worst case? — Present both for production systems.**

### Common Mistakes in Interviews

- Hand-wave 'it's O(n log n)' without justification
- Only average case for security-sensitive hash table
- Confuse best, average, and worst case

---
