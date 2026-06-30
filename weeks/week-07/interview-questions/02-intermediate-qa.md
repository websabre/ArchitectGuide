# Week 07 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Clustered index choice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Very Common |

### Question

What is Clustered index choice and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Clustered index choice when primary access path row ordering. Avoid when random guid clustered pk. Production example: Clustered on sequential OrderId not GUID.

### Detailed Answer (3–5 minutes)

**Concept:** Clustered index choice

**When to use:** Primary access path row ordering

**When to avoid:** Random GUID clustered PK

**Production example:** Clustered on sequential OrderId not GUID

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Clustered index choice to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Clustered index choice with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Clustered index choice overkill? — Random GUID clustered PK**
2. **How measure success after adopting Clustered index choice? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Clustered index choice without production example
- Using Clustered index choice when random guid clustered pk
- No rollback plan when Clustered index choice misconfigured

---

## Q032: Non-clustered covering index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Common |

### Question

What is Non-clustered covering index and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Non-clustered covering index when eliminate key lookups on hot queries. Avoid when write-heavy tables over-indexed. Production example: INCLUDE columns for order list query.

### Detailed Answer (3–5 minutes)

**Concept:** Non-clustered covering index

**When to use:** Eliminate key lookups on hot queries

**When to avoid:** Write-heavy tables over-indexed

**Production example:** INCLUDE columns for order list query

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Non-clustered covering index to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Non-clustered covering index with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Non-clustered covering index overkill? — Write-heavy tables over-indexed**
2. **How measure success after adopting Non-clustered covering index? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Non-clustered covering index without production example
- Using Non-clustered covering index when write-heavy tables over-indexed
- No rollback plan when Non-clustered covering index misconfigured

---

## Q033: Query execution plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

What is Query execution plan and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Query execution plan when diagnose scans and spills. Avoid when guess without measuring. Production example: Query Store finds top CPU queries.

### Detailed Answer (3–5 minutes)

**Concept:** Query execution plan

**When to use:** Diagnose scans and spills

**When to avoid:** Guess without measuring

**Production example:** Query Store finds top CPU queries

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Query execution plan to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Query execution plan with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Query execution plan overkill? — Guess without measuring**
2. **How measure success after adopting Query execution plan? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Query execution plan without production example
- Using Query execution plan when guess without measuring
- No rollback plan when Query execution plan misconfigured

---

## Q034: Isolation levels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

What is Isolation levels and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Isolation levels when balance consistency and concurrency. Avoid when serializable everywhere. Production example: RCSI for read-heavy catalog.

### Detailed Answer (3–5 minutes)

**Concept:** Isolation levels

**When to use:** Balance consistency and concurrency

**When to avoid:** Serializable everywhere

**Production example:** RCSI for read-heavy catalog

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Isolation levels to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Isolation levels with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Isolation levels overkill? — Serializable everywhere**
2. **How measure success after adopting Isolation levels? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Isolation levels without production example
- Using Isolation levels when serializable everywhere
- No rollback plan when Isolation levels misconfigured

---

## Q035: Always On AG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

What is Always On AG and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Always On AG when ha and dr for sql workloads. Avoid when single instance production. Production example: Sync replica same region RPO=0.

### Detailed Answer (3–5 minutes)

**Concept:** Always On AG

**When to use:** HA and DR for SQL workloads

**When to avoid:** Single instance production

**Production example:** Sync replica same region RPO=0

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Always On AG to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Always On AG with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Always On AG overkill? — Single instance production**
2. **How measure success after adopting Always On AG? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Always On AG without production example
- Using Always On AG when single instance production
- No rollback plan when Always On AG misconfigured

---

## Q036: Partitioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Occasional |

### Question

What is Partitioning and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Partitioning when archive and maintenance at 100m+ rows. Avoid when small tables early partition. Production example: Monthly SWITCH partition archive.

### Detailed Answer (3–5 minutes)

**Concept:** Partitioning

**When to use:** Archive and maintenance at 100M+ rows

**When to avoid:** Small tables early partition

**Production example:** Monthly SWITCH partition archive

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Partitioning to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Partitioning with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Partitioning overkill? — Small tables early partition**
2. **How measure success after adopting Partitioning? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Partitioning without production example
- Using Partitioning when small tables early partition
- No rollback plan when Partitioning misconfigured

---

## Q037: Tempdb contention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What is Tempdb contention and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Tempdb contention when high concurrency sort and version store. Avoid when ignore tempdb sizing. Production example: Multiple tempdb files on multi-core.

### Detailed Answer (3–5 minutes)

**Concept:** Tempdb contention

**When to use:** High concurrency sort and version store

**When to avoid:** Ignore tempdb sizing

**Production example:** Multiple tempdb files on multi-core

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Tempdb contention to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Tempdb contention with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Tempdb contention overkill? — Ignore tempdb sizing**
2. **How measure success after adopting Tempdb contention? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Tempdb contention without production example
- Using Tempdb contention when ignore tempdb sizing
- No rollback plan when Tempdb contention misconfigured

---

## Q038: Deadlock prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

What is Deadlock prevention and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Deadlock prevention when ordered access and short transactions. Avoid when long transactions with http inside. Production example: Consistent table lock order in SPs.

### Detailed Answer (3–5 minutes)

**Concept:** Deadlock prevention

**When to use:** Ordered access and short transactions

**When to avoid:** Long transactions with HTTP inside

**Production example:** Consistent table lock order in SPs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Deadlock prevention to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Deadlock prevention with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Deadlock prevention overkill? — Long transactions with HTTP inside**
2. **How measure success after adopting Deadlock prevention? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Deadlock prevention without production example
- Using Deadlock prevention when long transactions with http inside
- No rollback plan when Deadlock prevention misconfigured

---

## Q039: Columnstore analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Occasional |

### Question

What is Columnstore analytics and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Columnstore analytics when large aggregation scans. Avoid when oltp point lookups. Production example: NCCI on OLTP for reporting offload.

### Detailed Answer (3–5 minutes)

**Concept:** Columnstore analytics

**When to use:** Large aggregation scans

**When to avoid:** OLTP point lookups

**Production example:** NCCI on OLTP for reporting offload

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Columnstore analytics to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Columnstore analytics with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Columnstore analytics overkill? — OLTP point lookups**
2. **How measure success after adopting Columnstore analytics? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Columnstore analytics without production example
- Using Columnstore analytics when oltp point lookups
- No rollback plan when Columnstore analytics misconfigured

---

## Q040: Connection pooling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | .NET Integration |
| **Frequency** | Very Common |

### Question

What is Connection pooling and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Connection pooling when efficient sqlconnection reuse. Avoid when pooling disabled. Production example: Scoped DbContext per request.

### Detailed Answer (3–5 minutes)

**Concept:** Connection pooling

**When to use:** Efficient SqlConnection reuse

**When to avoid:** Pooling disabled

**Production example:** Scoped DbContext per request

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Connection pooling to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Connection pooling with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Connection pooling overkill? — Pooling disabled**
2. **How measure success after adopting Connection pooling? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Connection pooling without production example
- Using Connection pooling when pooling disabled
- No rollback plan when Connection pooling misconfigured

---

## Q041: Clustered index design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Common |

### Question

What is Clustered index design and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Clustered index design when primary access path. Avoid when guid clustered pk. Production example: BIGINT sequential clustered.

### Detailed Answer (3–5 minutes)

**Concept:** Clustered index design

**When to use:** Primary access path

**When to avoid:** GUID clustered PK

**Production example:** BIGINT sequential clustered

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Clustered index design to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Clustered index design with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Clustered index design overkill? — GUID clustered PK**
2. **How measure success after adopting Clustered index design? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Clustered index design without production example
- Using Clustered index design when guid clustered pk
- No rollback plan when Clustered index design misconfigured

---

## Q042: Index include columns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Occasional |

### Question

What is Index include columns and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Index include columns when covering queries. Avoid when include everything. Production example: INCLUDE selective columns.

### Detailed Answer (3–5 minutes)

**Concept:** Index include columns

**When to use:** Covering queries

**When to avoid:** Include everything

**Production example:** INCLUDE selective columns

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Index include columns to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Index include columns with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Index include columns overkill? — Include everything**
2. **How measure success after adopting Index include columns? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Index include columns without production example
- Using Index include columns when include everything
- No rollback plan when Index include columns misconfigured

---

## Q043: Filtered index partial

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Very Common |

### Question

What is Filtered index partial and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Filtered index partial when subset index. Avoid when filtered when full fine. Production example: WHERE Status=Active filtered index.

### Detailed Answer (3–5 minutes)

**Concept:** Filtered index partial

**When to use:** Subset index

**When to avoid:** Filtered when full fine

**Production example:** WHERE Status=Active filtered index

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Filtered index partial to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Filtered index partial with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Filtered index partial overkill? — Filtered when full fine**
2. **How measure success after adopting Filtered index partial? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Filtered index partial without production example
- Using Filtered index partial when filtered when full fine
- No rollback plan when Filtered index partial misconfigured

---

## Q044: Columnstore index OLAP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

What is Columnstore index OLAP and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Columnstore index OLAP when aggregation scan. Avoid when columnstore oltp point. Production example: NCCI analytics offload.

### Detailed Answer (3–5 minutes)

**Concept:** Columnstore index OLAP

**When to use:** Aggregation scan

**When to avoid:** Columnstore OLTP point

**Production example:** NCCI analytics offload

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Columnstore index OLAP to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Columnstore index OLAP with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Columnstore index OLAP overkill? — Columnstore OLTP point**
2. **How measure success after adopting Columnstore index OLAP? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Columnstore index OLAP without production example
- Using Columnstore index OLAP when columnstore oltp point
- No rollback plan when Columnstore index OLAP misconfigured

---

## Q045: Index maintenance rebuild

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Occasional |

### Question

What is Index maintenance rebuild and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Index maintenance rebuild when fragmentation fix. Avoid when rebuild nightly all. Production example: Reorganize vs rebuild threshold.

### Detailed Answer (3–5 minutes)

**Concept:** Index maintenance rebuild

**When to use:** Fragmentation fix

**When to avoid:** Rebuild nightly all

**Production example:** Reorganize vs rebuild threshold

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Index maintenance rebuild to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Index maintenance rebuild with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Index maintenance rebuild overkill? — Rebuild nightly all**
2. **How measure success after adopting Index maintenance rebuild? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Index maintenance rebuild without production example
- Using Index maintenance rebuild when rebuild nightly all
- No rollback plan when Index maintenance rebuild misconfigured

---

## Q046: Statistics auto update

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What is Statistics auto update and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Statistics auto update when cardinality accurate. Avoid when stats never updated. Production example: AUTO_UPDATE_STATISTICS_ASYNC.

### Detailed Answer (3–5 minutes)

**Concept:** Statistics auto update

**When to use:** Cardinality accurate

**When to avoid:** Stats never updated

**Production example:** AUTO_UPDATE_STATISTICS_ASYNC

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Statistics auto update to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Statistics auto update with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Statistics auto update overkill? — Stats never updated**
2. **How measure success after adopting Statistics auto update? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Statistics auto update without production example
- Using Statistics auto update when stats never updated
- No rollback plan when Statistics auto update misconfigured

---

## Q047: Parameter sniffing fix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What is Parameter sniffing fix and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Parameter sniffing fix when plan stability. Avoid when ignore sniffing. Production example: OPTIMIZE FOR UNKNOWN or RECOMPILE.

### Detailed Answer (3–5 minutes)

**Concept:** Parameter sniffing fix

**When to use:** Plan stability

**When to avoid:** Ignore sniffing

**Production example:** OPTIMIZE FOR UNKNOWN or RECOMPILE

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Parameter sniffing fix to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Parameter sniffing fix with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Parameter sniffing fix overkill? — Ignore sniffing**
2. **How measure success after adopting Parameter sniffing fix? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Parameter sniffing fix without production example
- Using Parameter sniffing fix when ignore sniffing
- No rollback plan when Parameter sniffing fix misconfigured

---

## Q048: Plan cache bloat

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

What is Plan cache bloat and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Plan cache bloat when adhoc query cache. Avoid when plan cache ignored. Production example: Forced parameterization review.

### Detailed Answer (3–5 minutes)

**Concept:** Plan cache bloat

**When to use:** Adhoc query cache

**When to avoid:** Plan cache ignored

**Production example:** Forced parameterization review

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Plan cache bloat to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Plan cache bloat with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Plan cache bloat overkill? — Plan cache ignored**
2. **How measure success after adopting Plan cache bloat? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Plan cache bloat without production example
- Using Plan cache bloat when plan cache ignored
- No rollback plan when Plan cache bloat misconfigured

---

## Q049: Query store regression

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What is Query store regression and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Query store regression when plan regression detect. Avoid when no baseline plan. Production example: Query Store force plan cautiously.

### Detailed Answer (3–5 minutes)

**Concept:** Query store regression

**When to use:** Plan regression detect

**When to avoid:** No baseline plan

**Production example:** Query Store force plan cautiously

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Query store regression to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Query store regression with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Query store regression overkill? — No baseline plan**
2. **How measure success after adopting Query store regression? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Query store regression without production example
- Using Query store regression when no baseline plan
- No rollback plan when Query store regression misconfigured

---

## Q050: Missing index DMV

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What is Missing index DMV and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Missing index DMV when index suggestions. Avoid when blind create all dmv. Production example: DMV suggestion review.

### Detailed Answer (3–5 minutes)

**Concept:** Missing index DMV

**When to use:** Index suggestions

**When to avoid:** Blind create all DMV

**Production example:** DMV suggestion review

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Missing index DMV to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Missing index DMV with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Missing index DMV overkill? — Blind create all DMV**
2. **How measure success after adopting Missing index DMV? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Missing index DMV without production example
- Using Missing index DMV when blind create all dmv
- No rollback plan when Missing index DMV misconfigured

---

## Q051: Index usage DMV

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Occasional |

### Question

What is Index usage DMV and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Index usage DMV when drop unused indexes. Avoid when keep all indexes. Production example: sys.dm_db_index_usage_stats.

### Detailed Answer (3–5 minutes)

**Concept:** Index usage DMV

**When to use:** Drop unused indexes

**When to avoid:** Keep all indexes

**Production example:** sys.dm_db_index_usage_stats

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Index usage DMV to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Index usage DMV with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Index usage DMV overkill? — Keep all indexes**
2. **How measure success after adopting Index usage DMV? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Index usage DMV without production example
- Using Index usage DMV when keep all indexes
- No rollback plan when Index usage DMV misconfigured

---

## Q052: Lock escalation control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Very Common |

### Question

What is Lock escalation control and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Lock escalation control when row to table lock. Avoid when escalation surprises. Production example: LOCK_ESCALATION disable niche.

### Detailed Answer (3–5 minutes)

**Concept:** Lock escalation control

**When to use:** Row to table lock

**When to avoid:** Escalation surprises

**Production example:** LOCK_ESCALATION disable niche

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Lock escalation control to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Lock escalation control with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Lock escalation control overkill? — Escalation surprises**
2. **How measure success after adopting Lock escalation control? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Lock escalation control without production example
- Using Lock escalation control when escalation surprises
- No rollback plan when Lock escalation control misconfigured

---

## Q053: Row versioning RCSI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Transactions |
| **Frequency** | Common |

### Question

What is Row versioning RCSI and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Row versioning RCSI when reader writer nonblock. Avoid when rcsi without tempdb plan. Production example: READ_COMMITTED_SNAPSHOT ON.

### Detailed Answer (3–5 minutes)

**Concept:** Row versioning RCSI

**When to use:** Reader writer nonblock

**When to avoid:** RCSI without tempdb plan

**Production example:** READ_COMMITTED_SNAPSHOT ON

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Row versioning RCSI to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Row versioning RCSI with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Row versioning RCSI overkill? — RCSI without tempdb plan**
2. **How measure success after adopting Row versioning RCSI? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Row versioning RCSI without production example
- Using Row versioning RCSI when rcsi without tempdb plan
- No rollback plan when Row versioning RCSI misconfigured

---

## Q054: Snapshot isolation level

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Transactions |
| **Frequency** | Occasional |

### Question

What is Snapshot isolation level and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Snapshot isolation level when statement consistent snapshot. Avoid when snapshot for all. Production example: ALLOW_SNAPSHOT_ISOLATION selective.

### Detailed Answer (3–5 minutes)

**Concept:** Snapshot isolation level

**When to use:** Statement consistent snapshot

**When to avoid:** Snapshot for all

**Production example:** ALLOW_SNAPSHOT_ISOLATION selective

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Snapshot isolation level to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Snapshot isolation level with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Snapshot isolation level overkill? — Snapshot for all**
2. **How measure success after adopting Snapshot isolation level? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Snapshot isolation level without production example
- Using Snapshot isolation level when snapshot for all
- No rollback plan when Snapshot isolation level misconfigured

---

## Q055: Serializable range locks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

What is Serializable range locks and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Serializable range locks when phantom prevention. Avoid when serializable catalog. Production example: Transfer SP serializable.

### Detailed Answer (3–5 minutes)

**Concept:** Serializable range locks

**When to use:** Phantom prevention

**When to avoid:** Serializable catalog

**Production example:** Transfer SP serializable

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Serializable range locks to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Serializable range locks with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Serializable range locks overkill? — Serializable catalog**
2. **How measure success after adopting Serializable range locks? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Serializable range locks without production example
- Using Serializable range locks when serializable catalog
- No rollback plan when Serializable range locks misconfigured

---

## Q056: Deadlock graph analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

What is Deadlock graph analysis and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Deadlock graph analysis when deadlock root cause. Avoid when retry forever no fix. Production example: Extended events deadlock graph.

### Detailed Answer (3–5 minutes)

**Concept:** Deadlock graph analysis

**When to use:** Deadlock root cause

**When to avoid:** Retry forever no fix

**Production example:** Extended events deadlock graph

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Deadlock graph analysis to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Deadlock graph analysis with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Deadlock graph analysis overkill? — Retry forever no fix**
2. **How measure success after adopting Deadlock graph analysis? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Deadlock graph analysis without production example
- Using Deadlock graph analysis when retry forever no fix
- No rollback plan when Deadlock graph analysis misconfigured

---

## Q057: Blocking chain analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Occasional |

### Question

What is Blocking chain analysis and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Blocking chain analysis when who blocks whom. Avoid when kill blocker always. Production example: sp_whoisactive blocking.

### Detailed Answer (3–5 minutes)

**Concept:** Blocking chain analysis

**When to use:** Who blocks whom

**When to avoid:** Kill blocker always

**Production example:** sp_whoisactive blocking

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Blocking chain analysis to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Blocking chain analysis with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Blocking chain analysis overkill? — Kill blocker always**
2. **How measure success after adopting Blocking chain analysis? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Blocking chain analysis without production example
- Using Blocking chain analysis when kill blocker always
- No rollback plan when Blocking chain analysis misconfigured

---

## Q058: Optimistic concurrency rowversion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Very Common |

### Question

What is Optimistic concurrency rowversion and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Optimistic concurrency rowversion when ef rowversion. Avoid when last write wins money. Production example: RowVersion column EF.

### Detailed Answer (3–5 minutes)

**Concept:** Optimistic concurrency rowversion

**When to use:** EF rowversion

**When to avoid:** Last write wins money

**Production example:** RowVersion column EF

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Optimistic concurrency rowversion to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Optimistic concurrency rowversion with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Optimistic concurrency rowversion overkill? — Last write wins money**
2. **How measure success after adopting Optimistic concurrency rowversion? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Optimistic concurrency rowversion without production example
- Using Optimistic concurrency rowversion when last write wins money
- No rollback plan when Optimistic concurrency rowversion misconfigured

---

## Q059: Application lock sp_getapplock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

What is Application lock sp_getapplock and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Application lock sp_getapplock when app level mutex. Avoid when applock everything. Production example: Batch job applock.

### Detailed Answer (3–5 minutes)

**Concept:** Application lock sp_getapplock

**When to use:** App level mutex

**When to avoid:** Applock everything

**Production example:** Batch job applock

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Application lock sp_getapplock to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Application lock sp_getapplock with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Application lock sp_getapplock overkill? — Applock everything**
2. **How measure success after adopting Application lock sp_getapplock? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Application lock sp_getapplock without production example
- Using Application lock sp_getapplock when applock everything
- No rollback plan when Application lock sp_getapplock misconfigured

---

## Q060: Sequence vs identity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design |
| **Frequency** | Occasional |

### Question

What is Sequence vs identity and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Sequence vs identity when distributed id gen. Avoid when identity scale out. Production example: SEQUENCE gap cache.

### Detailed Answer (3–5 minutes)

**Concept:** Sequence vs identity

**When to use:** Distributed id gen

**When to avoid:** Identity scale out

**Production example:** SEQUENCE gap cache

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Sequence vs identity to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Sequence vs identity with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Sequence vs identity overkill? — Identity scale out**
2. **How measure success after adopting Sequence vs identity? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Sequence vs identity without production example
- Using Sequence vs identity when identity scale out
- No rollback plan when Sequence vs identity misconfigured

---

## Q061: Temporal tables system

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Features |
| **Frequency** | Very Common |

### Question

What is Temporal tables system and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Temporal tables system when audit history. Avoid when temporal for all tables. Production example: SYSTEM_VERSIONING orders.

### Detailed Answer (3–5 minutes)

**Concept:** Temporal tables system

**When to use:** Audit history

**When to avoid:** Temporal for all tables

**Production example:** SYSTEM_VERSIONING orders

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Temporal tables system to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Temporal tables system with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Temporal tables system overkill? — Temporal for all tables**
2. **How measure success after adopting Temporal tables system? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Temporal tables system without production example
- Using Temporal tables system when temporal for all tables
- No rollback plan when Temporal tables system misconfigured

---

## Q062: Change data capture CDC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

What is Change data capture CDC and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Change data capture CDC when change stream sql. Avoid when cdc instead of events. Production example: CDC to event hub.

### Detailed Answer (3–5 minutes)

**Concept:** Change data capture CDC

**When to use:** Change stream SQL

**When to avoid:** CDC instead of events

**Production example:** CDC to event hub

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Change data capture CDC to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Change data capture CDC with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Change data capture CDC overkill? — CDC instead of events**
2. **How measure success after adopting Change data capture CDC? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Change data capture CDC without production example
- Using Change data capture CDC when cdc instead of events
- No rollback plan when Change data capture CDC misconfigured

---

## Q063: Change tracking lightweight

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Occasional |

### Question

What is Change tracking lightweight and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Change tracking lightweight when sync lightweight. Avoid when ct heavy analytics. Production example: CT mobile sync.

### Detailed Answer (3–5 minutes)

**Concept:** Change tracking lightweight

**When to use:** Sync lightweight

**When to avoid:** CT heavy analytics

**Production example:** CT mobile sync

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Change tracking lightweight to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Change tracking lightweight with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Change tracking lightweight overkill? — CT heavy analytics**
2. **How measure success after adopting Change tracking lightweight? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Change tracking lightweight without production example
- Using Change tracking lightweight when ct heavy analytics
- No rollback plan when Change tracking lightweight misconfigured

---

## Q064: Service broker async

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

What is Service broker async and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Service broker async when in-sql async. Avoid when service broker new apps. Production example: Legacy broker pattern.

### Detailed Answer (3–5 minutes)

**Concept:** Service broker async

**When to use:** In-SQL async

**When to avoid:** Service broker new apps

**Production example:** Legacy broker pattern

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Service broker async to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Service broker async with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Service broker async overkill? — Service broker new apps**
2. **How measure success after adopting Service broker async? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Service broker async without production example
- Using Service broker async when service broker new apps
- No rollback plan when Service broker async misconfigured

---

## Q065: Linked server security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

What is Linked server security and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Linked server security when cross server query. Avoid when linked server default. Production example: Pass-through auth review.

### Detailed Answer (3–5 minutes)

**Concept:** Linked server security

**When to use:** Cross server query

**When to avoid:** Linked server default

**Production example:** Pass-through auth review

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Linked server security to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Linked server security with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Linked server security overkill? — Linked server default**
2. **How measure success after adopting Linked server security? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Linked server security without production example
- Using Linked server security when linked server default
- No rollback plan when Linked server security misconfigured

---

## Q066: OpenQuery distributed

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Occasional |

### Question

What is OpenQuery distributed and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use OpenQuery distributed when remote query. Avoid when openquery injection. Production example: Parameterized openquery caution.

### Detailed Answer (3–5 minutes)

**Concept:** OpenQuery distributed

**When to use:** Remote query

**When to avoid:** OpenQuery injection

**Production example:** Parameterized openquery caution

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect OpenQuery distributed to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify OpenQuery distributed with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is OpenQuery distributed overkill? — OpenQuery injection**
2. **How measure success after adopting OpenQuery distributed? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting OpenQuery distributed without production example
- Using OpenQuery distributed when openquery injection
- No rollback plan when OpenQuery distributed misconfigured

---

## Q067: PolyBase external data

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

What is PolyBase external data and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use PolyBase external data when data lake query. Avoid when polybase oltp. Production example: PolyBase parquet lake.

### Detailed Answer (3–5 minutes)

**Concept:** PolyBase external data

**When to use:** Data lake query

**When to avoid:** PolyBase OLTP

**Production example:** PolyBase parquet lake

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect PolyBase external data to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify PolyBase external data with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is PolyBase external data overkill? — PolyBase OLTP**
2. **How measure success after adopting PolyBase external data? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting PolyBase external data without production example
- Using PolyBase external data when polybase oltp
- No rollback plan when PolyBase external data misconfigured

---

## Q068: Stretch database archive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Common |

### Question

What is Stretch database archive and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Stretch database archive when cold row archive. Avoid when stretch primary workload. Production example: Stretch archive policy.

### Detailed Answer (3–5 minutes)

**Concept:** Stretch database archive

**When to use:** Cold row archive

**When to avoid:** Stretch primary workload

**Production example:** Stretch archive policy

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Stretch database archive to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Stretch database archive with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Stretch database archive overkill? — Stretch primary workload**
2. **How measure success after adopting Stretch database archive? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Stretch database archive without production example
- Using Stretch database archive when stretch primary workload
- No rollback plan when Stretch database archive misconfigured

---

## Q069: In-memory OLTP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

What is In-memory OLTP and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use In-memory OLTP when latch free hot tables. Avoid when in-memory everything. Production example: Memory optimized table niche.

### Detailed Answer (3–5 minutes)

**Concept:** In-memory OLTP

**When to use:** Latch free hot tables

**When to avoid:** In-memory everything

**Production example:** Memory optimized table niche

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect In-memory OLTP to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify In-memory OLTP with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is In-memory OLTP overkill? — In-memory everything**
2. **How measure success after adopting In-memory OLTP? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting In-memory OLTP without production example
- Using In-memory OLTP when in-memory everything
- No rollback plan when In-memory OLTP misconfigured

---

## Q070: Natively compiled SP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What is Natively compiled SP and when would you apply it in SQL Server Architecture?

### Short Answer (30 seconds)

Use Natively compiled SP when in-memory sp. Avoid when natively compiled all. Production example: Nat compiled hot path.

### Detailed Answer (3–5 minutes)

**Concept:** Natively compiled SP

**When to use:** In-memory SP

**When to avoid:** Natively compiled all

**Production example:** Nat compiled hot path

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Natively compiled SP to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Natively compiled SP with production trade-offs in SQL Server Architecture.

### Follow-up Questions

1. **When is Natively compiled SP overkill? — Natively compiled all**
2. **How measure success after adopting Natively compiled SP? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Natively compiled SP without production example
- Using Natively compiled SP when natively compiled all
- No rollback plan when Natively compiled SP misconfigured

---
