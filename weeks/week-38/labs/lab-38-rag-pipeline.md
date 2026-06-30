# Lab 38 — RAG Pipeline with Azure AI Search + OpenAI

**Duration:** 4 hours

## Objectives
- Ingest markdown docs into Azure AI Search
- Configure vector + semantic hybrid search
- Build .NET minimal API that answers questions with citations

## Architecture

```
Blob Storage → Azure Function (chunk+embed) → AI Search index
User → ASP.NET API → Search → GPT-4o → Response with citations
```

## Key Steps
1. Create search index with vector field (1536 dimensions)
2. Use `text-embedding-3-small` for embeddings
3. Implement ACL filter: `filter=department eq 'Claims'`
4. Require LLM to cite `source_id` in response

## Rubric
| Criteria | Points |
|----------|--------|
| Hybrid search works | 25 |
| Citations in response | 25 |
| ACL filtering | 25 |
| Latency < 5s p95 | 25 |
