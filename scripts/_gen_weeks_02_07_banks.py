#!/usr/bin/env python3
"""Generate premium_qa_data_weeks_02_07_banks.py — 540 questions (weeks 2–7)."""

from __future__ import annotations

import os
import textwrap

from premium_qa_data import q
from qa_question_bank import CONCEPTS, WEEK_TOPICS, QUESTION_FORMS, EXPERT_SCENARIOS

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_02_07_banks.py")

WEEK_BANK_KEY = {2: ".NET", 3: "Architecture", 4: "Design Patterns", 5: "Data Structures", 6: "Algorithms", 7: "SQL Server"}

# Extra concept seeds per week to reach 90 unique questions
EXTRA_CONCEPTS: dict[int, list[tuple]] = {
    2: [
        ("JIT vs AOT compilation", "Runtime", "Latency-sensitive APIs", "Heavy reflection plugins", "Native AOT worker for edge inference"),
        ("AssemblyLoadContext", "Runtime", "Plugin isolation", "Simple single-app deploy", "Plugin host with collectible ALC"),
        ("Middleware pipeline order", "ASP.NET", "Cross-cutting concerns", "Random middleware registration", "Exception handler before auth"),
        ("Kestrel limits tuning", "Hosting", "High-concurrency APIs", "Default limits blindly", "MaxConcurrentConnections tuned per instance"),
        ("Generic host builder", "Hosting", "Unified worker/web hosting", "Duplicate Program.cs patterns", "Host.CreateDefaultBuilder shared template"),
        ("Options validation on start", "Configuration", "Fail-fast config", "Runtime null reference from config", "ValidateOnStart for payment settings"),
        ("Secret management Key Vault", "Configuration", "Production secrets", "Secrets in env without rotation", "Azure Key Vault provider + managed identity"),
        ("DI keyed services", "DI", "Multi-tenant providers", "Factory anti-pattern everywhere", "Keyed IPaymentGateway per region"),
        ("Scoped factory pattern", "DI", "Singleton needing scoped deps", "Captive dependency", "IServiceScopeFactory in background worker"),
        ("BackgroundService graceful stop", "Hosting", "Long-running consumers", "Kill -9 without drain", "StoppingToken honored in poll loop"),
        ("Health check liveness readiness", "Operations", "K8s probes", "DB check in liveness", "Separate /health/live and /ready"),
        ("YARP reverse proxy", "Hosting", "API gateway on .NET", "Custom proxy from scratch", "YARP routes to microservices"),
        ("gRPC streaming patterns", "API Design", "Bidirectional streams", "REST for bulk binary", "Server streaming for log tail"),
        ("SignalR backplane", "Real-time", "Multi-instance hubs", "Sticky sessions only", "Redis backplane for scale-out"),
        ("EF Core compiled queries", "EF Core", "Hot path queries", "LINQ recompile every call", "EF.CompileQuery for catalog lookup"),
        ("EF Core split queries", "EF Core", "Cartesian explosion joins", "Always single query", "AsSplitQuery on order+lines+payments"),
        ("EF Core global query filters", "EF Core", "Soft delete multi-tenant", "Filter in every repository", "HasQueryFilter on tenantId"),
        ("Dapper vs EF Core", "Data Access", "Read-heavy hot paths", "ORM for everything", "Dapper for reporting read models"),
        ("Connection resiliency", "Data Access", "Transient SQL errors", "No retry on failover", "EnableRetryOnFailure with backoff"),
        ("MemoryCache vs distributed cache", "Caching", "Single instance cache", "Redis for tiny app", "IMemoryCache + IDistributedCache tiered"),
        ("System.Text.Json vs Newtonsoft", "Serialization", "Default ASP.NET serialization", "Mixing serializers", "STJ source gen for AOT"),
        ("Source generators overview", "Modern C#", "Compile-time codegen", "Runtime reflection heavy paths", "Mapperly for DTO mapping"),
        ("Activity and diagnostics", "Observability", "Distributed tracing", "String-only logs", "ActivitySource spans per handler"),
        ("Metrics with System.Diagnostics.Metrics", "Observability", "Custom business metrics", "Log parsing for metrics", "Counter for orders_placed"),
        ("Culture and localization", "Globalization", "Multi-region APIs", "Hardcoded date formats", "RequestLocalization middleware"),
        ("CORS architecture", "Security", "Browser SPA clients", "AllowAnyOrigin in prod", "Explicit origins per environment"),
        ("Anti-forgery and CSRF", "Security", "Cookie-based MVC", "CSRF on state-changing APIs", "Antiforgery tokens on forms"),
        ("Certificate authentication", "Security", "mTLS service mesh", "Password for service-to-service", "Client cert auth middleware"),
        ("Kestrel HTTPS termination", "Hosting", "TLS at app", "TLS everywhere in app unnecessarily", "TLS at ingress terminate to HTTP"),
        ("Container image layering", "Containers", "Fast CI builds", "Fat single-layer images", "Multi-stage SDK→runtime slim"),
        ("dotnet monitor diagnostics", "Operations", "Production diagnostics", "Attach debugger in prod", "dotnet-monitor sidecar collection"),
        ("ReadyToRun images", "Performance", "Cold start reduction", "AOT incompatible code paths", "PublishReadyToRun for APIs"),
        ("ThreadPool tuning", "Performance", "Sync-over-async incidents", "Default pool for batch+web mixed", "Min threads adjusted after profiling"),
        ("ArrayPool and memory", "Performance", "Large buffer reuse", "new byte[] per request", "ArrayPool<byte>.Shared in parser"),
        ("Regex source generators", "Performance", "Hot path regex", "Compiled regex everywhere", "GeneratedRegex attribute"),
        ("Hosting startup assemblies", "Hosting", "Library middleware injection", "Copy-paste startup", "IHostingStartup in shared lib"),
        ("Endpoint routing vs conventional", "ASP.NET", "Minimal APIs attribute routing", "Legacy conventional only", "MapGroup for versioned APIs"),
        ("ProblemDetails correlation", "API Design", "Supportable errors", "Opaque 500 messages", "traceId extension in ProblemDetails"),
        ("OpenAPI document filters", "API Design", "Consistent API docs", "Manual swagger edits", "IDocumentFilter for security schemes"),
        ("Integration test WebApplicationFactory", "Testing", "Full pipeline tests", "Mock everything unit only", "WAF with Testcontainers SQL"),
        ("Testcontainers for SQL", "Testing", "Realistic integration tests", "In-memory EF only", "MsSql container in CI"),
        ("Roslyn analyzers in CI", "Quality", "Enforce architecture rules", "Review-only conventions", "NetArchTest + analyzers fail build"),
        ("Central package management", "Build", "Consistent package versions", "Per-project drift", "Directory.Packages.props"),
        ("NuGet vulnerability audit", "Security", "Supply chain hygiene", "Ignore NU190 warnings", "Audit in CI gate"),
        ("Globalization invariant mode", "Deployment", "Container size wins", "Apps needing all cultures", "InvariantGlobalization in slim images"),
        ("Quartz.NET scheduling", "Background Jobs", "Cron in .NET", "while(true) Thread.Sleep", "Quartz hosted service cluster"),
        ("Hangfire vs native workers", "Background Jobs", "Dashboard job ops", "Hangfire for 2 jobs", "IHostedService for simple queue drain"),
        ("MassTransit on .NET", "Messaging", "Abstracted messaging", "Raw SDK everywhere", "MassTransit + outbox pattern"),
        ("MediatR in minimal APIs", "Patterns", "Thin endpoints", "Fat minimal lambdas", "Send command from MapPost"),
        ("FluentValidation async rules", "Validation", "Remote validation", "Sync validation blocking", "MustAsync for uniqueness check"),
        ("Hybrid cache .NET 9", "Caching", "L1+L2 cache", "Manual two-tier cache", "HybridCache automatic L1 memory L2 Redis"),
        ("Rate limit partition keys", "ASP.NET", "Per-tenant limits", "Global limit only", "PartitionedRateLimiter by tenantId"),
        ("Output cache policies", "ASP.NET", "CDN-friendly GET caching", "Cache authenticated responses", "VaryByQuery policy on catalog"),
        ("IdentityServer vs Entra", "Security", "Custom OIDC", "Build IdP unnecessarily", "Entra ID for workforce customers"),
        ("Data annotations vs FluentValidation", "Validation", "Simple models", "Duplicate rules both places", "One validation layer per boundary"),
        ("Swagger security definitions", "API Design", "OAuth2 in OpenAPI", "Undocumented auth", "OAuth2 security scheme in swagger"),
        ("Grpc health checks", "gRPC", "K8s gRPC probes", "HTTP health only for gRPC", "MapGrpcHealthChecksService"),
        ("Wolverine messaging handler", "Messaging", "In-process messaging", "MediatR for integration", "Wolverine for local + external"),
        ("Orleans virtual actors", "Distributed .NET", "Stateful scale-out", "Orleans for CRUD API", "Orleans for session/game state"),
        ("Dapr sidecar .NET", "Distributed .NET", "Portable building blocks", "Dapr for monolith", "Dapr pub/sub from .NET service"),
        ("FusionCache", "Caching", "Stampede protection", "Naive cache-aside", "FusionCache with fail-safe"),
        ("AWS SDK vs Azure SDK DI", "Cloud SDK", "Multi-cloud workers", "Static clients", "IAmazonS3 injected singleton"),
        ("Azure App Configuration refresh", "Configuration", "Feature flags refresh", "Restart for flag change", "ConfigureRefresh sentinel key"),
        ("Feature management Microsoft", "Configuration", "Progressive rollout", "Custom flag DB", "IFeatureManager percentage filter"),
        ("Application Insights adaptive sampling", "Observability", "Cost control telemetry", "100% trace always", "Adaptive sampling production"),
        ("OpenTelemetry resource attributes", "Observability", "Service identification", "Missing service.name", "OTEL_RESOURCE_ATTRIBUTES deployment"),
        ("Custom middleware vs filters", "ASP.NET", "HTTP-only cross-cutting", "Duplicate logic both", "Middleware auth filters validation"),
        ("IExceptionHandler .NET 8", "ASP.NET", "Unified exception handling", "Multiple catch blocks", "IExceptionHandler pipeline"),
        ("Results pattern minimal APIs", "API Design", "TypedResults responses", "object returns", "Results<Ok<OrderDto>, NotFound>"),
        ("ValidationProblemDetails", "API Design", "Validation errors shape", "Custom 400 JSON", "ValidationProblem() standard"),
        ("ApiController attribute behavior", "API Design", "Automatic 400 on model state", "Duplicate validation", "[ApiController] conventions"),
        ("ProblemDetails in gRPC", "gRPC", "Rich error details", "Generic StatusCode only", "RpcException with ErrorInfo metadata"),
        ("CancellationToken propagation", "Async", "Graceful shutdown", "Ignored cancellation", "CancellationToken through all async calls"),
        ("ConfigureAwait in libraries", "Async", "Library code", "ConfigureAwait in app code", "ConfigureAwait(false) in shared lib"),
        ("ValueTask when to use", "Async", "Hot path cached results", "ValueTask everywhere", "ValueTask for cache hit sync path"),
        ("IAsyncEnumerable streaming", "API Design", "Large result streams", "Load all to memory", "IAsyncEnumerable<OrderDto> export"),
        ("Snowflake ID generation", "Identifiers", "Distributed unique IDs", "GUID clustered PK", "IdGen snowflake for orders"),
        ("ULID vs GUID", "Identifiers", "Sortable IDs", "Random GUID PK", "ULID for log correlation keys"),
    ],
    3: [
        ("Onion architecture layers", "Clean Arch", "Same dependency rule", "Religious layer count", "Domain core with adapters"),
        ("Bounded context boundaries", "DDD", "Team and model alignment", "One enterprise model", "Billing vs Support Customer types"),
        ("Aggregate consistency boundary", "DDD", "Transaction per aggregate", "Cross-aggregate single TX", "Order root owns lines"),
        ("Value object immutability", "DDD", "Money Address types", "Primitive obsession", "record Money with currency"),
        ("Domain service when", "DDD", "Logic across entities", "Anemic everything in service", "PricingService for cross-line discount"),
        ("Repository interface placement", "Clean Arch", "Domain or application debate", "EF in domain", "IOrderRepository in application layer"),
        ("CQRS without event sourcing", "CQRS", "Read write separation", "CQRS day one two tables", "Separate query handlers same DB"),
        ("Read model projection", "CQRS", "Optimized queries", "Join 12 tables on read", "OrderListDto projection table"),
        ("Anti-corruption layer", "Integration", "Legacy system isolation", "ERP DTOs in domain", "ErpOrderAdapter maps legacy"),
        ("Strangler fig migration", "Migration", "Incremental replacement", "Big bang rewrite", "Route new features to new module"),
        ("Modular monolith modules", "Architecture", "Clear module APIs", "Microservices too early", "Checkout module public API"),
        ("Shared kernel minimal", "DDD", "Tiny shared types", "Large shared library", "Shared Money and Address only"),
        ("Context mapping patterns", "DDD", "Document relationships", "Implicit coupling", "Upstream Payment conformist"),
        ("Event storming workshop", "Discovery", "Find boundaries", "Skip discovery", "Event storm → bounded contexts"),
        ("Rich domain model", "DDD", "Behavior on entities", "Anemic CRUD", "order.Confirm() not SetStatus"),
        ("Application service thin", "Clean Arch", "Orchestration only", "Business rules in app service", "Handler delegates to domain"),
        ("Infrastructure adapter swap", "Hexagonal", "Test doubles", "Concrete SQL in handler", "InMemoryOrderRepo for tests"),
        ("Presentation layer concerns", "Clean Arch", "HTTP mapping only", "Business logic in controller", "Controller maps to command"),
        ("Cross-cutting concerns placement", "Design", "Middleware vs behaviors", "Duplicate validation", "ValidationBehavior in pipeline"),
        ("Integration events vs domain", "Events", "Boundary crossing", "Domain events in integration bus", "Domain event → integration handler"),
        ("Outbox in clean architecture", "Reliability", "Atomic publish", "Fire after SaveChanges", "Outbox table in infrastructure"),
        ("Idempotent command handlers", "Reliability", "Retry safe commands", "Double charge on retry", "Idempotency key in handler"),
        ("Specification pattern queries", "Patterns", "Composable filters", "Copy-paste LINQ", "ActiveOrdersSpec in repository"),
        ("Unit of Work per request", "Patterns", "Single transaction", "Multiple SaveChanges", "One UoW scoped per HTTP request"),
        ("Domain exception taxonomy", "Design", "Business vs technical", "Exception for flow control all", "OrderNotFoundException domain type"),
        ("Result pattern application layer", "Design", "Expected failures", "Exception for not found", "Result<Order> from handler"),
        ("Vertical slice folders", "Organization", "Feature co-location", "Giant Services folder", "Features/Orders/Create/"),
        ("Request pipeline behaviors order", "MediatR", "Validation before transaction", "Wrong behavior order", "Logging→Validation→Transaction→Handler"),
        ("FluentValidation command rules", "Validation", "Input at boundary", "Validation in domain for format", "CreateOrderValidator on command"),
        ("Mapster vs AutoMapper", "Mapping", "Performance mapping", "Reflection map hot path", "Mapster compile-time config"),
        ("Manual mapping complex aggregates", "Mapping", "Explicit control", "AutoMapper magic", "Manual map for Order aggregate"),
        ("API model vs domain model", "Design", "Contract stability", "Expose EF entities", "CreateOrderRequest vs Order"),
        ("Pagination query objects", "CQRS", "List queries", "Return all rows", "GetOrdersQuery with cursor page"),
        ("Sorting whitelist", "Security", "Dynamic sort params", "Raw ORDER BY injection", "AllowedSortFields whitelist"),
        ("Authorization at handler", "Security", "Use-case permissions", "Controller-only auth", "IAuthorizationService in handler"),
        ("Policy-based handler auth", "Security", "Fine-grained rules", "Role checks scattered", "RequireClaim policy on command"),
        ("Audit trail cross-cutting", "Compliance", "Who changed what", "Manual audit fields", "AuditBehavior in MediatR pipeline"),
        ("Correlation ID propagation", "Observability", "Trace requests", "Missing correlation in logs", "CorrelationId middleware + Serilog"),
        ("Health checks module", "Operations", "Module readiness", "Monolith health only", "Per-module readiness tags"),
        ("Feature flags in handlers", "Release", "Decouple deploy release", "Branch by version", "IFeatureManager in handler"),
        ("Transactional email side effect", "Design", "After commit actions", "Email before commit", "Domain event after UoW commit"),
        ("Saga local vs distributed", "Transactions", "Cross-service workflow", "2PC across services", "Orchestrated saga with compensations"),
        ("Compensating transactions", "Saga", "Rollback distributed", "Hope manual fix", "ReleaseInventory on payment failure"),
        ("Eventual consistency UX", "UX", "Async workflows", "Sync UI for async", "Pending state polling webhook"),
        ("Read side denormalization", "CQRS", "Fast reads", "Normalize everything", "OrderSummary table updated by events"),
        ("Schema per bounded context", "Data", "Independent evolution", "Shared database antipattern", "Orders DB vs Catalog DB"),
        ("Database per service pragmatic", "Microservices", "True isolation", "DB per service day one", "Schema separation first step"),
        ("API composition vs aggregation", "Integration", "BFF pattern", "Chatty client calls", "BFF aggregates order view"),
        ("Gateway vs direct service", "Integration", "Cross-cutting at edge", "Gateway as god service", "APIM policies auth rate limit"),
        ("Versioning bounded context APIs", "API Design", "Independent evolution", "Breaking clients silently", "URL version per context"),
        ("Contract testing between contexts", "Testing", "Consumer-driven contracts", "Integration test only", "Pact between Order and Payment"),
        ("Architecture fitness functions", "Governance", "Automate rules", "Manual review only", "NetArchTest domain no infra refs"),
        ("ArchUnitNET layer rules", "Governance", "Enforce dependencies", "Convention docs ignored", "CI fails on layer violation"),
        ("Package by feature", "Organization", "Cohesion", "Package by layer", "Orders feature folder all layers"),
        ("Screaming architecture", "Organization", "Folder names domain", "Controllers Services Repos", "Orders not Infrastructure top"),
        ("When skip clean architecture", "Pragmatism", "Simple CRUD tools", "CA for admin panel", "Pragmatic 3-layer internal tool"),
        ("Clean architecture testing pyramid", "Testing", "Fast feedback", "E2E only", "Domain unit no DB majority"),
        ("Test doubles for ports", "Testing", "Isolated application tests", "Integration for everything", "Fake IEmailPort in handler test"),
        ("Integration test boundaries", "Testing", "Infrastructure adapters", "Full system every test", "Testcontainers for repo adapter"),
        ("Seed data for integration", "Testing", "Repeatable tests", "Shared mutable DB state", "Respawn reset between tests"),
        ("Domain event handler placement", "Events", "Application layer", "Domain calls HTTP", "OrderPlacedHandler in application"),
        ("Integration event schema versioning", "Events", "Backward compatible", "Breaking renames", "OrderPlacedV2 additive fields"),
        ("Idempotent event consumers", "Messaging", "At-least-once delivery", "Assume once only", "Consumer dedup by eventId"),
        ("Process manager pattern", "Saga", "Long-running workflow", "Synchronous chain", "OrderProcessManager state machine"),
        ("State machine for order", "Domain", "Status transitions", "Enum set anywhere", "OrderState pattern invalid transitions"),
        ("Policy pattern domain rules", "DDD", "Pluggable rules", "If else discount chain", "IDiscountPolicy implementations"),
        ("Factory in domain", "DDD", "Complex aggregate creation", "New in application", "OrderFactory enforces invariants"),
        ("Encapsulated collections", "DDD", "Aggregate children", "Public List<OrderLine>", "ReadOnlyCollection lines"),
        ("Domain event collection on aggregate", "DDD", "Raise from entity", "Event bus in entity", "AddDomainEvent in aggregate"),
        ("Dispatch domain events", "Application", "After SaveChanges", "Before persist", "DispatchEventsBehavior pre-commit"),
        ("Transactional boundary design", "Transactions", "One aggregate per TX", "Multi-aggregate transaction", "Eventual consistency between aggregates"),
        ("Optimistic concurrency rowversion", "Concurrency", "Conflict detection", "Last write wins", "RowVersion on Order entity"),
        ("Pessimistic locking rare cases", "Concurrency", "Financial ledger", "Pessimistic everywhere", "UPDLOCK on balance row only"),
        ("Cache invalidation on write", "Caching", "Read models", "Stale cache forever", "Invalidate on OrderUpdated event"),
        ("Distributed cache key design", "Caching", "Tenant isolation", "Global keys collide", "tenant:{id}:order:{id} key pattern"),
        ("Logging sensitive data rules", "Security", "PII in logs", "Log full credit card", "Redact PII structured logging policy"),
        ("GDPR delete in clean arch", "Compliance", "Right to erasure", "Hard delete everywhere", "Anonymize command cascades contexts"),
        ("Multi-tenant data isolation", "Security", "RLS or tenant filter", "App filter only", "Global query filter tenantId"),
        ("Plugin architecture ports", "Hexagonal", "Extensibility", "Core knows all plugins", "IPlugin port discovered at runtime"),
        ("Configuration per module", "Modular Monolith", "Module settings", "One giant appsettings", "Orders: section bound options"),
        ("Module communication patterns", "Modular Monolith", "In-process events", "Direct DB cross-module", "Integration event in-process bus"),
        ("Extract module to service", "Migration", "Strangler completion", "Big bang extract", "Module API becomes HTTP when ready"),
        ("Documentation living architecture", "Governance", "C4 per module", "Stale wiki", "Structurizr DSL in repo per module"),
        ("Onboarding path new developer", "Team", "Vertical slice learning", "Layer tour only", "Follow CreateOrder slice end-to-end"),
        ("Code review architecture checklist", "Governance", "Dependency rule", "Style only reviews", "Checklist: domain purity ports used"),
        ("Refactor toward clean arch", "Migration", "Incremental", "Stop world rewrite", "Introduce handler extract domain gradually"),
        ("Legacy anemic to rich domain", "Migration", "Behavior extraction", "Rewrite overnight", "Move method from service to entity"),
        ("Shared database migration", "Migration", "Split schemas", "Immediate DB per service", "Schema ownership then extract"),
        ("Team alignment Conway", "Organization", "Stream aligned teams", "Layer teams", "Order team owns vertical slice"),
        ("Architect role in clean arch", "Leadership", "Guardrails templates", "Code every feature", "Templates ADRs review fitness functions"),
        ("Performance read side", "CQRS", "Denormalized queries", "Domain model for lists", "Dapper on read model tables"),
        ("Security threat modeling clean arch", "Security", "Trust boundaries", "Security as afterthought", "STRIDE per adapter boundary"),
        ("Error handling consistent", "API Design", "ProblemDetails mapping", "500 for business errors", "Map domain exceptions to 409 404"),
        ("API idempotency headers", "Reliability", "POST retry safe", "Duplicate orders", "Idempotency-Key header middleware"),
        ("Webhook outbound adapter", "Integration", "Driven port", "HttpClient in domain", "IWebhookPort implemented infrastructure"),
        ("File storage port adapter", "Hexagonal", "Blob abstraction", "Azure SDK in handler", "IFileStorage S3 and Azure adapters"),
        ("Email notification port", "Hexagonal", "Side effect isolation", "SmtpClient in domain", "IEmailPort SendGrid adapter"),
        ("Clock abstraction testing", "Testing", "Time-dependent logic", "DateTime.UtcNow in domain", "IClock injectable fake"),
        ("Random abstraction testing", "Testing", "Deterministic tests", "Random in domain logic", "IRandom injectable seed"),
    ],
    4: [
        ("Object pool pattern", "Creational", "Expensive object reuse", "Pool everything", "SqlConnection pool built-in"),
        ("Lazy initialization thread-safe", "Creational", "Defer cost", "Lazy everywhere", "Lazy<T> for heavy config parse"),
        ("Flyweight pattern", "Structural", "Shared intrinsic state", "Duplicate data", "Glyph flyweight in text editor"),
        ("Facade vs Mediator", "Structural", "Simplify interactions", "Confuse patterns", "Facade checkout Mediator order events"),
        ("Decorator vs Proxy", "Structural", "Add behavior vs control", "Inheritance maze", "CachingDecorator vs SecurityProxy"),
        ("Adapter for third party SDK", "Structural", "Isolate vendor", "SDK calls in controllers", "StripeAdapter implements IPayment"),
        ("Bridge for multi-channel notify", "Structural", "Decouple abstraction", "Subclass explosion", "Notification bridge SMS email push"),
        ("Composite menu permissions", "Structural", "Tree operations", "Special case leaves", "Permission composite tree"),
        ("Iterator pattern LINQ", "Behavioral", "Collection traversal", "Manual index loops", "IEnumerable iterator pattern"),
        ("Interpreter rule engine", "Behavioral", "DSL evaluation", "Interpreter for simple if", "Promo rule interpreter"),
        ("Memento undo audit", "Behavioral", "State history", "Expose internals", "OrderMemento for audit trail"),
        ("Null object pattern", "Behavioral", "Avoid null checks", "Null everywhere", "NullLogger no-op implementation"),
        ("Specification business rules", "Enterprise", "Composable rules", "Nested if validation", "IsActiveCustomerSpec"),
        ("Service locator anti-pattern", "Anti-Pattern", "DI instead", "ServiceLocator.Current", "Constructor injection only"),
        ("Static singleton anti-pattern", "Anti-Pattern", "DI singleton", "static Database.Instance", "Register singleton in DI"),
        ("Anemic domain anti-pattern", "Anti-Pattern", "Rich model", "All logic in service", "Behavior on entity"),
        ("God object anti-pattern", "Anti-Pattern", "Split responsibilities", "ApplicationService 5000 lines", "Vertical slice handlers"),
        ("Spaghetti callback anti-pattern", "Anti-Pattern", "Events mediator", "Nested callbacks", "Async event flow"),
        ("Golden hammer anti-pattern", "Anti-Pattern", "Right pattern fit", "Microservices for CRUD", "Simplest solution first"),
        ("Copy paste programming", "Anti-Pattern", "DRY abstraction", "Duplicate validation", "Shared validator behavior"),
        ("Premature optimization", "Anti-Pattern", "Measure first", "Custom DS everywhere", "Profile before pattern"),
        ("Blob anti-pattern", "Anti-Pattern", "Split modules", "Single deployment all", "Modular boundaries"),
        ("Vendor lock wrapper", "Enterprise", "Adapter insulates", "Direct SDK 50 places", "IPaymentGateway adapter"),
        ("Retry pattern resilience", "Enterprise", "Transient failures", "Infinite retry", "Polly retry with jitter"),
        ("Circuit breaker pattern", "Enterprise", "Cascading failure", "Retry into dead service", "Circuit breaker open half-open"),
        ("Bulkhead pattern", "Enterprise", "Isolate resources", "Shared thread pool exhaustion", "Separate pool per dependency"),
        ("Timeout pattern", "Enterprise", "Bound wait time", "Infinite HttpClient wait", "Per-call timeout policy"),
        ("Cache aside pattern", "Enterprise", "Read heavy", "Cache through always", "Cache-aside product catalog"),
        ("Read through write through", "Enterprise", "Cache consistency", "Wrong strategy choice", "Write-through for inventory count"),
        ("Event aggregator", "Behavioral", "Loose coupling UI", "Direct form coupling", "Prism event aggregator"),
        ("Publish subscribe pattern", "Behavioral", "Domain events", "Tight coupling", "MediatR notification handlers"),
        ("Pipeline pattern", "Behavioral", "Sequential processing", "Monolithic method", "Validation pipeline behaviors"),
        ("Rules engine pattern", "Enterprise", "Changeable business rules", "Hardcoded rules", "RulesEngine JSON rules"),
        ("Active record vs repository", "Anti-Pattern", "Repository for domain", "Active record in DDD", "EF entity not domain model"),
        ("Transaction script pattern", "Enterprise", "Simple procedures", "Over-engineer DDD", "Transaction script for batch job"),
        ("Table module pattern", "Enterprise", "One table logic", "DDD for log import", "Table module staging import"),
        ("Domain model pattern", "Enterprise", "Complex business", "Transaction script complex", "Rich domain for orders"),
        ("Data mapper pattern", "Enterprise", "Separate domain persistence", "Active record", "Mapper between Order and OrderRow"),
        ("Identity map pattern", "Enterprise", "Per-request cache", "Duplicate entity loads", "DbContext identity map"),
        ("Lazy load pattern ORM", "Enterprise", "Navigation properties", "N+1 in API", "Explicit eager load or projection"),
        ("Query object pattern", "Enterprise", "Parameterized queries", "String concat SQL", "GetOrdersByStatusQuery object"),
        ("Parameter object pattern", "Enterprise", "Many parameters", "20 arg constructor", "DateRange parameter object"),
        ("Value object pattern", "DDD", "Immutable concepts", "string for email", "EmailAddress value object"),
        ("Aggregate pattern", "DDD", "Consistency boundary", "Giant aggregate", "Order aggregate root"),
        ("Domain event pattern", "DDD", "Business facts", "Integration in domain", "OrderPlaced domain event"),
        ("Anti-corruption layer pattern", "Integration", "Legacy isolation", "Import legacy model", "ACL translates ERP order"),
        ("Gateway pattern integration", "Enterprise", "External API facade", "Scatter HTTP calls", "PaymentGateway single entry"),
        ("Remote facade pattern", "Distributed", "Coarse grained API", "Chatty fine calls", "Coarse OrderFacade DTO"),
        ("Data transfer object pattern", "Enterprise", "Layer boundary", "Entity on wire", "OrderDto at API boundary"),
        ("Remote proxy pattern", "Distributed", "Client stub", "Raw HTTP everywhere", "gRPC client proxy"),
        ("Client session state", "Enterprise", "Shopping cart server", "Stateless where needed", "Session for cart only"),
        ("Server session clustering", "Enterprise", "Sticky or replicated", "In-memory session scale", "Redis session state"),
        ("Front controller pattern", "Enterprise", "Single entry dispatch", "Many servlet entry", "ASP.NET pipeline front controller"),
        ("Page controller vs front", "Enterprise", "MVC controllers", "Page controller legacy", "Controller per resource"),
        ("Application controller", "Enterprise", "Use case controller", "Fat page controller", "Application controller thin"),
        ("Template view pattern", "Enterprise", "Server render", "SPA where not needed", "Razor template view"),
        ("Transform view pattern", "Enterprise", "DTO to view model", "Domain in view", "Transform Order to OrderViewModel"),
        ("Two step view pattern", "Enterprise", "Layout composition", "Duplicate layout", "Two-step layout render"),
        ("Plugin pattern extensibility", "Enterprise", "Runtime discovery", "Core knows all plugins", "IPlugin MEF or DI scan"),
        ("Registry pattern", "Enterprise", "Lookup implementations", "Switch on type", "Strategy registry by key"),
        ("Servant pattern", "Behavioral", "External operations", "Wrong entity behavior", "OrderFormatter servant"),
        ("Marker interface pattern", "Enterprise", "Type metadata", "Marker abuse", "ISerializable marker considered"),
        ("Double dispatch pattern", "Behavioral", "Visitor alternative", "Overuse visitor", "Collision detection double dispatch"),
        ("Model view controller", "Enterprise", "Separation concerns", "MVC confused with layers", "MVC presentation only"),
        ("Model view presenter", "Enterprise", "Testable UI", "MVP for web API", "MVP desktop legacy"),
        ("Model view viewmodel", "Enterprise", "WPF binding", "MVVM for REST API", "MVVM XAML client"),
        ("Presentation model", "Enterprise", "Screen tailored model", "Domain on screen", "Presentation model per view"),
        ("Separated presentation", "Enterprise", "Independent UI deploy", "Monolith UI logic", "BFF separated presentation"),
        ("Layers pattern enterprise", "Enterprise", "Classic tiers", "Confuse with clean", "Presentation business data layers"),
        ("Table data gateway", "Enterprise", "Row oriented DB", "Repository when need domain", "Gateway for reporting import"),
        ("Row data gateway", "Enterprise", "Single row access", "Active record overlap", "Row gateway legacy DAL"),
        ("Data access object DAO", "Enterprise", "Persistence API", "DAO vs repository", "DAO when no domain model"),
        ("Mapper registry", "Enterprise", "Central mappers", "Scatter mapping", "Mapper registry singleton"),
        ("Lazy load virtual proxy", "Enterprise", "Deferred load", "N+1 problem", "Explicit include instead lazy"),
        ("Separated interface pattern", "Enterprise", "Package dep rule", "Concrete dependency", "Interface in domain impl infra"),
        ("Claim check pattern messaging", "Enterprise", "Large payload", "Big message body", "Blob claim check event"),
        ("Competing consumers pattern", "Enterprise", "Scale workers", "Single consumer", "Multiple queue consumers"),
        ("Consumer routing pattern", "Enterprise", "Message routing", "One queue all types", "Route by message type"),
        ("Message dispatcher pattern", "Enterprise", "Handler routing", "Switch in consumer", "Dispatcher to handlers"),
        ("Messaging gateway pattern", "Enterprise", "Send receive abstract", "SDK in domain", "IMessageGateway adapter"),
        ("Polling consumer pattern", "Enterprise", "Pull messages", "Push only when needed", "Polling for batch ETL"),
        ("Event driven consumer", "Enterprise", "React to events", "Sync orchestration", "Event driven inventory update"),
        ("Event sourcing pattern intro", "Enterprise", "Audit full history", "ES for simple CRUD", "Event store order history"),
        ("CQRS pattern intro", "Enterprise", "Read write split", "Separate DB day one", "Logical CQRS handlers first"),
        ("Materialized view pattern", "Enterprise", "Read optimization", "Live join 12 tables", "Materialized order summary"),
        ("Valet parking pattern", "Cloud", "Offload processing", "Sync long job", "Queue valet async process"),
        ("Ambassador pattern sidecar", "Cloud", "Proxy helper container", "Ambassador for monolith", "Logging ambassador sidecar"),
        ("Sidecar pattern containers", "Cloud", "Cross-cutting container", "Sidecar for business logic", "Envoy sidecar proxy"),
        ("Strangler pattern cloud", "Migration", "Incremental cloud", "Lift shift only", "Strangler route to new service"),
        ("Anti-pattern distributed monolith", "Anti-Pattern", "True boundaries", "Microservices shared DB", "Independent deploy schema"),
        ("Anti-pattern nanoservices", "Anti-Pattern", "Right service size", "One endpoint service", "Bounded context size service"),
        ("Pattern selection ADR", "Process", "Document pattern choice", "Pattern resume", "ADR why strategy not state"),
        ("Refactoring to patterns", "Process", "Incremental introduce", "Big bang pattern", "Extract strategy from switch"),
        ("Testing with patterns", "Testing", "Mock interfaces", "Test concrete singleton", "Mock IStrategy in unit test"),
        ("Pattern overuse smell", "Anti-Pattern", "YAGNI", "Abstract factory for one", "Simplest pattern that works"),
        ("Enterprise integration patterns book", "Terminology", "Messaging patterns", "Confuse with GoF", "EIP for messaging architecture"),
        ("GoF patterns relevance today", "Terminology", "Still foundational", "Patterns obsolete", "Strategy Command still daily"),
        ("Functional alternative patterns", "Modern", "Functions over patterns", "Visitor when switch enough", "Discriminated union vs visitor"),
        ("Record based immutable strategy", "Modern C#", "Strategy via records", "Class per strategy tiny", "record IShippingStrategy variants"),
        ("Pattern matching vs visitor", "Modern C#", "Closed hierarchies", "Visitor overkill", "switch expression on type"),
        ("DI as pattern enabler", "DI", "Inject strategies", "new Strategy in method", "DI registers all IStrategy"),
    ],
    5: [
        ("AVL tree self-balancing", "Trees", "Strict balance guarantees", "AVL for disk index", "In-memory ordered map AVL"),
        ("B-tree vs B+ tree", "Trees", "Disk index choice", "B-tree for database", "B+ tree SQL default"),
        ("Segment tree range query", "Trees", "Range sum queries", "Segment tree for CRUD", "Price range sum analytics"),
        ("Fenwick tree BIT", "Trees", "Prefix sum updates", "BIT for graph", "BIT frequency analytics"),
        ("Suffix tree advanced", "Trees", "Substring search", "Suffix tree interview only", "Bioinformatics substring"),
        ("Radix tree compressed trie", "Trees", "IP routing memory", "Standard trie sparse", "Radix tree route table"),
        ("Heapify operation", "Heaps", "Build heap O(n)", "Sort with heap wrong", "Heapify bottom-up build"),
        ("Fibonacci heap theory", "Heaps", "Theoretical Dijkstra", "Fibonacci in production", "Theory interview only"),
        ("Binomial heap merge", "Heaps", "Mergeable heaps", "Binomial in app code", "Academic merge heaps"),
        ("Pairing heap practical", "Heaps", "Simpler mergeable", "Pairing heap database", "Alternative priority queue"),
        ("Double-ended priority queue", "Heaps", "Min and max ends", "Two heaps awkward", "Interval scheduling DEQ"),
        ("Hash map load factor", "Hash Tables", "Resize tuning", "Load factor ignored", "0.75 resize threshold"),
        ("Cuckoo hashing", "Hash Tables", "O(1) worst lookup", "Cuckoo at scale DB", "Network switch FIB cuckoo"),
        ("Robin Hood hashing", "Hash Tables", "Reduce variance", "Robin Hood hand roll", "Open addressing variant"),
        ("Perfect hashing static", "Hash Tables", "Static key set", "Perfect hash dynamic", "Compiler keyword table"),
        ("Coalesced hashing", "Hash Tables", "Open addressing variant", "Coalesced in app", "Alternative collision"),
        ("Extendible hashing disk", "Hash Tables", "Dynamic disk hash", "Extendible in memory", "Database extendible hash"),
        ("Linear hashing disk", "Hash Tables", "Gradual bucket split", "Linear hash app", "Disk hash table growth"),
        ("Consistent hashing virtual nodes", "Distributed", "Even distribution", "No vnodes skew", "150 vnodes per physical node"),
        ("Rendezvous hashing", "Distributed", "Minimal remapping", "Rendezvous vs consistent", "Highest random weight hashing"),
        ("Jump consistent hash", "Distributed", "Minimal memory", "Jump hash client change", "Google jump consistent hash"),
        ("Magma hash ring", "Distributed", "Ketama compatible", "Roll own hash ring", "Memcached client ketama"),
        ("Geohash spatial index", "Hash", "Location proximity", "Geohash exact match", "Nearby drivers geohash"),
        ("Quadtree spatial", "Trees", "2D spatial queries", "Quadtree 1D", "Game collision quadtree"),
        ("R-tree spatial database", "Trees", "GIS database index", "R-tree in memory app", "PostGIS R-tree"),
        ("KD-tree nearest neighbor", "Trees", "Low dim nearest", "KD-tree high dim", "ML feature nearest KD-tree"),
        ("Ball tree high dim", "Trees", "Higher dim than KD", "Ball tree SQL", "Sklearn ball tree"),
        ("LSH locality sensitive", "Probabilistic", "Approx nearest neighbor", "LSH exact", "Vector search LSH band"),
        ("SimHash near duplicate", "Hash", "Document similarity", "SimHash encryption", "Near duplicate detection"),
        ("MinHash Jaccard similarity", "Probabilistic", "Set similarity", "MinHash exact", "Duplicate article MinHash"),
        ("Cuckoo filter vs bloom", "Probabilistic", "Delete support", "Cuckoo filter billing", "Negative lookup filter"),
        ("Quotient filter", "Probabilistic", "Better bloom variant", "Quotient overkill", "Alternative membership"),
        ("Counting bloom filter", "Probabilistic", "Delete in bloom", "Counting bloom huge", "Allow delete membership"),
        ("HyperLogLog merge", "Probabilistic", "Cardinality union", "HLL exact count", "Merge HLL across CDN edges"),
        ("Top-K heavy hitters", "Streaming", "Frequent items", "Sort all counts", "Count-min sketch then exact"),
        ("Space saving algorithm", "Streaming", "Heavy hitters", "Space saving billing", "Streaming top-K"),
        ("FM sketch distinct", "Streaming", "Distinct count stream", "FM exact", "Flajolet-Martin variant"),
        ("T-digest percentiles", "Streaming", "Streaming quantiles", "T-digest exact", "Latency percentile t-digest"),
        ("DDSketch percentiles", "Streaming", "Mergeable quantiles", "Histogram only", "Datadog DDSketch merge"),
        ("Exponential histogram", "Streaming", "OpenTelemetry metrics", "Fixed bucket histogram", "OTel exponential histogram"),
        ("Adjacency matrix dense graph", "Graphs", "Dense graph ops", "Matrix sparse social", "Dense 100 node graph"),
        ("Adjacency list sparse graph", "Graphs", "Sparse service graph", "List dense matrix", "Microservice adjacency list"),
        ("Edge list graph storage", "Graphs", "Simple edge iteration", "Edge list path query", "Batch graph edge list"),
        ("Incidence matrix", "Graphs", "Edge-node relations", "Incidence routing", "Academic incidence matrix"),
        ("Euler path circuit", "Graphs", "Route traversal", "Euler social graph", "Delivery route Euler"),
        ("Hamiltonian path", "Graphs", "Visit all nodes", "Hamiltonian production", "TSP related NP-hard"),
        ("Minimum spanning tree", "Graphs", "Network design", "MST service mesh", "Kruskal network backbone"),
        ("Union find path compression", "Graphs", "Near O(1) union find", "Union find no compression", "Path compression rank"),
        ("Tarjan SCC algorithm", "Graphs", "Strongly connected", "Tarjan microservices", "Dependency SCC cycles"),
        ("Articulation point bridge", "Graphs", "Single point failure", "Articulation network", "Bridge link critical"),
        ("Network flow max flow", "Graphs", "Capacity planning", "Max flow CRUD", "Traffic capacity flow"),
        ("Bipartite matching", "Graphs", "Assignment problems", "Bipartite API design", "Worker task assignment"),
        ("A star pathfinding", "Graphs", "Heuristic search", "A* SQL query", "Game map A* path"),
        ("Bidirectional BFS", "Graphs", "Shorter path search", "BFS always enough", "Social six degrees bidirectional"),
        ("Iterative deepening DFS", "Graphs", "Memory bounded DFS", "IDDFS production DB", "Game tree search"),
        ("Trie map autocomplete", "Tries", "Prefix completion", "Trie exact only", "Search autocomplete trie"),
        ("Patricia trie radix", "Tries", "Compressed prefix", "Patricia routing", "Linux routing table"),
        ("Suffix array vs suffix tree", "Strings", "Substring index", "Suffix array app", "Bioinformatics suffix array"),
        ("FM-index compression", "Strings", "Compressed full text", "FM-index API", "Compressed genome index"),
        ("Deque monotonic queue", "Deque", "Sliding window max", "Deque FIFO only", "Stock span monotonic deque"),
        ("Circular buffer overwrite", "Arrays", "Bounded telemetry", "Unbounded buffer", "Metrics ring buffer"),
        ("Gap buffer text editor", "Arrays", "Text editing", "Gap buffer API", "Editor gap buffer"),
        ("Rope data structure", "Strings", "Large string edit", "Rope small string", "Document editor rope"),
        ("Piece table text", "Strings", "Undo friendly text", "Piece table API", "IDE piece table"),
        ("Bitset compact flags", "Arrays", "Feature flags compact", "Bitset user profile", "Permission bitset"),
        ("Roaring bitmap", "Probabilistic", "Sparse set compression", "Roaring small set", "Analytics roaring bitmap"),
        ("Bitmap index columnstore", "Indexing", "Low cardinality filter", "Bitmap OLTP", "Columnstore bitmap filter"),
        ("Inverted index postings", "Search", "Full text core", "Inverted KV only", "Elasticsearch postings"),
        ("Forward index", "Search", "Doc to terms", "Forward search", "Highlight forward index"),
        ("Geospatial index R-tree", "Indexing", "Location queries", "Lat long string scan", "PostGIS spatial index"),
        ("Time series compression", "Arrays", "Gorilla timestamp", "Raw timestamp array", "Prometheus gorilla compression"),
        ("Learned index ML", "Indexing", "ML replaces B-tree research", "Learned index production default", "Research learned index"),
        ("Memtable skip list LSM", "Storage", "Write buffer ordered", "Memtable hash", "RocksDB memtable skiplist"),
        ("SSTable immutable", "Storage", "LSM disk level", "SSTable mutable", "Cassandra SSTable"),
        ("LSM tree compaction", "Storage", "Write amplification", "Ignore compaction", "Level compaction strategy"),
        ("B-tree vs LSM tradeoff", "Storage", "Read vs write heavy", "LSM for read heavy OLTP", "Choose by workload"),
        ("Memory mapped file index", "Storage", "OS page cache", "Mmap small file", "Embedded DB mmap"),
        ("Off heap storage", "Performance", "GC pressure reduce", "Off heap everywhere", "BigCache off-heap Go"),
        ("Struct of arrays SOA", "Performance", "Cache friendly batch", "AOS always", "SIMD SOA processing"),
        ("Array of structs AOS", "Performance", "Object oriented layout", "AOS analytics scan", "Default object layout"),
        ("Pointer chasing cost", "Performance", "Linked list cache miss", "Pointer chasing array", "Prefer array sequential"),
        ("Cache line false sharing", "Performance", "Concurrent counters", "False sharing ignored", "Padded counter per core"),
        ("Data structure selection framework", "Framework", "Match access pattern", "Resume DS trivia", "ADR hash vs B-tree"),
        ("Immutable persistent vector", "Functional DS", "Clojure style", "Persistent .NET default", "Immutable collections NuGet"),
        ("Hamt hash array mapped", "Functional DS", "Immutable map", "Hamt SQL index", "Clojure immutable map"),
        ("Zippers functional navigation", "Functional DS", "Tree navigation", "Zipper API design", "Functional tree edit"),
        ("CRDT data structures", "Distributed DS", "Conflict free replicate", "CRDT SQL primary", "Collaborative edit CRDT"),
        ("OR-set CRDT", "Distributed DS", "Add remove set", "OR-set billing", "Shopping cart OR-set"),
        ("G-counter PN-counter", "Distributed DS", "Distributed count", "G-counter ledger", "Metrics counter CRDT"),
        ("LWW-register last write", "Distributed DS", "Simple resolve", "LWW financial balance", "Profile preference LWW"),
        ("Merkle DAG IPFS", "Trees", "Content address graph", "Merkle DAG API", "IPFS merkle DAG"),
        ("Verkle tree ethereum", "Trees", "State commitment", "Verkle app DB", "Ethereum state tree"),
        ("Bw-tree lock free index", "Trees", "Research concurrent index", "Bw-tree hand roll", "SQL Server In-Memory OLTP"),
    ],
    6: [
        ("Quickselect kth element", "Selection", "O(n) average kth", "Sort for kth", "Median quickselect"),
        ("Median of medians", "Selection", "Worst case linear", "MoM overkill", "Theory guaranteed median"),
        ("Introselect hybrid", "Selection", "Practical kth", "Introselect API", "Hybrid select algorithm"),
        ("Timsort hybrid sort", "Sorting", "Real world data", "Timsort custom", "Python Java default sort"),
        ("Stable sort requirement", "Sorting", "Preserve order", "Unstable when need stable", "Sort orders by date stable"),
        ("External merge sort", "Sorting", "Disk large sort", "In-memory sort 1TB", "MapReduce shuffle sort"),
        ("Radix sort strings", "Sorting", "Fixed width keys", "Radix variable unicode", "IP address radix sort"),
        ("Counting sort frequency", "Sorting", "Small range keys", "Counting sort general", "Age bucket counting"),
        ("Bucket sort uniform", "Sorting", "Uniform distribution", "Bucket sort skewed", "Hash bucket sort"),
        ("Shell sort gap", "Sorting", "In-place medium", "Shell production", "Embedded sort shell"),
        ("Insertion sort nearly sorted", "Sorting", "Small nearly sorted", "Insertion large random", "Timsort run insertion"),
        ("Binary search bounds", "Search", "Lower upper bound", "Binary search exact only", "bisect_left bisect_right"),
        ("Exponential search unbounded", "Search", "Unbounded array", "Exponential bounded", "Infinite list search"),
        ("Interpolation search uniform", "Search", "Uniform sorted", "Interpolation skewed", "Phone book interpolation"),
        ("Ternary search unimodal", "Search", "Unimodal function", "Ternary general search", "Peak finding ternary"),
        ("BFS shortest unweighted", "Graphs", "Shortest path unweighted", "DFS shortest path", "Service blast BFS"),
        ("DFS cycle detection", "Graphs", "Detect cycles", "BFS cycle only", "Dependency cycle DFS"),
        ("Kahn topological sort", "Graphs", "DAG ordering", "Topo sort cyclic", "Build pipeline Kahn"),
        ("Floyd Warshall all pairs", "Graphs", "All pairs shortest", "Floyd large sparse", "Dense graph Floyd"),
        ("Johnson all pairs sparse", "Graphs", "Sparse all pairs", "Johnson dense", "Sparse APSP Johnson"),
        ("A* heuristic search", "Graphs", "Path with heuristic", "A* no heuristic", "Navigation A*"),
        ("Bidirectional Dijkstra", "Graphs", "Faster shortest path", "Unidirectional enough", "Large graph bidirectional"),
        ("Bellman Ford negative", "Graphs", "Negative edge weights", "Bellman no negative", "Currency arbitrage Bellman"),
        ("SPFA queue Bellman", "Graphs", "Bellman optimized", "SPFA adversarial", "Contest SPFA"),
        ("Prim MST algorithm", "Graphs", "Minimum spanning tree", "Prim dense graph", "Network Prim MST"),
        ("Kruskal MST union find", "Graphs", "MST sparse", "Kruskal dense", "Kruskal network design"),
        ("Tarjan bridges articulation", "Graphs", "Critical edges", "Tarjan overkill", "Network SPOF Tarjan"),
        ("Kosaraju SCC", "Graphs", "Strongly connected", "Kosaraju microservice", "SCC dependency analysis"),
        ("Edmonds Karp max flow", "Graphs", "Max flow", "Max flow CRUD", "Capacity planning flow"),
        ("Dinic max flow", "Graphs", "Faster max flow", "Dinic small graph", "Dinic competitive flow"),
        ("Min cut max flow theorem", "Graphs", "Cut capacity", "Min cut API", "Network partition min cut"),
        ("Hungarian assignment", "Graphs", "Bipartite assignment", "Hungarian large", "Task assignment Hungarian"),
        ("DP knapsack 0-1", "DP", "Resource allocation", "Knapsack unbounded wrong", "Budget feature knapsack"),
        ("DP longest increasing", "DP", "Sequence LIS", "LIS production DB", "Analytics LIS"),
        ("DP edit distance", "DP", "String similarity", "Edit distance real time", "Fuzzy match Levenshtein"),
        ("DP matrix chain multiply", "DP", "Optimal parenthesis", "Matrix chain API", "Query optimization chain"),
        ("DP coin change", "DP", "Minimum coins", "Coin change billing", "Denominations coin change"),
        ("DP subset sum", "DP", "Partition problem", "Subset sum API", "Resource partition subset"),
        ("DP palindrome partitioning", "DP", "String partition", "Palindrome API", "Text processing palindrome"),
        ("Memoization top down", "DP", "Recursive cache", "Memo everywhere", "Top-down expensive subproblems"),
        ("Tabulation bottom up", "DP", "Iterative DP", "Bottom up always", "Space optimized tabulation"),
        ("State machine DP", "DP", "Order state paths", "State machine overkill", "Workflow state DP"),
        ("Bitmask DP", "DP", "Small set TSP", "Bitmask large n", "TSP small n bitmask"),
        ("Tree DP on trees", "DP", "Tree optimization", "Tree DP SQL", "Org hierarchy tree DP"),
        ("Digit DP", "DP", "Count digit constraints", "Digit DP API", "Compliance digit rules"),
        ("Convex hull trick", "DP", "Optimization trick", "Convex hull general", "Competitive DP trick"),
        ("Divide conquer master theorem", "Complexity", "Recurrence solve", "Master theorem guess", "Merge sort analysis"),
        ("Karatsuba multiplication", "Divide Conquer", "Big integer", "Karatsuba crypto", "Large number multiply"),
        ("Strassen matrix multiply", "Divide Conquer", "Matrix faster", "Strassen small matrix", "ML Strassen large"),
        ("Closest pair divide", "Divide Conquer", "2D closest", "Closest pair API", "GIS closest pair"),
        ("FFT signal multiply", "Divide Conquer", "Polynomial multiply", "FFT API sort", "Signal processing FFT"),
        ("Greedy activity selection", "Greedy", "Scheduling intervals", "Greedy when DP needed", "Meeting room greedy"),
        ("Greedy Huffman coding", "Greedy", "Compression", "Huffman encryption", "Compression Huffman"),
        ("Greedy fractional knapsack", "Greedy", "Fractional items", "Greedy 0-1 knapsack wrong", "Resource fractional greedy"),
        ("Greedy interval scheduling", "Greedy", "Max non-overlap", "Greedy all intervals", "Maintenance window schedule"),
        ("Greedy minimum platforms", "Greedy", "Train platform", "Platform API design", "Scheduling platform greedy"),
        ("Amortized analysis dynamic array", "Complexity", "ArrayList resize", "Amortized ignored", "List resize amortized O(1)"),
        ("Amortized analysis splay tree", "Complexity", "Splay operations", "Splay production DB", "Splay amortized analysis"),
        ("Potential method amortized", "Complexity", "Accounting method", "Potential hand wave", "Fibonacci heap potential"),
        ("Aggregate analysis", "Complexity", "Total cost average", "Aggregate worst case", "Queue operations aggregate"),
        ("Worst average amortized", "Complexity", "Three analysis types", "Only average quote", "Hash table three analyses"),
        ("NP complete recognition", "Complexity", "Know intractable", "NP trivia only", "Route planning NP-hard"),
        ("Approximation algorithms", "Complexity", "Near optimal", "Approximate billing exact", "TSP 2-approx"),
        ("Randomized quicksort", "Sorting", "Expected O(n log n)", "Randomized deterministic need", "Quickselect randomized"),
        ("Monte Carlo algorithms", "Randomized", "Probabilistic correct", "Monte Carlo financial exact", "Primality Monte Carlo"),
        ("Las Vegas algorithms", "Randomized", "Always correct random time", "Las Vegas API", "Quickselect Las Vegas"),
        ("Reservoir sampling stream", "Randomized", "Stream sample k", "Reservoir full data", "Log stream reservoir"),
        ("Fisher Yates shuffle", "Randomized", "Uniform shuffle", "Sort random shuffle", "Playlist shuffle Fisher"),
        ("KMP string matching", "String", "Pattern search", "KMP short pattern", "DNA pattern KMP"),
        ("Rabin Karp rolling hash", "String", "Multi pattern", "Rabin Karp collision ignore", "Plagiarism Rabin Karp"),
        ("Z algorithm prefix", "String", "Prefix function", "Z algorithm API", "String analysis Z"),
        ("Suffix automaton", "String", "Advanced substring", "Suffix automaton CRUD", "Competitive substring"),
        ("Manacher palindrome", "String", "Longest palindrome", "Manacher API", "Text palindrome Manacher"),
        ("Two pointers sorted array", "Patterns", "Pair sum sorted", "Two pointers unsorted", "Merge sorted streams"),
        ("Sliding window variable", "Patterns", "Longest substring", "Fixed window only", "Rate limit sliding window"),
        ("Sliding window fixed", "Patterns", "Max sum size k", "Variable when fixed", "Metrics fixed window"),
        ("Prefix sum range query", "Patterns", "O(1) range sum", "Prefix sum update heavy", "Analytics prefix sum"),
        ("Difference array range update", "Patterns", "Range increment", "Diff array point query", "Bulk schedule diff array"),
        ("Monotonic stack", "Patterns", "Next greater element", "Monotonic queue only", "Stock span monotonic stack"),
        ("Monotonic queue", "Patterns", "Sliding max", "Monotonic stack max", "Window max monotonic queue"),
        ("Binary lifting LCA", "Trees", "Tree LCA query", "Binary lifting flat", "Org chart LCA"),
        ("Euler tour tree", "Trees", "Subtree query", "Euler tour API", "Tree path query euler"),
        ("Heavy light decomposition", "Trees", "Path query tree", "HLD SQL", "Tree analytics HLD"),
        ("Mo algorithm offline queries", "Patterns", "Offline range query", "Mo online", "Competitive range Mo"),
        ("Sqrt decomposition", "Patterns", "Block queries", "Sqrt decomposition stream", "Range query sqrt decomp"),
        ("Segment tree lazy propagation", "Trees", "Range update query", "Segment tree point only", "Price range lazy segtree"),
        ("Fenwick tree 2D", "Trees", "2D prefix sum", "2D BIT overkill", "Matrix frequency BIT"),
        ("Parallel merge sort", "Parallel", "Multi core sort", "Parallel small array", "Batch sort parallel"),
        ("MapReduce algorithm pattern", "Parallel", "Distributed batch", "MapReduce OLTP", "ETL MapReduce word count"),
        ("Fork join pool", "Parallel", "Recursive parallel", "Fork join API request", "Parallel LINQ PLINQ"),
        ("Algorithm choice ADR", "Framework", "Document algo choice", "Algo trivia", "ADR Dijkstra vs BFS"),
        ("Big O interview communication", "Complexity", "Explain scaling", "Memorize only", "This O(n) breaks at 10M rows"),
        ("Space time tradeoff", "Complexity", "Precompute lookup", "Always optimize time", "Lookup table space trade"),
        ("Cache oblivious algorithms", "Performance", "Memory hierarchy", "Cache oblivious API", "Research cache oblivious"),
        ("Branch prediction friendly", "Performance", "Sorted branchless", "Random branch chain", "Sort for branch prediction"),
        ("Algorithm profiling before optimize", "Performance", "Measure hot path", "Optimize cold path", "BenchmarkDotNet before algo change"),
    ],
    7: [
        ("Clustered index design", "Indexing", "Primary access path", "GUID clustered PK", "BIGINT sequential clustered"),
        ("Index include columns", "Indexing", "Covering queries", "Include everything", "INCLUDE selective columns"),
        ("Filtered index partial", "Indexing", "Subset index", "Filtered when full fine", "WHERE Status=Active filtered index"),
        ("Columnstore index OLAP", "Analytics", "Aggregation scan", "Columnstore OLTP point", "NCCI analytics offload"),
        ("Index maintenance rebuild", "Operations", "Fragmentation fix", "Rebuild nightly all", "Reorganize vs rebuild threshold"),
        ("Statistics auto update", "Performance", "Cardinality accurate", "Stats never updated", "AUTO_UPDATE_STATISTICS_ASYNC"),
        ("Parameter sniffing fix", "Performance", "Plan stability", "Ignore sniffing", "OPTIMIZE FOR UNKNOWN or RECOMPILE"),
        ("Plan cache bloat", "Performance", "Adhoc query cache", "Plan cache ignored", "Forced parameterization review"),
        ("Query store regression", "Performance", "Plan regression detect", "No baseline plan", "Query Store force plan cautiously"),
        ("Missing index DMV", "Performance", "Index suggestions", "Blind create all DMV", "DMV suggestion review"),
        ("Index usage DMV", "Operations", "Drop unused indexes", "Keep all indexes", "sys.dm_db_index_usage_stats"),
        ("Lock escalation control", "Concurrency", "Row to table lock", "Escalation surprises", "LOCK_ESCALATION disable niche"),
        ("Row versioning RCSI", "Transactions", "Reader writer nonblock", "RCSI without tempdb plan", "READ_COMMITTED_SNAPSHOT ON"),
        ("Snapshot isolation level", "Transactions", "Statement consistent snapshot", "Snapshot for all", "ALLOW_SNAPSHOT_ISOLATION selective"),
        ("Serializable range locks", "Transactions", "Phantom prevention", "Serializable catalog", "Transfer SP serializable"),
        ("Deadlock graph analysis", "Concurrency", "Deadlock root cause", "Retry forever no fix", "Extended events deadlock graph"),
        ("Blocking chain analysis", "Concurrency", "Who blocks whom", "Kill blocker always", "sp_whoisactive blocking"),
        ("Optimistic concurrency rowversion", "Concurrency", "EF rowversion", "Last write wins money", "RowVersion column EF"),
        ("Application lock sp_getapplock", "Concurrency", "App level mutex", "Applock everything", "Batch job applock"),
        ("Sequence vs identity", "Design", "Distributed id gen", "Identity scale out", "SEQUENCE gap cache"),
        ("Temporal tables system", "Features", "Audit history", "Temporal for all tables", "SYSTEM_VERSIONING orders"),
        ("Change data capture CDC", "Integration", "Change stream SQL", "CDC instead of events", "CDC to event hub"),
        ("Change tracking lightweight", "Integration", "Sync lightweight", "CT heavy analytics", "CT mobile sync"),
        ("Service broker async", "Messaging", "In-SQL async", "Service broker new apps", "Legacy broker pattern"),
        ("Linked server security", "Integration", "Cross server query", "Linked server default", "Pass-through auth review"),
        ("OpenQuery distributed", "Integration", "Remote query", "OpenQuery injection", "Parameterized openquery caution"),
        ("PolyBase external data", "Integration", "Data lake query", "PolyBase OLTP", "PolyBase parquet lake"),
        ("Stretch database archive", "Scale", "Cold row archive", "Stretch primary workload", "Stretch archive policy"),
        ("In-memory OLTP", "Performance", "Latch free hot tables", "In-memory everything", "Memory optimized table niche"),
        ("Natively compiled SP", "Performance", "In-memory SP", "Natively compiled all", "Nat compiled hot path"),
        ("Columnstore batch mode", "Analytics", "Vectorized execution", "Batch mode rowstore", "Batch mode columnstore"),
        ("Batch mode on rowstore", "Performance", "Rowstore batch", "Expect batch always", "Batch mode eligibility"),
        ("Intelligent query processing", "Performance", "Adaptive joins memory", "Disable IQP", "Adaptive query processing"),
        ("Memory grant feedback", "Performance", "Spill prevention", "Ignore spills", "Memory grant feedback adaptive"),
        ("Interleaved execution", "Performance", "TVF row estimate", "Multi statement TVF", "Inline TVF prefer"),
        ("Scalar UDF inline", "Performance", "UDF performance", "Scalar UDF hot path", "Inline UDF SQL 2019"),
        ("Tempdb optimization", "Operations", "Contention PFS GAM SGAM", "One tempdb file", "Multiple tempdb data files"),
        ("Tempdb version store", "Transactions", "RCSI snapshot cleanup", "Version store unmonitored", "Version store size alert"),
        ("Filegroup strategy", "Design", "Partition filegroups", "Single filegroup all", "DATA filegroup ARCHIVE separate"),
        ("Partition function scheme", "Scale", "Partition key choice", "Partition small table", "Monthly partition function"),
        ("Partition elimination", "Performance", "Query prune partitions", "Scan all partitions", "WHERE on partition key"),
        ("Sliding window partition", "Operations", "Archive maintenance", "DELETE millions archive", "SWITCH partition archive"),
        ("Compression row page", "Operations", "Storage save", "Compress OLTP hot", "PAGE compression archive"),
        ("Backup strategy full diff log", "Operations", "RPO RTO backup", "Full only huge DB", "Full weekly diff daily log 15min"),
        ("Tail log backup", "Operations", "Recover to point", "No tail log plan", "Tail log before migration"),
        ("Piecemeal restore", "Operations", "Large DB restore", "Full restore only", "Piecemeal filegroup restore"),
        ("Instant file initialization", "Operations", "Fast data file growth", "IFI off slow growth", "IFI service account privilege"),
        ("VLF count transaction log", "Operations", "Log performance", "Tiny log growth repeats", "VLF count reasonable growth"),
        ("Log reuse wait status", "Operations", "Log full diagnose", "Shrink log only fix", "DBCC LOGINFO VLF reuse"),
        ("Always On readable secondary", "HA/DR", "Read offload", "Stale read ignored", "ApplicationIntent ReadOnly"),
        ("Availability group listener", "HA/DR", "Failover connection", "Connect primary name", "Listener MultiSubnetFailover"),
        ("Distributed AG", "HA/DR", "Geo DR chain", "Distributed AG complexity", "Cross-region distributed AG"),
        ("Failover cluster instance", "HA/DR", "Shared storage HA", "FCI vs AG choice", "FCI SQL legacy"),
        ("Log shipping DR", "HA/DR", "Simple DR", "Log shipping HA primary", "Log shipping warm standby"),
        ("Database mirroring legacy", "HA/DR", "Legacy mirror", "Mirror new deploy", "AG replaces mirroring"),
        ("Replication transactional", "Integration", "Publisher subscriber", "Replication instead of CDC", "Transactional replication reporting"),
        ("Merge replication legacy", "Integration", "Bi-directional sync", "Merge new design", "Legacy merge mobile"),
        ("Snapshot replication", "Integration", "Initial sync", "Snapshot continuous", "Snapshot once then transactional"),
        ("Peer to peer replication", "Integration", "Multi master", "P2P conflict ignore", "P2P write conflict handling"),
        ("Contained database users", "Security", "Portability auth", "Contained always", "Contained user AAD"),
        ("TDE encryption", "Security", "At rest encrypt", "TDE without key mgmt", "TDE CMK Key Vault"),
        ("Always Encrypted", "Security", "Client side encrypt", "Always Encrypted search", "Deterministic AE limited"),
        ("Dynamic data masking", "Security", "Mask nonprod", "Mask instead of auth", "DDM credit card mask"),
        ("Row level security", "Security", "Tenant filter DB", "RLS only app filter", "RLS predicate tenant"),
        ("Column encryption keys", "Security", "Sensitive columns", "CEK overuse", "CEK SSN column"),
        ("Audit specification", "Compliance", "Who accessed what", "No SQL audit", "Server audit specification"),
        ("Extended events lightweight", "Diagnostics", "Trace replacement", "SQL Profiler prod", "XEvent deadlock capture"),
        ("DMV performance baseline", "Diagnostics", "Baseline metrics", "DMV snapshot once", "Baseline wait stats weekly"),
        ("Query hash plan analysis", "Performance", "Same query plans", "Ignore plan hash", "Query hash regression compare"),
        ("DBCC CHECKDB integrity", "Operations", "Corruption detect", "Skip checkdb", "CHECKDB weekly maintenance"),
        ("Index rebuild online", "Operations", "Enterprise online", "Offline rebuild peak", "ONLINE=ON Enterprise"),
        ("Maxdop degree parallelism", "Performance", "CPU parallelism", "MAXDOP 0 always", "MAXDOP 4 OLTP guidance"),
        ("Cost threshold parallelism", "Performance", "Parallel plan threshold", "Default 5 always", "Raise cost threshold OLTP"),
        ("Cardinality estimator CE", "Performance", "Legacy vs new CE", "CE change surprise", "Test with compatibility CE"),
        ("Database compatibility level", "Upgrades", "Upgrade test", "Compat bump blind", "Compat 150 test before"),
        ("Query hint use sparingly", "Performance", "Hint last resort", "Hint first fix", "RECOMPILE hint targeted"),
        ("Table variable cardinality", "Performance", "TV variable estimate", "TV large rows", "Temp table instead TV"),
        ("Temp table vs table variable", "Performance", "Stats on temp", "TV always", "#temp stats optimizer"),
        ("CTE vs temp table", "Performance", "Materialize choice", "CTE huge materialize", "Temp table intermediate"),
        ("Window functions performance", "Analytics", "ROW_NUMBER RANK", "Correlated subquery", "Window over self join"),
        ("PAGLOCK UPDLOCK hints", "Concurrency", "Explicit locking", "Hint without need", "Transfer UPDLOCK HOLDLOCK"),
        ("Isolation read uncommitted", "Transactions", "Dirty read report", "RU production default", "NOLOCK report only"),
        ("Distributed transaction MSDTC", "Transactions", "Cross DB TX", "MSDTC microservices", "Avoid MSDTC saga instead"),
        ("Elastic query cross database", "Azure", "Cross DB query", "Elastic OLTP primary", "Elastic query analytics"),
        ("Hyperscale architecture", "Azure", "Auto scale storage", "Hyperscale small DB", "Hyperscale 4TB+ Azure"),
        ("Serverless SQL auto pause", "Azure", "Dev cost save", "Serverless prod peak", "Serverless dev test"),
        ("Managed instance vs VM", "Azure", "PaaS SQL", "VM when MI fits", "MI migration assessment"),
        ("SqlPackage bacpac deploy", "DevOps", "Schema data deploy", "Manual script prod", "SqlPackage CI CD"),
        ("Flyway Liquibase SQL", "DevOps", "Migration tool", "Manual migration", "Flyway versioned migrations"),
        ("Redgate SQL compare", "DevOps", "Schema diff", "Compare no review", "SQL compare PR review"),
        ("Database unit test tSQLt", "Testing", "SP test", "No SQL tests", "tSQLt procedure tests"),
        ("Synthetic workload replay", "Testing", "Load test SQL", "Prod on test", "Replay distributed replay"),
        ("Query tuning methodology", "Performance", "Measure guide", "Index spam", "IO stats plan regressions"),
    ],
}


def _all_concepts(week: int) -> list[tuple]:
    key = WEEK_BANK_KEY[week]
    base = list(CONCEPTS.get(key, []))
    extra = EXTRA_CONCEPTS.get(week, [])
    return base + extra


def _tier_title(title: str, tier: str, idx: int) -> str:
    """Ensure unique display title per question."""
    if tier == "intermediate":
        return title
    if tier == "advanced":
        return f"{title} — Advanced"
    return f"{title} Scenario"


def _make_intermediate(concept: tuple, week: int, idx: int) -> dict:
    title, category, when_use, when_avoid, example = concept
    topic = WEEK_TOPICS[week][0]
    display = _tier_title(title, "intermediate", idx)
    return q(
        display,
        category,
        "Very Common" if idx % 3 == 0 else ("Common" if idx % 3 == 1 else "Occasional"),
        f"What is {title} and when would you apply it in {topic}?",
        f"Use {title} when {when_use.lower()}. Avoid when {when_avoid.lower()}. Production example: {example}.",
        f"**Concept:** {title}\n\n**When to use:** {when_use}\n\n**When to avoid:** {when_avoid}\n\n**Production example:** {example}\n\n"
        f"**Architect workflow:**\n1. Map the access pattern or runtime behavior to this concept\n"
        f"2. Validate with metrics (latency, throughput, memory, IO)\n"
        f"3. Document the choice in team standards or ADR when cross-cutting\n\n"
        f"**Interview tip:** Connect {title} to a real system you operated — not textbook definitions only.",
        f"Interviewers expect architects to justify {title} with production trade-offs in {topic}.",
        f"When is {title} overkill? — {when_avoid}",
        f"How measure success after adopting {title}? — Define before/after metric on the hot path.",
        f"Quoting {title} without production example",
        f"Using {title} when {when_avoid.lower()}",
        f"No rollback plan when {title} misconfigured",
    )


def _make_advanced(concept: tuple, week: int, idx: int) -> dict:
    title, category, when_use, when_avoid, example = concept
    topic = WEEK_TOPICS[week][0]
    display = _tier_title(title, "advanced", idx)
    return q(
        display,
        category,
        "Common" if idx % 2 == 0 else "Uncommon",
        f"What are the advanced trade-offs and failure modes of {title} at scale in {topic}?",
        f"At scale, {title} trades {when_use.lower()} against operational complexity. Primary failure mode: {when_avoid.lower()}.",
        f"**Advanced analysis of {title}:**\n\n"
        f"**Strengths at scale:** {when_use}\n\n"
        f"**Failure modes:**\n- Misapplication when {when_avoid.lower()}\n- Missing observability on the hot path\n- Team skill gap operating the pattern\n\n"
        f"**Production reference:** {example}\n\n"
        f"**Mitigations:**\n- Load test at 2× expected peak before production\n- Define rollback/feature-flag path\n- Add dashboards for the metrics this concept affects\n\n"
        f"**Architecture review question:** Would we still choose {title} if traffic 10× or team shrinks 50%?",
        f"Advanced questions probe whether you have operated {title} — not just defined it.",
        f"What monitoring proves {title} healthy? — SLI tied to {example.lower()}.",
        f"When would you remove or replace {title}? — Context change triggers ADR supersede.",
        f"Treating {title} as set-and-forget",
        f"No load test before enabling {title} in production",
        f"Ignoring cost/ops overhead of {title}",
    )


def _make_expert(concept: tuple, week: int, idx: int) -> dict:
    title, category, _when_use, _when_avoid, example = concept
    topic = WEEK_TOPICS[week][0]
    scenario_tpl = EXPERT_SCENARIOS[idx % len(EXPERT_SCENARIOS)]
    scenario_kind, scenario_q = scenario_tpl
    display = _tier_title(title, "expert", idx)
    prompt = scenario_q.format(topic=topic, title=title)
    return q(
        display,
        "Scenario",
        "Very Common" if idx % 4 == 0 else "Common",
        prompt,
        f"Lead with stabilization, evidence gathering, and a phased plan referencing {title} and {example.lower()}.",
        f"**Situation ({scenario_kind}):** {prompt}\n\n"
        f"**Immediate (0–48h):**\n- Stabilize customer impact; communicate status\n- Capture metrics/logs around {title}\n- Form cross-functional war room if revenue-impacting\n\n"
        f"**Diagnosis:**\n- Compare expected vs actual behavior of {title}\n- Check recent changes (deploy, config, scale event)\n- Reference production pattern: {example}\n\n"
        f"**Recommendation:**\n- Short-term containment with explicit residual risk\n- Medium-term fix with measurable acceptance criteria\n- Long-term ADR update and guardrails (dashboards, tests, runbooks)\n\n"
        f"**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.",
        f"Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.",
        f"What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.",
        f"Who must sign off residual risk? — Product + ops + security as applicable.",
        f"Panic changes without rollback plan",
        f"Technical fix without communication plan",
        f"No follow-up ADR or runbook update after incident",
    )


def build_week(week: int) -> tuple[list, list, list]:
    concepts = _all_concepts(week)
    if len(concepts) < 90:
        raise ValueError(f"Week {week}: need 90 concepts, have {len(concepts)}")
    concepts = concepts[:90]
    intermediate = [_make_intermediate(concepts[i], week, i) for i in range(40)]
    advanced = [_make_advanced(concepts[i], week, i) for i in range(40, 70)]
    expert = [_make_expert(concepts[i], week, i) for i in range(70, 90)]
    return intermediate, advanced, expert


def _render_list(name: str, items: list) -> str:
    lines = [f"{name} = ["]
    for item in items:
        lines.append("    q(")
        fields = [
            "title", "category", "frequency", "question", "short",
            "detailed", "perspective", "followups", "mistakes",
        ]
        # followups and mistakes are pre-formatted in q(); re-parse from dict
        d = item
        args = [
            d["title"], d["category"], d["frequency"], d["question"],
            d["short"], d["detailed"], d["perspective"],
        ]
        # Extract fu1,fu2,m1,m2,m3 from followups/mistakes
        fu_lines = [x.strip() for x in d["followups"].split("\n") if x.strip()]
        fu1 = fu_lines[0].lstrip("1. ").strip("*") if fu_lines else "Follow up?"
        fu2 = fu_lines[1].lstrip("2. ").strip("*") if len(fu_lines) > 1 else "Follow up 2?"
        fu1 = fu1.strip("*").strip()
        fu2 = fu2.strip("*").strip()
        m_lines = [x.lstrip("- ").strip() for x in d["mistakes"].split("\n") if x.strip()]
        while len(m_lines) < 3:
            m_lines.append("Incomplete response")
        args.extend([fu1, fu2, m_lines[0], m_lines[1], m_lines[2]])
        for i, a in enumerate(args):
            comma = "," if i < len(args) - 1 else ""
            lines.append(f"      {a!r}{comma}")
        lines.append("    ),")
    lines.append("]")
    return "\n".join(lines)


def main() -> None:
    weeks_data = {}
    all_titles: set[str] = set()
    for week in range(2, 8):
        inter, adv, exp = build_week(week)
        weeks_data[week] = (inter, adv, exp)
        for bank in (inter, adv, exp):
            assert len(bank) in (40, 30, 20), f"Week {week} wrong bank size"
            for item in bank:
                t = item["title"]
                if t in all_titles:
                    raise ValueError(f"Duplicate title: {t}")
                all_titles.add(t)

    header = textwrap.dedent(
        '''\
        """Hand-crafted premium interview banks for Weeks 2–7.

        Week 2: .NET Runtime (CLR, GC, DI, middleware, hosting, configuration)
        Week 3: SOLID & Clean Architecture (layers, dependency rule, ports/adapters)
        Week 4: Design Patterns (GoF, enterprise patterns, anti-patterns)
        Week 5: Data Structures (hash, trees, heaps, graphs, bloom, consistent hash)
        Week 6: Algorithms (Big O, sorting, graphs, DP, greedy)
        Week 7: SQL Server (indexing, plans, isolation, Always On, partitioning)

        Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
        Total: 540 questions.
        """

        from premium_qa_data import q

        '''
    )

    parts = [header]
    for week in range(2, 8):
        inter, adv, exp = weeks_data[week]
        parts.append(_render_list(f"WEEK_{week:02d}_INTERMEDIATE", inter))
        parts.append("")
        parts.append(_render_list(f"WEEK_{week:02d}_ADVANCED", adv))
        parts.append("")
        parts.append(_render_list(f"WEEK_{week:02d}_EXPERT", exp))
        parts.append("")

    bank_entries = []
    for week in range(2, 8):
        bank_entries.append(
            f"    {week}: {{\n"
            f'        "intermediate": WEEK_{week:02d}_INTERMEDIATE,\n'
            f'        "advanced": WEEK_{week:02d}_ADVANCED,\n'
            f'        "expert": WEEK_{week:02d}_EXPERT,\n'
            f"    }},"
        )
    parts.append("ALL_WEEKS_02_07_BANKS = {\n" + "\n".join(bank_entries) + "\n}\n")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))

    total = sum(len(inter) + len(adv) + len(exp) for inter, adv, exp in weeks_data.values())
    print(f"Wrote {OUT}")
    print(f"Total questions: {total}")
    for week in range(2, 8):
        inter, adv, exp = weeks_data[week]
        print(f"Week {week}: I={len(inter)} A={len(adv)} E={len(exp)}")


if __name__ == "__main__":
    main()
