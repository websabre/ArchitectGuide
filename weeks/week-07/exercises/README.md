# Week 07 — Exercises

> Theory: [theory/](../theory/README.md) · Lab: [lab-07-sql-indexing](../labs/lab-07-sql-indexing.md) · Interview: [interview-questions/](../interview-questions/README.md)

## Exercise 1: Index Design for Slow Query (60 min)

This query runs 400ms on a 50M-row `Orders` table:

```sql
SELECT o.OrderId, o.Total, c.CompanyName
FROM Orders o
JOIN Customers c ON o.CustomerId = c.CustomerId
WHERE o.Status = 'Shipped'
  AND o.OrderDate >= '2025-01-01'
ORDER BY o.OrderDate DESC;
```

**Tasks:**
1. Propose clustered vs non-clustered index strategy
2. Write `CREATE INDEX` statements with included columns
3. Predict index seek vs scan from the WHERE/ORDER BY shape

**Deliverable:** Index DDL + estimated improvement rationale. Compare with [lab-07](../labs/lab-07-sql-indexing.md).

---

## Exercise 2: Execution Plan Reading (45 min)

Given a plan showing: **Table Scan** on `Orders`, **Nested Loops** join, **Key Lookup** on `Customers`, **Sort** operator (cost 78%):

**Tasks:**
1. Identify the most expensive operator and why
2. List three changes that would eliminate the sort
3. Explain when a hash join would replace nested loops

**Deliverable:** Annotated plan screenshot (or text plan) with rewrite suggestions. See [theory/](../theory/README.md).

---

## Exercise 3: Isolation Level Scenario (30 min)

Two concurrent transactions on the same inventory row:

- **T1:** `READ COMMITTED` — reads qty=10, decides to ship 8
- **T2:** `REPEATABLE READ` — reads qty=10, updates to qty=2

**Tasks:**
1. Describe lost update, dirty read, phantom read for this scenario
2. Choose the minimum isolation level to prevent overselling
3. Propose optimistic concurrency (`ROWVERSION`) as an alternative

**Deliverable:** Timeline diagram of both transactions + recommended isolation level with justification.

---

## Exercise 4: Always On Failover Design (45 min)

Design HA for an Order DB: RPO 30s, RTO 2min, one synchronous replica in same region, one async in DR region.

**Tasks:**
1. Draw AG topology (primary, sync secondary, async DR)
2. Define failover policy: automatic vs manual — when to choose each
3. List application connection string changes (read-only routing, multi-subnet)

**Deliverable:** Architecture diagram + failover runbook outline (5 steps). Reference [diagrams/](../diagrams/README.md).

---

## Exercise 5: Interview Drill (30 min)

Answer aloud from [01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md):

1. Q001 (Clustered vs Non-Clustered Index)
2. Q005 (Always On Availability Groups)
3. Q010 (SQL Server vs Azure SQL Decision)

Target: cite one production tuning example per answer. Score 12+/15.

---

[← Back to Week 07](../README.md)
