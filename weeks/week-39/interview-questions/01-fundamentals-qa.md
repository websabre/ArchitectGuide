# Week 39 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: LLMOps Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | LLMOps |
| **Frequency** | Very Common |

### Question

Describe the LLMOps lifecycle and how it differs from traditional MLOps.

### Short Answer (30 seconds)

LLMOps manages prompt templates, model versions, RAG indexes, eval harnesses, guardrails, and cost — in addition to standard ML deploy/monitor. LLM systems change weekly via prompts and corpus updates, not just model retraining.

### Detailed Answer (3–5 minutes)

**LLMOps lifecycle:**
1. **Design** — use case, risk tier, RAI assessment
2. **Develop** — prompts, RAG pipeline, tool integrations
3. **Evaluate** — golden datasets, faithfulness, safety, latency, cost
4. **Deploy** — staged rollout, feature flags, canary traffic
5. **Monitor** — quality drift, toxicity, cost per query, user feedback
6. **Iterate** — prompt version bump, re-index, model upgrade

**vs MLOps additions:**
| MLOps | LLMOps Extra |
|-------|-------------|
| Model registry | + Prompt registry |
| Feature drift | + Corpus freshness, embedding version |
| AUC metrics | + LLM-judge, RAGAS faithfulness |
| GPU training | + Token cost FinOps |

**Architect:** LLMOps CI gate — no prompt deploy without eval regression check. Separate dev/staging/prod prompt + index versions.

### Architecture Perspective

LLMOps is MLOps plus prompt/index lifecycle — architects govern what changes without retrain.

### Follow-up Questions

1. **Prompt CI? — Eval harness in pipeline — block merge if faithfulness drops 5%.**
2. **Human feedback loop? — Thumbs down → labeling queue → golden set growth.**

### Common Mistakes in Interviews

- Deploy prompt change directly to prod without eval
- No version tracking for RAG index config
- Monitor only infrastructure not answer quality

---

## Q002: Prompt Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | LLMOps |
| **Frequency** | Very Common |

### Question

How architect prompt versioning for production LLM applications?

### Short Answer (30 seconds)

Prompts are code — version in Git, register in prompt registry, deploy via CI/CD with eval gates. Track `prompt_version` + `model_version` + `index_version` tuple in every production log.

### Detailed Answer (3–5 minutes)

**Versioning strategy:**
```
support-assistant/system-prompt/v2.3.1
support-assistant/retrieval-prompt/v1.0.0
```

**Storage:**
- Git repo (source of truth) + prompt registry (runtime lookup)
- Azure App Configuration or dedicated DB for hot reload in staging
- Never hardcode prompts in application strings scattered across services

**Deployment:**
1. PR changes prompt → eval suite runs
2. Tag version → deploy to staging
3. A/B or canary in prod (5% traffic)
4. Promote or rollback via config flip

**Observability:** Log `prompt_version` in OpenTelemetry span — debug quality regressions.

**Architect:** Immutable prod prompts — new version = new deployment, not in-place edit.

### Architecture Perspective

Prompt versioning enables rollback when v2.4 degrades answer quality — same as API versioning.

### Follow-up Questions

1. **Jinja vs plain text prompts? — Templating for variables — version template separately.**
2. **Few-shot examples versioning? — Examples are part of prompt artifact hash.**

### Common Mistakes in Interviews

- Prompts edited in production Azure portal without Git
- No link between prompt version and eval results
- Rollback requires emergency code deploy

---

## Q003: Content Safety Guardrails

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Very Common |

### Question

What content safety guardrails should architects layer around enterprise LLM APIs?

### Short Answer (30 seconds)

Defense in depth: input filter (jailbreak, PII), Azure Content Safety / OpenAI content filter, output filter (toxicity, PII leak), topic boundaries, rate limits, and human escalation for high-risk tiers.

### Detailed Answer (3–5 minutes)

**Guardrail layers:**
1. **Input** — Prompt injection detection, blocklisted topics, max token limits
2. **Retrieval** — ACL on chunks — user sees only authorized docs
3. **Model** — Azure OpenAI content filter (hate, violence, sexual)
4. **Output** — PII redaction, profanity filter, citation validation
5. **Operational** — Rate limit per user, anomaly detection on query patterns

**Risk-tiered design:**
| Tier | Example | Guardrails |
|------|---------|------------|
| Low | Internal FAQ | Standard filters |
| Medium | HR policy bot | PII scan + audit log |
| High | Medical/legal | Human-in-loop, abstain default |

**Architect:** Guardrails are not optional — budget latency (+50–100ms) and cost in NFR doc.

### Architecture Perspective

Content safety is architectural layer — not afterthought prompt instruction.

### Follow-up Questions

1. **Jailbreak mitigation? — System prompt hardening + input classifier + output refusal patterns.**
2. **PII in retrieval? — Redact at ingest + block in output — defense in depth.**

### Common Mistakes in Interviews

- Rely only on model built-in safety
- No retrieval ACL — cross-department data leak
- Skip output filtering for internal-only myth

---

## Q004: LLM Cost Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

How architects manage and optimize LLM inference costs at enterprise scale?

### Short Answer (30 seconds)

Track cost per query, per feature, per tenant. Optimize via model routing (small model first), prompt compression, caching, batch APIs, retrieval token limits, and FinOps dashboards with budgets/alerts.

### Detailed Answer (3–5 minutes)

**Cost drivers:**
- Input tokens (prompt + retrieved context)
- Output tokens (generation length)
- Model tier (GPT-4 vs GPT-4o-mini)
- Embedding calls at ingest and query
- Reranker API calls

**Optimization strategies:**
1. **Model routing** — Classify query complexity → mini for simple, premium for hard
2. **Cache** — Semantic cache for repeated similar questions
3. **Retrieve less** — Top-3 not top-20 chunks after rerank eval proves sufficient
4. **Prompt efficiency** — Remove redundant system instructions
5. **Batch API** — Non-urgent workloads 50% discount
6. **PTU vs pay-go** — Provisioned throughput when baseline QPS predictable

**Architect FinOps:**
```
Budget: $50K/month → alert at 80%
Dashboard: $/query by product line
cap: max_tokens output per request type
```

### Architecture Perspective

LLM cost is recurring OpEx — architects instrument from day one not after invoice shock.

### Follow-up Questions

1. **Semantic cache? — Embed query → cache hit on similarity — 30–50% savings on support bots.**
2. **Token budgeting per user? — Rate limit + max context prevents abuse.**

### Common Mistakes in Interviews

- GPT-4 for all queries including hello
- No logging of token usage per feature
- Retrieve 50 chunks 'to be safe' — 10× prompt cost

---

## Q005: Responsible AI Principles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Very Common |

### Question

What responsible AI principles must architects embed in enterprise LLM system design?

### Short Answer (30 seconds)

Microsoft RAIF framework: fairness, reliability/safety, privacy/security, inclusiveness, transparency, accountability. Architects translate principles into requirements, eval gates, and governance artifacts.

### Detailed Answer (3–5 minutes)

**Principle → Architecture mapping:**
| Principle | Design Action |
|-----------|---------------|
| Fairness | Bias eval on demographic slices; diverse golden sets |
| Reliability | Eval harness, abstain paths, human escalation |
| Privacy | PII redaction, data minimization, regional deployment |
| Inclusiveness | Multilingual eval, accessibility of UI |
| Transparency | Citations, AI disclosure, limitation statements |
| Accountability | Audit logs, incident runbook, named owner |

**Deliverables architects produce:**
- AI Impact Assessment before launch
- Risk tier classification (low/medium/high)
- Responsible AI checklist in launch gate
- Ongoing monitoring for harm signals

**Not checkbox:** Principles drive design decisions — high-risk tier mandates human-in-loop regardless of demo quality.

### Architecture Perspective

Responsible AI is non-functional requirement — architects gate launch on assessment completion.

### Follow-up Questions

1. **AI disclosure UX? — 'AI-generated' label — regulatory trend EU AI Act.**
2. **Bias in RAG? — Skewed corpus → skewed answers — audit source document diversity.**

### Common Mistakes in Interviews

- RAI assessment after production launch
- No human escalation path for high-risk tier
- Principles documented but no eval metrics mapped

---

## Q006: Prompt Management and Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | LLMOps |
| **Frequency** | Very Common |

### Question

Design prompt version management for production LLM applications.

### Short Answer (30 seconds)

Store prompts in Git registry with semver, link to eval results, deploy via config service, A/B test versions, rollback on metric regression.

### Detailed Answer (3–5 minutes)

**Structure:**
```
prompts/
  support-bot/
    v1.2.0/system.txt
    v1.2.0/metadata.yaml  # model, tokens, eval scores
```

**Runtime:** Load prompt by `promptId@version` from Azure App Configuration or MLflow.

**CI:** PR changes prompt → eval harness → merge → auto-deploy to staging.

**Architect:** Treat prompts as immutable versions — never edit v1.2.0 in place; create v1.2.1.

### Architecture Perspective

Prompt versioning enables rollback when tone or accuracy regresses.

### Follow-up Questions

1. **Jinja templates? — Parameterize prompts — separate template from data.**
2. **Who approves prompt promote? — Product + compliance for customer-facing.**

### Common Mistakes in Interviews

- Prompts scattered in code strings
- Edit production prompt without version bump
- No eval gate on prompt change

---

## Q007: LLM Evaluation Harness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | LLMOps |
| **Frequency** | Very Common |

### Question

Build LLM evaluation harness for regression testing before deploy.

### Short Answer (30 seconds)

Golden dataset, automated metrics (accuracy, faithfulness, toxicity, latency), LLM-as-judge, human spot-check, CI gate on thresholds.

### Detailed Answer (3–5 minutes)

**Harness components:**
1. **Dataset** — 500+ labeled scenarios by category
2. **Runners** — Batch invoke model+prompt
3. **Scorers** — RAGAS, custom rubric, regex checks
4. **Report** — Compare v1 vs v2 diff
5. **Gate** — Block deploy if faithfulness drops >3%

**Azure:** Prompt flow eval, Azure AI Evaluation SDK.

**Architect:** Eval runs on every prompt/model change — not annual manual test.

### Architecture Perspective

Eval harness is CI for LLMs — without it every deploy is gamble.

### Follow-up Questions

1. **Synthetic test cases? — Bootstrap — human validate 20% sample.**
2. **Eval model vs prod model? — Same model family — judge consistency.**

### Common Mistakes in Interviews

- Manual 'looks good' testing only
- Eval set never updated with prod failures
- No comparison report between versions

---

## Q008: Guardrails and Content Safety

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Very Common |

### Question

Architect guardrails for customer-facing LLM chatbot.

### Short Answer (30 seconds)

Input filter (jailbreak, PII), Azure Content Safety API, output filter (hate, violence, sexual), topic blocklist, escalation to human, logging.

### Detailed Answer (3–5 minutes)

**Layers:**
1. **Pre-input** — Prompt injection detection, max length
2. **Content Safety** — Categories severity 0–6, block ≥4
3. **Post-output** — PII redaction, citation check
4. **Business rules** — No competitor mentions, no legal advice
5. **Human handoff** — Confidence low or policy trigger

**Architect:** Fail closed — block and apologize rather than risk harmful output.

### Architecture Perspective

Guardrails are defense in depth — not single content filter call.

### Follow-up Questions

1. **NeMo Guardrails? — Programmable dialog rails — open source option.**
2. **False positive handling? — Appeal path — tune thresholds with data.**

### Common Mistakes in Interviews

- Content safety only on output not input
- No jailbreak testing before launch
- Log blocked content without privacy review

---

## Q009: Token Cost Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Reduce LLM token costs at architecture level.

### Short Answer (30 seconds)

Model routing (small for easy, large for hard), prompt compression, caching, shorter context, batch API for offline, fine-tune smaller model, set max_tokens.

### Detailed Answer (3–5 minutes)

**Levers:**
| Tactic | Savings |
|--------|--------|
| GPT-4o-mini vs GPT-4 | 10–20× |
| Semantic cache | 30–50% on FAQ |
| Summarize context | 40% input tokens |
| Batch API | 50% discount |
| Fine-tune small model | Variable |

**Monitor:** $/1K tokens by use case dashboard — FinOps weekly review.

**Architect:** Token budget per API endpoint — hard limits in APIM.

### Architecture Perspective

Token cost is recurring OpEx — architects own routing and caching strategy.

### Follow-up Questions

1. **Prompt trimming? — Remove few-shot examples on simple classifier route.**
2. **Output max_tokens? — Cap at 500 for summaries — prevent runaway.**

### Common Mistakes in Interviews

- GPT-4 for classification that needs 1 word
- Send entire 100-page doc in context
- No per-team cost allocation

---

## Q010: Model Routing Small vs Large

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | LLMOps |
| **Frequency** | Very Common |

### Question

Design router sending queries to small or large LLM.

### Short Answer (30 seconds)

Classifier or heuristic routes: simple FAQ → mini model, complex reasoning → GPT-4. Monitor quality on routed traffic, escalation path if low confidence.

### Detailed Answer (3–5 minutes)

**Router options:**
1. **Rule-based** — Intent detection → route
2. **Classifier model** — Fine-tuned BERT cheap
3. **LLM meta-router** — Small model picks big model (ironic cost)
4. **Cascade** — Try mini first, escalate if confidence low

**Metrics:** Track % routed to each tier, quality by tier, cost savings.

**Architect:** Escalation must be invisible to user — same API contract.

### Architecture Perspective

Model routing is primary LLM cost optimization at scale.

### Follow-up Questions

1. **Cascade latency? — Two calls worst case — set timeout fallback.**
2. **Router drift? — Retrain classifier on misrouted examples monthly.**

### Common Mistakes in Interviews

- Large model for everything 'to be safe'
- Router with no quality monitoring on cheap path
- Expose routing logic inconsistency to user

---

## Q011: Caching LLM Responses

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

When and how cache LLM responses in production?

### Short Answer (30 seconds)

Exact-match cache for deterministic prompts (low temperature). Semantic cache for similar queries (embedding distance). TTL by content freshness. Never cache personalized sensitive responses.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Exact Redis** — `hash(prompt+model)` → response, TTL 1h
- **Semantic** — Vector similarity >0.95 → return cached
- **CDN edge** — Public FAQ static responses

**Invalidation:** Prompt version change flushes cache namespace.

**Architect:** Cache hit rate KPI — target 20–40% for support bots. Exclude healthcare/legal personalized advice.

### Architecture Perspective

LLM caching cuts cost and latency — with staleness and privacy rules.

### Follow-up Questions

1. **Cache key includes model version? — Must — or wrong model response served.**
2. **PII in cache? — Encrypt, short TTL, or no cache for PII flows.**

### Common Mistakes in Interviews

- Cache personalized medical advice
- No cache invalidation on prompt update
- Semantic cache threshold too loose — wrong answers

---

## Q012: Rate Limiting LLM APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Rate limit LLM APIs to prevent abuse and cost overrun.

### Short Answer (30 seconds)

Per-user, per-API-key, per-tenant limits at APIM gateway. Token bucket for burst. 429 with Retry-After. Separate limits for expensive endpoints.

### Detailed Answer (3–5 minutes)

**Tiers:**
- Free: 10 req/min, 10K tokens/day
- Pro: 100 req/min, 500K tokens/day
- Enterprise: contract limits

**Protection:**
- Global emergency brake — 10K $/day cap
- Anomaly detection — spike alert
- WAF + auth before LLM

**Architect:** Rate limit before LLM call — not after token burn.

### Architecture Perspective

LLM rate limits protect budget and prevent abuse — mandatory at gateway.

### Follow-up Questions

1. **Token vs request limit? — Both — request limit prevents spam, token prevents cost.**
2. **Distributed rate limit? — Redis central — not per-node.**

### Common Mistakes in Interviews

- No rate limit on internal LLM proxy
- Per-request only ignoring token volume
- No emergency spend cap

---

## Q013: Azure OpenAI Deployment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

Design Azure OpenAI deployment for enterprise production.

### Short Answer (30 seconds)

Regional deployment, private endpoint, managed identity, multiple model deployments (gpt-4o, gpt-4o-mini), PTU or PAYG, content filter default, diagnostic logging to Log Analytics.

### Detailed Answer (3–5 minutes)

**Topology:**
- AOAI resource per environment (dev/prod)
- Model deployments named `gpt-4o-prod`, `embed-prod`
- APIM front door — hide keys, add policies
- VNet integration — no public access
- RBAC: `Cognitive Services OpenAI User`

**Capacity:** PTU for predictable latency; PAYG for dev/spiky.

**Architect:** Multi-region AOAI for DR — secondary region warm.

### Architecture Perspective

Azure OpenAI deployment is network + identity + capacity architecture.

### Follow-up Questions

1. **PTU vs PAYG? — PTU when steady high QPS — break-even math.**
2. **Model retirement? — Azure announces deprecation — migration runway.**

### Common Mistakes in Interviews

- API key in application config
- Public endpoint with customer data
- Single deployment no mini model fallback

---

## Q014: Content Filter Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Very Common |

### Question

Configure Azure OpenAI content filter policies for enterprise.

### Short Answer (30 seconds)

Set severity thresholds per category (hate, sexual, violence, self-harm), custom blocklists, annotate vs block mode, separate policies dev vs prod.

### Detailed Answer (3–5 minutes)

**Policy design:**
- **Customer support** — Block high severity all categories
- **Internal codegen** — Relaxed violence (game dev)
- **Annotate mode** — Log medium severity — don't block — tune thresholds

**Custom blocklist:** Competitor names, internal codenames.

**Architect:** Document policy in ADR — legal approves customer-facing thresholds.

### Architecture Perspective

Content filters are configurable — not one-size-fits-all.

### Follow-up Questions

1. **Jailbreak filter? — Separate from content categories — enable both.**
2. **Filter bypass for admins? — Audit logged — break-glass only.**

### Common Mistakes in Interviews

- Default filter settings without review
- Disable filters in prod 'for quality'
- No custom blocklist for brand terms

---

## Q015: PII Redaction in LLM Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Privacy |
| **Frequency** | Very Common |

### Question

Redact PII before sending text to LLM and before logging.

### Short Answer (30 seconds)

Presidio or Azure AI Language PII detection on input and output, tokenize reversible PII in vault if needed for processing, redact logs.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
User input → PII detect → redact/mask → LLM → PII detect output → User
                ↓
           Audit log (redacted)
```

**Patterns:**
- **Mask** — `John Doe` → `[PERSON_1]`
- **Block** — Refuse if SSN detected
- **Tokenize** — Vault detokenize only in secure enclave

**Architect:** DPIA documents what PII flows to AOAI — minimize by design.

### Architecture Perspective

PII redaction is compliance requirement — build into pipeline not afterthought.

### Follow-up Questions

1. **Re-identification from context? — Residual risk assessment.**
2. **Log retention redacted? — Still may have secrets — classify logs.**

### Common Mistakes in Interviews

- Send full customer record to LLM
- Log raw prompts to App Insights
- No output PII scan

---

## Q016: Audit Logging for Prompts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

What to audit-log in enterprise LLM applications?

### Short Answer (30 seconds)

UserId, timestamp, prompt hash (or redacted prompt), model version, token count, response hash, retrieval chunk IDs, guardrail triggers, cost — retain per policy.

### Detailed Answer (3–5 minutes)

**Log schema:**
```json
{userId, sessionId, model, promptVersion, inputTokens, outputTokens, retrievalIds[], filterResults, latencyMs, costUsd}
```

**Retention:** 7 years financial; 90 days PII-redacted support.

**Access:** SOC team read-only, encrypted at rest, immutable store (WORM).

**Architect:** Balance audit need vs privacy — redact PII in stored prompts.

### Architecture Perspective

Audit logs enable incident investigation and regulatory response.

### Follow-up Questions

1. **Prompt hash vs full text? — Hash for integrity; redacted text for review.**
2. **GDPR right to erasure? — Log anonymization procedure documented.**

### Common Mistakes in Interviews

- No logging of LLM interactions
- Full PII prompts in immutable logs forever
- Logs without model/prompt version

---

## Q017: Human in the Loop

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Common |

### Question

Design human-in-the-loop for high-stakes LLM decisions.

### Short Answer (30 seconds)

LLM drafts, human approves before send/action. Queue UI, SLA for review, feedback captured for improvement, escalation on low confidence.

### Detailed Answer (3–5 minutes)

**Use cases:** Medical prior auth, loan denial letters, legal contract summary.

**Architecture:**
- LLM generates draft → review queue (Service Bus)
- Human edits/approves → action executes
- Rejection feeds training/eval dataset

**SLA:** Review within 4 hours — auto-escalate.

**Architect:** HITL is feature not bug — regulators expect it for high-risk AI.

### Architecture Perspective

Human in the loop reduces risk — design queue and feedback from day one.

### Follow-up Questions

1. **Active learning? — Human corrections → fine-tune dataset.**
2. **Automation creep? — Resist removing HITL without formal risk reassessment.**

### Common Mistakes in Interviews

- Fully automated loan denial by LLM
- HITL queue with no SLA
- Human edits not captured for improvement

---

## Q018: Fine-Tuning vs RAG Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

When fine-tune LLM vs use RAG vs prompt engineering?

### Short Answer (30 seconds)

RAG for dynamic knowledge and citations. Fine-tune for style, format, domain language, or task-specific behavior. Prompt engineering first — cheapest baseline.

### Detailed Answer (3–5 minutes)

| Need | Approach |
|------|----------|
| Up-to-date docs | RAG |
| Consistent JSON output format | Fine-tune or structured output |
| Company tone/style | Fine-tune |
| Factual grounding | RAG |
| New capability (reasoning) | Bigger model or CoT prompt |

**Architect:** Default RAG + prompt; fine-tune when eval shows systematic format/style failure RAG can't fix.

### Architecture Perspective

Fine-tune vs RAG is common architecture decision — use decision matrix.

### Follow-up Questions

1. **Fine-tune on what data? — 1000+ quality examples — garbage in garbage out.**
2. **Combine both? — Fine-tune for tone + RAG for facts — common enterprise.**

### Common Mistakes in Interviews

- Fine-tune to inject facts that change weekly
- RAG for strict output schema without structured output mode
- Fine-tune without eval vs baseline

---

## Q019: RLHF Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Training |
| **Frequency** | Occasional |

### Question

Explain RLHF and relevance for enterprise architects.

### Short Answer (30 seconds)

Reinforcement Learning from Human Feedback: humans rank model outputs, train reward model, fine-tune LLM with RL to align with preferences. Powers ChatGPT quality — enterprise rarely trains RLHF from scratch.

### Detailed Answer (3–5 minutes)

**Stages:**
1. Pretrain base model
2. SFT on demonstrations
3. Reward model from human rankings
4. PPO optimization

**Enterprise relevance:**
- Use RLHF-aligned commercial models (GPT-4)
- **RLHF-lite:** Thumbs up/down → preference dataset → periodic fine-tune
- Not feasible to run full RLHF internally — cost billions

**Architect:** Collect user feedback infrastructure — enables future alignment iterations.

### Architecture Perspective

RLHF explains why base models differ from chat models — architects buy not build.

### Follow-up Questions

1. **DPO vs RLHF? — Direct Preference Optimization — simpler fine-tune alternative.**
2. **Feedback loop design? — Thumbs, edits, acceptance rate — store structured.**

### Common Mistakes in Interviews

- Plan to RLHF your own GPT from scratch
- Ignore user feedback collection
- Assume base model equals chat model quality

---

## Q020: Model Deprecation Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | LLMOps |
| **Frequency** | Common |

### Question

Handle Azure OpenAI model version deprecation in architecture.

### Short Answer (30 seconds)

Monitor deprecation notices, maintain model compatibility matrix, run eval harness on replacement model, dual-run period, cutover deadline, rollback plan.

### Detailed Answer (3–5 minutes)

**Playbook:**
1. Azure announces `gpt-4-32k` deprecation date
2. Eval `gpt-4o` on golden set — compare metrics
3. Update APIM routing to new deployment
4. Parallel run 2 weeks — shadow compare
5. Decommission old deployment before deadline

**Architect:** `modelAlias` in app config — not hardcode deployment name.

### Architecture Perspective

Model deprecation is recurring event — not one-time migration.

### Follow-up Questions

1. **Embedding model deprecation? — Full re-index required — plan early.**
2. **Automated deprecation alert? — Subscribe Azure Service Health.**

### Common Mistakes in Interviews

- Hardcode model name `gpt-4-0613` everywhere
- Ignore deprecation email until outage
- No eval on replacement model

---

## Q021: Multi-Tenant LLM Isolation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Isolate tenants in shared LLM platform architecture.

### Short Answer (30 seconds)

Separate API keys or JWT claims per tenant, tenantId in all logs/cache/index filters, per-tenant rate limits and cost caps, optional dedicated deployments for enterprise tier.

### Detailed Answer (3–5 minutes)

**Isolation layers:**
- **Data** — Vector index filter `tenantId` or separate index
- **Compute** — Shared AOAI with quota per tenant
- **Cache** — Key prefix `tenant:{id}:`
- **Config** — Per-tenant prompt versions

**Enterprise tier:** Dedicated AOAI PTU, silo index, CMK.

**Architect:** Test cross-tenant retrieval in security review — mandatory.

### Architecture Perspective

Multi-tenant LLM isolation mirrors SaaS data isolation patterns.

### Follow-up Questions

1. **Noisy neighbor on PTU? — Enterprise dedicated capacity.**
2. **Tenant offboarding? — Delete index partition, cache, logs per policy.**

### Common Mistakes in Interviews

- Shared cache key without tenant prefix
- Cross-tenant prompt injection via shared index
- No per-tenant cost tracking

---

## Q022: API Key vs Managed Identity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Authenticate to Azure OpenAI: API key or managed identity?

### Short Answer (30 seconds)

Managed identity for Azure-hosted apps — no secrets in config, RBAC, automatic rotation. API keys for local dev and third-party tools only — store in Key Vault, rotate quarterly.

### Detailed Answer (3–5 minutes)

**Production pattern:**
```csharp
var client = new AzureOpenAIClient(
  new Uri(endpoint),
  new DefaultAzureCredential());
```

**APIM:** OAuth between client and gateway; MI between APIM and AOAI.

**Architect:** CI/CD policy blocks API keys in prod appsettings — fail build.

### Architecture Perspective

Managed identity eliminates LLM API key leakage — standard for Azure apps.

### Follow-up Questions

1. **User-assigned vs system MI? — User-assigned for multi-app shared identity.**
2. **Local dev? — `az login` + DefaultAzureCredential — not prod keys on laptop.**

### Common Mistakes in Interviews

- API key committed to Git
- Shared API key across all microservices
- No key rotation procedure

---

## Q023: Streaming Responses UX

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | UX |
| **Frequency** | Common |

### Question

Architect streaming LLM responses for chat UX.

### Short Answer (30 seconds)

SSE or WebSocket from API, stream tokens as generated, show typing indicator, allow cancel mid-stream, handle reconnection, measure TTFB SLO.

### Detailed Answer (3–5 minutes)

**API design:**
```
GET /chat/stream → text/event-stream
 data: {"token": "Hello"}
```

**Benefits:** TTFB 200ms vs 3s wait — perceived latency cut dramatically.

**Considerations:** Partial response on cancel, idempotent message IDs, mobile background handling.

**Architect:** APIM supports streaming passthrough — verify not buffered.

### Architecture Perspective

Streaming is UX architecture decision — users expect ChatGPT-like experience.

### Follow-up Questions

1. **Cancel propagation? — Abort upstream AOAI call — save tokens.**
2. **Buffer for non-stream clients? — Fallback collect full response.**

### Common Mistakes in Interviews

- Block until full 4K token response
- APIM buffering breaks stream
- No cancel button — wasted tokens on abandoned requests

---

## Q024: Fallback Models

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Design fallback when primary LLM unavailable or rate limited.

### Short Answer (30 seconds)

Cascade: primary GPT-4o → fallback GPT-4o-mini → cached response → graceful degradation message. Circuit breaker on error rate.

### Detailed Answer (3–5 minutes)

**Triggers:** 429 rate limit, 503 unavailable, latency >5s, content filter block.

**Implementation:**
- Polly circuit breaker in .NET client
- APIM retry to secondary backend
- Static FAQ fallback for known queries

**Architect:** Fallback must not silently degrade quality on critical flows — inform user 'simplified mode.'

### Architecture Perspective

LLM fallback prevents total outage — plan before Azure incident.

### Follow-up Questions

1. **Cross-region fallback? — Secondary AOAI region — data residency check.**
2. **Fallback eval? — Mini model quality acceptable for degraded mode?**

### Common Mistakes in Interviews

- No fallback — hard fail on 503
- Fallback to model with no content filter
- Silent downgrade without user awareness

---

## Q025: LLM Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Runbook for LLM production incident: harmful output spike.

### Short Answer (30 seconds)

Detect via content filter alerts or user reports → disable endpoint via feature flag → preserve logs → root cause (prompt change? data poison?) → fix → eval → gradual re-enable.

### Detailed Answer (3–5 minutes)

**Severity levels:**
- **Sev1** — Harmful content at scale, data leak
- **Sev2** — Elevated error rate, cost spike
- **Sev3** — Quality degradation

**Immediate actions:**
1. Kill switch — APIM policy block route
2. Preserve audit logs
3. War room — legal if external harm
4. RCA within 48h

**Architect:** Pre-approved kill switch — no change approval needed in emergency.

### Architecture Perspective

LLM incidents include reputational harm — runbook beyond typical API outage.

### Follow-up Questions

1. **Communications? — Status page if customer-facing degradation.**
2. **Post-incident? — Add eval case — prevent recurrence.**

### Common Mistakes in Interviews

- No kill switch for LLM endpoint
- Delete logs during incident cleanup
- Re-enable without eval after harmful output

---

## Q026: Responsible AI Dashboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Common |

### Question

Design Responsible AI monitoring dashboard for LLM platform.

### Short Answer (30 seconds)

Track content filter blocks by category, fairness metrics, user complaints, jailbreak attempts, HITL override rate, model version distribution.

### Detailed Answer (3–5 minutes)

**Tiles:**
- Filter blocks/day by severity
- Thumbs down rate trend
- Jailbreak attempt count
- PII redaction triggers
- Human review queue depth
- Deprecation migration status

**Audience:** Engineering + compliance + legal monthly review.

**Architect:** Dashboard drives proactive policy tuning — not just incident reaction.

### Architecture Perspective

RAI dashboard makes responsible AI operational — not policy PDF.

### Follow-up Questions

1. **Benchmark periods? — Compare pre/post prompt change.**
2. **External audit? — Export quarterly RAI metrics report.**

### Common Mistakes in Interviews

- No visibility into filter blocks
- Ignore thumbs down trends
- Dashboard only engineering — exclude compliance

---

## Q027: EU AI Act Awareness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

How does EU AI Act affect enterprise LLM architecture decisions?

### Short Answer (30 seconds)

Classify AI systems by risk tier. High-risk (employment, credit, medical) requires conformity assessment, human oversight, transparency, logging. GPAI models have transparency obligations.

### Detailed Answer (3–5 minutes)

**Architect actions:**
1. Inventory AI systems — risk classification
2. High-risk: technical documentation, risk management, data governance
3. Transparency: disclose AI interaction to users
4. GPAI provider vs deployer obligations differ
5. Monitor implementing acts and timelines

**Partner legal** — architects supply system diagrams and data flows.

### Architecture Perspective

EU AI Act drives documentation and governance architecture — engage legal early.

### Follow-up Questions

1. **Prohibited practices? — Social scoring, manipulative AI — design review gate.**
2. **General-purpose AI? — Document training data summary if provider.**

### Common Mistakes in Interviews

- Ignore EU AI Act outside EU — global products affected
- No AI system inventory
- High-risk system without human oversight design

---

## Q028: Jailbreak Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Architect defenses against LLM jailbreak and prompt injection.

### Short Answer (30 seconds)

Input sanitization, system prompt hardening, content filters, output validation, privilege separation (user content never in system role), monitoring for attack patterns.

### Detailed Answer (3–5 minutes)

**Techniques:**
1. **Delimiter isolation** — `###user###` untrusted block
2. **Instruction hierarchy** — System > developer > user
3. **Azure Prompt Shields** — Attack detection
4. **Least capability** — Tools allowlist minimal
5. **Canary tokens** — Detect exfiltration attempts

**Red team:** Regular jailbreak testing — DAN, encoding tricks, multilingual attacks.

### Architecture Perspective

Jailbreak prevention is ongoing arms race — layer defenses.

### Follow-up Questions

1. **Indirect injection via RAG? — Sanitize indexed documents.**
2. **Defense in depth? — No single filter catches all — combine layers.**

### Common Mistakes in Interviews

- Trust user input in system prompt
- No red team before customer launch
- Disable safety filters for 'creativity'

---

## Q029: Synthetic Data Generation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data |
| **Frequency** | Common |

### Question

Use synthetic data for LLM fine-tuning and eval when real data scarce.

### Short Answer (30 seconds)

LLM generates training examples from seed samples, human review subset, deduplicate, validate quality metrics, never use synthetic for regulated decisions without disclosure.

### Detailed Answer (3–5 minutes)

**Pipeline:**
- Seed 50 real examples → GPT generates 500 variations
- Human QA 10% sample
- Filter low-quality via classifier
- Mix 70% real 30% synthetic max

**Risks:** Model collapse if only synthetic, bias amplification, privacy false sense.

**Architect:** Document synthetic % in model card — auditors ask.

### Architecture Perspective

Synthetic data augments scarce datasets — not replacement for governance.

### Follow-up Questions

1. **SDV / CTGAN for tabular? — Different from LLM text synthesis.**
2. **Privacy claim? — Synthetic not automatically anonymous — test re-id.**

### Common Mistakes in Interviews

- 100% synthetic fine-tune no human review
- Synthetic PII without redaction
- Claim GDPR exempt because synthetic

---

## Q030: LLMOps Maturity Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Describe LLMOps maturity levels for enterprise assessment.

### Short Answer (30 seconds)

Level 1: Ad-hoc prompts in apps. Level 2: Central prompts, logging. Level 3: Eval harness, guardrails, cost controls. Level 4: Full CI/CD, RAI gates, multi-tenant platform. Level 5: Continuous optimization, feedback loops, COE.

### Detailed Answer (3–5 minutes)

**Maturity ladder:**
| Level | Characteristics |
|-------|------------------|
| 1 Ad-hoc | Keys in code, no monitoring |
| 2 Managed | Prompt registry, basic logs |
| 3 Governed | Eval CI, content safety, FinOps |
| 4 Platform | Self-service, tenant isolation, HITL |
| 5 Optimized | RLHF-lite, automated routing, RAI dashboard |

**Architect:** Assess current level, roadmap +2 levels in 12 months with executive sponsorship.

### Architecture Perspective

LLMOps maturity model guides investment — avoid jumping to level 5 day one.

### Follow-up Questions

1. **Who owns platform? — AI CoE + platform engineering partnership.**
2. **Measure progress? — DORA-style: deploy frequency, incident rate, cost/query.**

### Common Mistakes in Interviews

- Claim level 4 without eval harness
- Skip levels — no prompt registry before CI/CD
- No executive sponsor for platform investment

---
