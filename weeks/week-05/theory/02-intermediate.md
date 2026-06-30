# Data Structures — Intermediate (System Design Applications)

> **Week 05** | **Level:** Intermediate

## 1. Sharding with Hash Tables

```
Shard = hash(userId) % number_of_shards
```

**Consistent hashing:** Virtual nodes on hash ring — add/remove DB nodes with minimal data movement.

**Architect checklist:**
- [ ] Shard key has high cardinality
- [ ] Queries mostly include shard key (avoid scatter-gather)
- [ ] Rebalancing plan documented
- [ ] Cross-shard transactions avoided or saga pattern used

---

## 2. Bloom Filters

Probabilistic structure: "definitely not in set" or "probably in set." No false negatives, possible false positives.

**Uses:**
- Cassandra/Memcached: avoid disk reads for non-existent keys
- Web crawlers: URL deduplication
- CDNs: cache negative responses

**Architect:** Reduce load on backend for "does this exist?" checks. Size bloom filter for acceptable false positive rate.

---

## 3. Count-Min Sketch

Estimate frequency of items in stream with bounded memory.

**Uses:** Hot key detection, rate limiting analytics, trending topics.

---

## 4. Ring Buffers (Circular Queues)

Fixed-size buffer, overwrite oldest when full. Lock-free variants for high throughput.

**Uses:** Logging pipelines, audio/video streaming buffers, disruptor pattern (LMAX exchange).

---

## 5. Data Structure → Azure/AWS Service Mapping

| Concept | Azure | AWS |
|---------|-------|-----|
| Hash cache | Redis Cache | ElastiCache |
| Sorted set / leaderboard | Redis ZSET | ElastiCache Redis |
| Queue | Service Bus | SQS |
| Stream | Event Hubs | Kinesis |
| Graph | Cosmos DB Gremlin | Neptune |
| Full-text index | AI Search | OpenSearch |

---

## Production Example

**URL shortener backend:**
- **Hash map:** short code → long URL (Redis)
- **Counter / base62:** generate unique codes
- **Optional Bloom filter:** reject invalid codes before Redis lookup

**Architect interview:** Draw this, discuss collision handling, cache eviction (LRU), and DB fallback.

**Next:** [03-advanced-expert.md](03-advanced-expert.md)
