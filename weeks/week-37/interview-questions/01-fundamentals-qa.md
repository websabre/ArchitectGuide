# Week 37 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: ML System Architecture Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ML Architecture |
| **Frequency** | Very Common |

### Question

Describe the high-level architecture of a production ML system from an architect's perspective.

### Short Answer (30 seconds)

Production ML = data pipelines + feature engineering + training + model registry + serving + monitoring + feedback loop. Architect defines boundaries, SLAs, and promotion gates — not just the model algorithm.

### Detailed Answer (3–5 minutes)

**Reference architecture:**
```
Data Sources → Ingestion → Feature Store → Training Pipeline → Model Registry
                                                              ↓
User/App → API Gateway → Inference Service → Model Runtime → Response
                              ↓
                    Monitoring (drift, latency, business KPIs)
```

**Key components:**
- **Data layer** — lake/warehouse, labeling, quality checks
- **Compute** — training clusters (GPU batch), serving endpoints (CPU/GPU)
- **Metadata** — experiment tracking, lineage, model versions
- **Serving** — REST/gRPC, batch scoring, edge deployment
- **Observability** — technical SLIs + business outcome metrics

**Architect responsibilities:** Environment isolation (dev/staging/prod), identity/RBAC, data residency, reproducibility, and handoff contracts between data science and platform teams.

**Anti-pattern:** Notebook → pickle file → production without pipeline.

### Architecture Perspective

ML architecture is systems engineering — model is one component among many.

### Follow-up Questions

1. **ML vs traditional microservice? — Adds data/model versioning and drift — same reliability bar.**
2. **Who owns production on-call? — Platform SRE + ML engineer rotation — define in RACI.**

### Common Mistakes in Interviews

- Deploy notebook output directly to prod
- No separation between experimentation and serving infrastructure
- Treat ML system as stateless CRUD API only

---

## Q002: Batch vs Real-Time Inference

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Inference |
| **Frequency** | Very Common |

### Question

When architect batch inference vs real-time online inference for ML workloads?

### Short Answer (30 seconds)

Batch scores large datasets on schedule (nightly churn, bulk recommendations). Real-time scores individual requests at interaction time (fraud, search ranking). Choose based on latency SLA, cost, and score freshness tolerance.

### Detailed Answer (3–5 minutes)

| Dimension | Batch | Real-Time |
|-----------|-------|----------|
| Latency | Minutes to hours | Milliseconds to seconds |
| Infrastructure | Scheduled jobs, spot VMs | Always-on endpoints, autoscale |
| Cost model | Pay per job run | Pay per uptime + QPS |
| Data | Historical snapshot | Live features from online store |
| UX impact | Stale scores unless labeled | Immediate personalization |

**Decision framework:**
1. Does user action require score within 1 second? → Real-time
2. Can UX tolerate 4–24 hour old scores? → Batch
3. Middle ground? → Micro-batch (5-min windows) or near-real-time streaming

**Architect examples:**
- Email campaign churn list → batch nightly on Spark/Azure ML batch endpoint
- Payment fraud → real-time <50ms p99 on dedicated inference pool
- Product recommendations homepage → hybrid: batch candidates + real-time rerank

**Document:** Score freshness in API contract — mobile app must know if recommendations are 6 hours old.

### Architecture Perspective

Inference mode drives infrastructure cost and UX — clarify latency before GPU procurement.

### Follow-up Questions

1. **Streaming inference? — Kafka + Flink scoring — between batch and REST synchronous.**
2. **Cold start for batch? — Event-triggered vs cron — cost and freshness trade-off.**

### Common Mistakes in Interviews

- Real-time GPU endpoint for monthly report scoring
- Batch scores presented as live without freshness disclosure
- No autoscale plan for real-time traffic spikes

---

## Q003: Feature Engineering Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Feature Engineering |
| **Frequency** | Very Common |

### Question

What is a feature engineering pipeline and how do architects design it?

### Short Answer (30 seconds)

Feature pipeline transforms raw data into model-ready features with consistent definitions for training and serving. Architect ensures point-in-time correctness, reproducibility, and training-serving parity.

### Detailed Answer (3–5 minutes)

**Pipeline stages:**
1. **Ingest** — events, DB snapshots, external APIs
2. **Clean** — null handling, outlier caps, type coercion
3. **Transform** — aggregations (7-day spend), encodings, embeddings
4. **Validate** — schema checks, distribution alerts, SLA on freshness
5. **Materialize** — offline store (training) + online store (inference)

**Critical architect concerns:**
- **Training-serving skew** — same SQL/logic in notebook vs prod → feature store solves
- **Point-in-time joins** — features as-of label timestamp — prevents data leakage
- **Feature versioning** — schema change = new model version

**Azure stack:** Spark/Databricks for batch transforms, Azure ML feature store, Redis/Cosmos for online lookup.

**Golden rule:** Feature definition is code in Git — not tribal knowledge in a notebook.

### Architecture Perspective

Feature pipeline is the contract between data engineering and ML — architects enforce parity.

### Follow-up Questions

1. **Feature store day one? — Single model can skip; 3+ models sharing user features → adopt.**
2. **Online feature latency SLA? — <10ms lookup typical for fraud — design accordingly.**

### Common Mistakes in Interviews

- Different feature logic in training notebook vs prod API
- No entity key design (userId vs sessionId confusion)
- Leak future data into training features

---

## Q004: Model Training vs Serving Separation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ML Architecture |
| **Frequency** | Very Common |

### Question

Why separate model training infrastructure from serving infrastructure?

### Short Answer (30 seconds)

Training is batch-oriented, GPU-heavy, bursty, tolerates failure retry. Serving is latency-sensitive, always-on, strict SLO, minimal dependencies. Mixing them causes cost blowout, security exposure, and outage risk.

### Detailed Answer (3–5 minutes)

**Training environment:**
- GPU clusters (NC-series), spot/preemptible OK
- Access to full historical datasets
- Experiment tracking, hyperparameter search
- Data scientist access, notebook-friendly
- No customer traffic dependency

**Serving environment:**
- CPU or right-sized GPU, autoscale on QPS
- Minimal attack surface — no raw training data
- Model artifact from registry only — immutable version
- Strict p99 latency, circuit breakers, rate limits
- Production RBAC, private endpoints

**Handoff:** Training pipeline registers `model v2.3` → approval gate → serving pulls artifact → blue-green traffic shift.

**Architect ADR:** Document why training VPC peers to data lake but serving VPC does not.

### Architecture Perspective

Separation of concerns applies to ML — training cluster compromise must not expose PII lake to internet.

### Follow-up Questions

1. **Train in serving container? — Anti-pattern — dependency bloat and GPU waste.**
2. **ONNX at boundary? — Framework-agnostic artifact between train and serve teams.**

### Common Mistakes in Interviews

- Jupyter notebook server on production inference subnet
- Serving endpoint pulls latest folder not registry version
- Training pipeline has production DB write access

---

## Q005: Build vs Buy ML Platform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

How decide between building a custom ML platform vs buying managed (Azure ML, Databricks)?

### Short Answer (30 seconds)

Buy managed when team <20 ML engineers, need speed to production, standard workloads, and Azure/compliance alignment. Build custom when unique regulatory requirements, deep K8s investment, or platform limits block critical workflows.

### Detailed Answer (3–5 minutes)

| Factor | Buy (Azure ML) | Build (Kubeflow/custom) |
|--------|----------------|-------------------------|
| Time to value | Weeks | Months to years |
| Compliance | Azure certifications inherited | You own audit evidence |
| Customization | Platform feature boundaries | Full control |
| TCO | Subscription OpEx | Engineering headcount |
| Skills | Lower ML ops burden | Requires platform team |

**Hybrid (common enterprise):** Azure ML for training/registry + custom ONNX serving on AKS + existing APIM gateway.

**Architect decision process:**
1. Inventory workloads (tabular, vision, LLM)
2. Assess team skills and headcount
3. 3-year TCO model including GPU spend
4. Data residency and compliance requirements
5. ADR with rejected option documented

**Exit strategy:** Prefer open formats — ONNX, MLflow — avoid proprietary lock-in without migration plan.

### Architecture Perspective

Platform choice is multi-year commitment — align to team size and compliance, not hype.

### Follow-up Questions

1. **Databricks vs Azure ML? — Databricks for Spark-heavy feature eng; AML for Azure-native deploy integration.**
2. **When revisit decision? — Annual review or when team doubles / compliance changes.**

### Common Mistakes in Interviews

- Build Kubeflow with 3 data scientists and no platform engineers
- Buy Azure ML without CI/CD integration plan
- Ignore data residency when selecting region

---

## Q006: ML Lifecycle and MLOps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | MLOps |
| **Frequency** | Very Common |

### Question

Describe the end-to-end ML lifecycle and where MLOps adds architectural value.

### Short Answer (30 seconds)

Lifecycle: problem framing → data → train → evaluate → deploy → monitor → retrain. MLOps adds versioned pipelines, reproducible environments, CI/CD for models, and production monitoring — same rigor as software delivery.

### Detailed Answer (3–5 minutes)

**Stages:**
1. **Problem definition** — metric aligned to business (not just accuracy)
2. **Data engineering** — ingestion, labeling, feature pipelines
3. **Experimentation** — tracked runs, hyperparameter search
4. **Model validation** — holdout, bias, explainability gates
5. **Deployment** — batch or real-time serving with rollback
6. **Monitoring** — drift, latency, business KPI impact
7. **Retrain loop** — triggered by drift or schedule

**MLOps architecture:** Git for code, DVC/MLflow for data+models, pipeline orchestrator (Azure ML Pipelines, Airflow), model registry, feature store, observability stack.

**Architect role:** Define promotion gates (dev → staging → prod), ownership boundaries between data science and platform teams, and SLIs for inference — not just training accuracy.

### Architecture Perspective

MLOps is how ML survives contact with production — interviewers test lifecycle completeness.

### Follow-up Questions

1. **MLOps vs DevOps? — Same principles; ML adds data/model versioning and drift monitoring.**
2. **When skip MLOps? — One-off research prototype — never for revenue-facing models.**

### Common Mistakes in Interviews

- Treating model deployment as 'upload pickle file'
- No monitoring after launch
- Data science team owns production on-call without platform support

---

## Q007: Feature Store Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Feature Engineering |
| **Frequency** | Very Common |

### Question

What is a feature store and when does an enterprise need one?

### Short Answer (30 seconds)

Feature store: centralized repository for curated, versioned features with online (low-latency) and offline (training) serving. Need when multiple models reuse features, training-serving skew is a problem, or teams duplicate feature pipelines.

### Detailed Answer (3–5 minutes)

**Components:**
- **Offline store** — data lake/warehouse for batch training (Parquet, Delta)
- **Online store** — Redis/Cosmos/Dedicated for real-time inference lookups
- **Feature registry** — metadata, lineage, owner, freshness SLA
- **Transformation layer** — point-in-time correct joins for training

**Problems solved:**
- Training-serving skew (different SQL in notebook vs prod)
- Feature reuse across fraud, churn, recommendation models
- Point-in-time correctness for backtesting

**Azure:** Azure ML managed feature store, or Feast on AKS. **Build vs buy:** Start without feature store if single model; adopt at 3+ production models sharing entities (user, product).

### Architecture Perspective

Feature store is the API layer between data engineering and ML — architects define entity model.

### Follow-up Questions

1. **Point-in-time correctness? — Join features as-of label timestamp — prevents leakage.**
2. **Online vs offline latency? — Online <10ms lookup; offline batch for retrain.**

### Common Mistakes in Interviews

- Feature store day one for one model
- No entity key design (userId vs sessionId confusion)
- Ignoring feature freshness SLAs

---

## Q008: Model Registry Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | MLOps |
| **Frequency** | Very Common |

### Question

Design a model registry for a team shipping 20 models per year.

### Short Answer (30 seconds)

Registry stores model artifacts, metadata, metrics, lineage, stage (Staging/Production/Archived), and approval workflow. Integrate with CI/CD — only promoted models deploy to serving endpoints.

### Detailed Answer (3–5 minutes)

**Metadata per model version:**
- Training data snapshot hash
- Metrics (AUC, F1, latency benchmark)
- Framework version (sklearn 1.4, ONNX opset)
- Responsible AI scan results
- Approver and promotion timestamp

**Workflow:**
```
Experiment → Register v2.3 → Staging deploy → A/B test → Approve → Production
```

**Azure ML Model Registry** provides versioning, tags, and deployment integration. **Architect:** Immutable artifacts — never overwrite Production tag; create new version.

### Architecture Perspective

Model registry is source of truth for what runs in production — like container registry for images.

### Follow-up Questions

1. **ONNX in registry? — Framework-agnostic deployment — register conversion artifact.**
2. **Rollback? — Repoint endpoint to previous registry version — seconds not retrain.**

### Common Mistakes in Interviews

- Models stored in shared folder without versioning
- No link between registry entry and training pipeline run
- Production tag moved without approval audit trail

---

## Q009: Batch vs Real-Time Inference

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Inference |
| **Frequency** | Very Common |

### Question

When choose batch inference vs real-time online inference?

### Short Answer (30 seconds)

Batch: score large datasets on schedule (nightly churn, bulk recommendations). Real-time: score single request at interaction time (fraud, search ranking). Decide on latency SLA, cost, and data freshness.

### Detailed Answer (3–5 minutes)

| Dimension | Batch | Real-Time |
|-----------|-------|----------|
| Latency | Minutes–hours | <100ms–1s |
| Cost | Spot/preemptible OK | Always-on endpoints |
| Use case | Email campaigns, reports | Fraud, personalization |
| Data | Historical snapshot | Live features |

**Hybrid:** Near-real-time micro-batch (5-min windows) for middle ground.

**Architect:** Batch on Spark/Azure ML batch endpoints for 10M rows/night; real-time on AKS GPU pool for fraud <50ms p99. Document stale-score tolerance for batch-driven UX.

### Architecture Perspective

Inference mode drives infrastructure cost and UX — clarify latency before choosing GPU clusters.

### Follow-up Questions

1. **Streaming inference? — Kafka + Flink scoring — between batch and REST.**
2. **Cold start batch job? — Schedule vs event-triggered — cost implications.**

### Common Mistakes in Interviews

- Real-time endpoint for nightly report scoring
- Batch scores shown as live personalization without freshness label
- No autoscale plan for real-time traffic spikes

---

## Q010: Model Serving Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Inference |
| **Frequency** | Very Common |

### Question

Compare model serving patterns: embedded, sidecar, dedicated inference service.

### Short Answer (30 seconds)

Embedded: model in app process — simple, tight coupling. Sidecar: model in companion container — isolation, shared pod. Dedicated service: central inference API — reuse, GPU pooling, independent scale.

### Detailed Answer (3–5 minutes)

**Patterns:**
1. **Embedded (.NET ML.NET)** — Low latency local, small models, edge devices
2. **Sidecar (ONNX Runtime container)** — K8s pod with app + inference sidecar
3. **Dedicated microservice** — `POST /score` behind API gateway, GPU node pool
4. **Serverless** — Azure ML managed endpoints, scale-to-zero for sporadic load
5. **Edge** — ONNX on device, cloud for retrain only

**Architect decision matrix:**
- Team autonomy → embedded per service (risk: duplication)
- GPU cost optimization → dedicated pool with queue
- Multi-framework → ONNX/Triton unified server

### Architecture Perspective

Serving pattern affects deploy velocity, GPU utilization, and blast radius.

### Follow-up Questions

1. **Triton Inference Server? — Multi-model GPU sharing — dynamic batching.**
2. **Blue-green model deploy? — Traffic split at gateway — 0% → 10% → 100%.**

### Common Mistakes in Interviews

- Every microservice bundles own GPU
- No health check on model load failure
- Synchronous scoring in request path without timeout

---

## Q011: GPU vs CPU Inference

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Infrastructure |
| **Frequency** | Very Common |

### Question

When is GPU inference justified vs CPU-only?

### Short Answer (30 seconds)

GPU: large neural nets, computer vision, LLM inference, high QPS deep learning. CPU: tree models (XGBoost), linear models, small nets, low QPS. GPU cost 5–20× — justify with throughput/latency math.

### Detailed Answer (3–5 minutes)

**GPU wins when:**
- Model too slow on CPU for p99 SLA
- Batch size amortizes GPU (dynamic batching)
- Transformer/vision models

**CPU wins when:**
- XGBoost/LightGBM tabular (often faster than GPU at small batch)
- <10 QPS simple model
- Edge without GPU hardware

**Azure:** NC-series VMs, Azure ML managed GPU endpoints. **Architect:** Benchmark both — profile with representative batch size. Consider INT8 quantization to run on CPU.

### Architecture Perspective

GPU is expensive — architects require throughput proof not 'we use deep learning'.

### Follow-up Questions

1. **Dynamic batching? — Queue requests 5ms window — higher GPU utilization.**
2. **ONNX quantization? — FP16/INT8 — 2–4× speedup — accuracy trade-off test.**

### Common Mistakes in Interviews

- GPU for logistic regression
- No batching on GPU endpoint — low utilization
- Ignoring CPU-optimized tree models for tabular data

---

## Q012: Model Versioning Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | MLOps |
| **Frequency** | Very Common |

### Question

How version models alongside application code in CI/CD?

### Short Answer (30 seconds)

Semantic versioning for models (v2.1.0), linked to training data hash, code commit, and container image. App references model version via config/registry — not baked into binary without traceability.

### Detailed Answer (3–5 minutes)

**Version tuple:** `model_version + feature_schema_version + training_data_snapshot`.

**CI/CD flow:**
1. Train pipeline produces artifact v2.1.0
2. Automated eval gates pass
3. Register in model registry
4. Deploy to staging endpoint
5. Integration tests against staging
6. Promote — update APIM route or K8s ConfigMap

**Rollback:** Previous version remains in registry — flip traffic in <1 min.

**Architect:** Model version in OpenTelemetry span attributes — debug production predictions.

### Architecture Perspective

Model versioning enables rollback — critical when bad model costs revenue.

### Follow-up Questions

1. **Schema version? — Feature contract change requires new model major version.**
2. **Shadow deployment? — Run new model parallel without serving — compare outputs.**

### Common Mistakes in Interviews

- Overwrite model file at same path
- No link between app deploy and model version
- Feature schema change without retrain

---

## Q013: A/B Testing ML Models

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Experimentation |
| **Frequency** | Common |

### Question

Design A/B test for new fraud model vs production baseline.

### Short Answer (30 seconds)

Split traffic 90/10, compare business metrics (fraud $ prevented, false positive rate), run until statistical significance. Shadow mode first — new model scores but doesn't act.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **Shadow** — Log both scores, production uses old model decisions
2. **Canary** — 5% traffic uses new model for decisions
3. **A/B** — 50/50 or 90/10 with guardrails
4. **Full rollout** — Promote registry stage

**Metrics:** Not just AUC — dollar impact, customer friction (false declines), latency.

**Guardrails:** Auto-rollback if false positive rate exceeds threshold. **Duration:** Minimum 2 weeks to capture weekly patterns.

### Architecture Perspective

ML A/B tests business impact — not offline metrics alone.

### Follow-up Questions

1. **Multi-armed bandit? — Adaptive traffic allocation — faster convergence.**
2. **Sample ratio mismatch? — Ensure random assignment by transactionId hash.**

### Common Mistakes in Interviews

- A/B test only offline holdout metrics
- Stop test after 1 day
- No rollback automation on metric regression

---

## Q014: Data Drift Detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Very Common |

### Question

How detect and respond to data drift in production ML?

### Short Answer (30 seconds)

Monitor input feature distributions (PSI, KL divergence) and output score distributions vs training baseline. Alert on threshold breach → investigate → retrain or rollback.

### Detailed Answer (3–5 minutes)

**Drift types:**
- **Covariate drift** — feature distribution shift (new user demographics)
- **Prior drift** — label base rate change
- **Concept drift** — relationship X→Y changed

**Implementation:**
- Baseline stats at training time stored in registry
- Hourly/daily comparison job (Evidently AI, Azure ML monitoring)
- Dashboard: PSI per feature, alert >0.2

**Response playbook:**
1. Confirm not data pipeline bug
2. Assess business impact on KPIs
3. Emergency retrain or rollback model
4. Root cause — market change vs bug

### Architecture Perspective

Drift detection is early warning — models decay silently without it.

### Follow-up Questions

1. **PSI threshold? — >0.2 significant — tune per feature criticality.**
2. **Label drift without labels? — Proxy metrics — score distribution, business KPI.**

### Common Mistakes in Interviews

- No training baseline stored
- Drift alert with no runbook
- Retrain automatically without human review on critical models

---

## Q015: Model Monitoring in Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Very Common |

### Question

What SLIs monitor for a production recommendation model?

### Short Answer (30 seconds)

Inference latency p99, error rate, throughput, feature null rate, score distribution, click-through rate (business), data drift PSI, and model version in use.

### Detailed Answer (3–5 minutes)

**Technical SLIs:**
- p50/p99 latency < 80ms
- 5xx rate < 0.1%
- Feature pipeline freshness < 5 min lag
- GPU memory utilization

**Model SLIs:**
- Score distribution shift
- Prediction volume per segment
- Fallback rate (default recommendations)

**Business SLIs:**
- CTR, revenue per session — tie ML to outcome

**Azure:** Application Insights + Azure ML model monitoring. **Architect:** SLO error budget — pause experiments if burn rate high.

### Architecture Perspective

Model monitoring bridges ML metrics and business outcomes.

### Follow-up Questions

1. **Data quality monitors? — Null spike in `userAge` — pipeline break not drift.**
2. **Explainability sampling? — Log SHAP for 1% requests — debug bad recommendations.**

### Common Mistakes in Interviews

- Only monitoring infrastructure CPU
- No business metric linkage
- Alerts on every score change without baseline

---

## Q016: Build vs Buy ML Platform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

Decide build custom ML platform vs buy managed (Azure ML, Databricks).

### Short Answer (30 seconds)

Buy managed when team <20 ML engineers, need speed to production, standard workloads. Build when unique compliance, deep customization, or existing K8s investment with MLOps maturity.

### Detailed Answer (3–5 minutes)

| Factor | Buy (Azure ML) | Build (Kubeflow/custom) |
|--------|----------------|-------------------------|
| Time to value | Weeks | Months–years |
| Compliance | Azure certifications | You own audit |
| Customization | Platform limits | Full control |
| Cost | OpEx subscription | Eng headcount |

**Hybrid common:** Azure ML for training/registry + custom serving on AKS.

**Architect ADR:** Document rejected option, 3-year TCO, team skill assessment.

### Architecture Perspective

Platform choice is multi-year commitment — align to team size and compliance.

### Follow-up Questions

1. **Databricks vs Azure ML? — Databricks for Spark-heavy feature eng; AML for Azure-native deploy.**
2. **Exit strategy? — Avoid proprietary formats — ONNX, MLflow open standards.**

### Common Mistakes in Interviews

- Build Kubeflow with 3 data scientists
- Buy platform without integration plan to existing CI/CD
- Ignore data residency requirements

---

## Q017: Azure ML Workspace Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

Design Azure ML workspace topology for enterprise with dev/staging/prod.

### Short Answer (30 seconds)

Separate workspaces or resource groups per environment, shared container registry, central model registry in prod workspace, private endpoints, managed identity, RBAC per team.

### Detailed Answer (3–5 minutes)

**Topology:**
- `aml-dev` — experimentation, open network optional
- `aml-staging` — pre-prod validation, production-like data subset
- `aml-prod` — locked down, approval gates, private link only

**Shared services:** Azure Container Registry, Key Vault (secrets), Application Insights, Storage (datasets with ACLs).

**Networking:** Private endpoints for workspace, storage, ACR. No public scoring endpoints — APIM front door.

**Identity:** Managed identity for compute → storage — no connection strings in notebooks.

### Architecture Perspective

Workspace topology mirrors software environment isolation — prod AML is tier-0.

### Follow-up Questions

1. **Compute clusters vs serverless? — Cluster for heavy train; serverless inference for variable QPS.**
2. **VNet injection? — Required for on-prem data access via ExpressRoute.**

### Common Mistakes in Interviews

- Single workspace for all environments
- Notebook with storage account key in code
- Public managed endpoint for internal model

---

## Q018: Responsible AI Principles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Very Common |

### Question

Apply Microsoft Responsible AI principles to a hiring screening model.

### Short Answer (30 seconds)

Fairness, reliability, privacy, inclusiveness, transparency, accountability — assess each before deploy. Hiring model: bias test across demographics, explainability for adverse decisions, human review gate, audit trail.

### Detailed Answer (3–5 minutes)

**Six principles applied:**
1. **Fairness** — Disparate impact analysis across protected groups
2. **Reliability** — Robust to resume format variations
3. **Privacy** — No PII leakage in features; GDPR lawful basis
4. **Inclusiveness** — Accessible design, multiple input formats
5. **Transparency** — Candidate notification of AI use (EU AI Act)
6. **Accountability** — Named owner, incident process, board review

**Architect:** Responsible AI impact assessment gate in model promotion pipeline — block prod without sign-off.

### Architecture Perspective

Responsible AI is architectural gate — not ethics slide deck only.

### Follow-up Questions

1. **Fairlearn integration? — Toolkit for fairness metrics in Azure ML pipeline.**
2. **High-risk AI system? — EU AI Act conformity assessment — legal involvement.**

### Common Mistakes in Interviews

- Deploy hiring model without bias testing
- No human override for adverse decisions
- Black box with no documentation

---

## Q019: Bias and Fairness Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Very Common |

### Question

How test ML model for bias before production?

### Short Answer (30 seconds)

Define protected attributes, measure metrics per group (equalized odds, demographic parity, calibration), set thresholds, test on holdout — block deploy if disparity exceeds policy.

### Detailed Answer (3–5 minutes)

**Process:**
1. Identify protected groups (gender, age band — legal review)
2. Choose fairness metric aligned to use case
3. Compare false positive/negative rates across groups
4. Mitigate: reweight training, post-processing thresholds, or reject model

**Tools:** Fairlearn, Azure ML responsible AI dashboard.

**Architect:** Fairness requirements in ADR — 'false decline rate disparity <5% across regions.' Automated gate in CI.

### Architecture Perspective

Fairness testing is compliance and reputation — architects define measurable thresholds.

### Follow-up Questions

1. **Equalized odds vs demographic parity? — Often conflict — business/legal picks priority.**
2. **Proxy discrimination? — Zip code correlates with race — feature audit required.**

### Common Mistakes in Interviews

- Accuracy-only evaluation
- Fairness tested only on training set
- No mitigation plan when bias detected

---

## Q020: Explainability with SHAP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Responsible AI |
| **Frequency** | Common |

### Question

When and how use SHAP for model explainability in regulated use cases?

### Short Answer (30 seconds)

SHAP provides per-prediction feature attributions. Use for credit, healthcare, hiring adverse decisions — regulators and users require 'why.' Global SHAP for model review, local SHAP per decision.

### Detailed Answer (3–5 minutes)

**SHAP types:**
- **TreeSHAP** — fast for XGBoost/LightGBM
- **KernelSHAP** — model-agnostic, slow
- **DeepSHAP** — neural networks

**Architecture:**
- Batch SHAP in training pipeline for model validation
- Online SHAP for sampled production requests (latency cost)
- Store explanations in audit log linked to decisionId

**Trade-off:** SHAP adds 50–500ms — async for non-real-time decisions.

### Architecture Perspective

Explainability is audit requirement — design logging into inference path.

### Follow-up Questions

1. **LIME vs SHAP? — SHAP theoretically grounded — preferred for regulatory.**
2. **Explanation to end user? — Plain language template — not raw SHAP values.**

### Common Mistakes in Interviews

- No explanation capability for credit denials
- SHAP on every request killing latency
- Explanations not stored for audit

---

## Q021: ML Pipeline Orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | MLOps |
| **Frequency** | Very Common |

### Question

Design orchestrated ML training pipeline with dependencies and retries.

### Short Answer (30 seconds)

DAG pipeline: ingest → validate → feature eng → train → evaluate → register. Orchestrator (Azure ML Pipelines, Airflow) handles retries, caching, parallel steps, and secrets.

### Detailed Answer (3–5 minutes)

**Pipeline steps:**
```
ingest_raw → data_quality_gate → feature_compute → train → eval_gate → register_model
         ↘ fail_alert          ↘ parallel hyperparam sweeps
```

**Patterns:**
- **Idempotent steps** — safe retry
- **Cached outputs** — skip unchanged upstream steps
- **Conditional** — deploy only if metric > threshold
- **Secrets** — Key Vault references, not parameters

**Architect:** Pipeline as code in Git — reviewed like application code. Schedule + event triggers (new data landed).

### Architecture Perspective

Orchestration turns ad-hoc notebooks into reproducible production systems.

### Follow-up Questions

1. **Azure ML pipeline vs Airflow? — AML native for Azure compute; Airflow if multi-cloud ETL.**
2. **Pipeline failure alert? — PagerDuty on eval_gate fail — data scientist on-call.**

### Common Mistakes in Interviews

- Manual notebook execution for prod retrain
- No data quality gate before train
- Secrets in pipeline YAML

---

## Q022: Training Data Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data Governance |
| **Frequency** | Very Common |

### Question

Govern training data access, lineage, and retention for enterprise ML.

### Short Answer (30 seconds)

Catalog all datasets, classify sensitivity, RBAC access, lineage from source to model, retention policy, approval for prod training data use.

### Detailed Answer (3–5 minutes)

**Controls:**
- **Data catalog** — Purview tags PII, confidential
- **Lineage** — model v2.1 trained on dataset snapshot `2024-06-01`
- **Access** — ABAC: only fraud-team reads fraud labels
- **Retention** — training snapshots 7 years for audit; raw PII minimized
- **Consent** — lawful basis documented per dataset

**Architect:** Training data request workflow — ticket + approval for new sensitive data in models.

### Architecture Perspective

Training data governance prevents compliance incidents and untraceable models.

### Follow-up Questions

1. **Right to erasure? — Retrain without erased users — pipeline must support exclusion list.**
2. **Synthetic data governance? — Same classification rules as real data.**

### Common Mistakes in Interviews

- Data scientists query prod DB directly
- No lineage from model to data snapshot
- Indefinite retention of PII in training sets

---

## Q023: PII in ML Datasets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Privacy |
| **Frequency** | Very Common |

### Question

Handle PII in ML training and inference pipelines?

### Short Answer (30 seconds)

Minimize, pseudonymize, tokenize at ingestion, separate PII store from feature store, encrypt at rest, redact in logs, DPIA for high-risk processing.

### Detailed Answer (3–5 minutes)

**Techniques:**
1. **Minimization** — train on `age_band` not DOB
2. **Pseudonymization** — irreversible hash with salt for join keys
3. **Tokenization** — vault detokenize only when legally required
4. **Differential privacy** — aggregate statistics only for sensitive cohorts
5. **Federated learning** — data stays on device (overview)

**Inference:** Never log raw prompts with PII to monitoring — redact first.

**Azure:** Purview classification, Key Vault, Private Link to data.

### Architecture Perspective

PII in ML is GDPR/CCPA risk — architects design minimization by default.

### Follow-up Questions

1. **Re-identification risk? — Combine quasi-identifiers — k-anonymity assessment.**
2. **LLM training on customer emails? — Separate consent and opt-out pipeline.**

### Common Mistakes in Interviews

- Full names in feature store online lookup
- Training exports with PII to data scientist laptops
- Model explanations expose PII attributes

---

## Q024: Model Deployment Slots

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deployment |
| **Frequency** | Common |

### Question

Use deployment slots for ML model endpoints like App Service slots?

### Short Answer (30 seconds)

Yes — blue-green or slot pattern: staging slot receives new model, smoke test, swap traffic to production slot. Azure ML supports traffic splitting on managed endpoints.

### Detailed Answer (3–5 minutes)

**Pattern:**
- **Slot A (prod)** — model v2.0, 100% traffic
- **Slot B (staging)** — model v2.1, 0% → 10% canary → swap

**Kubernetes:** Two deployments, service selector flip, or Istio traffic weight.

**Rollback:** Swap back — previous model still warm in slot.

**Architect:** Automated smoke tests post-deploy — score known fixtures, compare to golden outputs.

### Architecture Perspective

Deployment slots reduce model deploy risk — same pattern as app deploy.

### Follow-up Questions

1. **Warm-up? — Pre-load model in staging before traffic — avoid cold start spike.**
2. **Slot parity? — Staging must use prod-identical feature pipeline.**

### Common Mistakes in Interviews

- Direct overwrite production endpoint
- No smoke test before traffic shift
- Staging slot uses mock features

---

## Q025: Edge Inference Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Edge AI |
| **Frequency** | Common |

### Question

Design edge inference for manufacturing defect detection on factory floor.

### Short Answer (30 seconds)

ONNX model on edge gateway (Jetson/industrial PC), local inference <50ms, cloud for model updates and aggregated telemetry. Offline tolerance required.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Camera → edge device → ONNX Runtime → defect signal → PLC
- Model updates OTA via IoT Hub/Device Management
- Buffer images locally if cloud unreachable — sync later

**Constraints:** Limited GPU, power, no guaranteed internet.

**Architect:** Model size budget (<50MB), quantization INT8, fallback to rule-based if model fails load.

### Architecture Perspective

Edge inference trades cloud flexibility for latency and offline resilience.

### Follow-up Questions

1. **Split learning? — Edge inference, cloud retrain on aggregated labels.**
2. **Model signing? — Verify OTA artifact signature — supply chain security.**

### Common Mistakes in Interviews

- Cloud-only inference for assembly line stop decision
- Full model re-download daily over factory WiFi
- No offline fallback mode

---

## Q026: Federated Learning Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Distributed ML |
| **Frequency** | Occasional |

### Question

Explain federated learning and when architects consider it.

### Short Answer (30 seconds)

Federated learning trains model across decentralized data without centralizing raw data. Clients compute local gradients, server aggregates (FedAvg). Use when data cannot leave device/hospital/bank branch.

### Detailed Answer (3–5 minutes)

**Use cases:** Mobile keyboard prediction, hospital diagnostics (HIPAA), cross-bank fraud without sharing transactions.

**Challenges:**
- Non-IID data hurts convergence
- Communication cost
- Poisoning attacks on updates
- Complexity vs centralized training

**Architect:** Consider when legal blocks data centralization — not default pattern. Azure confidential computing + FL frameworks emerging.

### Architecture Perspective

Federated learning solves data residency — at significant ML engineering cost.

### Follow-up Questions

1. **FedAvg? — Average client model weights weighted by sample count.**
2. **Differential privacy in FL? — Add noise to gradients — privacy guarantee.**

### Common Mistakes in Interviews

- FL for convenience when data could be centralized
- No secure aggregation
- Ignoring straggler clients slowing rounds

---

## Q027: AutoML — When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AutoML |
| **Frequency** | Common |

### Question

When recommend AutoML vs custom model development?

### Short Answer (30 seconds)

AutoML for baseline models, tabular classification/regression, time series with standard metrics, POC timelines. Custom when domain features, architecture innovation, or explainability control required.

### Detailed Answer (3–5 minutes)

**AutoML fits:**
- First model for churn/fraud baseline
- Citizen data scientist workflows
- Tight deadline POC

**Custom fits:**
- Computer vision with custom architecture
- NLP with domain pretraining
- Strict latency/size constraints
- Novel loss functions

**Azure AutoML:** sweeps algorithms, hyperparameters — exports ONNX. **Architect:** AutoML output is starting point — validate fairness, monitor, iterate.

### Architecture Perspective

AutoML accelerates baseline — not replacement for ML engineering at scale.

### Follow-up Questions

1. **AutoML time budget? — 1 hour vs 24 hour — diminishing returns curve.**
2. **Ensemble from AutoML? — Often best pipeline — deploy winning pipeline.**

### Common Mistakes in Interviews

- AutoML for production without manual validation
- Custom deep learning when XGBoost suffices
- No export to standard format from AutoML

---

## Q028: Custom Model Training Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Training |
| **Frequency** | Common |

### Question

Design training infrastructure for custom PyTorch model at enterprise scale.

### Short Answer (30 seconds)

Distributed training on GPU cluster (Azure ML compute cluster), data on ADLS Gen2, experiment tracking, checkpointing, spot instances for cost, containerized reproducible environment.

### Detailed Answer (3–5 minutes)

**Stack:**
- **Data:** ADLS + mounted dataset to compute
- **Compute:** NC24ads_A100_v4 cluster, auto-scale 0–N
- **Code:** Git commit pinned in job definition
- **Tracking:** MLflow metrics, artifacts
- **Checkpoint:** Every epoch to blob — resume on preemption

**Distributed:** DDP for multi-GPU single node; Horovod/DeepSpeed for multi-node.

**Architect:** Training job budget caps — alert at $500/run. Right-size GPU — don't default to largest.

### Architecture Perspective

Custom training needs reproducibility and cost controls — not open-ended notebook.

### Follow-up Questions

1. **Spot instances? — 60–80% savings — checkpoint mandatory.**
2. **Data locality? — Compute in same region as data — egress cost.**

### Common Mistakes in Interviews

- Training on data scientist laptop for prod model
- No experiment tracking — cannot reproduce best run
- Largest GPU by default without profiling

---

## Q029: ML Cost Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Optimize ML infrastructure costs without sacrificing SLA.

### Short Answer (30 seconds)

Right-size compute, spot/preemptible training, serverless inference for low QPS, model compression, cache frequent predictions, autoscale to zero, schedule batch jobs off-peak.

### Detailed Answer (3–5 minutes)

**Levers:**
| Area | Tactic |
|------|--------|
| Training | Spot VMs, early stopping, smaller experiments |
| Inference | CPU for trees, shared GPU pool, batching |
| Data | Lifecycle tiers — hot SSD, cold blob |
| Features | Precompute vs on-demand — cost trade-off |
| Monitoring | Sample SHAP/explanations — not 100% |

**Unit economics:** $/1000 inferences, $/training run — dashboard for FinOps.

**Architect:** Monthly ML cost review — top 5 expensive endpoints.

### Architecture Perspective

ML GPU bills surprise CFOs — architects own unit economics.

### Follow-up Questions

1. **Scale to zero? — Azure ML serverless — cold start trade-off.**
2. **Model distillation? — Smaller student model — 10× cheaper inference.**

### Common Mistakes in Interviews

- Always-on GPU cluster for dev
- No autoscale on inference
- Ignoring egress from repeated dataset downloads

---

## Q030: ML Architecture ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Write ADR outline for choosing batch vs real-time fraud scoring.

### Short Answer (30 seconds)

Context: 50ms checkout SLA, 2M transactions/day. Decision: real-time XGBoost on CPU endpoint for approve/decline, batch graph model nightly for account-level risk. Consequences: dual pipeline ops, feature store required.

### Detailed Answer (3–5 minutes)

**ADR template for ML:**
1. **Context** — business requirement, constraints
2. **Options** — batch, real-time, hybrid
3. **Decision** — chosen pattern with model type
4. **Consequences** — ops burden, cost, latency
5. **Compliance** — fairness, explainability approach
6. **Metrics** — success criteria

**Library:** ADR-ML-001 batch churn, ADR-ML-002 real-time fraud — searchable repo.

**Review:** Architecture board approves high-risk ML ADRs.

### Architecture Perspective

ML ADRs document trade-offs — prevent re-litigating decisions each quarter.

### Follow-up Questions

1. **Supersede ADR? — Link ADR-ML-002 replaces 001 when migrate to real-time churn.**
2. **Stakeholders? — Risk, legal sign-off on fraud ADR.**

### Common Mistakes in Interviews

- Verbal model architecture decisions
- ADR without rejected alternatives
- No success metrics defined

---
