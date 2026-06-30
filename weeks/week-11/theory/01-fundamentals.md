# Azure Data Platform

## Service Selection
| Need | Service |
|------|---------|
| Relational OLTP | Azure SQL Database |
| Global distributed NoSQL | Cosmos DB |
| Object storage | Blob Storage |
| Data warehouse | Synapse Analytics |
| Streaming | Event Hubs |
| ETL | Data Factory |

## Azure SQL Database
- DTU vs vCore models
- Hyperscale for large DBs (100TB+)
- Elastic pools for multi-tenant
- Geo-replication for DR

## Cosmos DB
- Multi-model: document, key-value, graph, column-family
- SLA: 99.999% availability
- Partition key design critical
- Consistency levels: Strong → Eventual

## Blob Storage Tiers
- Hot, Cool, Cold, Archive
- Lifecycle management policies

## Architect Deep Dive: Data Platform Strategy

### SQL vs Cosmos vs Blob — decision matrix
| Need | Service |
|------|---------|
| ACID transactions, relational | Azure SQL / PostgreSQL Flexible |
| Global low-latency document, flexible schema | Cosmos DB |
| Files, images, backups, data lake | Blob / ADLS Gen2 |
| Analytics warehouse | Synapse / dedicated SQL pool |
| Search | AI Search (formerly Cognitive Search) |

### Cosmos DB partition key (critical)
Choose key with high cardinality and even distribution — `tenantId` or `userId`, **not** `status` or `country` alone (hot partition).

### Azure SQL tier selection
- **General Purpose** — most .NET OLTP
- **Business Critical** — low latency, readable secondaries in-region
- **Hyperscale** — 100TB+, rapid scale storage

### Backup & RPO
SQL automated backups: point-in-time restore. Define RPO with business — 5 min RPO may require geo-redundant backup + sync replica, not GP defaults alone.

