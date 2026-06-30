# Azure Data Platform — Advanced

> **Week 11** | **Level:** Advanced

## Multi-Region Data Architecture

- **SQL:** Active geo-replication (readable secondaries) vs failover groups (RPO ~5s)
- **Cosmos:** Multi-region writes with session consistency for most apps
- **Synapse:** Separate compute pools for ETL vs ad-hoc analytics

## RU/s Sizing and Cost Control

- Start with autoscale max RU; monitor 429 throttling
- Serverless for dev/spiky; provisioned for predictable production
- Partition merge/split planning before 20GB per partition limit

## Architect Scenario

Design data layer for multi-tenant SaaS: 500 tenants, 10K TPS reads, 500 TPS writes.

**Deliverables:** ER diagram, partition strategy, DR RPO/RTO, cost estimate order of magnitude.

## Architect Deep Dive: Data Residency & Scale

### Geo-replication patterns
- **Active geo-replication** (SQL) — readable secondaries, manual failover
- **Cosmos multi-region writes** — trade-off: eventual consistency across regions
- **Blob GRS/RA-GRS** — DR for static assets

### Data migration at scale
Use Azure Database Migration Service or staged bulk copy — never "big bang" cutover without parallel run validation and row-count reconciliation.

