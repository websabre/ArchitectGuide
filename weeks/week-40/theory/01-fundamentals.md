# AI Architecture Capstone — Enterprise Copilot

> **Week 40** | Design a document intelligence / copilot system end-to-end

## Capstone Brief

**Client:** Global insurance firm, 50K employees, 10M policy documents (PDF, Word, scanned).

**Goal:** Internal copilot answers policy questions, drafts claim summaries, cites sources.

**Constraints:**
- Data must not leave Azure tenant
- Sub-5s p95 response for chat
- 99.9% availability
- SOC 2, GDPR compliant
- Budget: $15K/month inference at launch

---

## Design Requirements

### 1. Ingestion Pipeline
- Event-driven on blob upload
- OCR for scanned PDFs (Document Intelligence)
- Chunking + embedding pipeline
- Incremental updates (not full re-index nightly)

### 2. Retrieval Layer
- Hybrid search (vector + keyword)
- Document-level ACL from Entra ID groups
- Reranking top 20 → top 5 chunks

### 3. Generation Layer
- Azure OpenAI GPT-4o with private endpoint
- System prompt: cite sources, refuse if not in context
- Streaming SSE to React frontend

### 4. LLMOps
- Prompt registry in Git
- Eval pipeline on golden 200 questions
- Cost dashboard per department

### 5. Observability
- Trace: query → retrieval → generation latency breakdown
- Log prompts/responses (redacted) for audit
- Alert on guardrail trigger rate spike

---

## Deliverables Checklist

- [ ] C4 Context + Container diagrams
- [ ] ADR: vector DB choice
- [ ] ADR: model selection (quality vs cost)
- [ ] Sequence diagram: happy path query
- [ ] Threat model: prompt injection, data exfiltration
- [ ] Cost estimate spreadsheet
- [ ] 45-minute whiteboard presentation script

## Rubric

| Area | Weight |
|------|--------|
| Security & compliance | 25% |
| RAG architecture quality | 25% |
| LLMOps & eval | 20% |
| Cost & scalability | 15% |
| Presentation clarity | 15% |
