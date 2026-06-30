# Lab 39 — LLMOps Eval Pipeline

**Duration:** 2–3 hours

## Objectives
- Create golden dataset (20 Q&A pairs)
- Run automated eval on prompt change
- Gate CI: eval score must not drop > 5%

## Eval Metrics
- Retrieval precision@3
- Answer groundedness (manual or LLM-as-judge)
- Latency p95

## GitHub Actions Job

```yaml
- name: Run RAG eval
  run: dotnet run --project tests/RagEval -- --baseline results/baseline.json
```

## Deliverable
Prompt versioning doc + rollback procedure.
