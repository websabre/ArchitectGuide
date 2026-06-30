"""Hand-crafted premium Q001–Q010 — helper and Week 5–8 content."""


def q(title, category, frequency, question, short, detailed, perspective, fu1, fu2, m1, m2, m3):
    return dict(
        title=title, category=category, frequency=frequency, question=question,
        short=short, detailed=detailed, perspective=perspective,
        followups=f"1. **{fu1}**\n2. **{fu2}**",
        mistakes=f"- {m1}\n- {m2}\n- {m3}",
    )


PREMIUM_HEADER = """# Week {week:02d} — Fundamentals Interview Q&A

> Q001–Q010: Premium format (Week 1 quality). Q011–Q030: Practice bank.  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---

"""

QA_BLOCK = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | {category} |
| **Frequency** | {frequency} |

### Question

{question}

### Short Answer (30 seconds)

{short}

### Detailed Answer (3–5 minutes)

{detailed}

### Architecture Perspective

{perspective}

### Follow-up Questions

{followups}

### Common Mistakes in Interviews

{mistakes}

---
"""

WEEK_5 = [
    q("Hash Table for O(1) Lookup", "Hash Tables", "Very Common",
      "Why are hash tables fundamental to system design? Give three production use cases.",
      "Hash tables provide average O(1) insert, lookup, and delete via a hash function mapping keys to buckets. Used for caches, indexes, deduplication, and rate limiters.",
      "A hash table hashes a key to a bucket index. Collisions are resolved via chaining (linked lists per bucket) or open addressing. **Average** O(1); worst case O(n) if all keys collide — architects care about worst case under attack.\n\n**Production use cases:**\n1. **Redis** — entire in-memory store is hash-based structures\n2. **Distributed caches** — consistent hashing places keys on nodes (Dynamo, Cassandra ring)\n3. **Rate limiting** — token bucket keyed by userId in memory\n\nFor a URL shortener, the mapping `shortCode → longUrl` is a hash map (or DB index behaving as one). At 100K reads/sec, in-memory hash + SSD backing is the standard pattern.\n\n**Trade-off:** Hash tables don't maintain order — use balanced BST or B-tree when you need range queries (timestamps, prices).",
      "Interviewers test whether you connect data structures to system components — not just Big-O memorization.",
      "What happens when the hash function is poor? — Clustering, O(n) lookups; use cryptographic or well-distributed hashes.",
      "Hash table vs B-tree for database index? — B-tree for range scans and disk locality; hash index only for equality.",
      "Quoting O(1) without mentioning collisions",
      "Using hash table when range queries dominate",
      "Ignoring memory bounds for in-memory maps"),
    q("Array vs Linked List at Scale", "Arrays & Lists", "Common",
      "When would you choose an array-based vs linked-list-based design in a distributed system?",
      "Arrays excel at cache locality and index access; linked lists at cheap inserts/deletes in the middle. At scale, arrays (or array-backed buffers) dominate for sequential and indexed access.",
      "**Array:** contiguous memory, O(1) index access, better CPU cache behavior. Used in: columnar storage, ring buffers, batch processing.\n\n**Linked list:** O(1) insert/delete at known node, but poor cache locality and no random access. Rarely used raw at scale — skip lists and B+ trees replace them in databases.\n\n**Architect example:** Kafka log segments are append-only files (array-like sequential storage) — not linked lists. Event sourcing append streams mirror this pattern.\n\nChoose linked structures conceptually when you need cheap middle insertion in memory (LRU cache combines hash map + doubly linked list).",
      "Connect classic DS to how Kafka, DB pages, and buffers actually work.",
      "Is ArrayList always better than LinkedList in .NET? — For almost all cases yes — cache locality wins.",
      "How does columnar storage relate? — Arrays of column values — analytical query performance.",
      "Recommending linked list for database storage",
      "Not mentioning cache locality",
      "Ignoring sequential access patterns in logs and streams"),
    q("Trees in System Design", "Trees", "Very Common",
      "What tree structures appear in production systems and when does each apply?",
      "B-trees/B+ trees for disk-backed indexes (SQL databases). Tries for prefix search (autocomplete). Red-black/AVL rarely used directly — DB engines handle this.",
      "**B+ tree:** Database indexes (SQL Server, PostgreSQL). Optimized for disk blocks — high fanout, leaf nodes linked for range scans.\n\n**Trie (prefix tree):** Autocomplete, IP routing tables, spell check. O(key length) lookup.\n\n**Binary search tree:** Teaching concept; production uses balanced variants inside DB engines.\n\n**Decision tree:** Not a storage structure — ML models; different context.\n\nFor system design interview: when they say 'index the data,' they mean B-tree unless it's a key-value equality store (hash) or full-text (inverted index).",
      "Architects name the right tree for the access pattern — equality vs range vs prefix.",
      "Why B+ tree not B-tree for databases? — Leaves linked for sequential scan; internal nodes only keys.",
      "Trie vs hash for autocomplete? — Trie supports prefix queries; hash only exact match.",
      "Saying 'use a tree' without specifying access pattern",
      "Confusing DOM tree with storage index",
      "Not knowing B+ tree is the default SQL index"),
    q("Heap and Priority Queue", "Heaps", "Common",
      "How would you use a priority queue in a system design?",
      "Priority queue (min/max heap) gives O(log n) insert and O(1) peek — used for scheduling, top-K, merge streams, Dijkstra. Production: task schedulers, rate limit windows, leaderboard top-N.",
      "**Use cases:**\n1. **Task scheduling** — execute highest priority jobs first (hospital triage queue)\n2. **Top-K** — maintain K most popular products with min-heap of size K\n3. **Merge k sorted logs** — heap of head elements from each stream\n4. **Dijkstra shortest path** — CDN routing, network paths\n\nAt scale, heaps move to specialized systems: Redis sorted sets (ZSET) implement leaderboard with O(log N) score updates.\n\n**Architect note:** Don't build a custom heap for top-K at 1M QPS — use Redis ZSET or managed service.",
      "Shows you map abstract DS to Redis, queues, and schedulers.",
      "Heap vs sorted array for top-10? — Sorted array if static; heap if streaming updates.",
      "Priority inversion in task queues? — Low priority task blocks high — use separate queues.",
      "Implementing heap when Redis ZSET exists",
      "O(n log n) sort on every request for leaderboard",
      "Not capping heap size for top-K"),
    q("Graphs for Architecture", "Graphs", "Common",
      "When do graphs appear in solution architecture (not just coding interviews)?",
      "Graphs model relationships: social networks, service dependencies, IAM permissions, network topology. Traversal (BFS/DFS) for impact analysis, shortest path for routing, topological sort for build pipelines.",
      "**Service dependency graph:** Nodes = services, edges = calls. DFS/BFS for blast radius analysis during incidents — 'if payment is down, what breaks?'\n\n**Social graph:** Followers/following — BFS for friend-of-friend; storage in adjacency list or graph DB (Neo4j) at extreme scale.\n\n**CI/CD DAG:** Topological sort for build order.\n\n**Network topology:** Shortest path routing.\n\nArchitects draw boxes-and-arrows — that *is* a graph. Formal graph thinking helps failure analysis and cycle detection (circular dependencies between microservices).",
      "Elevates whiteboard diagrams to analyzable dependency graphs.",
      "How detect circular microservice dependencies? — DFS cycle detection in dependency graph.",
      "Graph DB vs relational for social? — Relational fine to millions; graph DB when traversal is core query.",
      "Drawing architecture without analyzing dependency cycles",
      "BFS/DFS trivia without system mapping",
      "Ignoring graph storage cost at billion-edge scale"),
    q("Stack and Queue in Distributed Systems", "Stacks & Queues", "Common",
      "Explain how queue and stack semantics appear in messaging and workflow design.",
      "Queues: FIFO async processing (SQS, Service Bus). Stacks: undo, call stacks, DFS, LIFO buffers. Architects choose queue semantics for decoupling; stack for nested workflow scopes.",
      "**Queue (FIFO):** Order processing pipeline, email sending, event consumers. Guarantees (at-least-once, exactly-once) matter more than DS trivia.\n\n**Stack (LIFO):** Transaction scopes, saga compensation (reverse order), browser back button, parser state.\n\n**Deque:** Double-ended for sliding window rate limiting.\n\nIn Azure: Service Bus Queue = distributed queue. Kafka = log (append-only, different semantics).",
      "Links fundamental DS to messaging products architects actually specify.",
      "Kafka vs queue? — Kafka retains log for replay; traditional queue deletes on ack.",
      "Dead letter queue purpose? — Poison messages after max retries — don't block queue.",
      "Using sync HTTP for work that should be queued",
      "Unbounded in-memory queue without backpressure",
      "Ignoring message ordering requirements"),
    q("Bloom Filter", "Probabilistic Structures", "Occasional",
      "What is a bloom filter and where would you use it in architecture?",
      "Bloom filter: space-efficient probabilistic set membership — 'definitely not in set' or 'probably in set.' No false negatives. Use to avoid expensive DB lookups (cache poisoning prevention, CDN, distributed DB).",
      "A bloom filter uses k hash functions into a bit array. **False positives possible; false negatives impossible.**\n\n**Use cases:**\n- **Web crawler** — skip already-visited URLs\n- **Database (Cassandra, HBase)** — avoid disk seeks for non-existent keys\n- **CDN** — block known malicious paths cheaply\n\n**Cannot delete** (standard bloom) — use counting bloom filter if needed.\n\nArchitect: place bloom filter in front of expensive store — accept rare false positive (extra DB hit) for massive memory savings.",
      "Probabilistic DS separate senior architects from candidates who only know exact structures.",
      "Bloom vs hash set? — Bloom uses less memory; hash set exact but larger.",
      "False positive rate tuning? — More bits and hash functions reduce FP rate.",
      "Using bloom filter when exact membership required",
      "Not sizing bit array for expected element count",
      "Expecting delete from standard bloom filter"),
    q("Consistent Hashing", "Distributed Hashing", "Very Common",
      "Explain consistent hashing. Why is it essential for distributed caches?",
      "Consistent hashing maps keys and nodes to a ring — adding/removing a node only remaps K/n keys, not the entire keyspace. Essential for memcached, Dynamo, Cassandra, CDN sharding.",
      "Without consistent hashing, `hash(key) % N` remaps almost all keys when N changes — cache stampede on node add/remove.\n\n**Virtual nodes:** Each physical node has multiple positions on ring for even distribution.\n\n**Production:** Dynamo paper (Amazon), used in Cassandra, Riak, distributed caches.\n\nWhen designing sharded Redis cluster or custom shard router, consistent hashing is the default answer.",
      "Core distributed systems DS — appears in every senior system design interview.",
      "Rendezvous hashing vs consistent? — Rendezvous (highest random weight) — simpler, no ring management.",
      "Hot spot on ring? — Virtual nodes balance load; salting keys.",
      "Modulo hashing for production shard cluster",
      "Not considering replica placement on ring",
      "Ignoring hotspot keys regardless of hashing"),
    q("LRU Cache Design", "Caching", "Very Common",
      "Design an LRU cache. How does it combine data structures?",
      "Hash map + doubly linked list: map for O(1) key lookup, list for O(1) move-to-front and eviction. At scale: Redis with TTL + LRU eviction policy.",
      "**In-process:** `Dictionary<K, Node>` + doubly linked list — classic interview answer.\n\n**Distributed:** Redis `maxmemory-policy allkeys-lru` — approximate LRU at scale.\n\n**Architect decisions:**\n- Cache size bounded — always define eviction\n- TTL + LRU together — expire stale, evict when full\n- Cache-aside pattern: app loads on miss, writes invalidate\n\nFor 100K read QPS product catalog, Redis LRU cluster with consistent hashing is production pattern — not hand-rolled Java LinkedHashMap.",
      "Interview answer must scale from laptop DS to Redis cluster.",
      "LRU vs LFU? — LRU for temporal locality; LFU for frequency (hot products).",
      "Cache stampede on expiry? — Mutex, early refresh, staggered TTL.",
      "Unbounded cache without eviction policy",
      "Hand-rolled LRU in app when Redis exists",
      "Caching without invalidation strategy"),
    q("Time and Space Complexity Trade-offs", "Complexity", "Common",
      "How do you communicate complexity trade-offs to stakeholders?",
      "O(n) vs O(n log n) matters at billions of rows. Architects quantify: 'index adds 20% write cost, reads go from 30s to 50ms.' Business understands latency and cost — not Big-O notation alone.",
      "**Examples:**\n- Add index: space for time — disk + write overhead for read speed\n- Precompute aggregations: space (materialized view) for time (dashboard load)\n- Sharding: operational complexity for write scale\n\n**Interview:** State complexity, then translate: 'O(n) full table scan fails at 500M rows — 45 second query. B-tree index: O(log n) — 5ms.'\n\nStakeholder version: 'Investment in indexing saves $X in compute and improves checkout conversion.'",
      "Architects bridge algorithm analysis and business outcomes.",
      "Amortized analysis example? — Dynamic array resize — O(1) amortized append.",
      "When is O(n) acceptable? — Small n, batch offline jobs, rare admin queries.",
      "Only stating Big-O without scale numbers",
      "Optimizing algorithm before measuring real bottleneck",
      "Ignoring operational cost of complex structures"),
]

WEEK_6 = [
    q("Big O for Architects", "Complexity Analysis", "Very Common",
      "Why must architects understand Big O beyond coding interviews?",
      "Big O describes growth rate — architects use it to predict when designs break at 10x scale. O(n) scan on 1M rows is fine; on 1B rows it's an outage.",
      "**Architect applications:**\n- **Database:** missing index = O(n) scan → timeout at scale\n- **API:** nested loops over cart × products = O(n×m) — breaks on large carts\n- **Messaging:** O(n) fan-out to all users — need O(1) per user via push infra\n\nCommunicate with numbers: 'Current O(n) search at 10M records = 12s. Inverted index: O(log n) or O(1) — 20ms.'",
      "Transforms complexity from academic to capacity planning.",
      "Big O vs real latency? — Constants matter — hash O(1) with disk still slow.",
      "Worst vs average case? — Attackers target worst case — architects plan for it.",
      "Quoting O(1) for everything",
      "Ignoring hidden O(n) in ORM lazy loading",
      "No measurement before algorithm change"),
    q("Sorting at Scale", "Sorting", "Common",
      "When does sorting algorithm choice matter in production systems?",
      "In-memory sort algorithm (quicksort, mergesort) matters for batch jobs. At scale, external merge sort on disk, distributed sort (MapReduce), or pre-sorted indexes (B-tree) replace in-memory sorts.",
      "**Small data:** `Array.Sort` — Timsort O(n log n) — fine.\n\n**Large batch:** External sort — chunks fit in memory, merge passes on disk.\n\n**Distributed:** MapReduce sort, Spark `orderBy` — shuffle is expensive — architects minimize sorts.\n\n**Database:** `ORDER BY` uses index if available — O(n) scan + sort if not.\n\n**Architect rule:** Push sort to index where possible; avoid sorting millions of rows per request.",
      "Sorting cost appears in analytics pipelines and SQL — not just coding puzzles.",
      "Stable sort when needed? — Merge sort stable; quicksort often not — matters for multi-key sort.",
      "Top-K without full sort? — Heap O(n log k) better than O(n log n) full sort.",
      "ORDER BY on unindexed column at billions of rows",
      "Sorting in application when DB index could serve order",
      "Ignoring shuffle cost in distributed sorts"),
    q("Binary Search Beyond Arrays", "Search", "Common",
      "Where does binary search apply in system architecture?",
      "Binary search is O(log n) divide-and-conquer on sorted data. Applies to: B-tree index lookups, finding slot in ring buffer, versioned config rollout, git bisect for incident debugging.",
      "Any monotonic predicate supports binary search: 'find smallest deployment where latency exceeds 200ms.'\n\n**Database:** B-tree is multi-way binary search on disk blocks.\n\n**Load balancing:** Weighted selection sometimes uses binary search on prefix sums.\n\n**Time-series:** Binary search timestamp in sorted log for incident start.",
      "Generalizes binary search from array index to operational debugging.",
      "Binary search on rotated array? — Coding detail; architect cares about sorted index equivalence.",
      "Interpolation search? — When values uniformly distributed — O(log log n).",
      "Linear scan on sorted billion-row table",
      "Not using index for range queries",
      "Binary search without monotonic invariant"),
    q("Graph Traversal for Dependencies", "Graph Algorithms", "Common",
      "How do BFS and DFS apply to microservice dependency analysis?",
      "BFS: level-order — find all services N hops away (blast radius). DFS: deep path — detect circular dependencies, topological build order.",
      "**Incident response:** Payment down → BFS from payment node → list affected services for communication.\n\n**Deployment:** Topological sort (DFS-based) of service build DAG.\n\n**Cycle detection:** DFS with visited set — circular sync calls are architectural bugs.",
      "Graph algorithms operationalized for platform engineering.",
      "BFS vs DFS for shortest path? — BFS on unweighted graph; Dijkstra weighted.",
      "Transitive dependency risk? — A→B→C means A indirectly depends on C.",
      "No dependency graph for 20+ microservices",
      "Circular sync call chains undetected",
      "Manual incident impact analysis without traversal"),
    q("Dynamic Programming in Architecture", "DP", "Occasional",
      "Is dynamic programming relevant to architects?",
      "DP mindset — optimal substructure, memoization — applies to capacity planning, cost optimization, and caching computed results. Not about coding Fibonacci — about not recomputing expensive work.",
      "**Architectural DP:**\n- **Memoization:** Cache expensive aggregation results (dashboard metrics)\n- **Optimal substructure:** Shortest path routing — subpaths are optimal\n- **Batch precomputation:** Nightly jobs vs real-time — trade storage for CPU\n\nExample: shipping cost table precomputed for all zone pairs — O(1) lookup at checkout vs O(n) calculation per order.",
      "DP as 'avoid redundant computation' resonates with architects.",
      "DP vs greedy? — Greedy fails when local optimal ≠ global — need DP or proof.",
      "When precompute vs realtime? — Precompute when staleness OK and read >> write.",
      "Recomputing aggregates on every dashboard load",
      "Greedy algorithm for resource allocation without proof",
      "DP trivia without architectural mapping"),
    q("Amortized Analysis", "Complexity", "Occasional",
      "Explain amortized complexity with a production example.",
      "Amortized O(1): occasional expensive operation spread over many cheap ones. Dynamic array resize, append-only log compaction, garbage collection.",
      "**Examples:**\n- **ArrayList.Add:** Usually O(1), rare O(n) copy — amortized O(1)\n- **Kafka log compaction:** Periodic expensive merge — amortized write cost\n- **.NET GC:** Gen0 collections frequent and cheap; Gen2 rare and expensive — design for low Gen2 frequency\n\nArchitects care because p99 spikes often come from amortized 'rare' events — log compaction, full GC, resharding.",
      "Explains latency spikes that averages hide.",
      "Amortized vs average? — Amortized worst-case bound over sequence; average is probabilistic.",
      "Linked to p99? — Rare O(n) events cause tail latency spikes.",
      "Designing only for average latency",
      "Ignoring compaction/resharding spikes",
      "Not capacity-planning for worst-case batch jobs"),
    q("NP-Hard Problems in Architecture", "NP-Hard", "Rare",
      "How do architects handle NP-hard optimization problems (routing, scheduling)?",
      "Use heuristics, approximation algorithms, or solvers with time limits. Exact optimal routing for 10,000 delivery vehicles is NP-hard — use greedy + local search or specialized OR-Tools.",
      "**Real problems:** VRP (vehicle routing), bin packing (container placement), optimal shard balancing.\n\n**Architect approach:**\n1. Can you simplify constraints?\n2. Greedy good enough? (often 90% optimal)\n3. Offline optimization + online execution\n4. Human-in-the-loop for edge cases\n\nDon't block product launch waiting for perfect optimal — ship heuristic, measure gap.",
      "Shows pragmatic computer science for operations research problems.",
      "P vs NP interview trap? — Acknowledge; pivot to practical heuristics.",
      "OR-Tools / constraint solvers? — Use when problem well-defined and offline.",
      "Claiming exact optimal at massive scale",
      "No fallback when solver times out",
      "Over-engineering optimization for 100-item problem"),
    q("Recursion and Stack Overflow", "Recursion", "Common",
      "When does recursion become an architectural risk in .NET services?",
      "Deep recursion risks stack overflow. Architects prefer iterative processing, trampolining, or workflow engines for deeply nested business logic (approval chains, org hierarchies).",
      "**Risks:** 10,000-level org hierarchy recursive query — stack overflow. **Mitigations:** iterative BFS, materialized path pattern (`/1/5/23/`), closure table, or workflow engine (Durable Functions) for arbitrary depth.\n\n**JSON deserialization** deeply nested objects — configure max depth limits.",
      "Production recursion limits matter in hierarchical enterprise data.",
      "Tail recursion in .NET? — JIT may not optimize — don't rely on it.",
      "Materialized path pattern? — Store `/root/parent/id` for hierarchy queries.",
      "Unbounded recursive approval workflow",
      "Recursive SQL CTE without depth limit",
      "Stack overflow in production hierarchy API"),
    q("Sliding Window Algorithms", "Patterns", "Common",
      "How do sliding window patterns apply to streaming and monitoring?",
      "Sliding window: process contiguous subarray/substream in O(n). Used for rate limiting (requests per minute), moving averages in metrics, anomaly detection.",
      "**Rate limiter:** Count requests in last 60 seconds — sliding window log or approximate counter.\n\n**Metrics:** Rolling p99 latency over 5-minute window — streaming algorithms.\n\n**Stream processing:** Flink/Kafka windowed aggregations — tumbling vs sliding vs session windows.\n\nArchitect specifies window semantics in NFRs: 'alert when error rate > 5% over 5-minute sliding window.'",
      "Window semantics are architecture decisions in streaming pipelines.",
      "Tumbling vs sliding window? — Tumbling non-overlapping; sliding overlapping — different alert sensitivity.",
      "Count-min sketch? — Approximate frequency in streaming — memory efficient.",
      "Unbounded event buffer without window",
      "Wrong window size for seasonality",
      "Alert on single spike without smoothing"),
    q("Algorithm Choice Decision Framework", "Framework", "Common",
      "Walk through how you select algorithms and data structures for a new feature.",
      "Start from access pattern: read/write ratio, range vs point lookup, ordering needs, memory budget, consistency. Map pattern to DS, then to managed service (Redis, SQL index, Elasticsearch).",
      "**Framework:**\n1. **Access pattern** — equality, range, prefix, graph traversal?\n2. **Scale** — n = ? QPS = ?\n3. **Consistency** — strong or eventual?\n4. **Managed service** — build vs Redis/SQL/Cosmos\n5. **Measure** — prototype, load test, revise\n\nDocument in ADR with rejected alternatives.",
      "Structured selection beats 'we always use X.'",
      "Build vs buy for search? — Elasticsearch/Azure AI Search when full-text needed.",
      "When custom DS justified? — Extreme scale or unique constraints only.",
      "Algorithm before requirements",
      "Not documenting rejected alternatives in ADR",
      "Building custom cache when Redis suffices"),
]

# Weeks 7-8, 21-24, 33-36 continue in premium_qa_data_b.py
