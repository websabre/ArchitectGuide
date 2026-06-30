# Week 15 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Integration & Messaging | **Count:** 50

---


## Q001: Service Bus vs Event Grid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

Order placed event — Service Bus or Event Grid?

### Short Answer (30 seconds)

Service Bus: ordered processing, transactions, competing consumers, dead letter. Event Grid: reactive routing, fan-out, Azure resource events, serverless trigger.

### Detailed Answer (3–5 minutes)

**Domain event to microservices:** Service Bus topic. **React to Blob upload:** Event Grid.

**Architect:** Service Bus for business workflows; Event Grid for event-driven automation.

### Architecture Perspective

Messaging product fit is Azure architect essential.

### Follow-up Questions

1. **Service Bus sessions? — Ordered processing per orderId.**
2. **Event Grid delivery retry? — 24 hours with exponential backoff.**

### Common Mistakes in Interviews

- Event Grid for payment command processing
- Service Bus for simple blob notification only
- No DLQ on Service Bus

---

## Q002: Event Hubs for Streaming

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Streaming |
| **Frequency** | Common |

### Question

Design clickstream pipeline with Event Hubs.

### Short Answer (30 seconds)

Producers → Event Hubs partitions (key=userId) → Stream Analytics or Spark → Synapse/Data Lake. Capture to Blob for replay.

### Detailed Answer (3–5 minutes)

**Partitions:** throughput scale unit — plan partition count — hard to change later.

**Consumer groups:** independent readers — analytics vs real-time dashboard.

### Architecture Perspective

Streaming architecture common retail scenario.

### Follow-up Questions

1. **Kafka protocol? — Event Hubs Kafka endpoint — existing clients migrate.**
2. **Retention? — Days to weeks — replay vs cost.**

### Common Mistakes in Interviews

- Single partition 10M events/sec
- Consumer without checkpoint store
- No dead letter for poison events in stream processing

---

## Q003: API Management Role

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | APIM |
| **Frequency** | Very Common |

### Question

Why APIM in front of microservices?

### Short Answer (30 seconds)

Single entry, JWT validation, rate limiting, versioning, developer portal, request transformation, analytics.

### Detailed Answer (3–5 minutes)

**Architect:** External clients → APIM → internal services on private network.

**Policies:** `rate-limit`, `validate-jwt`, `set-backend-service` for routing.

### Architecture Perspective

APIM is API governance layer.

### Follow-up Questions

1. **Internal vs external APIM? — Developer SKU dev; Premium VNet internal prod.**
2. **Self-hosted gateway? — Hybrid on-prem gateway.**

### Common Mistakes in Interviews

- Clients call 10 microservices direct
- No rate limiting public API
- Business logic in APIM policy

---

## Q004: Outbox with Azure Service Bus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Implement transactional outbox with SQL + Service Bus?

### Short Answer (30 seconds)

Same SQL transaction: insert order + insert outbox row. Azure Function or worker polls outbox, sends to Service Bus, marks processed.

### Detailed Answer (3–5 minutes)

**Alternatives:** Debezium CDC from SQL to Event Hubs. **Idempotent consumers** mandatory.

**Architect:** At-least-once publish + idempotent handlers = effectively once.

### Architecture Perspective

Outbox is correct Azure integration pattern.

### Follow-up Questions

1. **Logic Apps poll outbox? — Possible low volume — Function more control.**
2. **Service Bus duplicate detection? — MessageId window — complement outbox.**

### Common Mistakes in Interviews

- Publish before DB commit
- No idempotent consumer
- Outbox relay single instance no HA

---

## Q005: Message Duplication and Idempotency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Service Bus delivers message twice — handle?

### Short Answer (30 seconds)

Idempotent handler with business key dedup table. Service Bus duplicate detection window. Application checks `messageId` processed.

### Detailed Answer (3–5 minutes)

**Payment:** idempotency key + unique constraint on payment reference.

**Architect:** Design all consumers for at-least-once semantics.

### Architecture Perspective

Messaging semantics literacy required.

### Follow-up Questions

1. **Exactly-once Service Bus? — Not guaranteed end-to-end — design idempotent.**
2. **Peek-lock vs receive-delete? — Peek-lock with complete after success.**

### Common Mistakes in Interviews

- Assume single delivery
- Complete message before processing
- No dedup store

---

## Q006: Event-Driven Choreography on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Choreography with Service Bus topics — pitfalls?

### Short Answer (30 seconds)

Hard to see global flow, cyclic dependencies, debugging distributed transactions. Mitigate: distributed tracing, event catalog documentation, compensation events.

### Detailed Answer (3–5 minutes)

**When orchestration better:** Durable Functions for visible saga state.

**Architect:** Start choreography simple; move to orchestration when steps > 5 or compensation complex.

### Architecture Perspective

Choreography vs orchestration Azure implementation.

### Follow-up Questions

1. **Event schema registry? — Azure Schema Registry for Service Bus.**
2. **Dead letter monitoring? — Alert on DLQ depth per subscription.**

### Common Mistakes in Interviews

- Circular event dependencies
- No correlation ID in messages
- Missing compensation events

---

## Q007: Integration Account and B2B

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Occasional |

### Question

EDI B2B integration on Azure?

### Short Answer (30 seconds)

Logic Apps + Integration Account for EDI schemas, partners, agreements. Maps to canonical XML/JSON for internal microservices.

### Detailed Answer (3–5 minutes)

**Modern:** prefer API/JSON partners; EDI when retail/manufacturing requires.

**Architect:** Anti-corruption layer from EDI to domain events.

### Architecture Perspective

Shows breadth beyond greenfield APIs.

### Follow-up Questions

1. **Logic Apps vs Functions integration? — Logic Apps low-code connectors; Functions code-heavy.**
2. **IPaaS cost? — Logic Apps per action — model high volume cost.**

### Common Mistakes in Interviews

- Custom EDI parser in monolith
- No partner certificate rotation
- Logic Apps without error handling

---

## Q008: Dead Letter Queue Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Service Bus DLQ growing — operational response?

### Short Answer (30 seconds)

Alert on DLQ count, dashboard per queue, runbook: inspect message, fix consumer bug, replay to main queue after fix, root cause in postmortem.

### Detailed Answer (3–5 minutes)

**Tools:** Service Bus Explorer, programmatic receive from DLQ.

**Architect:** DLQ not garbage — operational signal.

### Architecture Perspective

DLQ operations separate mature teams.

### Follow-up Questions

1. **Auto-replay dangerous? — Only after fix deployed — manual gate.**
2. **Poison message quarantine? — Separate storage for analysis.**

### Common Mistakes in Interviews

- Ignore DLQ alerts
- Delete DLQ messages without analysis
- No DLQ on critical queues

---

## Q009: Messaging Cost Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Reduce Service Bus and Event Hubs costs?

### Short Answer (30 seconds)

Right-size tier, batch messages, compress payloads, archive to Blob not retain in queue long, serverless Event Hubs for variable load.

### Detailed Answer (3–5 minutes)

**Architect:** Large payloads → Blob storage + event with URL reference.

**Review:** messages per business transaction — optimize chatty publishers.

### Architecture Perspective

Messaging cost scales with volume — design efficiently.

### Follow-up Questions

1. **Premium Service Bus when? — Predictable latency, higher throughput isolation.**
2. **Event Hubs throughput units? — Start low scale with auto-inflate.**

### Common Mistakes in Interviews

- Send full document in every message
- Premium tier for dev environment
- No message size limits documented

---

## Q010: APIM + Functions Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Expose Azure Functions through APIM — pattern?

### Short Answer (30 seconds)

Functions behind internal network or with function key; APIM validates JWT, strips keys, routes `/api/orders` to function backend.

### Detailed Answer (3–5 minutes)

**Security:** never expose function key to clients — APIM injects backend auth.

**Versioning:** `/v1/orders` APIM revision routes to function version.

### Architecture Perspective

Standard serverless API gateway pattern.

### Follow-up Questions

1. **Consumption Functions behind APIM? — Cold start at edge — consider Premium plan.**
2. **OpenAPI import? — APIM imports function OpenAPI definition.**

### Common Mistakes in Interviews

- Function key in mobile app
- Public function URL bypassing APIM
- No JWT validation at gateway

---

## Q011: Service Bus Queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Very Common |

### Question

When do you choose a Service Bus queue over a topic, and how do you design for competing consumers?

### Short Answer (30 seconds)

Use a queue for point-to-point work distribution — one logical consumer pool processes each message once. Topics fan out to multiple independent subscribers.

### Detailed Answer (3–5 minutes)

**Queue pattern:** order-fulfillment queue with 5 worker instances using peek-lock receive — each message handled by exactly one consumer.

**Design:** Enable duplicate detection on business key, set max delivery count (e.g. 10) before DLQ, use sessions only when ordering per entity is required.

**Architect:** Queue = command/work item. Topic = domain event broadcast. Don't use queue when inventory, billing, and analytics all need the same event.

### Architecture Perspective

Queue vs topic is the first Service Bus design fork — interviewers probe whether you understand competing consumers vs pub/sub.

### Follow-up Questions

1. **Queue vs Storage Queue? — Service Bus for enterprise messaging (sessions, transactions, DLQ); Storage Queue for simple high-volume at lowest cost.**
2. **How scale consumers? — Add competing receivers on same queue; partition with sessions if order per key matters.**

### Common Mistakes in Interviews

- Using queue when multiple services need same event
- Receive-delete without idempotent handler
- No max delivery count configured

---

## Q012: Service Bus Topics and Subscriptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Very Common |

### Question

Design a Service Bus topic for OrderPlaced with three subscribers — what subscription filters and rules apply?

### Short Answer (30 seconds)

One topic `order-events`; subscriptions: `inventory-svc` (filter: eventType=OrderPlaced), `notification-svc`, `analytics-svc`. Each subscription is independent with own DLQ.

### Detailed Answer (3–5 minutes)

**Topic:** publisher sends once; N subscriptions receive independently.

**Filters:** SQL filters or correlation filters on `eventType`, `tenantId`. Avoid catch-all subscription without filter — costs and noise.

**Architect:** Subscription = bounded context consumer. Document event catalog: schema, version, subscribers. Use separate subscriptions per service, not shared subscription with in-app routing.

### Architecture Perspective

Topic/subscription is Azure event-driven microservices backbone.

### Follow-up Questions

1. **Forward to another topic? — Subscription forward rules for routing without custom code.**
2. **Subscription auto-delete on idle? — Useful for ephemeral dev; dangerous in prod without review.**

### Common Mistakes in Interviews

- Single subscription shared by three services
- No subscription-level DLQ monitoring
- Publisher knows subscriber implementation details

---

## Q013: Service Bus Sessions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Very Common |

### Question

Order line items must process in sequence per orderId — implement with Service Bus sessions?

### Short Answer (30 seconds)

Set `SessionId = orderId` on send. Consumer accepts session, processes all messages for that order sequentially, then completes session.

### Detailed Answer (3–5 minutes)

**Sessions:** FIFO guarantee per session ID — not global FIFO.

**Pattern:** payment events for order-123 always processed in order; different orders parallel across consumers.

**Architect:** Sessions reduce throughput per session — don't session-key entire platform on low-cardinality key (e.g. `country=US`). Session lock timeout and renewal required for long handlers.

### Architecture Perspective

Sessions solve per-entity ordering — common follow-up to queue design.

### Follow-up Questions

1. **Session lock lost? — Handler must be idempotent; renew lock during long processing.**
2. **Sessions on Premium only? — Available Standard and Premium; Premium for higher throughput.**

### Common Mistakes in Interviews

- Sessions for all messages regardless of ordering need
- Low-cardinality session key causing hot partition
- No lock renewal on 5-minute handler

---

## Q014: Service Bus Partitioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Common |

### Question

When enable partitioning on Service Bus entity and what changes?

### Short Answer (30 seconds)

Partitioning spreads entity across multiple message brokers for throughput. Enable at creation — cannot add later. Trade: ordering only within partition via sessions.

### Detailed Answer (3–5 minutes)

**Use when:** sustained high ingress/egress on single queue/topic exceeds non-partitioned limits.

**Architect:** Plan partition strategy upfront. Partitioned entities still need session ID for per-key order. Geo-DR pairing differs — document MS docs for paired regions.

### Architecture Perspective

Partitioning is capacity planning decision — not toggle-on in crisis.

### Follow-up Questions

1. **Partition key vs session ID? — Related concepts; session routes to partition bucket.**
2. **Migrate non-partitioned to partitioned? — Recreate entity; plan dual-write cutover.**

### Common Mistakes in Interviews

- Enable partitioning after production launch
- Assume global FIFO on partitioned queue
- No throughput measurement before partitioning

---

## Q015: Service Bus Premium Tier

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Common |

### Question

Justify Service Bus Premium over Standard for a payment platform?

### Short Answer (30 seconds)

Premium: dedicated capacity, predictable latency, larger message size (100 MB vs 256 KB Standard with claim check), VNet integration, geo-disaster recovery pairing.

### Detailed Answer (3–5 minutes)

**When Standard enough:** moderate volume, cost-sensitive, no VNet requirement.

**When Premium:** noisy-neighbor isolation, compliance requires private endpoint, sustained >1000 msg/sec per messaging unit, mission-critical latency SLA.

**Architect:** Model messaging units (MUs) and cost vs SLA risk. Premium Messaging SKU bundles with isolated hardware.

### Architecture Perspective

Tier selection ties messaging to enterprise SLA and network design.

### Follow-up Questions

1. **Premium geo-DR? — Alias-based pairing between namespaces in paired regions.**
2. **Auto-scaling MUs? — Premium supports messaging unit scale within namespace.**

### Common Mistakes in Interviews

- Premium for dev/test environments
- Standard with 10 MB messages without claim check pattern
- No VNet requirement cited but Premium chosen for hype

---

## Q016: Event Grid System Topics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event Grid |
| **Frequency** | Very Common |

### Question

React to BlobCreated in Storage without polling — Event Grid system topic design?

### Short Answer (30 seconds)

Enable system topic on storage account; Event Subscription filters event type `Microsoft.Storage.BlobCreated` → Function or Logic App webhook endpoint.

### Detailed Answer (3–5 minutes)

**System topics:** Azure resource publishes automatically — no custom publisher code.

**Flow:** upload to `incoming/` container → Event Grid → virus scan Function → move to `clean/`.

**Architect:** Prefer Event Grid over Storage polling for reactive automation. RBAC: Event Grid needs permission to deliver to destination (e.g. Function with RBAC trigger).

### Architecture Perspective

System topics are default Azure-native event routing.

### Follow-up Questions

1. **Event delivery schema? — Event Grid envelope with `data` payload per resource provider.**
2. **Dead letter for failed delivery? — Configure storage blob DLQ destination on subscription.**

### Common Mistakes in Interviews

- Polling blob container every minute
- No filter — all storage events to one handler
- Missing managed identity on Event Grid subscription

---

## Q017: Event Grid Custom Topics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event Grid |
| **Frequency** | Very Common |

### Question

Publish domain events from order microservice via Event Grid custom topic?

### Short Answer (30 seconds)

Create custom topic; order service publishes CloudEvents/EG schema via REST or SDK with SAS key or MI. Subscribers create event subscriptions with filters.

### Detailed Answer (3–5 minutes)

**Custom topic:** your application is publisher — decouples subscribers from order API.

**Security:** prefer managed identity + RBAC (`EventGrid Data Sender`) over long-lived keys.

**Architect:** Custom topic for external/partner fan-out; Service Bus often better for ordered transactional workflows with DLQ semantics.

### Architecture Perspective

Custom topics bridge application events to Azure serverless consumers.

### Follow-up Questions

1. **CloudEvents on custom topic? — Supported — improves portability.**
2. **Input schema validation? — Event Grid advanced filtering and partner topics.**

### Common Mistakes in Interviews

- Direct HTTP calls from publisher to every subscriber
- Shared SAS key in all microservices
- Custom topic for payment command with strict ordering

---

## Q018: Event Grid Domains

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event Grid |
| **Frequency** | Common |

### Question

When use Event Grid domain vs multiple custom topics?

### Short Answer (30 seconds)

Domain: single endpoint managing thousands of topics (multi-tenant SaaS). Each tenant gets topic within domain. Centralized auth and quota.

### Detailed Answer (3–5 minutes)

**SaaS pattern:** domain `contoso-events.azure.net` → topic per tenant `tenant-abc` → their subscriptions.

**Architect:** Domain reduces management overhead at scale (10K tenants). Custom topic per bounded context for simpler estates (<50 topics).

### Architecture Perspective

Domains are multi-tenant event routing control plane.

### Follow-up Questions

1. **Domain RBAC? — Assign at domain or topic level per tenant isolation.**
2. **Domain throughput limits? — Plan partition across domains if exceeding quotas.**

### Common Mistakes in Interviews

- Separate custom topic per tenant at 5000 tenants
- No tenant isolation on domain RBAC
- Domain for single-app three events only

---

## Q019: Event Hubs Partitions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event Hubs |
| **Frequency** | Very Common |

### Question

Size Event Hubs partition count for 50K events/sec clickstream?

### Short Answer (30 seconds)

Throughput scales with partitions — plan partition count at creation (increase limited). Partition key (userId) ensures related events land same partition for ordered consumer read.

### Detailed Answer (3–5 minutes)

**Rule of thumb:** 1 MB/s ingress per throughput unit; partitions distribute load. Consumer groups read the read load — one consumer instance per partition max for balanced read.

**Architect:** Cannot easily shrink partitions — over-provision with growth plan. Hot partition if poor key choice (e.g. constant key).

### Architecture Perspective

Partition planning is irreversible Event Hubs decision.

### Follow-up Questions

1. **Partition vs consumer group? — Partitions = write scale; consumer groups = independent readers.**
2. **Auto-inflate TUs? — Scale throughput units; partitions fixed at create.**

### Common Mistakes in Interviews

- Single partition for high-volume stream
- Random partition key when per-user order needed
- More consumers than partitions expecting scale

---

## Q020: Event Hubs Capture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event Hubs |
| **Frequency** | Common |

### Question

Enable Capture on Event Hubs for analytics replay — configuration?

### Short Answer (30 seconds)

Capture writes Avro files to ADLS/Blob on time (e.g. 5 min) or size window. Downstream Synapse/Spark reads lake; stream processor handles real-time path.

### Detailed Answer (3–5 minutes)

**Benefits:** cheap long-term retention vs keeping in Event Hubs; replay for ML retraining.

**Architect:** Capture + Stream Analytics = lambda architecture on Azure. Set lifecycle policy on capture container to cool/archive tiers.

### Architecture Perspective

Capture is batch archive complement to real-time stream.

### Follow-up Questions

1. **Capture vs Consumer reading to lake? — Capture automatic, no consumer code maintenance.**
2. **Avro schema evolution? — Plan compatibility in downstream Spark jobs.**

### Common Mistakes in Interviews

- Retain all events in Event Hubs 365 days
- No capture for compliance audit trail
- Capture container public access enabled

---

## Q021: Event Hubs Kafka Endpoint

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event Hubs |
| **Frequency** | Common |

### Question

Migrate on-prem Kafka producers to Azure without code change?

### Short Answer (30 seconds)

Event Hubs Kafka surface — same bootstrap `*.servicebus.windows.net:9093` with connection string or OAuth. Existing Kafka clients connect with minimal config change.

### Detailed Answer (3–5 minutes)

**Limits:** not 100% Kafka API parity — verify admin operations and exact protocol features.

**Architect:** Accelerates migration lift-and-shift. Long-term evaluate native Event Hubs SDK for Azure optimizations. Enable Kafka on existing namespace.

### Architecture Perspective

Kafka endpoint is migration bridge not eternal architecture.

### Follow-up Questions

1. **Kafka vs native AMQP? — Kafka for existing clients; AMQP for Azure-native greenfield.**
2. **Schema Registry with Kafka endpoint? — Azure Schema Registry integrates.**

### Common Mistakes in Interviews

- Assume full Kafka broker feature parity
- No TLS/SASL config update in clients
- Kafka endpoint without monitoring partition lag

---

## Q022: Azure Relay Hybrid Connections

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Expose on-prem SQL to Azure Function without VPN — Relay Hybrid Connection?

### Short Answer (30 seconds)

Install Hybrid Connection Manager on-prem; Relay namespace hybrid connection maps TCP endpoint. Azure Function/App connects outbound through Relay — no inbound firewall hole.

### Detailed Answer (3–5 minutes)

**vs VPN/ExpressRoute:** Relay for single endpoint quick connect; VPN for full network mesh.

**Architect:** Hybrid Connections for legacy SOAP/SQL during migration. Not replacement for Private Link long-term — latency and ops overhead higher.

### Architecture Perspective

Relay solves hybrid reach without site-to-site VPN for one service.

### Follow-up Questions

1. **Hybrid vs Private Link? — Private Link for Azure PaaS; Relay for on-prem TCP.**
2. **HCM high availability? — Multiple HCM instances for redundancy.**

### Common Mistakes in Interviews

- Open inbound SQL port to Azure IP range
- Relay for all microservice traffic instead of VPN
- Single HCM node no HA

---

## Q023: Logic Apps Consumption vs Standard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Logic Apps |
| **Frequency** | Very Common |

### Question

Choose Logic Apps Consumption vs Standard for B2B EDI workflow?

### Short Answer (30 seconds)

Standard: VNet integration, fixed predictable cost, Integration Account, long-running workflows, single-tenant isolation. Consumption: serverless pay-per-action, quick integrations, no VNet.

### Detailed Answer (3–5 minutes)

**EDI high volume:** Standard in ASE or dedicated plan — action cost at scale breaks Consumption economics.

**Architect:** Consumption for webhooks and simple connectors; Standard for enterprise integration with on-prem gateways and private APIs.

### Architecture Perspective

Plan selection drives integration cost and network posture.

### Follow-up Questions

1. **Consumption limits? — Run duration, connector throttling, no VNet.**
2. **Stateful workflows Standard? — Better for long B2B processes with human approval.**

### Common Mistakes in Interviews

- Consumption for high-volume EDI 500K actions/day
- Standard without VNet when calling private API
- Logic App for core synchronous OLTP path

---

## Q024: API Management Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | APIM |
| **Frequency** | Very Common |

### Question

Implement JWT validation, header injection, and backend routing in APIM policy pipeline?

### Short Answer (30 seconds)

Inbound: `validate-jwt` → `set-header` correlation ID → `set-backend-service` based on `/v2/` path. Outbound: strip internal headers. On-error: return JSON problem details.

### Detailed Answer (3–5 minutes)

**Policy scopes:** global → product → API → operation — narrowest wins.

**Architect:** Keep business logic out of policies — gateway concerns only (auth, rate limit, routing, transformation). Version policies in Git with APIM DevOps.

### Architecture Perspective

Policy pipeline is APIM architect core skill.

### Follow-up Questions

1. **Policy expressions vs fragments? — Fragments reuse across APIs.**
2. **Trace policy for debug? — Enable in dev; disable prod verbose trace.**

### Common Mistakes in Interviews

- 500 lines business rules in XML policy
- No validate-jwt on external API
- Policies edited only in portal not IaC

---

## Q025: APIM Rate Limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | APIM |
| **Frequency** | Very Common |

### Question

Design tiered rate limits: 100 req/min free, 10K partner?

### Short Answer (30 seconds)

Products per tier with `rate-limit` or `quota` policies keyed by subscription. `rate-limit-by-key` on `context.Subscription.Id` or JWT claim `partnerId`.

### Detailed Answer (3–5 minutes)

**429 response:** include `Retry-After`. Combine with Azure Front Door rate limiting for DDoS edge layer.

**Architect:** Rate limit at gateway — protect backends uniformly. Document limits in developer portal. Monitor 429 metrics per product.

### Architecture Perspective

Rate limiting protects platform and enables monetization tiers.

### Follow-up Questions

1. **Rate limit vs quota? — Rate = per window burst; quota = total over period.**
2. **Bypass for internal callers? — Separate product or IP filter policy.**

### Common Mistakes in Interviews

- Rate limit in each microservice differently
- No 429 or Retry-After header
- Unlimited public API on launch

---

## Q026: APIM OAuth and OIDC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | APIM |
| **Frequency** | Very Common |

### Question

Secure APIM API with Entra ID OAuth 2.0 client credentials and user delegation?

### Short Answer (30 seconds)

Register API in Entra; APIM `validate-jwt` with tenant issuer and audience. Client credentials for service-to-service; auth code + PKCE for user-facing apps via developer portal OAuth config.

### Detailed Answer (3–5 minutes)

**Pattern:** mobile app → auth code → bearer token → APIM validates → forwards to backend with optional `Authorization` or managed identity to backend.

**Architect:** Never pass client secret to mobile. APIM caches JWKS. Separate app registrations per environment.

### Architecture Perspective

OAuth at gateway is standard Azure API security pattern.

### Follow-up Questions

1. **OAuth 2.0 vs Easy Auth? — APIM for external API; Easy Auth for App Service direct.**
2. **Certificate-bound tokens? — CAE and continuous access evaluation with CA policies.**

### Common Mistakes in Interviews

- API key only for partner integration
- validate-jwt without audience check
- Same app registration prod and dev

---

## Q027: APIM Self-Hosted Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | APIM |
| **Frequency** | Common |

### Question

Deploy APIM self-hosted gateway for on-prem API consumers?

### Short Answer (30 seconds)

Self-hosted gateway container in on-prem K8s/VM connects outbound to APIM control plane in cloud. Local traffic stays local; policies sync from cloud.

### Detailed Answer (3–5 minutes)

**Use cases:** hybrid latency-sensitive, data residency requires local gateway termination, air-gapped edge sites.

**Architect:** Premium APIM feature. Control plane cloud; data plane local. HA: multiple gateway replicas.

### Architecture Perspective

Self-hosted gateway extends APIM to hybrid edge.

### Follow-up Questions

1. **vs Azure API gateway on AKS? — APIM policy consistency across cloud and edge.**
2. **Gateway upgrade? — Container image updates from APIM; plan rolling update.**

### Common Mistakes in Interviews

- Self-hosted without HA replicas
- Developer SKU expecting self-hosted
- All traffic through cloud APIM adding latency unnecessarily

---

## Q028: Integration Account B2B

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Configure Integration Account for partner onboarding and EDI X12?

### Short Answer (30 seconds)

Integration Account stores schemas, maps, partners, agreements. Logic Apps uses account for encode/decode AS2/X12, validate against schema, transform to canonical JSON.

### Detailed Answer (3–5 minutes)

**Partner record:** AS2 identifier, certificate, MDN settings. **Agreement:** links partners with protocol settings.

**Architect:** Anti-corruption layer — EDI → canonical Order domain event → Service Bus. Rotate partner certs before expiry with monitoring.

### Architecture Perspective

Integration Account is Azure iPaaS B2B anchor.

### Follow-up Questions

1. **Integration Account tier? — Basic vs Standard for HL7/X12 features.**
2. **Maps vs Liquid transforms? — Liquid in Logic Apps for JSON/XML mapping.**

### Common Mistakes in Interviews

- Custom EDI parser in monolith
- Partner cert expiry not monitored
- No error handling on decode failure

---

## Q029: AS2 EDI Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Occasional |

### Question

Design AS2 receive flow for retail partner PO files on Azure?

### Short Answer (30 seconds)

Logic App AS2 receive trigger → Integration Account agreement validates signature/decrypt → parse X12 850 → map to JSON → Service Bus `PurchaseOrderReceived`.

### Detailed Answer (3–5 minutes)

**AS2:** HTTPS + signing/encryption + MDN async/sync acknowledgment.

**Architect:** Store raw EDI in Blob for audit 7 years. DLQ failed parses. Idempotent on PO number. Compare with managed SFTP + Function for simpler partners.

### Architecture Perspective

AS2 shows legacy integration competence.

### Follow-up Questions

1. **AS2 vs SFTP? — AS2 real-time HTTP push; SFTP batch file drop.**
2. **MDN failure handling? — Retry and partner alert; poison quarantine.**

### Common Mistakes in Interviews

- Skip MDN acknowledgment
- No raw archive for compliance
- Process PO before signature validation

---

## Q030: Azure Functions Durable Orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

Implement order saga with Durable Functions vs Service Bus choreography?

### Short Answer (30 seconds)

Durable orchestrator: call inventory (activity) → payment → shipping with compensating transactions on failure. State persisted in storage table — visible workflow.

### Detailed Answer (3–5 minutes)

**When Durable:** complex branching, human approval timers, need orchestration visibility.

**When Service Bus:** loose coupling, many subscribers, event-native teams.

**Architect:** Durable = orchestration; Service Bus topics = choreography. Sub-orchestrations for nested flows.

### Architecture Perspective

Orchestration choice is integration architecture classic.

### Follow-up Questions

1. **Durable vs Logic Apps? — Code-heavy logic Durable; connector-rich low-code Logic Apps.**
2. **Fan-out fan-in pattern? — Durable Task API parallel activities with timeout.**

### Common Mistakes in Interviews

- Choreography for 12-step order with compensation
- Durable for simple fire-and-forget notification
- No idempotent activities in orchestration

---

## Q031: Messaging Idempotency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Design idempotent Service Bus consumer for payment capture?

### Short Answer (30 seconds)

Store processed `messageId` or business key `paymentId` in SQL with unique constraint. Handler checks before side effect; complete message only after commit.

### Detailed Answer (3–5 minutes)

**At-least-once delivery:** assume duplicates. **Effectively-once:** idempotent write + dedup table.

**Architect:** Idempotency key propagated from API through outbox to message properties. TTL dedup table to bound storage.

### Architecture Perspective

Idempotency is non-negotiable for messaging consumers.

### Follow-up Questions

1. **Idempotency vs duplicate detection? — Broker window vs app-level permanent dedup.**
2. **Outbox + idempotent consumer together? — Yes — standard production pattern.**

### Common Mistakes in Interviews

- Complete message before DB commit
- Assume exactly-once Service Bus delivery
- No dedup for financial side effects

---

## Q032: Dead Letter Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Operational playbook when Service Bus DLQ depth exceeds threshold?

### Short Answer (30 seconds)

Alert → triage sample messages → classify poison vs transient → fix consumer → replay via script to main queue after deploy → postmortem root cause.

### Detailed Answer (3–5 minutes)

**Tools:** Service Bus Explorer, `ServiceBusReceiver` on sub-queue `$deadletterqueue`. **Never** auto-replay all without fix.

**Architect:** DLQ metrics per subscription in dashboard. Runbook linked in alert. Separate DLQ for manual review vs automated retry queue.

### Architecture Perspective

DLQ operations separate mature integration teams.

### Follow-up Questions

1. **DLQ retention? — Messages persist until explicitly removed — capacity plan.**
2. **Move to Blob for analysis? — Export poison payload for dev reproduction.**

### Common Mistakes in Interviews

- Delete DLQ messages without analysis
- No alert on DLQ growth
- Auto-replay before fix deployed

---

## Q033: Message Size Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Common |

### Question

Service Bus 256 KB limit blocks large order payload — pattern?

### Short Answer (30 seconds)

Claim check: upload document to Blob; message carries URL + SAS token or MI-accessible path + metadata. Consumer fetches payload from storage.

### Detailed Answer (3–5 minutes)

**Standard limit:** 256 KB message; Premium up to 100 MB but claim check still best practice.

**Architect:** Keep messages lean for throughput and cost. Compress small JSON if near limit. Event Grid + Blob pattern same principle.

### Architecture Perspective

Claim check is universal large-payload messaging pattern.

### Follow-up Questions

1. **Batch send for small messages? — `ServiceBusMessageBatch` reduces round trips.**
2. **Event Hubs 1 MB event limit? — Same claim check applies.**

### Common Mistakes in Interviews

- Embed 2 MB PDF in message body
- Public SAS on blob in message forever
- Ignore size in load test design

---

## Q034: Schema Registry for Event Hubs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Schema |
| **Frequency** | Common |

### Question

Enforce Avro schema evolution for Event Hubs producers and consumers?

### Short Answer (30 seconds)

Azure Schema Registry in Event Hubs namespace; producers register schema; serialize with schema ID; consumers deserialize with compatibility mode (backward/forward).

### Detailed Answer (3–5 minutes)

**Benefits:** contract enforcement, fewer deserialization failures, documentation.

**Architect:** CI validates schema compatibility before deploy. Version bump strategy: add optional fields backward compatible. Link to event catalog in repo.

### Architecture Perspective

Schema registry prevents silent contract breaks in streaming.

### Follow-up Questions

1. **Schema Registry vs Protobuf? — Azure SR supports Avro primary; JSON Schema emerging.**
2. **Incompatible schema deploy? — Block in pipeline with compatibility check API.**

### Common Mistakes in Interviews

- Undocumented JSON blobs in stream
- Breaking rename field without version
- No schema in code repo

---

## Q035: CloudEvents Format

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Standards |
| **Frequency** | Common |

### Question

Standardize cross-service events with CloudEvents 1.0 on Azure?

### Short Answer (30 seconds)

Wrap payload: `specversion`, `type`, `source`, `id`, `time`, `datacontenttype`. Publish to Event Grid or Service Bus application properties + JSON body.

### Detailed Answer (3–5 minutes)

**Interoperability:** Knative, AWS EventBridge, on-prem tools understand CloudEvents.

**Architect:** Map domain event names to `type` (`com.contoso.order.placed.v1`). `id` for dedup. Event Grid natively supports CloudEvents schema.

### Architecture Perspective

CloudEvents is portable event envelope standard.

### Follow-up Questions

1. **CloudEvents vs custom envelope? — Standard wins multi-cloud and tooling.**
2. **Binary vs structured mode? — Structured JSON common on HTTP; binary for AMQP.**

### Common Mistakes in Interviews

- Inconsistent event headers per team
- No version in event type string
- Duplicate id across publishers

---

## Q036: Saga with Service Bus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Implement compensating saga for travel booking with Service Bus?

### Short Answer (30 seconds)

Choreography: `BookingStarted` → reserve flight/hotel/car via subscriptions; failures publish `BookingFailed` triggering compensating `Release*` events. Correlation ID ties saga.

### Detailed Answer (3–5 minutes)

**Orchestration alternative:** Durable Functions central coordinator.

**Architect:** Document saga state transitions. Timeout events for stuck steps. Idempotent compensation — `ReleaseFlight` safe if already released.

### Architecture Perspective

Saga pattern is distributed transaction interview staple.

### Follow-up Questions

1. **Saga vs 2PC? — No distributed locks — eventual consistency accepted.**
2. **Monitoring saga? — App Insights with correlation across messages.**

### Common Mistakes in Interviews

- Synchronous chain of 6 REST calls
- Missing compensation on partial failure
- No saga timeout handling

---

## Q037: Outbox with Azure SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Transactional outbox: SQL order insert + Service Bus publish atomically?

### Short Answer (30 seconds)

Same transaction inserts order row and outbox row (`status=pending`). Background worker polls or SQL trigger → Function sends to Service Bus → marks `processed`.

### Detailed Answer (3–5 minutes)

**Alternatives:** Debezium CDC, SQL Server Change Tracking to Event Hubs.

**Architect:** Polling interval vs latency trade-off. Index outbox on status+created. Horizontal scale workers with lease pattern to avoid double-send.

### Architecture Perspective

Outbox solves dual-write problem correctly.

### Follow-up Questions

1. **Outbox vs dual write? — Dual write loses consistency on partial failure.**
2. **At-least-once outbox relay? — Idempotent consumer handles duplicate send.**

### Common Mistakes in Interviews

- Publish to Service Bus before SQL commit
- No outbox cleanup/archival
- Single worker SPOF without lease

---

## Q038: Inbox Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

Implement inbox pattern alongside outbox for incoming Service Bus messages?

### Short Answer (30 seconds)

Consumer transaction: insert inbox record with messageId (unique) → process business logic → mark processed. Duplicate delivery hits unique constraint — skip safely.

### Detailed Answer (3–5 minutes)

**Pairs with outbox** for end-to-end reliability in integration service.

**Architect:** Inbox table per consumer service. Same DB as business write for single transaction. Cleanup processed inbox rows on schedule.

### Architecture Perspective

Inbox completes consumer-side idempotency story.

### Follow-up Questions

1. **Inbox vs dedup cache? — Inbox durable audit trail; Redis dedup faster but volatile.**
2. **Process then insert inbox? — Wrong order — insert first in same TX as handler.**

### Common Mistakes in Interviews

- Handler side effects before inbox insert
- No unique constraint on messageId
- Inbox table unbounded growth

---

## Q039: Event-Driven Microservices on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Draw Azure event-driven reference for e-commerce microservices?

### Short Answer (30 seconds)

Sync: APIM → order API. Async: OrderPlaced/OrderShipped on Service Bus topic → inventory, notification, analytics subscriptions. Outbox from writers. Event Grid for infra events.

### Detailed Answer (3–5 minutes)

**Principles:** choreograph by default; orchestrate when needed; schema registry; DLQ everywhere; correlation IDs.

**Architect:** Bounded context owns its events. No shared database — events are contract.

### Architecture Perspective

Event-driven is week 15 synthesis architecture.

### Follow-up Questions

1. **Event notification vs event-carried state? — Prefer slim events + query API for large state.**
2. **Azure Service Bus vs Event Hubs for domain events? — Service Bus for business messaging; Event Hubs for telemetry firehose.**

### Common Mistakes in Interviews

- Distributed monolith via shared DB
- Synchronous mesh between all services
- No event versioning strategy

---

## Q040: CQRS with Service Bus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

Separate read model updates using Service Bus after command side write?

### Short Answer (30 seconds)

Command API writes to SQL → outbox → `OrderUpdated` event → projection handler updates Cosmos/read store or Elasticsearch.

### Detailed Answer (3–5 minutes)

**Benefits:** scale reads independently, optimized query models.

**Architect:** Accept eventual consistency lag (seconds). Version projections for schema change. Separate consumer group/subscription for read model updater.

### Architecture Perspective

CQRS on Azure commonly uses messaging for projection pipeline.

### Follow-up Questions

1. **CQRS vs CRUD? — CQRS when read/write shapes diverge significantly.**
2. **Replay projections? — Rebuild read model from event log or replay topic.**

### Common Mistakes in Interviews

- Same table for command and complex read joins
- No lag monitoring on projection
- Projection update synchronous in command API

---

## Q041: Webhooks vs Polling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

Partner asks webhook vs your polling their API — decision criteria?

### Short Answer (30 seconds)

Webhooks: real-time, efficient, requires public endpoint or Event Grid partner topic, signature verification, retry logic. Polling: simpler firewall, higher latency, rate limit risk.

### Detailed Answer (3–5 minutes)

**Azure:** expose webhook via APIM with HMAC validation; or Logic App recurrence poll with delta token.

**Architect:** Prefer webhooks at scale; polling for legacy partners without push capability. Idempotent webhook handler — partners retry.

### Architecture Perspective

Push vs pull integration is common partner discussion.

### Follow-up Questions

1. **Webhook security? — HMAC-SHA256 signature, timestamp anti-replay, IP allowlist.**
2. **Event Grid webhook delivery? — Built-in retry and DLQ.**

### Common Mistakes in Interviews

- Poll every 10 seconds at 1000 partners
- Webhook without signature verification
- No idempotency on webhook retries

---

## Q042: Async API Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Very Common |

### Question

Design async REST API: submit job returns 202 with status URL?

### Short Answer (30 seconds)

POST `/reports` → 202 Accepted + `Location: /reports/{id}/status` + optional `Retry-After`. Client polls status or registers webhook callback URL. Result in Blob when complete.

### Detailed Answer (3–5 minutes)

**Headers:** `Operation-Location`, correlation ID. **Storage:** job state in Table/Cosmos.

**Architect:** Never block HTTP 30s for long work — Service Bus + Functions backend. Document async pattern in OpenAPI.

### Architecture Perspective

Async API pattern prevents gateway timeouts and improves UX at scale.

### Follow-up Questions

1. **vs gRPC streaming? — Async REST for broad client compatibility.**
2. **Cancel async operation? — DELETE on operation ID signals cancellation token to worker.**

### Common Mistakes in Interviews

- HTTP 200 after 45 second report generation
- No status endpoint for 202
- Lost jobs without durable state store

---

## Q043: Backpressure in Messaging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Consumers fall behind producers — apply backpressure on Azure?

### Short Answer (30 seconds)

Monitor queue depth lag; scale out consumers (KEDA); throttle producers via 429 from API; max queue size policy; pause non-critical publishers.

### Detailed Answer (3–5 minutes)

**KEDA:** scale Function/ACA on Service Bus queue length. **Architect:** Define SLA max lag (e.g. 5 min). Alert on age of oldest message. Premium Service Bus for headroom.

### Architecture Perspective

Backpressure protects downstream from overload collapse.

### Follow-up Questions

1. **Prefetch count tuning? — Higher prefetch throughput but uneven if consumer slow.**
2. **Dead letter old messages? — Only if business allows — usually the scale out.**

### Common Mistakes in Interviews

- Unbounded queue with no lag alerts
- Single consumer on growing queue
- Producer ignores 503 backpressure signal

---

## Q044: KEDA Service Bus Scaler

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Configure KEDA to scale AKS deployment on Service Bus queue depth?

### Short Answer (30 seconds)

Install KEDA; ScaledObject references deployment; trigger `azure-servicebus` with connection string or frontend length threshold (e.g. scale at 100 messages per pod).

### Detailed Answer (3–5 minutes)

**Auth:** workload identity preferred over connection string in ScaledObject.

**Architect:** minReplicas > 0 for latency-sensitive; maxReplicas cap cost. Cooldown prevents flapping.

### Architecture Perspective

KEDA connects messaging metrics to compute scale.

### Follow-up Questions

1. **KEDA vs HPA CPU? — KEDA event-driven; HPA for CPU-bound sync APIs.**
2. **Multiple triggers? — Combine Service Bus + CPU in ScaledObject.**

### Common Mistakes in Interviews

- CPU-only HPA on queue worker
- maxReplicas unlimited cost surprise
- Connection string in ScaledObject YAML in git

---

## Q045: Functions Service Bus Trigger

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

Configure Azure Function Service Bus trigger with peek-lock and retry?

### Short Answer (30 seconds)

Trigger on queue/subscription; `autoCompleteMessages: false` for manual complete after success; `maxAutoLockRenewalDuration` for long handlers; poison → DLQ after max deliveries.

### Detailed Answer (3–5 minutes)

**Settings:** batch size, prefetch, session handler for session-enabled entity.

**Architect:** Function Premium or dedicated plan for VNet + always-ready instances on critical queues.

### Architecture Perspective

Functions trigger is default Azure message consumer.

### Follow-up Questions

1. **Trigger vs Runbook? — Function for code; Logic App for connector workflows.**
2. **Managed identity trigger auth? — RBAC `Azure Service Bus Data Receiver`.**

### Common Mistakes in Interviews

- autoComplete true before DB commit
- Consumption plan cold start on critical queue
- No DLQ configured on subscription

---

## Q046: Ordering Guarantees

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

What ordering guarantees exist across Azure messaging services?

### Short Answer (30 seconds)

Service Bus sessions: FIFO per session ID. Event Hubs: order within partition. Event Grid: no ordering guarantee. Standard queues: no global order.

### Detailed Answer (3–5 minutes)

**Design:** assign session/partition key deliberately. Don't assume cross-partition order.

**Architect:** Sequence numbers for gap detection. Reorder buffer in consumer if minor disorder acceptable.

### Architecture Perspective

Ordering guarantees vary — architects match service to requirement.

### Follow-up Questions

1. **Global order requirement? — Single session/partition bottleneck — often wrong design.**
2. **Out-of-order handling? — Version field + discard stale updates.**

### Common Mistakes in Interviews

- Assume Event Grid ordered delivery
- Random partition key needing order
- No sequence number in event schema

---

## Q047: Duplicate Detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Common |

### Question

Enable Service Bus duplicate detection for idempotent publishes?

### Short Answer (30 seconds)

Set `MessageId` or duplicate detection history window on queue/topic; broker drops duplicate within window (default 10 min, max 7 days).

### Detailed Answer (3–5 minutes)

**Complements** application idempotency — not replacement.

**Architect:** Use business key as MessageId for natural dedup (`order-123-placed`). Enable at entity creation. Document window for ops.

### Architecture Perspective

Broker duplicate detection reduces consumer load.

### Follow-up Questions

1. **Duplicate detection vs sessions? — Orthogonal features both can enable.**
2. **Window expired duplicate? — App-level dedup still required.**

### Common Mistakes in Interviews

- Random GUID MessageId every retry
- Duplicate detection disabled on payment queue
- Assume broker dedup replaces inbox pattern

---

## Q048: TTL on Messages

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Common |

### Question

Set message TTL for time-sensitive fraud check events?

### Short Answer (30 seconds)

Set `TimeToLive` on message or default on entity — expired messages dropped or dead-lettered depending on config.

### Detailed Answer (3–5 minutes)

**Use case:** price quote valid 15 minutes — TTL 15m on quote events; consumer ignores stale anyway.

**Architect:** Align TTL with business validity. Monitor expired counts. Don't TTL audit events prematurely.

### Architecture Perspective

TTL prevents processing stale business events.

### Follow-up Questions

1. **TTL vs scheduled enqueue? — TTL expires; scheduled delays delivery.**
2. **Default TTL on entity? — Applies when message TTL not set.**

### Common Mistakes in Interviews

- Process expired payment authorization
- No TTL on time-bound offers
- TTL 7 days on fraud hold needing 24h max

---

## Q049: Scheduled Messages

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Service Bus |
| **Frequency** | Common |

### Question

Schedule payment capture 24 hours after order shipment?

### Short Answer (30 seconds)

Send message with `ScheduledEnqueueTimeUtc` — broker holds until time, then delivers to queue for capture worker.

### Detailed Answer (3–5 minutes)

**vs Durable timer:** Service Bus schedule simpler for single delay; Durable for complex workflow timers.

**Architect:** Cancel scheduled message by sequence number if order cancelled before capture.

### Architecture Perspective

Scheduled messages replace hacky sleep in workers.

### Follow-up Questions

1. **Schedule limit? — Large backlog of scheduled messages — monitor namespace metrics.**
2. **Cancel scheduled message? — CancelScheduledMessageAsync with sequence number.**

### Common Mistakes in Interviews

- Sleep 24h in Function execution
- Cron poll DB for ready captures
- No cancel path on order cancellation

---

## Q050: Geo-Disaster Recovery for Messaging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Common |

### Question

Design Service Bus geo-disaster recovery for critical namespace?

### Short Answer (30 seconds)

Premium: pair primary/secondary namespaces with alias; metadata sync; failover breaks pairing until re-pair. Apps use connection string alias for transparent failover.

### Detailed Answer (3–5 minutes)

**Failover:** manual or scripted; in-flight messages primary may lost — document RPO. **Re-pair** after primary healthy.

**Architect:** DR drill includes messaging failover + consumer reconnect test. Event Hubs geo-disaster recovery similar with alias.

### Architecture Perspective

Messaging DR is often overlooked in DR plans.

### Follow-up Questions

1. **Active-active messaging? — Complex conflict resolution — prefer active-passive for Service Bus.**
2. **Event Grid DR? — Multi-region publish endpoints; custom topic redundancy patterns.**

### Common Mistakes in Interviews

- No DR on messaging tier Standard mission-critical
- Failover never tested in game day
- Hardcoded primary namespace connection only

---
