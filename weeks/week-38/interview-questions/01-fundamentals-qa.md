# Week 38 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: RAG Architecture Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Explain RAG (Retrieval-Augmented Generation) architecture for enterprise knowledge systems.

### Short Answer (30 seconds)

RAG grounds LLM responses in retrieved documents — ingest corpus, chunk, embed, index; at query time retrieve relevant chunks, augment prompt, generate answer with citations. Default pattern for enterprise factual Q&A.

### Detailed Answer (3–5 minutes)

**End-to-end flow:**
```
Documents → Ingest/OCR → Chunk → Embed → Vector Index
                                              ↓
User Query → Embed Query → Retrieve Top-K → Rerank → Prompt + Context → LLM → Answer + Citations
```

**Core components:**
- **Ingestion pipeline** — batch/event-driven on document changes
- **Vector store** — Azure AI Search, pgvector, dedicated vector DB
- **Orchestrator** — retrieval logic, prompt assembly, guardrails
- **LLM gateway** — Azure OpenAI with content filter, rate limits, logging
- **Observability** — retrieval hit rate, faithfulness, latency, cost per query

**Architect principles:**
- Separate ingestion (batch) from query path (real-time)
- Hybrid search (vector + keyword) for enterprise docs with SKUs and codes
- Citations mandatory for trust and audit

**Not RAG:** General creative writing, tasks solvable from model parametric knowledge alone.

### Architecture Perspective

RAG is default enterprise LLM pattern — architects know every pipeline stage and boundary.

### Follow-up Questions

1. **RAG vs fine-tuning first? — RAG for fresh/private docs; fine-tune for style/behavior.**
2. **Orchestrator build vs buy? — Semantic Kernel, LangChain, or custom .NET — consistency matters.**

### Common Mistakes in Interviews

- LLM answers factual questions without retrieval for proprietary data
- Re-embed entire corpus on every user query
- No citation requirement in enterprise assistant design

---

## Q002: When RAG vs Fine-Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

When recommend RAG vs fine-tuning for enterprise LLM customization?

### Short Answer (30 seconds)

RAG for dynamic/private knowledge, citation needs, and fast iteration without retraining. Fine-tuning for domain language, task format, classification, and behavior — not for frequently changing document corpus.

### Detailed Answer (3–5 minutes)

| Need | RAG | Fine-Tuning |
|------|-----|-------------|
| Private doc Q&A | ✅ Primary | ❌ Can't inject new docs |
| Citations to source | ✅ Natural | ❌ No source attribution |
| Domain terminology/style | ⚠️ Prompt engineering | ✅ Strong fit |
| Structured output format | ⚠️ Prompt + JSON mode | ✅ Reliable |
| Data changes weekly | ✅ Re-index only | ❌ Retrain cost |
| Small labeled task dataset | ❌ Overkill | ✅ Efficient |
| Reduce prompt length/cost | ❌ Retrieval adds tokens | ✅ Compress into weights |

**Architect recommendation flow:**
1. Start RAG + strong system prompt for knowledge assistants
2. Add fine-tune if eval shows consistent format/style failures RAG can't fix
3. Combine: fine-tuned model + RAG for best enterprise assistants

**Cost:** RAG = retrieval infra + larger prompts. Fine-tune = training GPU + redeploy cycle per update.

### Architecture Perspective

RAG and fine-tuning solve different problems — architects avoid fine-tuning the knowledge base.

### Follow-up Questions

1. **RLHF vs fine-tuning? — RLHF for alignment preference; SFT fine-tune for task — different pipelines.**
2. **Embeddings fine-tune? — Domain embedding model — improves retrieval before LLM fine-tune.**

### Common Mistakes in Interviews

- Fine-tune to memorize policy PDF that changes monthly
- RAG for simple sentiment classification with 10K labels
- Skip eval comparing RAG-only vs fine-tune-only on golden set

---

## Q003: Vector Database Role

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Vector Search |
| **Frequency** | Very Common |

### Question

What role does a vector database play in RAG architecture?

### Short Answer (30 seconds)

Vector DB stores document chunk embeddings and enables similarity search — given query embedding, return top-k nearest chunks. Often combined with metadata filtering and hybrid keyword search.

### Detailed Answer (3–5 minutes)

**Responsibilities:**
- Store high-dimensional vectors (384–3072 dims) with chunk metadata
- Approximate nearest neighbor search (HNSW, IVF) at scale
- Metadata filters (`department eq HR`, `docType eq policy`)
- Hybrid search integration (vector + BM25)

**Not responsible for:**
- LLM inference (separate service)
- Document parsing/OCR (ingestion pipeline)
- Access control to raw documents (enforce at query time via filters + auth)

**Selection criteria:**
- Scale (1M vs 100M vectors)
- Hybrid search requirement
- Azure integration vs multi-cloud
- Ops model (managed vs self-hosted)

**Architect:** Index per sensitivity tier — confidential HR index separate from public KB — network isolation + RBAC.

### Architecture Perspective

Vector DB is retrieval engine — not the whole RAG system.

### Follow-up Questions

1. **Same index all classifications? — Security violation — partition by sensitivity.**
2. **Re-index trigger? — Embedding model change = full re-index migration event.**

### Common Mistakes in Interviews

- Vector DB chosen without hybrid search evaluation
- No metadata filters for multi-tenant isolation
- Treat vector DB as primary document store

---

## Q004: Chunking Strategy Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

What are chunking strategy fundamentals architects must define for RAG?

### Short Answer (30 seconds)

Chunking splits documents into retrievable units — size, overlap, and boundary rules directly affect recall and answer quality. Architects document chunk policy per content type and evaluate on golden questions.

### Detailed Answer (3–5 minutes)

**Fundamental strategies:**
| Strategy | Description | Best For |
|----------|-------------|----------|
| Fixed-size | 512 tokens + 50 overlap | General docs |
| Structure-aware | Split on Markdown headings | Technical wikis |
| Semantic | Paragraph/section boundaries | Narrative content |
| Parent-child | Small retrieve, large parent context | Long policies |

**Key parameters:**
- **Chunk size** — 256–1024 tokens; smaller = precise, larger = context
- **Overlap** — 10–20% prevents boundary information loss
- **Metadata** — `docId`, `section`, `page`, `lastModified` on every chunk

**Evaluation:** Golden set 100+ questions → measure recall@5 per strategy before production.

**Architect:** Chunk config is versioned — change triggers re-index and re-eval gate.

### Architecture Perspective

Chunk quality drives retrieval quality — more impactful than embedding model choice initially.

### Follow-up Questions

1. **Code documents? — AST-aware chunking — don't split mid-function.**
2. **Tables in PDFs? — Specialized extraction — naive text split destroys structure.**

### Common Mistakes in Interviews

- One giant chunk per 200-page PDF
- Zero overlap on fixed-size chunks
- Change chunk size without re-running retrieval eval

---

## Q005: Grounding and Citations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

How do grounding and citations work in enterprise RAG systems?

### Short Answer (30 seconds)

Grounding constrains LLM to answer only from retrieved context. Citations link each claim to source chunk — enabling verification, audit, and trust. No citation = don't show answer in high-compliance domains.

### Detailed Answer (3–5 minutes)

**Grounding mechanisms:**
1. **Prompt instruction** — 'Answer only using provided context; say I don't know if insufficient'
2. **Retrieval threshold** — score <0.7 → abstain or escalate to human
3. **Citation-required mode** — LLM outputs `[1]` references mapped to chunk metadata
4. **Post-generation check** — verify claims appear in retrieved text (faithfulness score)

**Citation architecture:**
```
Chunk metadata: { docId, title, url, page, lastModified }
Response: { answer, citations: [{ index: 1, source: url, excerpt }] }
```

**UX:** Show source title, link, and 'last updated' date — transparency reduces hallucination distrust.

**Compliance:** Audit log stores query, retrieved chunks, model version, and response for regulatory review.

**Architect:** Grounding is system design — retrieval + prompt + abstain policy + eval — not prompt tweak alone.

### Architecture Perspective

Citations transform LLM from black box to auditable knowledge system.

### Follow-up Questions

1. **Abstain vs hallucinate? — Enterprise prefers 'I don't know' over confident wrong answer.**
2. **Azure grounding API? — OpenAI on-your-data pattern — built-in citation support.**

### Common Mistakes in Interviews

- Answers without source links in legal/compliance assistant
- High temperature on factual grounded Q&A
- No audit log of retrieved context per query

---

## Q006: RAG Pipeline Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Design end-to-end RAG pipeline architecture for enterprise knowledge assistant.

### Short Answer (30 seconds)

Ingest documents → chunk → embed → index in vector store → at query time: embed query → retrieve top-k → augment prompt → LLM generate → cite sources. Add reranker, guardrails, and observability.

### Detailed Answer (3–5 minutes)

**Components:**
1. **Ingestion** — SharePoint, blob, PDF pipeline with OCR
2. **Chunking** — semantic or fixed-size with overlap
3. **Embedding** — ada-002 or open model → vector DB
4. **Retrieval** — hybrid search (vector + BM25)
5. **Generation** — Azure OpenAI with grounded prompt
6. **Post-process** — citations, content filter, logging

**Architecture diagram flow:**
```
User → APIM → RAG Orchestrator → [Retriever || Vector DB] → LLM → Response + Citations
```

**Architect:** Separate ingestion pipeline (batch) from query path (real-time). Cache embeddings — don't re-embed corpus per query.

### Architecture Perspective

RAG is the default enterprise LLM pattern — know every pipeline stage.

### Follow-up Questions

1. **Orchestrator framework? — LangChain, Semantic Kernel, custom .NET service.**
2. **Sync vs async ingest? — Event-driven on document upload — near-real-time index.**

### Common Mistakes in Interviews

- LLM without retrieval for factual enterprise Q&A
- Re-embed entire corpus on every query
- No citation requirement in design

---

## Q007: Chunking Strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Compare chunking strategies for technical documentation RAG.

### Short Answer (30 seconds)

Fixed-size (512 tokens + overlap), semantic (split on paragraphs/headings), document-structure (Markdown headers), parent-child (small chunks retrieve, large parent provides context).

### Detailed Answer (3–5 minutes)

**Strategies:**
| Strategy | Pros | Cons |
|----------|------|------|
| Fixed 512 + 50 overlap | Simple | Splits mid-sentence |
| Semantic | Coherent units | Slower preprocessing |
| Parent-child | Better context | Complex retrieval |
| Code-aware | Preserves functions | Needs language parser |

**Tuning:** Evaluate retrieval recall@k per strategy on golden question set.

**Architect:** Store chunk metadata — `docId`, `section`, `page`, `lastModified` — for filtering and citations.

### Architecture Perspective

Chunk quality drives retrieval quality — more important than embedding model choice initially.

### Follow-up Questions

1. **Overlap size? — 10–20% of chunk — prevents boundary information loss.**
2. **Tables in PDFs? — Specialized table extraction — don't naive text split.**

### Common Mistakes in Interviews

- Single giant chunk per document
- No overlap on fixed-size chunks
- Ignore document structure (headings)

---

## Q008: Embedding Model Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

How choose embedding model for production RAG?

### Short Answer (30 seconds)

Evaluate on domain retrieval benchmark (MRR, recall@5). Consider dimension size (storage cost), latency, multilingual needs, and whether managed (Azure OpenAI) vs open (e5, BGE).

### Detailed Answer (3–5 minutes)

**Factors:**
- **Domain fit** — general vs fine-tuned on legal/medical
- **Dimensions** — 1536 (ada-002) vs 384 (MiniLM) — storage/latency trade-off
- **Latency** — batch embed at ingest; query embed <50ms
- **Cost** — $/1M tokens at ingest scale
- **Compliance** — data residency — Azure OpenAI in region

**Process:** Golden dataset 100 Q&A pairs → compare models → pick Pareto optimal.

**Architect:** Version embeddings — model change requires full re-index.

### Architecture Perspective

Embedding model change is migration event — plan re-index pipeline.

### Follow-up Questions

1. **Matryoshka embeddings? — Truncate dimensions with modest quality loss.**
2. **Same model query and document? — Must match — asymmetric models exist but rare.**

### Common Mistakes in Interviews

- Pick embedding model from blog post without eval
- Mix embedding models in same index
- No re-index plan when upgrading model

---

## Q009: Vector Database Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Vector Search |
| **Frequency** | Very Common |

### Question

Compare vector DB options: Azure AI Search, Pinecone, pgvector, Cosmos DB.

### Short Answer (30 seconds)

Azure AI Search for hybrid + enterprise Azure integration. pgvector when already on Postgres and <10M vectors. Dedicated (Pinecone, Qdrant) for vector-only at scale. Cosmos for multi-model global.

### Detailed Answer (3–5 minutes)

| Option | Best For |
|--------|----------|
| Azure AI Search | Hybrid search, semantic ranker, Azure stack |
| pgvector | Existing Postgres, moderate scale |
| Pinecone/Qdrant | Pure vector, high QPS |
| Cosmos DB vector | Global distribution, multi-model |

**Criteria:** Hybrid search need, metadata filtering, SLA, ops burden, cost at N million vectors.

**Architect:** POC with production-scale sample (1M vectors) before commitment.

### Architecture Perspective

Vector DB choice binds hybrid search, filtering, and ops for years.

### Follow-up Questions

1. **HNSW params in each DB? — efConstruction, M — tune for recall/latency.**
2. **Managed vs self-hosted? — Weaviate on AKS — you own patching.**

### Common Mistakes in Interviews

- Vector DB without metadata filter support
- Postgres pgvector at 100M vectors without benchmark
- Ignore hybrid search requirement

---

## Q010: Azure AI Search Hybrid Search

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

Design hybrid search with Azure AI Search for RAG.

### Short Answer (30 seconds)

Combine vector search (semantic) with BM25 (keyword) via hybrid query. Semantic ranker re-orders top results. Index schema: content, contentVector, metadata fields.

### Detailed Answer (3–5 minutes)

**Index schema:**
- `content` — searchable text (BM25)
- `contentVector` — 1536-dim embedding
- `department`, `docType` — filterable
- `sourceUrl` — citation

**Query:**
```
hybrid search: vector(query_embedding) + search(query_text)
semantic reranker: enabled
```

**Benefits:** Exact SKU matches (keyword) + conceptual matches (vector). Critical for product codes, legal citations.

**Architect:** Private endpoint, managed identity, separate indexes per sensitivity tier.

### Architecture Perspective

Hybrid search fixes pure vector weakness on exact token matches.

### Follow-up Questions

1. **Semantic ranker cost? — Per query surcharge — budget in cost model.**
2. **Index partitions? — Scale beyond single partition limits.**

### Common Mistakes in Interviews

- Vector-only ignoring product SKUs
- Public search endpoint with confidential docs
- No semantic ranker on production index

---

## Q011: Semantic Ranking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

What is semantic ranking and where does it fit in RAG?

### Short Answer (30 seconds)

Semantic ranker (Azure AI Search L2, cross-encoder) re-scores top-k retrieved chunks for relevance before LLM context. Improves precision — fewer irrelevant chunks in prompt.

### Detailed Answer (3–5 minutes)

**Two-stage retrieval:**
1. **Stage 1 (fast)** — vector + BM25 → top 50 candidates
2. **Stage 2 (slow)** — cross-encoder scores query-chunk pairs → top 5 to LLM

**Trade-off:** +100–300ms latency, better answer quality, lower token waste.

**Architect:** A/B test with/without reranker on answer faithfulness metrics.

### Architecture Perspective

Semantic ranking is precision layer — recall from stage 1, accuracy from stage 2.

### Follow-up Questions

1. **Cross-encoder vs bi-encoder? — Bi-encoder for retrieve; cross-encoder for rerank.**
2. **Cohere Rerank API? — Alternative to Azure semantic ranker.**

### Common Mistakes in Interviews

- Send top-50 chunks to LLM without rerank
- Rerank entire corpus per query
- Ignore latency budget impact

---

## Q012: Retrieval Quality Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

How measure retrieval quality in RAG systems?

### Short Answer (30 seconds)

Recall@k, MRR, nDCG on golden dataset. Track hit rate (any relevant doc in top-k), context precision in production samples.

### Detailed Answer (3–5 minutes)

**Offline metrics:**
- **Recall@5** — % questions with relevant chunk in top 5
- **MRR** — mean reciprocal rank of first relevant hit
- **nDCG** — graded relevance

**Online proxies:**
- User thumbs down 'wrong source'
- Citation click-through
- LLM faithfulness score (RAGAS)

**Golden set:** 200+ domain Q&A with expected source docIds — maintain as living asset.

**Architect:** Retrieval eval gate in CI — block index config change if recall drops >5%.

### Architecture Perspective

Retrieval metrics isolate problems before blaming the LLM.

### Follow-up Questions

1. **Hit rate vs MRR? — Hit rate simpler for stakeholder reporting.**
2. **Synthetic golden set? — Bootstrap then human validate — don't trust only synthetic.**

### Common Mistakes in Interviews

- Only measure end-to-end answer quality
- No golden dataset maintained
- Change chunk size without re-evaluating retrieval

---

## Q013: Hallucination Mitigation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Architectural patterns to reduce LLM hallucinations in RAG.

### Short Answer (30 seconds)

Ground on retrieved context only, low temperature, cite-or-abstain prompts, confidence thresholds, cross-check multiple sources, content filters, human review for high-risk.

### Detailed Answer (3–5 minutes)

**Patterns:**
1. **Strict grounding prompt** — 'Answer only from context; say I don't know if not found'
2. **Citation required** — No citation → don't show answer
3. **Abstain threshold** — retrieval score <0.7 → escalate
4. **Self-consistency** — multiple samples, majority vote (costly)
5. **Fact verification** — secondary lookup on extracted claims

**Architect:** Hallucination rate KPI — sample audit weekly. High-risk domains (medical, legal) → human in loop.

### Architecture Perspective

Hallucination mitigation is system design — not prompt tweak alone.

### Follow-up Questions

1. **Temperature for RAG? — 0–0.3 factual; higher for creative tasks.**
2. **Grounding API? — Azure OpenAI on-your-data pattern — built-in citations.**

### Common Mistakes in Interviews

- Trust LLM with no retrieval for facts
- High temperature on compliance Q&A
- No 'I don't know' path in UX

---

## Q014: Grounding Responses

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

How ensure LLM responses are grounded in retrieved documents?

### Short Answer (30 seconds)

Inject retrieved chunks in system prompt with source IDs, instruct model to quote sources, validate citations exist in index, log context sent per response.

### Detailed Answer (3–5 minutes)

**Prompt structure:**
```
Context:
[1] {chunk text} (source: doc-A, p3)
[2] {chunk text} (source: doc-B, p1)
Answer using only [1] and [2]. Cite as [n].
```

**Validation:** Post-process — parse citations, verify chunk IDs exist, strip uncited claims for regulated use.

**Architect:** Store `retrievalContext` in audit log — reproduce any answer.

### Architecture Perspective

Grounding is traceability — auditors ask 'show me the source.'

### Follow-up Questions

1. **Context window limits? — Rerank to fit top-5 chunks — don't truncate randomly.**
2. **Lost in the middle? — Put best chunks at start/end of context.**

### Common Mistakes in Interviews

- No source attribution in response
- Context not logged for audit
- Retrieve but don't pass context to LLM

---

## Q015: Prompt Engineering for RAG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Best practices for RAG system prompts at architecture level.

### Short Answer (30 seconds)

Version prompts in registry, separate system/user templates, include role, grounding rules, citation format, refusal conditions, and output schema.

### Detailed Answer (3–5 minutes)

**System prompt elements:**
- Role and scope boundaries
- Grounding instruction
- Citation format `[docId:section]`
- Refusal: legal advice, PII requests
- Output: JSON schema if structured

**Management:** Prompt registry (Azure ML, Git), A/B test prompt versions, track token count per template.

**Architect:** Prompt changes go through CI — eval harness must pass before promote.

### Architecture Perspective

Prompts are code — version, test, and review like application logic.

### Follow-up Questions

1. **Few-shot in RAG? — 2–3 examples of good cited answers — improves format.**
2. **Prompt injection defense? — Delimiter + instruction hierarchy — user input untrusted.**

### Common Mistakes in Interviews

- Prompts hardcoded in application without version
- Change prompt without re-running eval
- No refusal instructions for out-of-scope

---

## Q016: Index Refresh Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

Design index refresh when source documents change frequently.

### Short Answer (30 seconds)

Event-driven incremental update on document change, nightly full reconcile, embedding version tracking, blue-green index swap for zero-downtime re-index.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Incremental** — Service Bus event on blob update → re-chunk, re-embed, upsert
- **Full rebuild** — Weekly — catch missed events
- **Blue-green index** — Build `index-v2`, swap alias, delete old
- **Tombstone** — Mark deleted docs — remove from index

**SLA:** 'New policy doc searchable within 15 minutes.'

**Architect:** `lastIndexedAt` metadata — monitor staleness alerts.

### Architecture Perspective

Stale index causes wrong answers — freshness is architectural SLA.

### Follow-up Questions

1. **Delete handling? — Hard delete vectors on source removal — GDPR.**
2. **Partial update failure? — Dead letter queue + reconcile job.**

### Common Mistakes in Interviews

- Weekly batch only for hourly-changing docs
- No delete path from index
- Re-index production in-place without swap

---

## Q017: Multi-Modal RAG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

Extend RAG to images, diagrams, and scanned PDFs.

### Short Answer (30 seconds)

OCR + layout analysis for PDFs, vision embedding models for images, caption generation for diagrams, unified index with modality metadata.

### Detailed Answer (3–5 minutes)

**Pipeline:**
- **PDF** — Azure Document Intelligence → text + tables + figure descriptions
- **Images** — GPT-4V or CLIP embeddings → vector index
- **Query** — Text query retrieves text + image descriptions

**Challenges:** Higher cost, larger chunks, vision model latency.

**Architect:** Modality tag in metadata — filter `modality=image` when user asks for diagrams.

### Architecture Perspective

Multi-modal RAG needs document intelligence — not plain text extract.

### Follow-up Questions

1. **Document Intelligence layout? — Preserves reading order — better chunks.**
2. **Chart understanding? — Export data table + caption — dual index.**

### Common Mistakes in Interviews

- Naive PDF text extract on scanned docs
- Ignore images in engineering diagrams
- Vision model on every query regardless of need

---

## Q018: Citation in Responses

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Design citation UX and backend for enterprise RAG answers.

### Short Answer (30 seconds)

Inline numbered citations linking to source doc, page, and snippet highlight. Backend stores chunkId → sourceUrl mapping.

### Detailed Answer (3–5 minutes)

**UX:**
- Answer text with `[1][2]` superscripts
- Click opens source in viewer with highlight
- Show `lastUpdated` date per source

**Backend:**
- Return `citations: [{id, title, url, snippet, confidence}]`
- Validate URLs still accessible

**Compliance:** User can verify every claim — required for regulated industries.

### Architecture Perspective

Citations build trust and enable audit — architectural requirement not UI polish.

### Follow-up Questions

1. **Broken link handling? — Cache snippet even if source moved.**
2. **Confidence per citation? — Show low-confidence sources differently.**

### Common Mistakes in Interviews

- Vague 'according to internal docs' without link
- Citation to chunk user cannot access — permission check
- No snippet preview in citation

---

## Q019: Vector Index Sizing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

Estimate vector index size for 500K document chunks.

### Short Answer (30 seconds)

500K chunks × 1536 dims × 4 bytes ≈ 3GB vectors + HNSW graph overhead 1.5–2× ≈ 5–6GB RAM minimum + metadata + replicas.

### Detailed Answer (3–5 minutes)

**Formula:** `vectors_gb = num_vectors × dimensions × 4 bytes`

**HNSW overhead:** ~1.5–2× vector storage for graph links.

**Total:** vectors + metadata (text preview, filters) + replica factor.

**500K @ 1536d:** ~6GB primary + replica → 12GB cluster.

**Architect:** Load test at 2× projected size. Consider dimension reduction or smaller embedding model if cost constrained.

### Architecture Perspective

Index sizing prevents production OOM and cost surprises.

### Follow-up Questions

1. **Quantized vectors? — Product quantization — 4–8× smaller — recall trade-off.**
2. **Shard at what size? — Vendor-specific — AI Search partition limits.**

### Common Mistakes in Interviews

- No sizing calc before procurement
- Ignore replica memory doubling
- Store full document text redundantly in every chunk vector row

---

## Q020: HNSW vs IVF Index Types

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Vector Search |
| **Frequency** | Common |

### Question

Compare HNSW and IVF vector index algorithms.

### Short Answer (30 seconds)

HNSW: graph-based, high recall, higher memory, great for interactive search. IVF: clusters vectors, faster build, lower memory, good for very large static indexes.

### Detailed Answer (3–5 minutes)

| | HNSW | IVF |
|---|------|-----|
| Recall | High | Tunable |
| Memory | Higher | Lower |
| Build time | Slower | Faster |
| Update | Incremental OK | Prefer batch rebuild |
| Use | RAG query <100ms | Billion-scale batch |

**Tuning HNSW:** `M=16`, `efConstruction=200`, query `efSearch=100` — raise efSearch for recall.

**Architect:** Default HNSW for enterprise RAG; IVF for offline similarity at massive scale.

### Architecture Perspective

Index algorithm affects recall, latency, and RAM — not invisible infrastructure.

### Follow-up Questions

1. **Flat (brute force)? — Exact — only tiny indexes.**
2. **efSearch tuning? — Higher = better recall + slower query.**

### Common Mistakes in Interviews

- IVF for real-time RAG without recall testing
- Default params without tuning on golden set
- Rebuild IVF on every document add

---

## Q021: Metadata Filtering in Retrieval

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Very Common |

### Question

Use metadata filters to improve RAG retrieval precision.

### Short Answer (30 seconds)

Pre-filter vector search by department, date, docType, security clearance before k-NN. Combines structured query with semantic search.

### Detailed Answer (3–5 minutes)

**Example:** User in HR asks policy question → filter `department=HR AND classification<=internal`.

**Implementation:**
- Azure AI Search: OData filter on index fields
- pgvector: SQL WHERE + vector ORDER BY distance

**Architect:** Security filter mandatory — never retrieve docs user cannot access. Inject user claims into filter expression.

### Architecture Perspective

Metadata filtering is security and precision — not optional enrichment.

### Follow-up Questions

1. **Filter before or after vector search? — Before (pre-filter) for security; post-filter risks leakage.**
2. **ACL per document? — Store allowedGroups[] — filter by user group membership.**

### Common Mistakes in Interviews

- Vector search without tenant filter in multi-tenant
- Post-filter security — chunks leak in logs
- No doc classification metadata

---

## Q022: Query Rewriting for RAG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

When use query rewriting / HyDE in RAG pipelines?

### Short Answer (30 seconds)

Rewrite vague user query to search-friendly form, or HyDE (generate hypothetical document embedding). Use when initial retrieval recall is low on conversational queries.

### Detailed Answer (3–5 minutes)

**Techniques:**
1. **Query expansion** — LLM adds synonyms, disambiguation
2. **HyDE** — Generate fake answer, embed it, search with that vector
3. **Multi-query** — 3 rewritten queries, merge results
4. **Step-back** — Abstract question for broader context retrieval

**Cost:** Extra LLM call per query — +latency +tokens.

**Architect:** Enable for low-confidence first-pass retrieval only — not every query.

### Architecture Perspective

Query rewriting trades cost for recall on ambiguous questions.

### Follow-up Questions

1. **HyDE failure mode? — Hypothetical doc drifts off-topic — monitor precision.**
2. **Cache rewritten queries? — Same FAQ phrasing — Redis cache.**

### Common Mistakes in Interviews

- HyDE on every query doubling cost
- Rewrite without logging original query
- No fallback if rewrite degrades results

---

## Q023: Re-Ranking with Cross-Encoder

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

Add cross-encoder reranking to RAG retrieval pipeline.

### Short Answer (30 seconds)

Retrieve top-50 with bi-encoder, rerank with cross-encoder (query+chunk joint encoding), pass top-5 to LLM. Models: ms-marco-MiniLM, Cohere rerank-v3.

### Detailed Answer (3–5 minutes)

**Pipeline latency:**
- Bi-encoder retrieve: 20ms
- Cross-encoder 50 pairs: 150ms
- LLM generate: 800ms

**Worth it when:** Precision more important than 150ms — legal, support KB.

**Architect:** Deploy reranker as separate microservice — scale independently. Batch score pairs on GPU.

### Architecture Perspective

Cross-encoder reranking is standard production pattern for quality RAG.

### Follow-up Questions

1. **MonoT5 vs cross-encoder? — Alternative rerank architectures.**
2. **Rerank top-k how many? — 50 retrieve, 5 to LLM — tune on eval set.**

### Common Mistakes in Interviews

- Skip rerank with noisy retrieval
- Rerank 500 chunks — latency explosion
- Reranker model mismatch with embedding model domain

---

## Q024: RAGAS Evaluation Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

How use RAGAS to evaluate RAG pipeline quality?

### Short Answer (30 seconds)

RAGAS metrics: faithfulness, answer relevancy, context precision, context recall. Run on golden Q&A dataset, track over prompt/index/model changes.

### Detailed Answer (3–5 minutes)

**Metrics:**
- **Faithfulness** — Answer grounded in context?
- **Answer relevancy** — Addresses question?
- **Context precision** — Retrieved chunks relevant?
- **Context recall** — All needed info retrieved?

**CI integration:** Eval job on staging after index change — thresholds: faithfulness >0.85.

**Architect:** RAGAS complements retrieval metrics — catches grounded-but-wrong and ungrounded-right.

### Architecture Perspective

RAGAS automates LLM-as-judge eval — essential for regression testing.

### Follow-up Questions

1. **LLM judge cost? — Batch eval nightly — not per user query.**
2. **Human eval sample? — 5% of prod traffic — gold standard calibration.**

### Common Mistakes in Interviews

- No automated eval before production prompt change
- Single metric obsession (faithfulness only)
- Eval set not representative of prod queries

---

## Q025: Security for RAG Data

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Threat model for enterprise RAG — data exfiltration, prompt injection, ACL bypass.

### Short Answer (30 seconds)

Threats: prompt injection via documents, cross-tenant retrieval, PII in responses, index poisoning, embedding inversion. Mitigate: ACL filters, content safety, input sanitization, audit logs.

### Detailed Answer (3–5 minutes)

**Controls:**
1. **Document ACL** — Index inherits source permissions
2. **Prompt injection** — Sanitize docs, delimiter isolation, output filter
3. **Tenant isolation** — Separate indexes or strict tenantId filter
4. **PII scan** — On ingest and response
5. **Audit** — Log query, user, chunks retrieved, response
6. **Rate limit** — Prevent bulk exfiltration via queries

**Architect:** Red team RAG — attempt to retrieve other dept docs via crafted prompts.

### Architecture Perspective

RAG expands attack surface — documents become prompt injection vectors.

### Follow-up Questions

1. **Indirect injection? — Malicious text in indexed PDF — scan on ingest.**
2. **Embedding inversion? — Sensitive docs — access control primary defense.**

### Common Mistakes in Interviews

- Single shared index all employees
- No retrieval audit log
- Ignore poisoned document upload

---

## Q026: Cost per Query RAG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Estimate cost per RAG query and optimize.

### Short Answer (30 seconds)

Typical: embed query $0.0001 + retrieve negligible + LLM 2K in/500 out $0.02 + rerank $0.001 ≈ $0.02–0.05/query. At 1M queries/month = $20–50K.

### Detailed Answer (3–5 minutes)

**Breakdown:**
| Step | Cost driver |
|------|-------------|
| Query embed | Tokens |
| Retrieval | Index SKU fixed |
| Rerank | Pairs scored |
| LLM | Input+output tokens |

**Optimize:** Cache frequent queries, smaller model for simple Q, compress context, route to GPT-4o-mini vs GPT-4.

### Architecture Perspective

RAG unit economics determine viability at scale — model CFO conversations.

### Follow-up Questions

1. **Semantic cache? — Similar query embedding match — skip LLM.**
2. **Token budget per query? — Hard cap truncate context — predictable cost.**

### Common Mistakes in Interviews

- GPT-4 for all queries including FAQ
- No caching on identical questions
- Ignore ingest embedding one-time cost

---

## Q027: Latency Optimization for RAG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Reduce p99 RAG query latency from 3s to under 1.5s.

### Short Answer (30 seconds)

Parallel retrieve+rerank prep, streaming LLM response, smaller/faster models, regional deployment, connection pooling, pre-warmed endpoints, reduce context tokens.

### Detailed Answer (3–5 minutes)

**Tactics:**
1. **Streaming** — TTFB <500ms — user sees tokens immediately
2. **Parallel** — Embed query while auth check runs
3. **Model** — GPT-4o-mini for draft, escalate rare
4. **Context** — Top-3 not top-10 chunks
5. **Cache** — Redis for hot queries
6. **Geo** — Deploy in user region

**Measure:** Trace each stage — often LLM dominates; sometimes reranker.

### Architecture Perspective

RAG latency is UX — streaming masks total time.

### Follow-up Questions

1. **Time to first token SLO? — Separate from total generation time.**
2. **CDN for static FAQ? — Bypass RAG entirely for top 100 questions.**

### Common Mistakes in Interviews

- Sequential waterfall with no parallelism
- Cold start serverless every query
- 3s blocking wait with no streaming UI

---

## Q028: Private Data RAG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Architect RAG on confidential data with zero public model training exposure.

### Short Answer (30 seconds)

Azure OpenAI with private endpoint, no training on customer data (contractual), data stays in tenant VNet, managed identity, customer-managed keys, no logging prompts to vendor.

### Detailed Answer (3–5 minutes)

**Checklist:**
- [ ] Azure OpenAI private link only
- [ ] `data logging opt-out` confirmed
- [ ] Documents in private storage
- [ ] CMK encryption
- [ ] No PII in Application Insights without redaction
- [ ] On-prem option evaluated (AI Studio hybrid)

**Architect:** Legal review of Microsoft DPA and data flow diagram for audit.

### Architecture Perspective

Private RAG is default enterprise ask — prove data boundary diagram.

### Follow-up Questions

1. **Bring your own model? — Self-host Llama on AKS — more ops, full control.**
2. **Cross-border? — Embed and LLM in same region as data.**

### Common Mistakes in Interviews

- Public OpenAI API with customer PII
- Assume 'enterprise tier' without reading DPA
- Log full prompts to third-party analytics

---

## Q029: Agentic RAG Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | RAG |
| **Frequency** | Common |

### Question

How does agentic RAG differ from single-shot retrieve-generate?

### Short Answer (30 seconds)

Agent iterates: plan → retrieve → evaluate sufficiency → maybe re-query → tool calls → synthesize. Handles multi-hop questions requiring several retrieval steps.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
User Q → Agent planner → [Retrieve tool] → 'Need more on X?' → [Retrieve] → [Calculator tool] → Final answer
```

**Frameworks:** LangGraph, Semantic Kernel planners, AutoGen.

**Trade-offs:** Higher latency (multiple LLM calls), cost, better on complex research tasks.

**Architect:** Guardrails on max iterations (5), tool allowlist, budget cap per session.

### Architecture Perspective

Agentic RAG is emerging pattern — know when complexity justified.

### Follow-up Questions

1. **ReAct pattern? — Reason + Act interleaved — common agent loop.**
2. **When not agentic? — Simple FAQ — single-shot cheaper and faster.**

### Common Mistakes in Interviews

- Agent with unbounded tool access
- No iteration limit — runaway cost
- Agent for every query regardless of complexity

---

## Q030: RAG Production Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Architecture checklist before RAG goes to production.

### Short Answer (30 seconds)

Eval harness passing, ACL on index, monitoring (latency, faithfulness sample, cost), index refresh tested, rollback plan, content filter, PII redaction, rate limits, DR index replica, runbook.

### Detailed Answer (3–5 minutes)

**Go-live checklist:**
- [ ] Golden set eval ≥ thresholds
- [ ] Load test 2× peak QPS
- [ ] Security red team completed
- [ ] Observability dashboards live
- [ ] Index blue-green swap tested
- [ ] Fallback 'search unavailable' UX
- [ ] On-call runbook with escalation
- [ ] Cost alerts configured
- [ ] User feedback thumbs up/down wired
- [ ] Legal/compliance sign-off

**Architect:** Sign checklist — same rigor as microservice launch.

### Architecture Perspective

RAG production checklist prevents 'demo to prod' gap.

### Follow-up Questions

1. **Canary launch? — 5% users week 1 — monitor faithfulness.**
2. **Rollback? — Revert index alias + prompt version — <15 min.**

### Common Mistakes in Interviews

- Ship after demo without eval
- No monitoring on retrieval stage
- Skip legal review on regulated content

---
