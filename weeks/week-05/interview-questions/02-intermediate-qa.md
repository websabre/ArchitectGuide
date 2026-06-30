# Week 05 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Hash table

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Very Common |

### Question

What is Hash table and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Hash table when o(1) key lookup caches and indexes. Avoid when ordered range queries. Production example: Redis key-value and consistent hashing rings.

### Detailed Answer (3–5 minutes)

**Concept:** Hash table

**When to use:** O(1) key lookup caches and indexes

**When to avoid:** Ordered range queries

**Production example:** Redis key-value and consistent hashing rings

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Hash table to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Hash table with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Hash table overkill? — Ordered range queries**
2. **How measure success after adopting Hash table? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Hash table without production example
- Using Hash table when ordered range queries
- No rollback plan when Hash table misconfigured

---

## Q032: B+ tree index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Common |

### Question

What is B+ tree index and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use B+ tree index when disk-backed range queries in databases. Avoid when in-memory only workloads. Production example: SQL Server clustered index leaf pages.

### Detailed Answer (3–5 minutes)

**Concept:** B+ tree index

**When to use:** Disk-backed range queries in databases

**When to avoid:** In-memory only workloads

**Production example:** SQL Server clustered index leaf pages

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect B+ tree index to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify B+ tree index with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is B+ tree index overkill? — In-memory only workloads**
2. **How measure success after adopting B+ tree index? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting B+ tree index without production example
- Using B+ tree index when in-memory only workloads
- No rollback plan when B+ tree index misconfigured

---

## Q033: Trie prefix search

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Occasional |

### Question

What is Trie prefix search and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Trie prefix search when autocomplete and ip routing tables. Avoid when exact match only workloads. Production example: Typeahead search over product catalog.

### Detailed Answer (3–5 minutes)

**Concept:** Trie prefix search

**When to use:** Autocomplete and IP routing tables

**When to avoid:** Exact match only workloads

**Production example:** Typeahead search over product catalog

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Trie prefix search to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Trie prefix search with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Trie prefix search overkill? — Exact match only workloads**
2. **How measure success after adopting Trie prefix search? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Trie prefix search without production example
- Using Trie prefix search when exact match only workloads
- No rollback plan when Trie prefix search misconfigured

---

## Q034: Min-heap priority queue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Heaps |
| **Frequency** | Very Common |

### Question

What is Min-heap priority queue and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Min-heap priority queue when top-k and job scheduling. Avoid when uniform priority workloads. Production example: Redis ZSET for game leaderboards.

### Detailed Answer (3–5 minutes)

**Concept:** Min-heap priority queue

**When to use:** Top-K and job scheduling

**When to avoid:** Uniform priority workloads

**Production example:** Redis ZSET for game leaderboards

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Min-heap priority queue to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Min-heap priority queue with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Min-heap priority queue overkill? — Uniform priority workloads**
2. **How measure success after adopting Min-heap priority queue? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Min-heap priority queue without production example
- Using Min-heap priority queue when uniform priority workloads
- No rollback plan when Min-heap priority queue misconfigured

---

## Q035: Bloom filter

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Probabilistic |
| **Frequency** | Common |

### Question

What is Bloom filter and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Bloom filter when cheap membership tests before db lookup. Avoid when exact membership required. Production example: Cassandra negative lookup before disk read.

### Detailed Answer (3–5 minutes)

**Concept:** Bloom filter

**When to use:** Cheap membership tests before DB lookup

**When to avoid:** Exact membership required

**Production example:** Cassandra negative lookup before disk read

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Bloom filter to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Bloom filter with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Bloom filter overkill? — Exact membership required**
2. **How measure success after adopting Bloom filter? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Bloom filter without production example
- Using Bloom filter when exact membership required
- No rollback plan when Bloom filter misconfigured

---

## Q036: Consistent hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed |
| **Frequency** | Occasional |

### Question

What is Consistent hashing and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Consistent hashing when shard routing with minimal remapping. Avoid when single-node stores. Production example: Memcached client shard selection.

### Detailed Answer (3–5 minutes)

**Concept:** Consistent hashing

**When to use:** Shard routing with minimal remapping

**When to avoid:** Single-node stores

**Production example:** Memcached client shard selection

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Consistent hashing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Consistent hashing with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Consistent hashing overkill? — Single-node stores**
2. **How measure success after adopting Consistent hashing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Consistent hashing without production example
- Using Consistent hashing when single-node stores
- No rollback plan when Consistent hashing misconfigured

---

## Q037: LRU cache structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

What is LRU cache structure and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use LRU cache structure when bounded in-memory hot key cache. Avoid when unbounded caching. Production example: Hash map + doubly linked list → Redis LRU policy.

### Detailed Answer (3–5 minutes)

**Concept:** LRU cache structure

**When to use:** Bounded in-memory hot key cache

**When to avoid:** Unbounded caching

**Production example:** Hash map + doubly linked list → Redis LRU policy

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect LRU cache structure to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify LRU cache structure with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is LRU cache structure overkill? — Unbounded caching**
2. **How measure success after adopting LRU cache structure? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting LRU cache structure without production example
- Using LRU cache structure when unbounded caching
- No rollback plan when LRU cache structure misconfigured

---

## Q038: Graph dependency map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is Graph dependency map and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Graph dependency map when service blast-radius analysis. Avoid when linear pipelines only. Production example: DFS on microservice call graph during incidents.

### Detailed Answer (3–5 minutes)

**Concept:** Graph dependency map

**When to use:** Service blast-radius analysis

**When to avoid:** Linear pipelines only

**Production example:** DFS on microservice call graph during incidents

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Graph dependency map to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Graph dependency map with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Graph dependency map overkill? — Linear pipelines only**
2. **How measure success after adopting Graph dependency map? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Graph dependency map without production example
- Using Graph dependency map when linear pipelines only
- No rollback plan when Graph dependency map misconfigured

---

## Q039: Queue FIFO semantics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Queues |
| **Frequency** | Occasional |

### Question

What is Queue FIFO semantics and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Queue FIFO semantics when async work distribution. Avoid when lifo undo workflows. Production example: Service Bus queue for order emails.

### Detailed Answer (3–5 minutes)

**Concept:** Queue FIFO semantics

**When to use:** Async work distribution

**When to avoid:** LIFO undo workflows

**Production example:** Service Bus queue for order emails

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Queue FIFO semantics to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Queue FIFO semantics with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Queue FIFO semantics overkill? — LIFO undo workflows**
2. **How measure success after adopting Queue FIFO semantics? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Queue FIFO semantics without production example
- Using Queue FIFO semantics when lifo undo workflows
- No rollback plan when Queue FIFO semantics misconfigured

---

## Q040: Ring buffer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Arrays |
| **Frequency** | Very Common |

### Question

What is Ring buffer and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Ring buffer when high-throughput streaming buffers. Avoid when random access primary. Production example: Disruptor pattern in low-latency pipelines.

### Detailed Answer (3–5 minutes)

**Concept:** Ring buffer

**When to use:** High-throughput streaming buffers

**When to avoid:** Random access primary

**Production example:** Disruptor pattern in low-latency pipelines

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Ring buffer to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Ring buffer with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Ring buffer overkill? — Random access primary**
2. **How measure success after adopting Ring buffer? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Ring buffer without production example
- Using Ring buffer when random access primary
- No rollback plan when Ring buffer misconfigured

---

## Q041: Skip list

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Lists |
| **Frequency** | Common |

### Question

What is Skip list and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Skip list when ordered in-memory indexes. Avoid when simple few-element lists. Production example: Redis internal sorted set implementation concept.

### Detailed Answer (3–5 minutes)

**Concept:** Skip list

**When to use:** Ordered in-memory indexes

**When to avoid:** Simple few-element lists

**Production example:** Redis internal sorted set implementation concept

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Skip list to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Skip list with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Skip list overkill? — Simple few-element lists**
2. **How measure success after adopting Skip list? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Skip list without production example
- Using Skip list when simple few-element lists
- No rollback plan when Skip list misconfigured

---

## Q042: Inverted index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Occasional |

### Question

What is Inverted index and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Inverted index when full-text search token lookup. Avoid when key-value only access. Production example: Elasticsearch term → document IDs.

### Detailed Answer (3–5 minutes)

**Concept:** Inverted index

**When to use:** Full-text search token lookup

**When to avoid:** Key-value only access

**Production example:** Elasticsearch term → document IDs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Inverted index to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Inverted index with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Inverted index overkill? — Key-value only access**
2. **How measure success after adopting Inverted index? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Inverted index without production example
- Using Inverted index when key-value only access
- No rollback plan when Inverted index misconfigured

---

## Q043: Count-min sketch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Probabilistic |
| **Frequency** | Very Common |

### Question

What is Count-min sketch and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Count-min sketch when streaming frequency estimation. Avoid when exact counts required. Production example: Heavy hitter detection in CDN logs.

### Detailed Answer (3–5 minutes)

**Concept:** Count-min sketch

**When to use:** Streaming frequency estimation

**When to avoid:** Exact counts required

**Production example:** Heavy hitter detection in CDN logs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Count-min sketch to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Count-min sketch with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Count-min sketch overkill? — Exact counts required**
2. **How measure success after adopting Count-min sketch? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Count-min sketch without production example
- Using Count-min sketch when exact counts required
- No rollback plan when Count-min sketch misconfigured

---

## Q044: Union-find disjoint set

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Graphs |
| **Frequency** | Common |

### Question

What is Union-find disjoint set and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Union-find disjoint set when connected components grouping. Avoid when strict hierarchy only. Production example: Network connectivity grouping in topology tools.

### Detailed Answer (3–5 minutes)

**Concept:** Union-find disjoint set

**When to use:** Connected components grouping

**When to avoid:** Strict hierarchy only

**Production example:** Network connectivity grouping in topology tools

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Union-find disjoint set to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Union-find disjoint set with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Union-find disjoint set overkill? — Strict hierarchy only**
2. **How measure success after adopting Union-find disjoint set? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Union-find disjoint set without production example
- Using Union-find disjoint set when strict hierarchy only
- No rollback plan when Union-find disjoint set misconfigured

---

## Q045: Sliding window deque

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Queues |
| **Frequency** | Occasional |

### Question

What is Sliding window deque and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Sliding window deque when rate limiting time windows. Avoid when stateless counting. Production example: Requests-per-minute rolling window limiter.

### Detailed Answer (3–5 minutes)

**Concept:** Sliding window deque

**When to use:** Rate limiting time windows

**When to avoid:** Stateless counting

**Production example:** Requests-per-minute rolling window limiter

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Sliding window deque to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Sliding window deque with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Sliding window deque overkill? — Stateless counting**
2. **How measure success after adopting Sliding window deque? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Sliding window deque without production example
- Using Sliding window deque when stateless counting
- No rollback plan when Sliding window deque misconfigured

---

## Q046: AVL tree self-balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Very Common |

### Question

What is AVL tree self-balancing and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use AVL tree self-balancing when strict balance guarantees. Avoid when avl for disk index. Production example: In-memory ordered map AVL.

### Detailed Answer (3–5 minutes)

**Concept:** AVL tree self-balancing

**When to use:** Strict balance guarantees

**When to avoid:** AVL for disk index

**Production example:** In-memory ordered map AVL

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect AVL tree self-balancing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify AVL tree self-balancing with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is AVL tree self-balancing overkill? — AVL for disk index**
2. **How measure success after adopting AVL tree self-balancing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting AVL tree self-balancing without production example
- Using AVL tree self-balancing when avl for disk index
- No rollback plan when AVL tree self-balancing misconfigured

---

## Q047: B-tree vs B+ tree

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Common |

### Question

What is B-tree vs B+ tree and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use B-tree vs B+ tree when disk index choice. Avoid when b-tree for database. Production example: B+ tree SQL default.

### Detailed Answer (3–5 minutes)

**Concept:** B-tree vs B+ tree

**When to use:** Disk index choice

**When to avoid:** B-tree for database

**Production example:** B+ tree SQL default

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect B-tree vs B+ tree to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify B-tree vs B+ tree with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is B-tree vs B+ tree overkill? — B-tree for database**
2. **How measure success after adopting B-tree vs B+ tree? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting B-tree vs B+ tree without production example
- Using B-tree vs B+ tree when b-tree for database
- No rollback plan when B-tree vs B+ tree misconfigured

---

## Q048: Segment tree range query

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Occasional |

### Question

What is Segment tree range query and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Segment tree range query when range sum queries. Avoid when segment tree for crud. Production example: Price range sum analytics.

### Detailed Answer (3–5 minutes)

**Concept:** Segment tree range query

**When to use:** Range sum queries

**When to avoid:** Segment tree for CRUD

**Production example:** Price range sum analytics

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Segment tree range query to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Segment tree range query with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Segment tree range query overkill? — Segment tree for CRUD**
2. **How measure success after adopting Segment tree range query? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Segment tree range query without production example
- Using Segment tree range query when segment tree for crud
- No rollback plan when Segment tree range query misconfigured

---

## Q049: Fenwick tree BIT

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Very Common |

### Question

What is Fenwick tree BIT and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Fenwick tree BIT when prefix sum updates. Avoid when bit for graph. Production example: BIT frequency analytics.

### Detailed Answer (3–5 minutes)

**Concept:** Fenwick tree BIT

**When to use:** Prefix sum updates

**When to avoid:** BIT for graph

**Production example:** BIT frequency analytics

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Fenwick tree BIT to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Fenwick tree BIT with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Fenwick tree BIT overkill? — BIT for graph**
2. **How measure success after adopting Fenwick tree BIT? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Fenwick tree BIT without production example
- Using Fenwick tree BIT when bit for graph
- No rollback plan when Fenwick tree BIT misconfigured

---

## Q050: Suffix tree advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Common |

### Question

What is Suffix tree advanced and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Suffix tree advanced when substring search. Avoid when suffix tree interview only. Production example: Bioinformatics substring.

### Detailed Answer (3–5 minutes)

**Concept:** Suffix tree advanced

**When to use:** Substring search

**When to avoid:** Suffix tree interview only

**Production example:** Bioinformatics substring

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Suffix tree advanced to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Suffix tree advanced with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Suffix tree advanced overkill? — Suffix tree interview only**
2. **How measure success after adopting Suffix tree advanced? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Suffix tree advanced without production example
- Using Suffix tree advanced when suffix tree interview only
- No rollback plan when Suffix tree advanced misconfigured

---

## Q051: Radix tree compressed trie

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Occasional |

### Question

What is Radix tree compressed trie and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Radix tree compressed trie when ip routing memory. Avoid when standard trie sparse. Production example: Radix tree route table.

### Detailed Answer (3–5 minutes)

**Concept:** Radix tree compressed trie

**When to use:** IP routing memory

**When to avoid:** Standard trie sparse

**Production example:** Radix tree route table

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Radix tree compressed trie to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Radix tree compressed trie with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Radix tree compressed trie overkill? — Standard trie sparse**
2. **How measure success after adopting Radix tree compressed trie? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Radix tree compressed trie without production example
- Using Radix tree compressed trie when standard trie sparse
- No rollback plan when Radix tree compressed trie misconfigured

---

## Q052: Heapify operation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Heaps |
| **Frequency** | Very Common |

### Question

What is Heapify operation and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Heapify operation when build heap o(n). Avoid when sort with heap wrong. Production example: Heapify bottom-up build.

### Detailed Answer (3–5 minutes)

**Concept:** Heapify operation

**When to use:** Build heap O(n)

**When to avoid:** Sort with heap wrong

**Production example:** Heapify bottom-up build

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Heapify operation to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Heapify operation with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Heapify operation overkill? — Sort with heap wrong**
2. **How measure success after adopting Heapify operation? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Heapify operation without production example
- Using Heapify operation when sort with heap wrong
- No rollback plan when Heapify operation misconfigured

---

## Q053: Fibonacci heap theory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Heaps |
| **Frequency** | Common |

### Question

What is Fibonacci heap theory and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Fibonacci heap theory when theoretical dijkstra. Avoid when fibonacci in production. Production example: Theory interview only.

### Detailed Answer (3–5 minutes)

**Concept:** Fibonacci heap theory

**When to use:** Theoretical Dijkstra

**When to avoid:** Fibonacci in production

**Production example:** Theory interview only

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Fibonacci heap theory to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Fibonacci heap theory with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Fibonacci heap theory overkill? — Fibonacci in production**
2. **How measure success after adopting Fibonacci heap theory? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Fibonacci heap theory without production example
- Using Fibonacci heap theory when fibonacci in production
- No rollback plan when Fibonacci heap theory misconfigured

---

## Q054: Binomial heap merge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Heaps |
| **Frequency** | Occasional |

### Question

What is Binomial heap merge and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Binomial heap merge when mergeable heaps. Avoid when binomial in app code. Production example: Academic merge heaps.

### Detailed Answer (3–5 minutes)

**Concept:** Binomial heap merge

**When to use:** Mergeable heaps

**When to avoid:** Binomial in app code

**Production example:** Academic merge heaps

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Binomial heap merge to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Binomial heap merge with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Binomial heap merge overkill? — Binomial in app code**
2. **How measure success after adopting Binomial heap merge? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Binomial heap merge without production example
- Using Binomial heap merge when binomial in app code
- No rollback plan when Binomial heap merge misconfigured

---

## Q055: Pairing heap practical

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Heaps |
| **Frequency** | Very Common |

### Question

What is Pairing heap practical and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Pairing heap practical when simpler mergeable. Avoid when pairing heap database. Production example: Alternative priority queue.

### Detailed Answer (3–5 minutes)

**Concept:** Pairing heap practical

**When to use:** Simpler mergeable

**When to avoid:** Pairing heap database

**Production example:** Alternative priority queue

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Pairing heap practical to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Pairing heap practical with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Pairing heap practical overkill? — Pairing heap database**
2. **How measure success after adopting Pairing heap practical? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Pairing heap practical without production example
- Using Pairing heap practical when pairing heap database
- No rollback plan when Pairing heap practical misconfigured

---

## Q056: Double-ended priority queue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Heaps |
| **Frequency** | Common |

### Question

What is Double-ended priority queue and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Double-ended priority queue when min and max ends. Avoid when two heaps awkward. Production example: Interval scheduling DEQ.

### Detailed Answer (3–5 minutes)

**Concept:** Double-ended priority queue

**When to use:** Min and max ends

**When to avoid:** Two heaps awkward

**Production example:** Interval scheduling DEQ

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Double-ended priority queue to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Double-ended priority queue with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Double-ended priority queue overkill? — Two heaps awkward**
2. **How measure success after adopting Double-ended priority queue? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Double-ended priority queue without production example
- Using Double-ended priority queue when two heaps awkward
- No rollback plan when Double-ended priority queue misconfigured

---

## Q057: Hash map load factor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Occasional |

### Question

What is Hash map load factor and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Hash map load factor when resize tuning. Avoid when load factor ignored. Production example: 0.75 resize threshold.

### Detailed Answer (3–5 minutes)

**Concept:** Hash map load factor

**When to use:** Resize tuning

**When to avoid:** Load factor ignored

**Production example:** 0.75 resize threshold

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Hash map load factor to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Hash map load factor with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Hash map load factor overkill? — Load factor ignored**
2. **How measure success after adopting Hash map load factor? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Hash map load factor without production example
- Using Hash map load factor when load factor ignored
- No rollback plan when Hash map load factor misconfigured

---

## Q058: Cuckoo hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Very Common |

### Question

What is Cuckoo hashing and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Cuckoo hashing when o(1) worst lookup. Avoid when cuckoo at scale db. Production example: Network switch FIB cuckoo.

### Detailed Answer (3–5 minutes)

**Concept:** Cuckoo hashing

**When to use:** O(1) worst lookup

**When to avoid:** Cuckoo at scale DB

**Production example:** Network switch FIB cuckoo

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Cuckoo hashing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Cuckoo hashing with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Cuckoo hashing overkill? — Cuckoo at scale DB**
2. **How measure success after adopting Cuckoo hashing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Cuckoo hashing without production example
- Using Cuckoo hashing when cuckoo at scale db
- No rollback plan when Cuckoo hashing misconfigured

---

## Q059: Robin Hood hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Common |

### Question

What is Robin Hood hashing and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Robin Hood hashing when reduce variance. Avoid when robin hood hand roll. Production example: Open addressing variant.

### Detailed Answer (3–5 minutes)

**Concept:** Robin Hood hashing

**When to use:** Reduce variance

**When to avoid:** Robin Hood hand roll

**Production example:** Open addressing variant

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Robin Hood hashing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Robin Hood hashing with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Robin Hood hashing overkill? — Robin Hood hand roll**
2. **How measure success after adopting Robin Hood hashing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Robin Hood hashing without production example
- Using Robin Hood hashing when robin hood hand roll
- No rollback plan when Robin Hood hashing misconfigured

---

## Q060: Perfect hashing static

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Occasional |

### Question

What is Perfect hashing static and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Perfect hashing static when static key set. Avoid when perfect hash dynamic. Production example: Compiler keyword table.

### Detailed Answer (3–5 minutes)

**Concept:** Perfect hashing static

**When to use:** Static key set

**When to avoid:** Perfect hash dynamic

**Production example:** Compiler keyword table

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Perfect hashing static to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Perfect hashing static with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Perfect hashing static overkill? — Perfect hash dynamic**
2. **How measure success after adopting Perfect hashing static? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Perfect hashing static without production example
- Using Perfect hashing static when perfect hash dynamic
- No rollback plan when Perfect hashing static misconfigured

---

## Q061: Coalesced hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Very Common |

### Question

What is Coalesced hashing and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Coalesced hashing when open addressing variant. Avoid when coalesced in app. Production example: Alternative collision.

### Detailed Answer (3–5 minutes)

**Concept:** Coalesced hashing

**When to use:** Open addressing variant

**When to avoid:** Coalesced in app

**Production example:** Alternative collision

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Coalesced hashing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Coalesced hashing with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Coalesced hashing overkill? — Coalesced in app**
2. **How measure success after adopting Coalesced hashing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Coalesced hashing without production example
- Using Coalesced hashing when coalesced in app
- No rollback plan when Coalesced hashing misconfigured

---

## Q062: Extendible hashing disk

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Common |

### Question

What is Extendible hashing disk and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Extendible hashing disk when dynamic disk hash. Avoid when extendible in memory. Production example: Database extendible hash.

### Detailed Answer (3–5 minutes)

**Concept:** Extendible hashing disk

**When to use:** Dynamic disk hash

**When to avoid:** Extendible in memory

**Production example:** Database extendible hash

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Extendible hashing disk to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Extendible hashing disk with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Extendible hashing disk overkill? — Extendible in memory**
2. **How measure success after adopting Extendible hashing disk? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Extendible hashing disk without production example
- Using Extendible hashing disk when extendible in memory
- No rollback plan when Extendible hashing disk misconfigured

---

## Q063: Linear hashing disk

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash Tables |
| **Frequency** | Occasional |

### Question

What is Linear hashing disk and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Linear hashing disk when gradual bucket split. Avoid when linear hash app. Production example: Disk hash table growth.

### Detailed Answer (3–5 minutes)

**Concept:** Linear hashing disk

**When to use:** Gradual bucket split

**When to avoid:** Linear hash app

**Production example:** Disk hash table growth

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Linear hashing disk to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Linear hashing disk with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Linear hashing disk overkill? — Linear hash app**
2. **How measure success after adopting Linear hashing disk? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Linear hashing disk without production example
- Using Linear hashing disk when linear hash app
- No rollback plan when Linear hashing disk misconfigured

---

## Q064: Consistent hashing virtual nodes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed |
| **Frequency** | Very Common |

### Question

What is Consistent hashing virtual nodes and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Consistent hashing virtual nodes when even distribution. Avoid when no vnodes skew. Production example: 150 vnodes per physical node.

### Detailed Answer (3–5 minutes)

**Concept:** Consistent hashing virtual nodes

**When to use:** Even distribution

**When to avoid:** No vnodes skew

**Production example:** 150 vnodes per physical node

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Consistent hashing virtual nodes to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Consistent hashing virtual nodes with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Consistent hashing virtual nodes overkill? — No vnodes skew**
2. **How measure success after adopting Consistent hashing virtual nodes? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Consistent hashing virtual nodes without production example
- Using Consistent hashing virtual nodes when no vnodes skew
- No rollback plan when Consistent hashing virtual nodes misconfigured

---

## Q065: Rendezvous hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed |
| **Frequency** | Common |

### Question

What is Rendezvous hashing and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Rendezvous hashing when minimal remapping. Avoid when rendezvous vs consistent. Production example: Highest random weight hashing.

### Detailed Answer (3–5 minutes)

**Concept:** Rendezvous hashing

**When to use:** Minimal remapping

**When to avoid:** Rendezvous vs consistent

**Production example:** Highest random weight hashing

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Rendezvous hashing to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Rendezvous hashing with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Rendezvous hashing overkill? — Rendezvous vs consistent**
2. **How measure success after adopting Rendezvous hashing? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Rendezvous hashing without production example
- Using Rendezvous hashing when rendezvous vs consistent
- No rollback plan when Rendezvous hashing misconfigured

---

## Q066: Jump consistent hash

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed |
| **Frequency** | Occasional |

### Question

What is Jump consistent hash and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Jump consistent hash when minimal memory. Avoid when jump hash client change. Production example: Google jump consistent hash.

### Detailed Answer (3–5 minutes)

**Concept:** Jump consistent hash

**When to use:** Minimal memory

**When to avoid:** Jump hash client change

**Production example:** Google jump consistent hash

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Jump consistent hash to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Jump consistent hash with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Jump consistent hash overkill? — Jump hash client change**
2. **How measure success after adopting Jump consistent hash? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Jump consistent hash without production example
- Using Jump consistent hash when jump hash client change
- No rollback plan when Jump consistent hash misconfigured

---

## Q067: Magma hash ring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed |
| **Frequency** | Very Common |

### Question

What is Magma hash ring and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Magma hash ring when ketama compatible. Avoid when roll own hash ring. Production example: Memcached client ketama.

### Detailed Answer (3–5 minutes)

**Concept:** Magma hash ring

**When to use:** Ketama compatible

**When to avoid:** Roll own hash ring

**Production example:** Memcached client ketama

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Magma hash ring to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Magma hash ring with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Magma hash ring overkill? — Roll own hash ring**
2. **How measure success after adopting Magma hash ring? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Magma hash ring without production example
- Using Magma hash ring when roll own hash ring
- No rollback plan when Magma hash ring misconfigured

---

## Q068: Geohash spatial index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hash |
| **Frequency** | Common |

### Question

What is Geohash spatial index and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Geohash spatial index when location proximity. Avoid when geohash exact match. Production example: Nearby drivers geohash.

### Detailed Answer (3–5 minutes)

**Concept:** Geohash spatial index

**When to use:** Location proximity

**When to avoid:** Geohash exact match

**Production example:** Nearby drivers geohash

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Geohash spatial index to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Geohash spatial index with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Geohash spatial index overkill? — Geohash exact match**
2. **How measure success after adopting Geohash spatial index? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Geohash spatial index without production example
- Using Geohash spatial index when geohash exact match
- No rollback plan when Geohash spatial index misconfigured

---

## Q069: Quadtree spatial

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Occasional |

### Question

What is Quadtree spatial and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use Quadtree spatial when 2d spatial queries. Avoid when quadtree 1d. Production example: Game collision quadtree.

### Detailed Answer (3–5 minutes)

**Concept:** Quadtree spatial

**When to use:** 2D spatial queries

**When to avoid:** Quadtree 1D

**Production example:** Game collision quadtree

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Quadtree spatial to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Quadtree spatial with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is Quadtree spatial overkill? — Quadtree 1D**
2. **How measure success after adopting Quadtree spatial? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Quadtree spatial without production example
- Using Quadtree spatial when quadtree 1d
- No rollback plan when Quadtree spatial misconfigured

---

## Q070: R-tree spatial database

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Trees |
| **Frequency** | Very Common |

### Question

What is R-tree spatial database and when would you apply it in Data Structures for System Design?

### Short Answer (30 seconds)

Use R-tree spatial database when gis database index. Avoid when r-tree in memory app. Production example: PostGIS R-tree.

### Detailed Answer (3–5 minutes)

**Concept:** R-tree spatial database

**When to use:** GIS database index

**When to avoid:** R-tree in memory app

**Production example:** PostGIS R-tree

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect R-tree spatial database to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify R-tree spatial database with production trade-offs in Data Structures for System Design.

### Follow-up Questions

1. **When is R-tree spatial database overkill? — R-tree in memory app**
2. **How measure success after adopting R-tree spatial database? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting R-tree spatial database without production example
- Using R-tree spatial database when r-tree in memory app
- No rollback plan when R-tree spatial database misconfigured

---
