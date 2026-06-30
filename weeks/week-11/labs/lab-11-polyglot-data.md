# Lab 11: Azure SQL + Cosmos DB Polyglot Data

| **Week** | 11 | **Duration** | 90 min |

## Objectives
- [ ] Provision Azure SQL Database and Cosmos DB
- [ ] Design order data in SQL, product catalog in Cosmos
- [ ] Connect .NET app with Managed Identity

## Steps

### 1. Create Azure SQL
```bash
az sql server create --name sql-archlab-$RANDOM --resource-group rg-architect-lab-09 \
  --location eastus --enable-ad-only-auth false --admin-user sqladmin --admin-password '<SecurePass1!>'

az sql db create --resource-group rg-architect-lab-09 --server <server> \
  --name ordersdb --service-objective S0
```

### 2. Create Cosmos DB (Serverless)
```bash
az cosmosdb create --name cosmos-archlab-$RANDOM --resource-group rg-architect-lab-09 \
  --locations regionName=eastus --default-consistency-level Session

az cosmosdb sql database create --account-name <cosmos> --resource-group rg-architect-lab-09 --name catalog
az cosmosdb sql container create --account-name <cosmos> --resource-group rg-architect-lab-09 \
  --database-name catalog --name products --partition-key-path /categoryId --throughput 400
```

### 3. Partition Key Exercise
Document why `/categoryId` was chosen. What happens if you chose `/id`?

### 4. .NET Connection (EF Core + Cosmos SDK)
- SQL: orders with EF Core
- Cosmos: product catalog reads
- Both use `DefaultAzureCredential`

## Architect Report
1. When would you use Cosmos vs SQL for the same catalog?
2. Cost comparison: Cosmos RU/s vs SQL DTU for 1M products
3. Draw polyglot persistence diagram

## Cleanup
Delete resource group after lab.
