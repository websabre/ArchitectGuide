# Week 05 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Hash Table for O(1) Lookup

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hash Tables |
| **Frequency** | Very Common |

### Question

Why are hash tables fundamental to system design? Give three production use cases.

### Short Answer (30 seconds)

Hash tables provide average O(1) insert, lookup, and delete via a hash function mapping keys to buckets. Used for caches, indexes, deduplication, and rate limiters.

### Detailed Answer (3–5 minutes)

A hash table hashes a key to a bucket index. Collisions are resolved via chaining (linked lists per bucket) or open addressing. **Average** O(1); worst case O(n) if all keys collide — architects care about worst case under attack.

**Production use cases:**
1. **Redis** — entire in-memory store is hash-based structures
2. **Distributed caches** — consistent hashing places keys on nodes (Dynamo, Cassandra ring)
3. **Rate limiting** — token bucket keyed by userId in memory

For a URL shortener, the mapping `shortCode → longUrl` is a hash map (or DB index behaving as one). At 100K reads/sec, in-memory hash + SSD backing is the standard pattern.

**Trade-off:** Hash tables don't maintain order — use balanced BST or B-tree when you need range queries (timestamps, prices).

### Architecture Perspective

Interviewers test whether you connect data structures to system components — not just Big-O memorization.

### Follow-up Questions

1. **What happens when the hash function is poor? — Clustering, O(n) lookups; use cryptographic or well-distributed hashes.**
2. **Hash table vs B-tree for database index? — B-tree for range scans and disk locality; hash index only for equality.**

### Common Mistakes in Interviews

- Quoting O(1) without mentioning collisions
- Using hash table when range queries dominate
- Ignoring memory bounds for in-memory maps

---

## Q002: Array vs Linked List at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Arrays & Lists |
| **Frequency** | Common |

### Question

When would you choose an array-based vs linked-list-based design in a distributed system?

### Short Answer (30 seconds)

Arrays excel at cache locality and index access; linked lists at cheap inserts/deletes in the middle. At scale, arrays (or array-backed buffers) dominate for sequential and indexed access.

### Detailed Answer (3–5 minutes)

**Array:** contiguous memory, O(1) index access, better CPU cache behavior. Used in: columnar storage, ring buffers, batch processing.

**Linked list:** O(1) insert/delete at known node, but poor cache locality and no random access. Rarely used raw at scale — skip lists and B+ trees replace them in databases.

**Architect example:** Kafka log segments are append-only files (array-like sequential storage) — not linked lists. Event sourcing append streams mirror this pattern.

Choose linked structures conceptually when you need cheap middle insertion in memory (LRU cache combines hash map + doubly linked list).

### Architecture Perspective

Connect classic DS to how Kafka, DB pages, and buffers actually work.

### Follow-up Questions

1. **Is ArrayList always better than LinkedList in .NET? — For almost all cases yes — cache locality wins.**
2. **How does columnar storage relate? — Arrays of column values — analytical query performance.**

### Common Mistakes in Interviews

- Recommending linked list for database storage
- Not mentioning cache locality
- Ignoring sequential access patterns in logs and streams

---

## Q003: Trees in System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Trees |
| **Frequency** | Very Common |

### Question

What tree structures appear in production systems and when does each apply?

### Short Answer (30 seconds)

B-trees/B+ trees for disk-backed indexes (SQL databases). Tries for prefix search (autocomplete). Red-black/AVL rarely used directly — DB engines handle this.

### Detailed Answer (3–5 minutes)

**B+ tree:** Database indexes (SQL Server, PostgreSQL). Optimized for disk blocks — high fanout, leaf nodes linked for range scans.

**Trie (prefix tree):** Autocomplete, IP routing tables, spell check. O(key length) lookup.

**Binary search tree:** Teaching concept; production uses balanced variants inside DB engines.

**Decision tree:** Not a storage structure — ML models; different context.

For system design interview: when they say 'index the data,' they mean B-tree unless it's a key-value equality store (hash) or full-text (inverted index).

### Architecture Perspective

Architects name the right tree for the access pattern — equality vs range vs prefix.

### Follow-up Questions

1. **Why B+ tree not B-tree for databases? — Leaves linked for sequential scan; internal nodes only keys.**
2. **Trie vs hash for autocomplete? — Trie supports prefix queries; hash only exact match.**

### Common Mistakes in Interviews

- Saying 'use a tree' without specifying access pattern
- Confusing DOM tree with storage index
- Not knowing B+ tree is the default SQL index

---

## Q004: Heap and Priority Queue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Heaps |
| **Frequency** | Common |

### Question

How would you use a priority queue in a system design?

### Short Answer (30 seconds)

Priority queue (min/max heap) gives O(log n) insert and O(1) peek — used for scheduling, top-K, merge streams, Dijkstra. Production: task schedulers, rate limit windows, leaderboard top-N.

### Detailed Answer (3–5 minutes)

**Use cases:**
1. **Task scheduling** — execute highest priority jobs first (hospital triage queue)
2. **Top-K** — maintain K most popular products with min-heap of size K
3. **Merge k sorted logs** — heap of head elements from each stream
4. **Dijkstra shortest path** — CDN routing, network paths

At scale, heaps move to specialized systems: Redis sorted sets (ZSET) implement leaderboard with O(log N) score updates.

**Architect note:** Don't build a custom heap for top-K at 1M QPS — use Redis ZSET or managed service.

### Architecture Perspective

Shows you map abstract DS to Redis, queues, and schedulers.

### Follow-up Questions

1. **Heap vs sorted array for top-10? — Sorted array if static; heap if streaming updates.**
2. **Priority inversion in task queues? — Low priority task blocks high — use separate queues.**

### Common Mistakes in Interviews

- Implementing heap when Redis ZSET exists
- O(n log n) sort on every request for leaderboard
- Not capping heap size for top-K

---

## Q005: Graphs for Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

When do graphs appear in solution architecture (not just coding interviews)?

### Short Answer (30 seconds)

Graphs model relationships: social networks, service dependencies, IAM permissions, network topology. Traversal (BFS/DFS) for impact analysis, shortest path for routing, topological sort for build pipelines.

### Detailed Answer (3–5 minutes)

**Service dependency graph:** Nodes = services, edges = calls. DFS/BFS for blast radius analysis during incidents — 'if payment is down, what breaks?'

**Social graph:** Followers/following — BFS for friend-of-friend; storage in adjacency list or graph DB (Neo4j) at extreme scale.

**CI/CD DAG:** Topological sort for build order.

**Network topology:** Shortest path routing.

Architects draw boxes-and-arrows — that *is* a graph. Formal graph thinking helps failure analysis and cycle detection (circular dependencies between microservices).

### Architecture Perspective

Elevates whiteboard diagrams to analyzable dependency graphs.

### Follow-up Questions

1. **How detect circular microservice dependencies? — DFS cycle detection in dependency graph.**
2. **Graph DB vs relational for social? — Relational fine to millions; graph DB when traversal is core query.**

### Common Mistakes in Interviews

- Drawing architecture without analyzing dependency cycles
- BFS/DFS trivia without system mapping
- Ignoring graph storage cost at billion-edge scale

---

## Q006: Stack and Queue in Distributed Systems

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Stacks & Queues |
| **Frequency** | Common |

### Question

Explain how queue and stack semantics appear in messaging and workflow design.

### Short Answer (30 seconds)

Queues: FIFO async processing (SQS, Service Bus). Stacks: undo, call stacks, DFS, LIFO buffers. Architects choose queue semantics for decoupling; stack for nested workflow scopes.

### Detailed Answer (3–5 minutes)

**Queue (FIFO):** Order processing pipeline, email sending, event consumers. Guarantees (at-least-once, exactly-once) matter more than DS trivia.

**Stack (LIFO):** Transaction scopes, saga compensation (reverse order), browser back button, parser state.

**Deque:** Double-ended for sliding window rate limiting.

In Azure: Service Bus Queue = distributed queue. Kafka = log (append-only, different semantics).

### Architecture Perspective

Links fundamental DS to messaging products architects actually specify.

### Follow-up Questions

1. **Kafka vs queue? — Kafka retains log for replay; traditional queue deletes on ack.**
2. **Dead letter queue purpose? — Poison messages after max retries — don't block queue.**

### Common Mistakes in Interviews

- Using sync HTTP for work that should be queued
- Unbounded in-memory queue without backpressure
- Ignoring message ordering requirements

---

## Q007: Bloom Filter

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Probabilistic Structures |
| **Frequency** | Occasional |

### Question

What is a bloom filter and where would you use it in architecture?

### Short Answer (30 seconds)

Bloom filter: space-efficient probabilistic set membership — 'definitely not in set' or 'probably in set.' No false negatives. Use to avoid expensive DB lookups (cache poisoning prevention, CDN, distributed DB).

### Detailed Answer (3–5 minutes)

A bloom filter uses k hash functions into a bit array. **False positives possible; false negatives impossible.**

**Use cases:**
- **Web crawler** — skip already-visited URLs
- **Database (Cassandra, HBase)** — avoid disk seeks for non-existent keys
- **CDN** — block known malicious paths cheaply

**Cannot delete** (standard bloom) — use counting bloom filter if needed.

Architect: place bloom filter in front of expensive store — accept rare false positive (extra DB hit) for massive memory savings.

### Architecture Perspective

Probabilistic DS separate senior architects from candidates who only know exact structures.

### Follow-up Questions

1. **Bloom vs hash set? — Bloom uses less memory; hash set exact but larger.**
2. **False positive rate tuning? — More bits and hash functions reduce FP rate.**

### Common Mistakes in Interviews

- Using bloom filter when exact membership required
- Not sizing bit array for expected element count
- Expecting delete from standard bloom filter

---

## Q008: Consistent Hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Distributed Hashing |
| **Frequency** | Very Common |

### Question

Explain consistent hashing. Why is it essential for distributed caches?

### Short Answer (30 seconds)

Consistent hashing maps keys and nodes to a ring — adding/removing a node only remaps K/n keys, not the entire keyspace. Essential for memcached, Dynamo, Cassandra, CDN sharding.

### Detailed Answer (3–5 minutes)

Without consistent hashing, `hash(key) % N` remaps almost all keys when N changes — cache stampede on node add/remove.

**Virtual nodes:** Each physical node has multiple positions on ring for even distribution.

**Production:** Dynamo paper (Amazon), used in Cassandra, Riak, distributed caches.

When designing sharded Redis cluster or custom shard router, consistent hashing is the default answer.

### Architecture Perspective

Core distributed systems DS — appears in every senior system design interview.

### Follow-up Questions

1. **Rendezvous hashing vs consistent? — Rendezvous (highest random weight) — simpler, no ring management.**
2. **Hot spot on ring? — Virtual nodes balance load; salting keys.**

### Common Mistakes in Interviews

- Modulo hashing for production shard cluster
- Not considering replica placement on ring
- Ignoring hotspot keys regardless of hashing

---

## Q009: LRU Cache Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

Design an LRU cache. How does it combine data structures?

### Short Answer (30 seconds)

Hash map + doubly linked list: map for O(1) key lookup, list for O(1) move-to-front and eviction. At scale: Redis with TTL + LRU eviction policy.

### Detailed Answer (3–5 minutes)

**In-process:** `Dictionary<K, Node>` + doubly linked list — classic interview answer.

**Distributed:** Redis `maxmemory-policy allkeys-lru` — approximate LRU at scale.

**Architect decisions:**
- Cache size bounded — always define eviction
- TTL + LRU together — expire stale, evict when full
- Cache-aside pattern: app loads on miss, writes invalidate

For 100K read QPS product catalog, Redis LRU cluster with consistent hashing is production pattern — not hand-rolled Java LinkedHashMap.

### Architecture Perspective

Interview answer must scale from laptop DS to Redis cluster.

### Follow-up Questions

1. **LRU vs LFU? — LRU for temporal locality; LFU for frequency (hot products).**
2. **Cache stampede on expiry? — Mutex, early refresh, staggered TTL.**

### Common Mistakes in Interviews

- Unbounded cache without eviction policy
- Hand-rolled LRU in app when Redis exists
- Caching without invalidation strategy

---

## Q010: Time and Space Complexity Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Complexity |
| **Frequency** | Common |

### Question

How do you communicate complexity trade-offs to stakeholders?

### Short Answer (30 seconds)

O(n) vs O(n log n) matters at billions of rows. Architects quantify: 'index adds 20% write cost, reads go from 30s to 50ms.' Business understands latency and cost — not Big-O notation alone.

### Detailed Answer (3–5 minutes)

**Examples:**
- Add index: space for time — disk + write overhead for read speed
- Precompute aggregations: space (materialized view) for time (dashboard load)
- Sharding: operational complexity for write scale

**Interview:** State complexity, then translate: 'O(n) full table scan fails at 500M rows — 45 second query. B-tree index: O(log n) — 5ms.'

Stakeholder version: 'Investment in indexing saves $X in compute and improves checkout conversion.'

### Architecture Perspective

Architects bridge algorithm analysis and business outcomes.

### Follow-up Questions

1. **Amortized analysis example? — Dynamic array resize — O(1) amortized append.**
2. **When is O(n) acceptable? — Small n, batch offline jobs, rare admin queries.**

### Common Mistakes in Interviews

- Only stating Big-O without scale numbers
- Optimizing algorithm before measuring real bottleneck
- Ignoring operational cost of complex structures

---

## Q011: Trie for Prefix Search

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Tries |
| **Frequency** | Common |

### Question

When would you choose a trie over a hash table for search in system design?

### Short Answer (30 seconds)

Trie (prefix tree) supports O(key length) prefix lookup — autocomplete, IP routing, spell check. Hash tables only do exact key match in O(1) average.

### Detailed Answer (3–5 minutes)

**Trie structure:** Each node represents a character; paths from root spell keys. Shared prefixes compress storage.

**Production use cases:**
1. **Autocomplete** — type 'arch' → suggest 'architecture', 'archive'
2. **IP routing (CIDR)** — longest prefix match in routers
3. **Search suggestions** — Elasticsearch completion suggester uses FST (finite state transducer), trie variant

**Trade-offs:** Memory-heavy for sparse alphabets; use compressed trie (radix tree) or FST for disk efficiency.

For a typeahead API at 50K QPS, trie in Redis or dedicated suggest service beats scanning hash keys.

### Architecture Perspective

Architects match prefix vs exact-match access patterns to the right structure.

### Follow-up Questions

1. **Trie vs Elasticsearch for autocomplete? — ES FST at scale; in-memory trie for small catalogs.**
2. **Radix tree vs standard trie? — Radix compresses single-child chains — less memory.**

### Common Mistakes in Interviews

- Using hash map and scanning all keys for prefix
- Not compressing trie for large sparse keyspaces
- Ignoring case-folding and Unicode normalization in prefix keys

---

## Q012: Skip List

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Probabilistic Structures |
| **Frequency** | Occasional |

### Question

What is a skip list and where does it appear in production systems?

### Short Answer (30 seconds)

Skip list: probabilistic layered linked list giving O(log n) search/insert — simpler than balanced trees. Used in Redis sorted sets (ZSET) internals and LevelDB/RocksDB memtables.

### Detailed Answer (3–5 minutes)

**How it works:** Base level is sorted linked list; upper levels 'skip' forward with probability p (often 0.5). Search starts at top, drops down — like express lanes.

**Why production cares:**
- **Redis ZSET** — scores + member ordering via skip list + hash map combo
- **LevelDB** — memtable before flush to SSTable

**vs Red-black tree:** Skip list easier to implement concurrently (lock-free variants); similar O(log n) bounds probabilistically.

Architect: when you need ordered in-memory structure with concurrent inserts, skip list (or managed ZSET) beats hand-rolled BST.

### Architecture Perspective

Skip lists bridge interview DS trivia and Redis internals.

### Follow-up Questions

1. **Skip list vs B+ tree on disk? — B+ tree wins for disk; skip list for in-memory ordered sets.**
2. **Concurrent skip list? — Redis uses dual structure; research papers on lock-free skip lists.**

### Common Mistakes in Interviews

- Implementing BST when Redis ZSET exists
- Assuming skip list is deterministic O(log n) worst case
- Not knowing Redis ZSET is skip list + hash

---

## Q013: Inverted Index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Search |
| **Frequency** | Very Common |

### Question

Explain inverted indexes. Why are they fundamental to search systems?

### Short Answer (30 seconds)

Inverted index maps term → list of document IDs (postings list). Enables O(1) term lookup instead of O(n) full-text scan. Core of Elasticsearch, Lucene, SQL full-text indexes.

### Detailed Answer (3–5 minutes)

**Structure:**
- **Dictionary:** term → pointer to postings
- **Postings list:** sorted doc IDs + positions/frequencies for ranking

**Query:** AND/OR postings lists (merge sorted lists) — 'architecture AND azure' intersects two lists.

**Production:** Elasticsearch shard = Lucene index = inverted index segments. Azure AI Search same pattern.

**Architect decision:** Inverted index for full-text; B-tree for structured filters; combine in hybrid query planner.

At 100M documents, scanning text is impossible — inverted index is non-negotiable for search.

### Architecture Perspective

Search architecture starts with inverted index — not SQL LIKE.

### Follow-up Questions

1. **Inverted vs forward index? — Forward: doc → terms (for highlighting); inverted: term → docs (for search).**
2. **BM25 ranking? — Scoring function using term frequency and doc frequency from postings.**

### Common Mistakes in Interviews

- SQL LIKE '%term%' on billion-row table
- No stemming/normalization in index pipeline
- Ignoring index rebuild cost on schema change

---

## Q014: Count-Min Sketch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Probabilistic Structures |
| **Frequency** | Occasional |

### Question

What is a count-min sketch and when would an architect use it?

### Short Answer (30 seconds)

Count-min sketch: probabilistic frequency estimator — O(1) update, fixed memory. Overestimates counts (never underestimates). Used for heavy hitter detection, CDN traffic, streaming analytics.

### Detailed Answer (3–5 minutes)

**How it works:** d hash functions × w buckets matrix. Increment all d buckets on add; query returns min across d buckets.

**Use cases:**
- **Heavy hitters** — find top talkers in network traffic without storing every flow
- **Streaming dashboards** — approximate request counts per endpoint
- **DDoS detection** — flag IPs exceeding threshold in sliding window

**Trade-off:** Approximate counts with tunable error ε. Exact counts need hash map — memory explodes at billions of keys.

Architect: pair count-min sketch with exact store for candidates that sketch flags as heavy hitters.

### Architecture Perspective

Streaming systems need approximate DS — count-min sketch is the architect's tool.

### Follow-up Questions

1. **Count-min vs HyperLogLog? — Count-min estimates frequency; HyperLogLog estimates distinct count.**
2. **Error bound tuning? — Width w and depth d trade memory vs accuracy.**

### Common Mistakes in Interviews

- Storing every event in memory for frequency
- Treating sketch count as exact for billing
- No second-stage exact verification for flagged keys

---

## Q015: Union-Find Disjoint Set

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

How does union-find apply to system design beyond coding interviews?

### Short Answer (30 seconds)

Union-find (disjoint set) tracks connected components with near O(1) union/find via path compression + rank. Used for network connectivity, Kruskal MST, dynamic cluster merging, permission group equivalence.

### Detailed Answer (3–5 minutes)

**Production mappings:**
1. **Network connectivity** — are two nodes in same partition after link failures?
2. **Kubernetes** — union-find variants in cluster federation grouping
3. **Social 'mutual group'** — transitive closure queries with periodic rebuild
4. **Image processing pipelines** — connected component labeling

**Architect note:** For static graphs, precompute components offline. Union-find shines when edges arrive dynamically (streaming merges).

With path compression, amortized α(n) — effectively constant for practical n.

### Architecture Perspective

Union-find models 'are these things in the same group?' at scale.

### Follow-up Questions

1. **Union-find vs graph DB traversal? — Union-find for dynamic connectivity; BFS for path queries.**
2. **When rebuild vs incremental? — If queries are batch, rebuild nightly; streaming needs union-find.**

### Common Mistakes in Interviews

- BFS on every connectivity check at high QPS
- Not applying path compression in hand-rolled implementation
- Using union-find when you need shortest path

---

## Q016: Sliding Window Deque

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deque |
| **Frequency** | Common |

### Question

How does a deque enable O(n) sliding window maximum algorithms and rate limiting?

### Short Answer (30 seconds)

Deque (double-ended queue) maintains monotonic candidate indices — O(1) push/pop each end. Enables sliding window max/min in O(n) and implements sliding window rate limiters.

### Detailed Answer (3–5 minutes)

**Sliding window maximum:** Deque stores indices of decreasing values — front always current max. Each element enters and exits once — O(n) total.

**Rate limiting:** Sliding window log stores timestamps in deque — drop expired from front, reject if count exceeds limit.

**Production:** NGINX rate limiting, API gateways (Kong, APIM), custom middleware using deque or Redis sorted set for distributed windows.

**Architect:** Specify window type in NFR — fixed vs sliding vs token bucket. Deque backs precise sliding window; approximate counters save memory at scale.

### Architecture Perspective

Deque connects algorithm pattern to gateway rate-limit design.

### Follow-up Questions

1. **Deque vs circular buffer for window? — Deque for variable-size eviction; ring buffer for fixed slots.**
2. **Distributed sliding window? — Redis ZSET with timestamp scores; trim expired range.**

### Common Mistakes in Interviews

- Re-sorting entire window on every request O(n log n)
- Fixed window when sliding required — boundary burst abuse
- Unbounded deque growth without expiry

---

## Q017: B+ Tree Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Trees |
| **Frequency** | Very Common |

### Question

Explain B+ tree internals. Why is it the default database index?

### Short Answer (30 seconds)

B+ tree: high fanout balanced tree; keys only in internal nodes, all data in linked leaf nodes. Optimized for disk block reads — minimizes I/O per lookup.

### Detailed Answer (3–5 minutes)

**Key properties:**
- **Fanout 100–500** — one disk read covers hundreds of keys
- **Leaf linked list** — efficient range scans (`WHERE price BETWEEN 10 AND 50`)
- **Height log_{fanout}(n)** — billion rows ≈ 3–4 levels

**vs B-tree:** B+ tree doesn't store values in internal nodes — more keys per page, shallower tree.

**Production:** PostgreSQL, SQL Server, MySQL InnoDB clustered index IS a B+ tree. Page size (8KB default) drives fanout.

**Architect:** Every `WHERE` on unindexed column = leaf-to-leaf scan. Index design = choosing B+ tree columns and order.

### Architecture Perspective

B+ tree is the bridge between SQL performance and disk physics.

### Follow-up Questions

1. **Clustered vs non-clustered index? — Clustered = table sorted by B+ tree key (one per table).**
2. **Index column order? — Leftmost prefix rule — (a,b) index helps `WHERE a=?` not `WHERE b=?` alone.**

### Common Mistakes in Interviews

- Assuming hash index for range queries
- Too many indexes — write amplification on every insert
- Ignoring fill factor and page splits under heavy insert

---

## Q018: Ring Buffer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Arrays |
| **Frequency** | Common |

### Question

When do architects use ring buffers (circular buffers) in production?

### Short Answer (30 seconds)

Ring buffer: fixed-size array with head/tail pointers — O(1) enqueue/dequeue, cache-friendly, no allocation. Used in logging, IPC, streaming, kernel drivers, LMAX Disruptor.

### Detailed Answer (3–5 minutes)

**Properties:**
- **Bounded memory** — backpressure when full (block or drop)
- **Sequential access** — CPU cache friendly
- **Lock-free variants** — single producer/single consumer without mutex

**Production:**
- **LMAX Disruptor** — financial exchange inter-thread messaging
- **Kernel pipe buffers, NIC ring descriptors**
- **Embedded telemetry** — bounded log before flush to disk

**Architect:** Choose ring buffer when throughput > latency variance tolerance and memory must be bounded. Use queue (Kafka) when you need durability and replay.

### Architecture Perspective

Ring buffer is the high-performance bounded queue pattern.

### Follow-up Questions

1. **Ring buffer vs Kafka? — Ring buffer in-process; Kafka cross-process durable log.**
2. **Power-of-two size? — Enables bitmask instead of modulo for index wrap.**

### Common Mistakes in Interviews

- Unbounded in-memory queue in latency-critical path
- Multi-producer without lock-free design — contention
- No strategy when buffer full — silent drop vs block

---

## Q019: Hash Collision Strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hash Tables |
| **Frequency** | Common |

### Question

What hash collision strategies exist and when does each matter at scale?

### Short Answer (30 seconds)

Collisions inevitable (pigeonhole). Strategies: chaining (linked list per bucket), open addressing (probe sequence), cuckoo hashing (relocate), robin hood (reduce variance). Choice affects cache behavior and worst-case under attack.

### Detailed Answer (3–5 minutes)

**Chaining:** Simple, handles high load factor; pointer chasing hurts cache.

**Open addressing:** Linear probing (cache friendly, clustering), quadratic, double hashing. Better memory locality; clustering risk.

**Cuckoo hashing:** O(1) worst-case lookup with two tables — used in some network switches and high-performance maps.

**Attack surface:** Adversarial keys hashing to same bucket → O(n) — use SipHash or randomized seed per process.

**Architect:** .NET Dictionary uses chaining; Python 3.7+ dict is open addressing. Know your runtime; for custom sharding, test distribution with production key samples.

### Architecture Perspective

Collision handling affects tail latency and security — not just Big-O average.

### Follow-up Questions

1. **Load factor tuning? — 0.75 typical; resize when exceeded — amortized cost.**
2. **Consistent hashing collision? — Virtual nodes reduce imbalance; separate from bucket collision.**

### Common Mistakes in Interviews

- Ignoring adversarial hash attack on public API
- Assuming uniform distribution without measuring key skew
- Quoting O(1) without mentioning resize/rehash cost

---

## Q020: Open Addressing vs Chaining

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hash Tables |
| **Frequency** | Common |

### Question

Compare open addressing and chaining for in-memory hash maps at scale.

### Short Answer (30 seconds)

Chaining: bucket → linked list/tree of entries. Open addressing: all entries in array, probe on collision. Open addressing better cache locality; chaining simpler deletion and high load factors.

### Detailed Answer (3–5 minutes)

**Open addressing:**
- Probing: linear, quadratic, double hashing
- **Pros:** No pointer overhead, cache-friendly sequential probe
- **Cons:** Clustering, sensitive to load factor (>0.7 degrades)

**Chaining:**
- **Pros:** Tolerates load factor >1, simple delete, worst-case bucket → tree (Java HashMap)
- **Cons:** Pointer chasing, allocator pressure

**At scale:** Redis dict uses chaining. Many language runtimes moved to open addressing for memory density.

**Architect:** For embedded/edge with tight memory, open addressing. For unknown key distribution with deletes, chaining. Profile — don't assume.

### Architecture Perspective

Implementation choice affects memory per key and p99 lookup.

### Follow-up Questions

1. **Robin Hood hashing? — Reduces probe length variance — better tail latency.**
2. **When treeify bucket? — Java HashMap treeifies bucket at 8+ collisions — O(log n) bucket.**

### Common Mistakes in Interviews

- Choosing without measuring memory per entry
- Open addressing with load factor 0.95
- Not considering deletion tombstone buildup in open addressing

---

## Q021: Red-Black Tree Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Trees |
| **Frequency** | Occasional |

### Question

What is a red-black tree and where does it appear in production systems?

### Short Answer (30 seconds)

Red-black tree: self-balancing BST with color invariants — O(log n) insert/delete/search. Used in Linux kernel rbtree, Java TreeMap, C++ std::map, epoll timer management, some memory allocators.

### Detailed Answer (3–5 minutes)

**Invariants (simplified):** Black height equal on all paths; no consecutive reds. Rotations restore balance on insert/delete.

**vs AVL:** Red-black allows slightly looser balance — fewer rotations on insert (better write-heavy). AVL stricter — faster reads.

**Production:**
- **Linux CFQ scheduler, VMA management** — kernel rbtree
- **Java TreeMap** — sorted map when you need in-order traversal
- **Timer wheels vs rbtree** — rbtree for many arbitrary timeouts

**Architect:** You rarely implement rbtree — use sorted structures from runtime or Redis ZSET. Know it when ordered in-memory map with range queries is needed and hash won't work.

### Architecture Perspective

Red-black tree is the default ordered map behind many standard libraries.

### Follow-up Questions

1. **Red-black vs B+ tree? — In-memory ordered map vs disk-backed index — different layers.**
2. **Skip list vs red-black? — Similar use case; skip list easier concurrent; rbtree in standard libs.**

### Common Mistakes in Interviews

- Hand-rolling rbtree in application code
- Using TreeMap for equality-only lookups
- Not knowing ordered map needed for range queries

---

## Q022: Adjacency List vs Matrix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

When use adjacency list vs adjacency matrix for graph storage in architecture?

### Short Answer (30 seconds)

Adjacency list: O(V+E) space, iterate neighbors fast — sparse graphs. Adjacency matrix: O(V²) space, O(1) edge lookup — dense graphs or small V.

### Detailed Answer (3–5 minutes)

**Adjacency list (default):**
- Social graphs, service dependencies, road networks
- Storage: array of neighbor lists, or edge table in SQL
- **Neo4j, graph DBs** — optimized adjacency traversal

**Adjacency matrix:**
- Small fixed node sets (10–100), need O(1) `isConnected(i,j)`
- Network topology among known datacenter nodes
- Floyd-Warshall all-pairs shortest path preprocessing

**Architect at scale:** Billion-node social graph cannot use matrix — adjacency list / graph partition / adjacency compression. Service mesh with 200 services — adjacency list in config or service catalog.

### Architecture Perspective

Graph storage choice determines memory and query feasibility at scale.

### Follow-up Questions

1. **Edge table in SQL? — `from_id, to_id` — adjacency list in relational form.**
2. **Graph partitioning? — Shard adjacency list by node ID range for distributed graph.**

### Common Mistakes in Interviews

- Adjacency matrix for million-node graph
- Storing full graph in single machine memory
- No index on edge table for neighbor lookups

---

## Q023: Topological Sort Applications

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

Where does topological sort appear in system architecture?

### Short Answer (30 seconds)

Topological sort orders DAG nodes so dependencies come first. Used in build pipelines, task schedulers, schema migrations, infrastructure-as-code dependency graphs, package managers.

### Detailed Answer (3–5 minutes)

**Production examples:**
1. **CI/CD** — build service B before A if A depends on B's API contract
2. **Terraform/Pulumi** — resource dependency graph → apply order
3. **Database migrations** — migration scripts with FK dependencies
4. **npm/Docker layer builds** — Dockerfile instruction order

**Algorithm:** Kahn's (BFS in-degree) or DFS post-order. O(V+E).

**Architect:** Circular dependency = no topological order = design bug. Detect cycles before deploy pipeline runs.

### Architecture Perspective

Deploy and build systems are topological sorts in production.

### Follow-up Questions

1. **Kahn vs DFS topo sort? — Kahn detects cycles explicitly; DFS with coloring.**
2. **Parallel topo levels? — All nodes with in-degree 0 at same level can run parallel.**

### Common Mistakes in Interviews

- Manual deploy order for 50 microservices
- Circular IaC dependency undetected until apply fails
- Running migrations out of dependency order

---

## Q024: Dijkstra Structure Needs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What data structures does Dijkstra's algorithm require and where is it used in architecture?

### Short Answer (30 seconds)

Dijkstra needs: weighted graph (adjacency list), min-priority queue (heap), distance array. O((V+E) log V). Used in CDN routing, network path selection, service mesh weighted routing.

### Detailed Answer (3–5 minutes)

**Structures:**
- **Adjacency list** — sparse graph storage
- **Min-heap / priority queue** — extract minimum distance node
- **Distance map** — best known cost to each node
- **Predecessor map** — reconstruct path

**Production:**
- **OSPF/BGP** — link-state routing (variants of shortest path)
- **Maps APIs** — road network shortest path (often A* with heuristics)
- **Service mesh** — weighted latency routing between nodes

**Limitation:** Non-negative weights only — negative weights need Bellman-Ford.

**Architect:** At internet scale, precompute or use hierarchical routing — full Dijkstra on billion-node graph is offline batch, not per-request.

### Architecture Perspective

Dijkstra maps to weighted dependency and routing problems.

### Follow-up Questions

1. **Dijkstra vs A*? — A* adds heuristic — faster when goal-directed (maps).**
2. **Bidirectional Dijkstra? — Search from both ends — cuts search space.**

### Common Mistakes in Interviews

- Running Dijkstra per request on full internet graph
- Using Dijkstra with negative edge weights
- Array-based priority queue instead of heap — slower

---

## Q025: Memory Locality and Cache-Friendly Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

How does memory locality affect architectural choices for data structures?

### Short Answer (30 seconds)

CPU cache lines (~64 bytes) favor sequential access. Arrays and struct-of-arrays beat linked lists and array-of-structs for hot paths. False sharing and pointer chasing cause cache misses.

### Detailed Answer (3–5 minutes)

**Cache-friendly patterns:**
- **Columnar storage** — scan one column (array) — analytics
- **Ring buffer** — sequential access
- **Open addressing hash** — probe in contiguous memory
- **Struct of arrays (SoA)** — process one field across all entities in SIMD-friendly loops

**Cache-unfriendly:**
- Linked list traversal — random memory jumps
- Object graphs with pointers everywhere

**Architect impact:** ORM materializing object graphs vs DTO projection — projection reduces allocations and improves locality. Data-oriented design in game engines and HFT applies same principle to services processing batches.

### Architecture Perspective

Locality explains why arrays beat linked lists at scale beyond Big-O.

### Follow-up Questions

1. **False sharing? — Two threads write adjacent fields — same cache line invalidated.**
2. **NUMA awareness? — On multi-socket servers, memory affinity matters for hot structures.**

### Common Mistakes in Interviews

- Linked list for hot-path iteration over millions of items
- Array of objects when SoA would vectorize
- Ignoring allocation pressure from small object churn

---

## Q026: Probabilistic Structures Tradeoffs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Probabilistic Structures |
| **Frequency** | Common |

### Question

Compare bloom filter, HyperLogLog, and count-min sketch for architects.

### Short Answer (30 seconds)

Bloom: set membership (maybe yes, definitely no). HyperLogLog: distinct count estimate. Count-min: frequency estimate. All trade exactness for fixed memory at scale.

### Detailed Answer (3–5 minutes)

| Structure | Answers | Error | Delete? |
|-----------|---------|-------|--------|
| Bloom filter | Is x in set? | False positives | No (standard) |
| HyperLogLog | How many unique? | ~0.81% std error | N/A |
| Count-min sketch | How many x? | Overestimate | N/A |

**Combined pattern:** Bloom in front of DB → HyperLogLog for UV metrics → count-min for heavy hitter detection → exact store for flagged items.

**Architect:** Document acceptable error rate in ADR. Billing needs exact; CDN cache negative lookup can tolerate bloom FP.

### Architecture Perspective

Probabilistic DS suite covers membership, cardinality, frequency.

### Follow-up Questions

1. **Redis HyperLogLog? — `PFADD`/`PFCOUNT` — built-in UV counting.**
2. **Counting bloom filter? — Supports delete via counter per bit.**

### Common Mistakes in Interviews

- Using bloom filter for billing exact counts
- Not sizing structures for expected cardinality
- Single probabilistic structure for all query types

---

## Q027: Data Structure Selection ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Framework |
| **Frequency** | Common |

### Question

How do you document data structure choices in an Architecture Decision Record?

### Short Answer (30 seconds)

ADR captures: access pattern, scale, consistency, rejected alternatives, consequences. Template: Context → Decision → Hash/B-tree/Trie/Redis → Rejected options with why.

### Detailed Answer (3–5 minutes)

**Example ADR snippet:**
- **Context:** Product search 10M SKUs, prefix + full-text
- **Decision:** Elasticsearch inverted index + Redis cache for hot SKUs
- **Rejected:** SQL LIKE (O(n) scan); in-memory trie (memory bound)
- **Consequences:** Ops overhead, index rebuild pipeline, eventual consistency on index lag

**Architect:** DS selection is not permanent — ADR revision when scale crosses threshold (10M → 1B).

### Architecture Perspective

ADR makes DS choice auditable and teachable to team.

### Follow-up Questions

1. **When revisit ADR? — 10x scale, new access pattern, cost threshold.**
2. **Who approves DS ADR? — Tech lead + DBA/search owner for managed services.**

### Common Mistakes in Interviews

- Verbal decision with no rejected alternatives documented
- Choosing technology before access pattern analysis
- No migration path when DS choice hits limit

---

## Q028: Immutable Persistent Structures

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Functional DS |
| **Frequency** | Occasional |

### Question

What are immutable persistent data structures and where do they help in distributed systems?

### Short Answer (30 seconds)

Persistent DS preserve previous versions on update — structural sharing, not full copy. Immutable structures simplify concurrency, event sourcing, and Git-like versioning.

### Detailed Answer (3–5 minutes)

**Benefits:**
- **Thread safety** — no locks on read path
- **Event sourcing** — each event produces new version; old state queryable
- **Copy-on-write** — B-tree, persistent vector (Clojure, Immutable.js)

**Production:**
- **Git** — Merkle DAG of commits (immutable tree objects)
- **Kafka log** — append-only immutable segments
- **Cosmos DB / CRDT** — conflict-free replicated data types build on immutable merge

**Trade-off:** Updates allocate new nodes — GC pressure. Use when read >> write and history matters.

### Architecture Perspective

Immutability enables safe sharing and audit trails in distributed design.

### Follow-up Questions

1. **Persistent vs ephemeral? — Persistent keeps old versions; ephemeral discards.**
2. **Structural sharing? — New version shares unchanged subtrees — O(log n) copy.**

### Common Mistakes in Interviews

- Deep-cloning entire state on every event
- Mutable shared state across threads without synchronization
- Ignoring storage growth from retained versions

---

## Q029: HyperLogLog Cardinality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Probabilistic Structures |
| **Frequency** | Common |

### Question

Explain HyperLogLog. When estimate unique visitors instead of exact count?

### Short Answer (30 seconds)

HyperLogLog estimates distinct count in O(1) memory (~12KB for 64K buckets, ~0.81% error). Redis `PFADD`/`PFCOUNT`, BigQuery `APPROX_COUNT_DISTINCT`, Datadog UV metrics.

### Detailed Answer (3–5 minutes)

**How it works:** Hash each element; track maximum leading zeros in registers; more unique elements → more varied hashes → higher max zeros statistically.

**Use when:**
- Unique visitors at billions of events/day
- Network flow distinct IP counting
- Database `COUNT(DISTINCT)` too expensive

**Don't use when:** Exact count required (billing, compliance), small cardinality (just use set).

**Architect:** Pipeline: HyperLogLog for real-time dashboard → nightly exact batch for reconciliation if needed.

### Architecture Perspective

Cardinality estimation is standard infra — not exotic.

### Follow-up Questions

1. **HLL merge? — Union of sketches from shards — `PFMERGE` in Redis.**
2. **HLL++ improvements? — Google bias correction — better small cardinalities.**

### Common Mistakes in Interviews

- Exact distinct on 10B row table per dashboard load
- Not merging per-shard HLL at query time
- HyperLogLog for 'top 10 products by count' — wrong tool

---

## Q030: Merkle Tree Integrity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Trees |
| **Frequency** | Common |

### Question

What is a Merkle tree and how is it used for data integrity in distributed systems?

### Short Answer (30 seconds)

Merkle tree: hash tree where leaf = data hash, parent = hash(children). Root hash commits to entire dataset — O(log n) proof of inclusion. Used in Git, blockchain, Cassandra repair, certificate transparency.

### Detailed Answer (3–5 minutes)

**Production:**
1. **Git** — commit tree objects; root identifies snapshot
2. **Cassandra** — Merkle trees compare replica data for anti-entropy repair
3. **Certificate Transparency** — log inclusion proofs
4. **IPFS** — content-addressed DAG

**Verification:** To prove block D in tree: provide O(log n) sibling hashes — verifier recomputes root.

**Architect:** Merkle proofs enable light clients and efficient sync — 'prove this record existed at this root' without downloading full dataset.

### Architecture Perspective

Merkle trees are integrity and sync primitives for distributed data.

### Follow-up Questions

1. **Merkle vs plain checksum? — Merkle localizes corruption and enables partial verification.**
2. **Blockchain relevance? — Block header includes Merkle root of transactions.**

### Common Mistakes in Interviews

- Full dataset compare for replica sync on TB data
- SHA1 for new integrity systems — use SHA-256
- Not versioning root hash when data mutates

---
