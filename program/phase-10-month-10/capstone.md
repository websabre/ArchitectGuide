# Month 10 Capstone — Enterprise Document Intelligence Copilot

> **Phase 10** | Complete after weeks in this month.

## Brief

RAG architecture with security, LLMOps, cost model.

## Scenario

**LegalEdge Corp** (~2,000 attorneys) wants an internal **document intelligence copilot** over **500K contracts and policies** stored in SharePoint and Azure Blob. Users ask natural-language questions and receive cited answers. Constraints: no customer data in model training, answers must include source citations, PII must be redacted in logs, and monthly inference budget is capped at **$15K**. Stakeholders include legal (accuracy and privilege), security (tenant isolation, prompt injection), and FinOps (token cost per query). You are designing the production RAG platform for the AI governance board.

## Architecture Expectations

A passing solution must cover the full GenAI architecture lifecycle:

- **RAG pipeline diagram** — ingest, chunk, embed, index, retrieve, augment, generate
- **Vector store selection** — Azure AI Search, pgvector, or equivalent with hybrid search
- **Security architecture** — Entra ID auth, document-level ACL filtering at retrieval, Key Vault for keys
- **LLMOps** — prompt versioning, eval pipeline, golden dataset, regression gates
- **Responsible AI** — content safety, jailbreak mitigation, human review for low-confidence answers
- **Cost model** — tokens per query, embedding refresh cost, storage, compute
- **NFRs** — P95 latency < 8 s, citation accuracy ≥90% on golden set, audit log retention
- **Mermaid sequence diagram** — user query → retrieve → filter by ACL → LLM → cited response

## Deliverables

- [ ] **C4 Container diagram** — copilot UI, orchestrator, vector index, LLM, data sources
- [ ] **RAG pipeline diagram** (Mermaid) — batch ingest + online query paths
- [ ] **Security architecture doc** — authN/Z, ACL filtering, secrets, prompt injection defenses
- [ ] **ADR: vector store + embedding model** — selection rationale
- [ ] **ADR: orchestration framework** — Semantic Kernel, LangChain, or custom
- [ ] **Eval pipeline design** — 50 golden questions, metrics (faithfulness, relevance, citation match)
- [ ] **Golden question dataset** — 50 Q&A pairs with expected citations (spreadsheet or JSON)
- [ ] **Cost model spreadsheet** — per-query and monthly at 5K queries/day
- [ ] **Week 40 capstone brief** — complete per [Week 40](../../weeks/week-40/README.md) requirements
- [ ] **LLMOps runbook outline** — deploy prompt v2, run eval, promote or rollback

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Document corpus scope and ACL model defined
- Accuracy and citation requirements quantified
- Budget and latency constraints explicit

**Architecture quality (30 pts)**

- RAG pipeline handles ingest freshness and re-embedding
- Retrieval respects document-level permissions
- Eval pipeline gates production prompt changes

**Trade-off documentation (20 pts)**

- Vector store ADR compares latency, cost, hybrid search
- Orchestration ADR considers team skills and Azure fit
- Chunking strategy justified with trade-offs

**Production realism (15 pts)**

- PII redaction in logs and traces
- Content safety and jailbreak layers documented
- Cost model includes embedding refresh and storage

**Presentation / ADRs (15 pts)**

- AI governance board narrative (20 min) prepared
- Golden eval results summarized honestly
- Week 40 lab artifacts linked

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 10:

| Day | Focus |
|-----|-------|
| **Mon W1** | Requirements — corpus, ACL, budget, accuracy targets |
| **Tue W1** | C4 diagram + RAG pipeline (ingest + query) |
| **Wed W1** | Security architecture — auth, ACL filter, injection defense |
| **Thu W1** | ADR: vector store + embedding model |
| **Fri W1** | ADR: orchestration framework |
| **Mon W2** | Build golden dataset (50 questions + expected citations) |
| **Tue W2** | Eval pipeline design + initial benchmark run |
| **Wed W2** | Cost model — per-query and monthly projection |
| **Thu W2** | Complete Week 40 capstone lab |
| **Fri W2** | AI governance walkthrough; submit package |

## References

- [Week 37 — AI/ML Architecture Fundamentals](../../weeks/week-37/README.md)
- [Week 38 — RAG, Vector Search & LLM Integration](../../weeks/week-38/README.md)
- [Week 39 — LLMOps & Responsible AI](../../weeks/week-39/README.md)
- [Week 40 — AI Architecture Capstone](../../weeks/week-40/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
