# Week 05 — Exercises

> Theory: [theory/](../theory/README.md) · Lab: [lab-05-data-structures](../labs/lab-05-data-structures.md) · Interview: [interview-questions/](../interview-questions/README.md)

## Exercise 1: Leaderboard Data Structure (45 min)

Design a real-time game leaderboard:

- 10M players, top-100 query every second
- Score updates: 50K/sec peak
- Must return rank + score for any player on demand
- Memory budget: ~4 GB

**Tasks:**
1. Compare sorted array, balanced BST, skip list, Redis ZSET
2. Choose primary + fallback structure
3. Estimate memory and update/query complexity

**Deliverable:** 1-page design doc with Big-O table. Reference [theory/](../theory/README.md) fundamentals.

---

## Exercise 2: Consistent Hashing Design (45 min)

A CDN cache cluster has 8 nodes. Keys are image URLs. You must add/remove nodes without full cache flush.

**Tasks:**
1. Draw a consistent hash ring with 3 virtual nodes per physical node
2. Show what happens when node 3 fails (which keys move?)
3. Compare vs naive `hash(key) % N` — quantify remapping %

**Deliverable:** Diagram + pseudocode for `GetNode(string key)`. Compare with [diagrams/](../diagrams/README.md).

---

## Exercise 3: Bloom Filter Use Case (30 min)

A URL shortener receives 1B redirect checks/day. 0.1% are to non-existent slugs. DB lookup costs 5ms; false positive is acceptable (redirect to 404 page).

**Tasks:**
1. Size a bloom filter for 100M slugs at 1% false-positive rate
2. Decide where it sits in the request path (before DB? before cache?)
3. Define the fallback when bloom says "maybe exists"

**Deliverable:** Architecture sketch + estimated memory (bits formula). See [lab-05](../labs/lab-05-data-structures.md).

---

## Exercise 4: Complexity Analysis Exercise (60 min)

Analyze each operation for a social feed storing posts in a doubly-linked list per user, with a hash map `userId → list head`:

```csharp
void AddPost(Guid userId, Post post);      // prepend
List<Post> GetFeed(Guid userId, int n);    // first n posts
void DeletePost(Guid userId, Guid postId);   // by id
```

**Tasks:**
1. State time/space Big-O for each (best, average, worst)
2. Identify the bottleneck at 1M users, 500 posts/user
3. Propose one structure change that fixes the bottleneck

**Deliverable:** Annotated complexity table + redesigned structure.

---

## Exercise 5: Interview Drill (30 min)

Answer aloud from [01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md):

1. Q001 (Hash Table for O(1) Lookup)
2. Q005 (Graphs for Architecture)
3. Q010 (Time and Space Complexity Trade-offs)

Target: connect each answer to a real system you have built. Score 12+/15.

---

[← Back to Week 05](../README.md)
