# Lab 37 — ML Model Serving with Azure ML Endpoint

**Duration:** 2–3 hours

## Objectives
- Deploy a scikit-learn model as Azure ML managed endpoint
- Call from .NET client
- Compare latency: managed endpoint vs Azure OpenAI for classification task

## Steps
1. Register model in Azure ML workspace
2. Create managed online endpoint (CPU, B1 instance)
3. Deploy with blue-green traffic split
4. .NET client with `HttpClient` + API key or AAD token
5. Load test with 100 RPS — record p99

## Deliverable
ADR: When to use custom ML endpoint vs GPT-4 classification prompt.
