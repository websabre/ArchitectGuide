# Data Structures for System Design — Fundamentals

> **Week 05** | **Module:** [dsa](../../../modules/dsa/README.md)

## Learning Objectives
- Map data structures to system design decisions
- Choose structures based on access patterns, not familiarity
- Connect DSA to database indexing and caching

---

## 1. Arrays and Lists

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Random access | O(1) | O(n) |
| Insert at end | O(1) amortized | O(1) |
| Insert at middle | O(n) | O(1) if pointer known |
| Memory | Contiguous, cache-friendly | Scattered, pointer overhead |

**System design:** Arrays back dynamic arrays in languages, buffer pools, ring buffers for streaming. Linked lists rare in production — cache unfriendly.

**Architect example:** Circular buffer for log aggregation before batch write to Event Hubs.

---

## 2. Hash Tables (Hash Maps)

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert/Lookup/Delete | O(1) | O(n) |

**Production uses:**
- In-memory caches (Redis is hash-based + more)
- Distributed hash tables (sharding by `hash(key) % N`)
- DNS resolution, load balancer consistent hashing

**Consistent hashing:** When adding/removing nodes, only K/N keys remap — critical for distributed caches (Redis Cluster, CDN).

```mermaid
flowchart LR
    Key[customerId:12345] --> Hash[hash function]
    Hash --> Node[Server 3 of 8]
```

**Architect decision:** Shard users by `userId` hash across DB partitions.

---

## 3. Trees

### Binary Search Tree (BST)
- Ordered insert/search: O(log n) average, O(n) worst (unbalanced)
- **Database connection:** B-Tree and B+ Tree are generalized BSTs — SQL Server indexes are B+ Trees

### B-Tree / B+ Tree (Databases)
- Optimized for disk I/O — high branching factor, minimizes disk reads
- **Why architects care:** Index design = B+ Tree traversal. Composite index `(tenantId, createdAt)` — leftmost prefix rule

### Trie (Prefix Tree)
- Autocomplete, IP routing tables, spell checkers
- **System design:** Typeahead search, URL routing

### Heap (Priority Queue)
- Min/max element O(1), insert/delete O(log n)
- **Uses:** Task schedulers, Dijkstra's algorithm, top-K problems (leaderboards)

---

## 4. Graphs

Represent: social networks, service dependencies, network topology, state machines.

| Algorithm | Use Case | Complexity |
|-----------|----------|------------|
| BFS | Shortest path (unweighted), level-order | O(V+E) |
| DFS | Cycle detection, topological sort | O(V+E) |
| Dijkstra | Shortest path (weighted) | O((V+E) log V) |

**Architect uses:**
- Dependency graph for microservice deployment order
- Cycle detection in workflow engines
- Network path analysis

---

## 5. Structure Selection for System Design

| Requirement | Structure | Example |
|-------------|-----------|---------|
| Fast lookup by key | Hash table | User session cache |
| Ordered range queries | B+ Tree (DB index) | Orders by date range |
| Priority processing | Heap | Job queue |
| Relationships | Graph | Social graph, service mesh |
| FIFO | Queue | Message queue |
| LIFO | Stack | Undo operations, call stack |
| Unique + order | TreeSet / sorted set | Leaderboard |

---

## 6. Skip Lists and LSM Trees (Advanced Awareness)

**Skip lists:** Redis sorted sets (ZSET) use skip lists — O(log n) with simpler concurrency than balanced trees.

**LSM Trees:** Write-optimized storage (Cassandra, RocksDB, LevelDB). Batch writes to memory, flush to sorted files. **Trade-off:** Fast writes, compaction overhead, read amplification.

**Architect:** Know when NoSQL uses LSM (write-heavy) vs B-Tree (read-heavy, SQL).

---

## Common Mistakes
1. Using wrong structure for access pattern (array for frequent middle inserts)
2. Ignoring O(n) hash collisions in capacity planning
3. Not connecting B+ Tree to SQL index design
4. Over-engineering graph DB when relational suffices

**Next:** [02-intermediate.md](02-intermediate.md)
