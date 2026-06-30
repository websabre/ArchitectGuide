# Week 05 — Data Structures for System Design Diagrams

## 1. Structure Selection for Hot Paths

```mermaid
flowchart TD
    A[Need fast lookup?] --> B{Ordered keys?}
    B -->|Yes| C{Range scans?}
    B -->|No| D[HashMap / Dictionary]
    C -->|Yes| E[B-Tree / Sorted Dictionary]
    C -->|No| F[HashSet]
    D --> G[O1 average get/put]
    E --> H[O log n + ordered iteration]
```

> **Architect note:** In .NET, `Dictionary<K,V>` for general purpose; `SortedDictionary` when you need ordered keys; `ImmutableDictionary` for read-heavy config snapshots.

## 2. Leaderboard — Skip List vs Heap vs Sorted Set

```mermaid
flowchart LR
    subgraph Writes["Score Updates"]
        U[Update score] --> R[Redis ZSET]
    end
    subgraph Reads["Top-N Query"]
        R --> Z[ZRANGEBYSCORE]
        Z --> API[API Response]
    end
```

## 3. Consistent Hashing — Cache Ring

```mermaid
flowchart TB
    subgraph Ring["Hash Ring"]
        N1[Node A]
        N2[Node B]
        N3[Node C]
    end
  Key[cache key hash] --> Ring
  Ring --> N2
```

> **Architect note:** Use virtual nodes (vnodes) to reduce rebalance churn when adding/removing cache nodes.

## 4. Bloom Filter — Duplicate Detection

```mermaid
sequenceDiagram
    participant API
    participant BF as Bloom Filter
    participant DB

    API->>BF: Might exist?
    alt Probably not
        BF-->>API: No
        API->>DB: Insert
    else Maybe yes
        BF-->>API: Yes
        API->>DB: Confirm exists
    end
```

## 5. LRU Cache Eviction

```mermaid
flowchart LR
    Get[Get key] --> Move[Move to MRU]
    Put[Put key] --> Full{At capacity?}
    Full -->|Yes| Evict[Evict LRU]
    Full -->|No| Insert[Insert]
```

## Practice Exercise

Redraw diagrams 1 and 3 from memory. For a 10M-key session store, justify HashMap vs Redis cluster.

---

[← Back to Week 05](../README.md)
