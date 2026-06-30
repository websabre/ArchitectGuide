# AI/ML Architecture — Intermediate

> **Week 37** | Data pipelines, model registry, GPU economics

## 1. Training Data Pipelines

```mermaid
flowchart LR
    Raw[Raw Data Lake] --> Clean[Cleaning / PII Redaction]
    Clean --> Label[Labeling]
    Label --> Feature[Feature Store]
    Feature --> Train[Training Job]
```

**Architect concerns:** Data contracts, lineage (who changed what), reproducibility (seed, dataset version).

---

## 2. Model Registry

| Capability | Azure ML | AWS SageMaker |
|------------|----------|---------------|
| Versioning | Model registry | Model registry |
| Stage promotion | Staging → Prod | Approved stages |
| Lineage | Run ID → dataset | Pipeline tracking |

**Gate:** No model reaches production without eval metrics on holdout set.

---

## 3. GPU vs CPU Economics

| Workload | Compute |
|----------|---------|
| Batch inference nightly | CPU spot instances |
| Real-time LLM | GPU (A100/H100) or managed API |
| Embedding generation | CPU often sufficient at < 1M docs |
| Fine-tuning | GPU required |

**Break-even:** Managed API cheaper until ~500K requests/month at 2K tokens — then evaluate self-hosted.

---

## 4. Batch vs Real-Time Feature Serving

**Training-serving skew:** Features computed differently offline vs online → wrong predictions.

**Solution:** Feature store serves same transformation logic for both paths.
