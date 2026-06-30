# Week 08 — Exercises

> Theory: [theory/](../theory/README.md) · Lab: [lab-08-postgresql-docker](../labs/lab-08-postgresql-docker.md) · Interview: [interview-questions/](../interview-questions/README.md)

## Exercise 1: JSONB Schema Design (60 min)

A product catalog needs flexible attributes (color, size, specs) without 50 nullable columns.

**Tasks:**
1. Design a hybrid schema: fixed columns + `attributes JSONB`
2. Write indexes: GIN on `attributes`, expression index on `(attributes->>'brand')`
3. Compare JSONB vs EAV table — query ergonomics and indexability

**Deliverable:** `CREATE TABLE` DDL + sample queries. Extend [lab-08](../labs/lab-08-postgresql-docker.md).

---

## Exercise 2: MVCC & Vacuum Tuning Scenario (45 min)

A `events` table (500M rows) has 40% dead tuples. Autovacuum lags; queries slow down; disk grows.

**Tasks:**
1. Explain why dead tuples accumulate (long transactions, bulk updates)
2. Recommend `autovacuum_vacuum_scale_factor`, `autovacuum_vacuum_cost_delay` changes
3. Decide when to run `VACUUM FULL` vs routine autovacuum

**Deliverable:** Before/after config table + monitoring queries (`pg_stat_user_tables`). See [theory/](../theory/README.md).

---

## Exercise 3: Replication Lag Handling (45 min)

PostgreSQL primary in `eastus`, read replica in `westus`. Replica lag spikes to 45s during batch ETL.

**Tasks:**
1. Draw streaming replication flow
2. Define app strategies: stale-read tolerance, read-your-writes routing, lag circuit breaker
3. Choose which endpoints hit primary vs replica for an e-commerce app

**Deliverable:** Routing decision table (endpoint → primary/replica + fallback). Reference [diagrams/](../diagrams/README.md).

---

## Exercise 4: Migration from SQL Server Plan (60 min)

Migrate a 200 GB SQL Server OLTP database to PostgreSQL. 15 tables, 40 stored procedures, SSIS nightly ETL.

**Tasks:**
1. Phase the migration: schema, data, procedures, cutover
2. Map T-SQL constructs: `IDENTITY` → `SERIAL`/`GENERATED`, `MERGE`, `TRY/CATCH`
3. Define rollback criteria and parallel-run validation strategy

**Deliverable:** Migration timeline (4 phases) + risk register (top 5 risks). Use [templates/adr-template.md](../../../templates/adr-template.md) for cutover decision.

---

## Exercise 5: Interview Drill (30 min)

Practice aloud from [01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md):

1. Q001 (PostgreSQL vs SQL Server)
2. Q005 (JSONB for Schema Flexibility)
3. Q010 (CAP and Postgres HA)

Target: give polyglot persistence examples (when Postgres + SQL Server coexist). Score 12+/15.

---

[← Back to Week 08](../README.md)
