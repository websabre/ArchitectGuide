# LLMOps & Responsible AI

> **Week 39** | **Module:** [ai-architecture-rag-llmops](../../../modules/ai-architecture-rag-llmops/README.md)

## Learning Objectives
- Implement prompt management and evaluation pipelines
- Design guardrails for enterprise AI
- Balance cost, latency, and quality

---

## 1. Prompt Management

| Practice | Tool |
|----------|------|
| Version prompts | Git, Promptflow, LangSmith |
| Parameterize | Templates with `{context}`, `{user_query}` |
| A/B test prompts | Feature flags + eval metrics |
| Environment promotion | dev → staging → prod prompt registry |

**Architect:** Treat prompts as code — PR review, CI eval gate before prod.

---

## 2. Evaluation Framework

| Eval Type | Metric |
|-----------|--------|
| **Retrieval** | Precision@K, MRR, nDCG |
| **Generation** | Groundedness, relevance, coherence |
| **Safety** | Harmful content rate, PII leakage |
| **Business** | Task completion rate, user thumbs |

```python
# Example: groundedness check
# Does answer only use retrieved context?
```

**Golden dataset:** 100–500 representative Q&A pairs with expected behavior. Run on every prompt/model change.

---

## 3. Guardrails

| Layer | Control |
|-------|---------|
| Input | Jailbreak detection, PII filter |
| Retrieval | ACL on documents (user sees only authorized chunks) |
| Output | Content safety API, citation requirement |
| Infrastructure | Private endpoints, no data retention |

**Azure:** Content Safety API, Prompt Shields. **AWS:** Bedrock Guardrails.

---

## 4. Cost & Latency Optimization

| Technique | Savings |
|-----------|---------|
| Smaller model for routing | GPT-4o-mini classifies intent |
| Cache embeddings | Don't re-embed static docs |
| Semantic cache | Similar queries → cached answer |
| Batch API | Non-real-time workloads |
| Token budgeting | Max context window discipline |

**Architect math:** 1M queries/month × 2K tokens × $0.01/1K = $20K/month. Model choice matters at scale.

---

## 5. Responsible AI Principles

1. **Fairness** — Test across demographics/use cases
2. **Transparency** — Disclose AI-generated content
3. **Privacy** — Minimize data sent to model
4. **Accountability** — Human override for high-stakes decisions
5. **Safety** — Fail closed on guardrail breach

**Regulated industries:** Document model card, data lineage, human-in-the-loop for medical/legal advice.

**Next:** Week 40 AI Capstone
