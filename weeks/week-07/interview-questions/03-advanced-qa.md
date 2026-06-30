# Week 07 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Columnstore batch mode — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Columnstore batch mode at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Columnstore batch mode trades vectorized execution against operational complexity. Primary failure mode: batch mode rowstore.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Columnstore batch mode:**

**Strengths at scale:** Vectorized execution

**Failure modes:**
- Misapplication when batch mode rowstore
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Batch mode columnstore

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Columnstore batch mode if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Columnstore batch mode — not just defined it.

### Follow-up Questions

1. **What monitoring proves Columnstore batch mode healthy? — SLI tied to batch mode columnstore.**
2. **When would you remove or replace Columnstore batch mode? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Columnstore batch mode as set-and-forget
- No load test before enabling Columnstore batch mode in production
- Ignoring cost/ops overhead of Columnstore batch mode

---

## Q072: Batch mode on rowstore — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Batch mode on rowstore at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Batch mode on rowstore trades rowstore batch against operational complexity. Primary failure mode: expect batch always.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Batch mode on rowstore:**

**Strengths at scale:** Rowstore batch

**Failure modes:**
- Misapplication when expect batch always
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Batch mode eligibility

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Batch mode on rowstore if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Batch mode on rowstore — not just defined it.

### Follow-up Questions

1. **What monitoring proves Batch mode on rowstore healthy? — SLI tied to batch mode eligibility.**
2. **When would you remove or replace Batch mode on rowstore? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Batch mode on rowstore as set-and-forget
- No load test before enabling Batch mode on rowstore in production
- Ignoring cost/ops overhead of Batch mode on rowstore

---

## Q073: Intelligent query processing — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Intelligent query processing at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Intelligent query processing trades adaptive joins memory against operational complexity. Primary failure mode: disable iqp.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Intelligent query processing:**

**Strengths at scale:** Adaptive joins memory

**Failure modes:**
- Misapplication when disable iqp
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Adaptive query processing

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Intelligent query processing if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Intelligent query processing — not just defined it.

### Follow-up Questions

1. **What monitoring proves Intelligent query processing healthy? — SLI tied to adaptive query processing.**
2. **When would you remove or replace Intelligent query processing? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Intelligent query processing as set-and-forget
- No load test before enabling Intelligent query processing in production
- Ignoring cost/ops overhead of Intelligent query processing

---

## Q074: Memory grant feedback — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Memory grant feedback at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Memory grant feedback trades spill prevention against operational complexity. Primary failure mode: ignore spills.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Memory grant feedback:**

**Strengths at scale:** Spill prevention

**Failure modes:**
- Misapplication when ignore spills
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Memory grant feedback adaptive

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Memory grant feedback if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Memory grant feedback — not just defined it.

### Follow-up Questions

1. **What monitoring proves Memory grant feedback healthy? — SLI tied to memory grant feedback adaptive.**
2. **When would you remove or replace Memory grant feedback? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Memory grant feedback as set-and-forget
- No load test before enabling Memory grant feedback in production
- Ignoring cost/ops overhead of Memory grant feedback

---

## Q075: Interleaved execution — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Interleaved execution at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Interleaved execution trades tvf row estimate against operational complexity. Primary failure mode: multi statement tvf.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Interleaved execution:**

**Strengths at scale:** TVF row estimate

**Failure modes:**
- Misapplication when multi statement tvf
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Inline TVF prefer

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Interleaved execution if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Interleaved execution — not just defined it.

### Follow-up Questions

1. **What monitoring proves Interleaved execution healthy? — SLI tied to inline tvf prefer.**
2. **When would you remove or replace Interleaved execution? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Interleaved execution as set-and-forget
- No load test before enabling Interleaved execution in production
- Ignoring cost/ops overhead of Interleaved execution

---

## Q076: Scalar UDF inline — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Scalar UDF inline at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Scalar UDF inline trades udf performance against operational complexity. Primary failure mode: scalar udf hot path.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Scalar UDF inline:**

**Strengths at scale:** UDF performance

**Failure modes:**
- Misapplication when scalar udf hot path
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Inline UDF SQL 2019

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Scalar UDF inline if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Scalar UDF inline — not just defined it.

### Follow-up Questions

1. **What monitoring proves Scalar UDF inline healthy? — SLI tied to inline udf sql 2019.**
2. **When would you remove or replace Scalar UDF inline? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Scalar UDF inline as set-and-forget
- No load test before enabling Scalar UDF inline in production
- Ignoring cost/ops overhead of Scalar UDF inline

---

## Q077: Tempdb optimization — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Tempdb optimization at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Tempdb optimization trades contention pfs gam sgam against operational complexity. Primary failure mode: one tempdb file.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Tempdb optimization:**

**Strengths at scale:** Contention PFS GAM SGAM

**Failure modes:**
- Misapplication when one tempdb file
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Multiple tempdb data files

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Tempdb optimization if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Tempdb optimization — not just defined it.

### Follow-up Questions

1. **What monitoring proves Tempdb optimization healthy? — SLI tied to multiple tempdb data files.**
2. **When would you remove or replace Tempdb optimization? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Tempdb optimization as set-and-forget
- No load test before enabling Tempdb optimization in production
- Ignoring cost/ops overhead of Tempdb optimization

---

## Q078: Tempdb version store — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Transactions |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Tempdb version store at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Tempdb version store trades rcsi snapshot cleanup against operational complexity. Primary failure mode: version store unmonitored.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Tempdb version store:**

**Strengths at scale:** RCSI snapshot cleanup

**Failure modes:**
- Misapplication when version store unmonitored
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Version store size alert

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Tempdb version store if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Tempdb version store — not just defined it.

### Follow-up Questions

1. **What monitoring proves Tempdb version store healthy? — SLI tied to version store size alert.**
2. **When would you remove or replace Tempdb version store? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Tempdb version store as set-and-forget
- No load test before enabling Tempdb version store in production
- Ignoring cost/ops overhead of Tempdb version store

---

## Q079: Filegroup strategy — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Design |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Filegroup strategy at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Filegroup strategy trades partition filegroups against operational complexity. Primary failure mode: single filegroup all.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Filegroup strategy:**

**Strengths at scale:** Partition filegroups

**Failure modes:**
- Misapplication when single filegroup all
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** DATA filegroup ARCHIVE separate

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Filegroup strategy if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Filegroup strategy — not just defined it.

### Follow-up Questions

1. **What monitoring proves Filegroup strategy healthy? — SLI tied to data filegroup archive separate.**
2. **When would you remove or replace Filegroup strategy? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Filegroup strategy as set-and-forget
- No load test before enabling Filegroup strategy in production
- Ignoring cost/ops overhead of Filegroup strategy

---

## Q080: Partition function scheme — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Partition function scheme at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Partition function scheme trades partition key choice against operational complexity. Primary failure mode: partition small table.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Partition function scheme:**

**Strengths at scale:** Partition key choice

**Failure modes:**
- Misapplication when partition small table
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Monthly partition function

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Partition function scheme if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Partition function scheme — not just defined it.

### Follow-up Questions

1. **What monitoring proves Partition function scheme healthy? — SLI tied to monthly partition function.**
2. **When would you remove or replace Partition function scheme? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Partition function scheme as set-and-forget
- No load test before enabling Partition function scheme in production
- Ignoring cost/ops overhead of Partition function scheme

---

## Q081: Partition elimination — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Partition elimination at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Partition elimination trades query prune partitions against operational complexity. Primary failure mode: scan all partitions.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Partition elimination:**

**Strengths at scale:** Query prune partitions

**Failure modes:**
- Misapplication when scan all partitions
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** WHERE on partition key

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Partition elimination if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Partition elimination — not just defined it.

### Follow-up Questions

1. **What monitoring proves Partition elimination healthy? — SLI tied to where on partition key.**
2. **When would you remove or replace Partition elimination? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Partition elimination as set-and-forget
- No load test before enabling Partition elimination in production
- Ignoring cost/ops overhead of Partition elimination

---

## Q082: Sliding window partition — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Sliding window partition at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Sliding window partition trades archive maintenance against operational complexity. Primary failure mode: delete millions archive.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Sliding window partition:**

**Strengths at scale:** Archive maintenance

**Failure modes:**
- Misapplication when delete millions archive
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** SWITCH partition archive

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Sliding window partition if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Sliding window partition — not just defined it.

### Follow-up Questions

1. **What monitoring proves Sliding window partition healthy? — SLI tied to switch partition archive.**
2. **When would you remove or replace Sliding window partition? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Sliding window partition as set-and-forget
- No load test before enabling Sliding window partition in production
- Ignoring cost/ops overhead of Sliding window partition

---

## Q083: Compression row page — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Compression row page at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Compression row page trades storage save against operational complexity. Primary failure mode: compress oltp hot.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Compression row page:**

**Strengths at scale:** Storage save

**Failure modes:**
- Misapplication when compress oltp hot
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** PAGE compression archive

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Compression row page if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Compression row page — not just defined it.

### Follow-up Questions

1. **What monitoring proves Compression row page healthy? — SLI tied to page compression archive.**
2. **When would you remove or replace Compression row page? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Compression row page as set-and-forget
- No load test before enabling Compression row page in production
- Ignoring cost/ops overhead of Compression row page

---

## Q084: Backup strategy full diff log — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Backup strategy full diff log at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Backup strategy full diff log trades rpo rto backup against operational complexity. Primary failure mode: full only huge db.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Backup strategy full diff log:**

**Strengths at scale:** RPO RTO backup

**Failure modes:**
- Misapplication when full only huge db
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Full weekly diff daily log 15min

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Backup strategy full diff log if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Backup strategy full diff log — not just defined it.

### Follow-up Questions

1. **What monitoring proves Backup strategy full diff log healthy? — SLI tied to full weekly diff daily log 15min.**
2. **When would you remove or replace Backup strategy full diff log? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Backup strategy full diff log as set-and-forget
- No load test before enabling Backup strategy full diff log in production
- Ignoring cost/ops overhead of Backup strategy full diff log

---

## Q085: Tail log backup — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Tail log backup at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Tail log backup trades recover to point against operational complexity. Primary failure mode: no tail log plan.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Tail log backup:**

**Strengths at scale:** Recover to point

**Failure modes:**
- Misapplication when no tail log plan
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Tail log before migration

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Tail log backup if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Tail log backup — not just defined it.

### Follow-up Questions

1. **What monitoring proves Tail log backup healthy? — SLI tied to tail log before migration.**
2. **When would you remove or replace Tail log backup? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Tail log backup as set-and-forget
- No load test before enabling Tail log backup in production
- Ignoring cost/ops overhead of Tail log backup

---

## Q086: Piecemeal restore — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Piecemeal restore at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Piecemeal restore trades large db restore against operational complexity. Primary failure mode: full restore only.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Piecemeal restore:**

**Strengths at scale:** Large DB restore

**Failure modes:**
- Misapplication when full restore only
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Piecemeal filegroup restore

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Piecemeal restore if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Piecemeal restore — not just defined it.

### Follow-up Questions

1. **What monitoring proves Piecemeal restore healthy? — SLI tied to piecemeal filegroup restore.**
2. **When would you remove or replace Piecemeal restore? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Piecemeal restore as set-and-forget
- No load test before enabling Piecemeal restore in production
- Ignoring cost/ops overhead of Piecemeal restore

---

## Q087: Instant file initialization — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Instant file initialization at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Instant file initialization trades fast data file growth against operational complexity. Primary failure mode: ifi off slow growth.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Instant file initialization:**

**Strengths at scale:** Fast data file growth

**Failure modes:**
- Misapplication when ifi off slow growth
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** IFI service account privilege

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Instant file initialization if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Instant file initialization — not just defined it.

### Follow-up Questions

1. **What monitoring proves Instant file initialization healthy? — SLI tied to ifi service account privilege.**
2. **When would you remove or replace Instant file initialization? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Instant file initialization as set-and-forget
- No load test before enabling Instant file initialization in production
- Ignoring cost/ops overhead of Instant file initialization

---

## Q088: VLF count transaction log — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of VLF count transaction log at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, VLF count transaction log trades log performance against operational complexity. Primary failure mode: tiny log growth repeats.

### Detailed Answer (3–5 minutes)

**Advanced analysis of VLF count transaction log:**

**Strengths at scale:** Log performance

**Failure modes:**
- Misapplication when tiny log growth repeats
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** VLF count reasonable growth

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose VLF count transaction log if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated VLF count transaction log — not just defined it.

### Follow-up Questions

1. **What monitoring proves VLF count transaction log healthy? — SLI tied to vlf count reasonable growth.**
2. **When would you remove or replace VLF count transaction log? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating VLF count transaction log as set-and-forget
- No load test before enabling VLF count transaction log in production
- Ignoring cost/ops overhead of VLF count transaction log

---

## Q089: Log reuse wait status — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Log reuse wait status at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Log reuse wait status trades log full diagnose against operational complexity. Primary failure mode: shrink log only fix.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Log reuse wait status:**

**Strengths at scale:** Log full diagnose

**Failure modes:**
- Misapplication when shrink log only fix
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** DBCC LOGINFO VLF reuse

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Log reuse wait status if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Log reuse wait status — not just defined it.

### Follow-up Questions

1. **What monitoring proves Log reuse wait status healthy? — SLI tied to dbcc loginfo vlf reuse.**
2. **When would you remove or replace Log reuse wait status? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Log reuse wait status as set-and-forget
- No load test before enabling Log reuse wait status in production
- Ignoring cost/ops overhead of Log reuse wait status

---

## Q090: Always On readable secondary — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HA/DR |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Always On readable secondary at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Always On readable secondary trades read offload against operational complexity. Primary failure mode: stale read ignored.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Always On readable secondary:**

**Strengths at scale:** Read offload

**Failure modes:**
- Misapplication when stale read ignored
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** ApplicationIntent ReadOnly

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Always On readable secondary if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Always On readable secondary — not just defined it.

### Follow-up Questions

1. **What monitoring proves Always On readable secondary healthy? — SLI tied to applicationintent readonly.**
2. **When would you remove or replace Always On readable secondary? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Always On readable secondary as set-and-forget
- No load test before enabling Always On readable secondary in production
- Ignoring cost/ops overhead of Always On readable secondary

---

## Q091: Availability group listener — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Availability group listener at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Availability group listener trades failover connection against operational complexity. Primary failure mode: connect primary name.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Availability group listener:**

**Strengths at scale:** Failover connection

**Failure modes:**
- Misapplication when connect primary name
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Listener MultiSubnetFailover

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Availability group listener if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Availability group listener — not just defined it.

### Follow-up Questions

1. **What monitoring proves Availability group listener healthy? — SLI tied to listener multisubnetfailover.**
2. **When would you remove or replace Availability group listener? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Availability group listener as set-and-forget
- No load test before enabling Availability group listener in production
- Ignoring cost/ops overhead of Availability group listener

---

## Q092: Distributed AG — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HA/DR |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Distributed AG at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Distributed AG trades geo dr chain against operational complexity. Primary failure mode: distributed ag complexity.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Distributed AG:**

**Strengths at scale:** Geo DR chain

**Failure modes:**
- Misapplication when distributed ag complexity
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Cross-region distributed AG

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Distributed AG if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Distributed AG — not just defined it.

### Follow-up Questions

1. **What monitoring proves Distributed AG healthy? — SLI tied to cross-region distributed ag.**
2. **When would you remove or replace Distributed AG? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Distributed AG as set-and-forget
- No load test before enabling Distributed AG in production
- Ignoring cost/ops overhead of Distributed AG

---

## Q093: Failover cluster instance — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Failover cluster instance at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Failover cluster instance trades shared storage ha against operational complexity. Primary failure mode: fci vs ag choice.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Failover cluster instance:**

**Strengths at scale:** Shared storage HA

**Failure modes:**
- Misapplication when fci vs ag choice
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** FCI SQL legacy

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Failover cluster instance if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Failover cluster instance — not just defined it.

### Follow-up Questions

1. **What monitoring proves Failover cluster instance healthy? — SLI tied to fci sql legacy.**
2. **When would you remove or replace Failover cluster instance? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Failover cluster instance as set-and-forget
- No load test before enabling Failover cluster instance in production
- Ignoring cost/ops overhead of Failover cluster instance

---

## Q094: Log shipping DR — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HA/DR |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Log shipping DR at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Log shipping DR trades simple dr against operational complexity. Primary failure mode: log shipping ha primary.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Log shipping DR:**

**Strengths at scale:** Simple DR

**Failure modes:**
- Misapplication when log shipping ha primary
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Log shipping warm standby

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Log shipping DR if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Log shipping DR — not just defined it.

### Follow-up Questions

1. **What monitoring proves Log shipping DR healthy? — SLI tied to log shipping warm standby.**
2. **When would you remove or replace Log shipping DR? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Log shipping DR as set-and-forget
- No load test before enabling Log shipping DR in production
- Ignoring cost/ops overhead of Log shipping DR

---

## Q095: Database mirroring legacy — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Database mirroring legacy at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Database mirroring legacy trades legacy mirror against operational complexity. Primary failure mode: mirror new deploy.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Database mirroring legacy:**

**Strengths at scale:** Legacy mirror

**Failure modes:**
- Misapplication when mirror new deploy
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** AG replaces mirroring

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Database mirroring legacy if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Database mirroring legacy — not just defined it.

### Follow-up Questions

1. **What monitoring proves Database mirroring legacy healthy? — SLI tied to ag replaces mirroring.**
2. **When would you remove or replace Database mirroring legacy? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Database mirroring legacy as set-and-forget
- No load test before enabling Database mirroring legacy in production
- Ignoring cost/ops overhead of Database mirroring legacy

---

## Q096: Replication transactional — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Replication transactional at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Replication transactional trades publisher subscriber against operational complexity. Primary failure mode: replication instead of cdc.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Replication transactional:**

**Strengths at scale:** Publisher subscriber

**Failure modes:**
- Misapplication when replication instead of cdc
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Transactional replication reporting

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Replication transactional if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Replication transactional — not just defined it.

### Follow-up Questions

1. **What monitoring proves Replication transactional healthy? — SLI tied to transactional replication reporting.**
2. **When would you remove or replace Replication transactional? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Replication transactional as set-and-forget
- No load test before enabling Replication transactional in production
- Ignoring cost/ops overhead of Replication transactional

---

## Q097: Merge replication legacy — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Merge replication legacy at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Merge replication legacy trades bi-directional sync against operational complexity. Primary failure mode: merge new design.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Merge replication legacy:**

**Strengths at scale:** Bi-directional sync

**Failure modes:**
- Misapplication when merge new design
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Legacy merge mobile

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Merge replication legacy if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Merge replication legacy — not just defined it.

### Follow-up Questions

1. **What monitoring proves Merge replication legacy healthy? — SLI tied to legacy merge mobile.**
2. **When would you remove or replace Merge replication legacy? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Merge replication legacy as set-and-forget
- No load test before enabling Merge replication legacy in production
- Ignoring cost/ops overhead of Merge replication legacy

---

## Q098: Snapshot replication — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Snapshot replication at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Snapshot replication trades initial sync against operational complexity. Primary failure mode: snapshot continuous.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Snapshot replication:**

**Strengths at scale:** Initial sync

**Failure modes:**
- Misapplication when snapshot continuous
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Snapshot once then transactional

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Snapshot replication if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Snapshot replication — not just defined it.

### Follow-up Questions

1. **What monitoring proves Snapshot replication healthy? — SLI tied to snapshot once then transactional.**
2. **When would you remove or replace Snapshot replication? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Snapshot replication as set-and-forget
- No load test before enabling Snapshot replication in production
- Ignoring cost/ops overhead of Snapshot replication

---

## Q099: Peer to peer replication — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Peer to peer replication at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Peer to peer replication trades multi master against operational complexity. Primary failure mode: p2p conflict ignore.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Peer to peer replication:**

**Strengths at scale:** Multi master

**Failure modes:**
- Misapplication when p2p conflict ignore
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** P2P write conflict handling

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Peer to peer replication if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Peer to peer replication — not just defined it.

### Follow-up Questions

1. **What monitoring proves Peer to peer replication healthy? — SLI tied to p2p write conflict handling.**
2. **When would you remove or replace Peer to peer replication? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Peer to peer replication as set-and-forget
- No load test before enabling Peer to peer replication in production
- Ignoring cost/ops overhead of Peer to peer replication

---

## Q100: Contained database users — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Contained database users at scale in SQL Server Architecture?

### Short Answer (30 seconds)

At scale, Contained database users trades portability auth against operational complexity. Primary failure mode: contained always.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Contained database users:**

**Strengths at scale:** Portability auth

**Failure modes:**
- Misapplication when contained always
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Contained user AAD

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Contained database users if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Contained database users — not just defined it.

### Follow-up Questions

1. **What monitoring proves Contained database users healthy? — SLI tied to contained user aad.**
2. **When would you remove or replace Contained database users? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Contained database users as set-and-forget
- No load test before enabling Contained database users in production
- Ignoring cost/ops overhead of Contained database users

---
