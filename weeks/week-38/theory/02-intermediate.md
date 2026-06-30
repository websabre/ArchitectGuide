# RAG — Intermediate: Production Hardening

> **Week 38** | Reranking, ingestion at scale, multi-modal

## 1. Reranking Pipeline

```
Query → Retrieve top 50 (hybrid) → Rerank to top 5 (Cohere/cross-encoder) → LLM
```

Improves precision 15–30% on enterprise doc sets. Adds 100–300ms latency.

---

## 2. Incremental Indexing

| Event | Action |
|-------|--------|
| Document created | Embed + upsert chunk |
| Document updated | Delete old chunks + re-embed |
| Document deleted | Remove from index |
| ACL change | Update metadata filter only |

**Event-driven:** Blob trigger → Service Bus → indexer function.

---

## 3. Multi-Modal RAG

Images, tables, charts in PDFs require:
- Document Intelligence layout model
- Table extraction to structured text
- Optional: CLIP embeddings for image search

---

## 4. Citation & Grounding

Force structured output:
```json
{ "answer": "...", "sources": ["doc-id-1", "doc-id-2"], "confidence": 0.85 }
```

Reject answers with empty sources for compliance Q&A.
