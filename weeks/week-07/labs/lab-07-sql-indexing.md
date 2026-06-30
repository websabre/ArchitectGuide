# Lab 07: SQL Server Indexing & Execution Plans

## Objectives
- Create clustered/non-clustered/covering indexes
- Read execution plans (seek vs scan)
- Find missing indexes with DMVs

## Steps
1. Docker: `docker run -e ACCEPT_EULA=Y -e SA_PASSWORD='...' -p 1433:1433 mcr.microsoft.com/mssql/server:2022-latest`
2. Create Orders table with 1M rows
3. Query without index — note scan
4. Add index — note seek
5. Run missing index DMV query

## Report: Which indexes for e-commerce order queries?
