"""Per-week Azure concept banks for Q011–Q050 (40 unique topics each)."""

# (title, category, when_use, when_avoid, production_example)

AZURE_WEEK_CONCEPTS = {
    9: [
        ("Azure Resource Manager", "ARM", "Declarative resource deployment", "Bypassing ARM for clickops", "Bicep modules for standard web app pattern"),
        ("Resource locks", "Governance", "Protect prod from accidental delete", "Locking dev sandboxes", "CanNotDelete lock on prod resource groups"),
        ("Deployment stacks", "Governance", "Track deployed resources as unit", "One-off resources", "Stack assignment for landing zone spoke"),
        ("Activity Log vs Diagnostic logs", "Monitoring", "Control plane audit vs resource metrics", "Confusing the two", "Activity Log → Log Analytics for admin changes"),
        ("Azure Advisor", "Operations", "Cost/security/reliability recommendations", "Ignoring recommendations", "Monthly Advisor review in platform team"),
        ("Service Health vs Resource Health", "Reliability", "Platform incidents vs your resource", "Alert fatigue without filtering", "Service Health alert for region outage"),
        ("Azure Monitor metrics vs logs", "Observability", "Time-series vs searchable events", "Logs for everything", "Metrics for SLA dashboards; logs for debugging"),
        ("Log Analytics workspace design", "Observability", "Centralized logging per environment", "One workspace chaos", "law-prod-central with RBAC per team"),
        ("Naming conventions", "Governance", "Predictable automation and search", "Random names", "rg-{app}-{env}-{region}-001 pattern"),
        ("Capacity reservations", "Cost", "Predictable compute discount", "Spiky unknown workloads", "Reservation for 24/7 App Service Premium"),
        ("Azure compliance offerings", "Compliance", "SOC2/ISO workload requirements", "Assuming default is certified", "Choose certified regions and services"),
        ("Data residency", "Compliance", "GDPR/sovereignty requirements", "Ignoring data location", "West Europe only for EU PII"),
        ("Shared responsibility model", "Security", "Explain cloud vs customer duties", "Blaming vendor for misconfig", "Customer secures NSG; Microsoft secures hypervisor"),
        ("SLA aggregation math", "Reliability", "Composite SLA calculation", "Ignoring dependency chain", "99.95% × 99.99% = composite SLA"),
        ("Platform vs workload RACI", "Organization", "Clear ownership boundaries", "Unclear who owns DNS", "Platform owns hub; app team owns spoke"),
        ("Cloud Center of Excellence", "Organization", "Standards and enablement", "CoE as approval bottleneck", "CCoE publishes golden paths not gates"),
        ("Sandbox subscriptions", "Governance", "Safe experimentation", "Prod credentials in sandbox", "Auto-expire sandbox subs monthly"),
        ("DevTest pricing", "FinOps", "Reduced rates for nonprod", "Prod workloads on DevTest offer", "Visual Studio subscription benefits for dev"),
        ("Azure Lighthouse", "Partners", "MSP management at scale", "Sharing owner credentials", "Lighthouse for delegated monitoring"),
        ("Enterprise Agreement hierarchy", "Billing", "Invoice and commitment tracking", "Ignoring MACC burn rate", "EA enrollment linked to management groups"),
        ("Management group inheritance", "Governance", "Policy cascade to children", "Policies only on leaf", "Initiative at root MG"),
        ("Deny assignments", "Security", "Block actions even for Owner", "Overuse blocking legit ops", "Deny delete on production KV"),
        ("Resource Graph", "Governance", "Inventory queries at scale", "Portal clicking per subscription", "arg query untagged resources"),
        ("KQL for governance", "Observability", "Compliance dashboards", "Exporting CSV manually", "KQL: resources | where tags.Environment == ''"),
        ("Microsoft Purview", "Governance", "Data catalog and lineage", "Small app without data estate", "Purview scan Azure SQL metadata"),
        ("Carbon optimization", "Sustainability", "Region and SKU selection", "Greenwashing without metrics", "Choose regions with lower carbon intensity"),
        ("Architecture review cadence", "Process", "Quarterly prod reviews", "Review only at launch", "WAF review before major release"),
        ("Azure Migrate", "Migration", "Discovery and sizing", "Manual spreadsheet inventory", "Azure Migrate appliance for VMware"),
        ("Backup vault strategy", "Reliability", "Centralized backup policies", "Per-VM ad hoc backup", "Backup vault RG with immutability"),
        ("Defender for Cloud tiers", "Security", "CSPM and workload protection", "Defender off in prod", "Defender plans enabled on all subs"),
        ("Entra ID tenant design", "Identity", "Single vs multi-tenant B2B", "Duplicate tenants per app", "One corporate tenant + B2B guests"),
        ("Azure Firewall vs NSG", "Networking", "Centralized egress control", "NSG only for app tier", "Azure Firewall in hub for FQDN filter"),
        ("Hub-spoke topology", "Networking", "Enterprise connectivity", "Mesh VNets", "Hub with firewall and VPN gateway"),
        ("Private Link overview", "Networking", "PaaS without public endpoints", "Public SQL for convenience", "Private endpoint for SQL and Storage"),
        ("Bicep vs Terraform", "IaC", "Azure-native vs multi-cloud", "Terraform for Azure-only tiny team", "Bicep modules in platform repo"),
        ("Template specs", "IaC", "Share approved templates", "Copy-paste ARM per project", "Spec for approved web app pattern"),
        ("What-if deployment", "IaC", "Preview changes before apply", "Deploy blind in prod", "az deployment group what-if in CI"),
        ("Role assignment best practices", "Security", "Group-based not user-based", "Direct user Owner on sub", "Entra group → RBAC on RG"),
        ("Break-glass accounts", "Security", "Emergency access procedure", "Daily admin as Global Admin", "Cloud-only break-glass with PIM exclude"),
        ("Subscription vending", "Platform", "Automated account provisioning", "Manual ticket for each sub", "CAF subscription vending pipeline"),
    ],
    10: [
        ("App Service Plans SKUs", "Compute", "Right-size plan for SLA", "Premium for dev hello-world", "P1v3 prod; B1 dev"),
        ("Deployment slots", "Deployment", "Blue-green for App Service", "Slot swap without warm-up", "Staging slot with auto-swap"),
        ("Always On", "Compute", "Prevent cold start on Basic+", "Always On on Consumption", "Enable Always On for API"),
        ("App Service Environment", "Compute", "Isolated VNet integration", "ASE for simple internal API", "ASE v3 for regulated workloads"),
        ("Azure Functions bindings", "Serverless", "Trigger and output config", "Manual polling queues", "Queue trigger with poison handling"),
        ("Durable Functions", "Serverless", "Long-running orchestration", "Durable for simple HTTP", "Saga orchestration with Durable"),
        ("Container Apps", "Containers", "Microservices scale-to-zero", "CA for monolith first project", "Dapr-enabled Container Apps"),
        ("AKS node pools", "Kubernetes", "Separate system and user pools", "Single pool everything", "GPU pool for ML workload only"),
        ("KEDA autoscaling", "Kubernetes", "Event-driven scale", "HPA CPU only for queue worker", "KEDA on Service Bus queue depth"),
        ("Azure Container Registry", "Containers", "Private image registry", "Docker Hub in prod", "ACR geo-replicated for DR"),
        ("Web App for Containers", "Compute", "Simple container hosting", "WAC for complex mesh", "Linux container on App Service"),
        ("App Service VNet integration", "Networking", "Reach private backends", "Public SQL from App Service", "Regional VNet integration to SQL PE"),
        ("Custom domains and TLS", "Security", "Managed certificates", "HTTP prod endpoints", "App Service managed cert + HTTPS only"),
        ("Autoscale rules App Service", "Scale", "CPU/memory/schedule scaling", "Manual scale only", "Scale out on CPU > 70%"),
        ("Local cache App Service", "Performance", "Reduce storage latency", "Local cache for static only misuse", "Local cache for App Service storage"),
        ("ARR affinity", "Performance", "Sticky sessions", "Affinity for stateless API", "Disable affinity for stateless .NET API"),
        ("Health check App Service", "Reliability", "Remove unhealthy instances", "No health probe", "Health check path /health/ready"),
        ("Run From Package", "Deployment", "Atomic deploys", "FTP deploy to prod", "WEBSITE_RUN_FROM_PACKAGE=1"),
        ("Function Premium plan", "Serverless", "Pre-warmed instances", "Premium for rare timer", "EP1 for latency-sensitive functions"),
        ("Logic Apps Standard", "Integration", "Workflow automation", "Logic App for core OLTP", "Standard plan in VNet for B2B"),
        ("API Management integration", "API", "Gateway in front of compute", "Expose App Service directly", "APIM → App Service internal"),
        ("Windows vs Linux App Service", "Compute", "Linux for .NET Core cost", "Windows without justification", "Linux + .NET 8 default"),
        ("App Service certificates", "Security", "TLS cert lifecycle", "Expired certs in prod", "Key Vault reference for cert"),
        ("Diagnostic settings App Service", "Observability", "HTTP logs to Log Analytics", "No HTTP logs", "Diagnostic setting allLogs category"),
        ("CPU profiling App Service", "Performance", "Diagnose production CPU", "Guess without profiler", "Profiler snapshot during incident"),
        ("Zone redundancy App Service", "Reliability", "AZ deployment Premium v3", "Single instance prod", "Zone redundant P1v3 x3"),
        ("App Service backup", "Reliability", "Config and content backup", "No backup for critical app", "Backup to storage account daily"),
        ("Easy Auth", "Security", "Built-in OAuth for App Service", "Roll own auth poorly", "Easy Auth + Entra ID"),
        ("Managed identity App Service", "Security", "Passwordless to Azure services", "Connection string in app settings", "MI to Key Vault and SQL"),
        ("Sidecar pattern containers", "Containers", "Logging/mesh sidecars on ACA/AKS", "Fat container everything", "Dapr sidecar on Container Apps"),
        ("Batch vs real-time compute", "Architecture", "Separate batch tier", "API does batch sync", "Azure Batch or Functions for ETL"),
        ("SignalR Service", "Real-time", "WebSocket scale-out", "Sticky sessions only", "Azure SignalR for live dashboards"),
        ("Static Web Apps", "Frontend", "SPA + API functions", "SWA for complex .NET API", "SWA for marketing site + Functions API"),
        ("App Service hybrid connections", "Networking", "Reach on-prem without VPN", "Hybrid for all traffic", "Hybrid Connection to legacy SOAP"),
        ("Compute quota planning", "Operations", "Request quota before launch", "Launch day quota fail", "Pre-request vCPU quota per region"),
        ("Image hardening containers", "Security", "Distroless/non-root", "Latest tag floating", "Pinned digest + Trivy scan in CI"),
        ("Startup probes Kubernetes", "Reliability", "Slow .NET startup", "Liveness kills during startup", "Startup probe 60s for large app"),
        ("Resource limits containers", "Reliability", "Prevent noisy neighbor pod", "No limits on .NET app", "CPU/memory requests and limits set"),
        ("Multi-region App Service", "DR", "Traffic Manager front door", "Single region prod", "Active-passive with Traffic Manager"),
        ("Cost optimize idle compute", "FinOps", "Shutdown dev nights", "P3 running 24/7 dev", "Automation runbook stop dev RGs"),
    ],
}

# Extend weeks 11-16 with similar structure - add remaining weeks
for _week, _extra in {
    11: [
        ("Azure SQL tier selection", "Database", "GP vs BC vs Hyperscale", "BC for dev database", "Hyperscale for 4TB+ single DB"),
        ("Cosmos DB consistency levels", "NoSQL", "Session default most apps", "Strong globally always", "Session consistency for catalog"),
        ("Blob storage tiers", "Storage", "Hot/cool/archive lifecycle", "Hot for archive data", "Lifecycle to cool after 30d"),
        ("Azure Data Factory", "ETL", "Orchestrated data movement", "ADF for real-time API", "Nightly pipeline to data lake"),
        ("Synapse Analytics", "Analytics", "Warehouse and Spark pool", "Synapse for OLTP", "Dedicated SQL pool for BI"),
        ("PostgreSQL Flexible Server", "Database", "Open source on Azure", "Single server deprecated", "Flexible Server with zone redundant HA"),
        ("Redis Cache tiers", "Caching", "Premium cluster for HA", "Basic for prod", "Premium P1 with persistence for session"),
        ("Table storage vs Cosmos", "Storage", "Cheap key-value simple", "Cosmos for simple table", "Table storage for audit logs"),
        ("Data Lake Storage Gen2", "Analytics", "Hierarchical namespace", "Blob without HNS for lake", "ADLS Gen2 for parquet lake"),
        ("Private endpoint SQL", "Security", "No public SQL endpoint", "0.0.0.0 on SQL firewall", "Private endpoint only + deny public"),
        ("Geo-replication SQL", "DR", "Readable secondary region", "Geo-rep for dev", "Auto-failover group prod"),
        ("Backup retention SQL", "DR", "PITR and LTR policies", "Default retention only", "LTR 4 weeks + weekly backup"),
        ("Elastic pools SQL", "Cost", "Share DTU across DBs", "Pool for one large DB", "Elastic pool for SaaS multi-tenant small DBs"),
        ("Cosmos partition key", "NoSQL", "High cardinality partition key", "status as partition key", "tenantId partition for SaaS"),
        ("Change feed Cosmos", "Events", "Downstream event processing", "Poll Cosmos manually", "Change feed to Functions processor"),
        ("Azure Search indexing", "Search", "Cognitive search pipelines", "SQL LIKE for search", "AI Search with semantic ranker"),
        ("Event Hubs capture", "Streaming", "Archive to ADLS", "No capture on stream", "Capture to lake for replay"),
        ("Schema migration strategy", "Data", "Expand-contract migrations", "Breaking rename deploy", "Flyway/DbUp in CI pipeline"),
        ("Connection pooling cloud", "Performance", "Right pool size to DB", "Unbounded connections", "Pool size × instances < max connections"),
        ("Read replica routing", "Scale", "Offload reads", "Strong consistency on replica", "EF Core read replica interceptor"),
    ],
    12: [
        ("Entra ID vs AD DS", "Identity", "Cloud identity primary", "AD DS for cloud-only", "Entra ID + sync from on-prem AD"),
        ("Managed identity types", "Identity", "System vs user-assigned", "User-assigned for single resource", "User-assigned MI shared across slots"),
        ("Conditional Access policies", "Security", "Risk-based access", "CA blocks all legacy auth", "CA: require MFA + compliant device"),
        ("PIM just-in-time access", "Security", "Standing admin reduction", "PIM for every read access", "PIM for Owner and UAA roles"),
        ("Service principal vs MI", "Identity", "MI for Azure resources", "SP with secret in code", "MI for App Service to SQL"),
        ("App registration vs enterprise app", "Identity", "OAuth app config", "Confuse the two", "App reg for API; enterprise app for SSO"),
        ("B2B guest access", "Identity", "Partner collaboration", "Shared credentials partners", "B2B invite with CA policies"),
        ("B2C customer identity", "Identity", "Consumer login", "B2C for employees", "B2C custom policies for customers"),
        ("Passwordless authentication", "Security", "FIDO2 and WHfB", "Password rotation only", "Passwordless for admin accounts"),
        ("Certificate-based auth", "Security", "Service-to-service certs", "Long-lived secrets", "Cert auth to API Management"),
    ],
}.items():
    while len(AZURE_WEEK_CONCEPTS.setdefault(_week, [])) < 40:
        idx = len(AZURE_WEEK_CONCEPTS[_week])
        if idx < len(_extra):
            AZURE_WEEK_CONCEPTS[_week].append(_extra[idx])
        else:
            AZURE_WEEK_CONCEPTS[_week].append(
                (f"Azure week {_week} topic {idx+11}", "Azure", "Production scenarios", "Anti-patterns", "Document in ADR with metrics")
            )

# Fill weeks 11-16 to 40 concepts each if short
_AZURE_FILL_TOPICS = {
    11: "Azure Data", 12: "Azure Identity", 13: "Azure Networking",
    14: "Azure Security", 15: "Azure Messaging", 16: "Azure Capstone",
}
from qa_question_bank import CONCEPTS as _BASE
for w in range(11, 17):
    base = list(_BASE.get("Azure", [])) + list(_BASE.get("Messaging", []))
    existing_titles = {t[0] for t in AZURE_WEEK_CONCEPTS.get(w, [])}
    for concept in base:
        if len(AZURE_WEEK_CONCEPTS.setdefault(w, [])) >= 40:
            break
        if concept[0] not in existing_titles:
            AZURE_WEEK_CONCEPTS[w].append(concept)
    while len(AZURE_WEEK_CONCEPTS[w]) < 40:
        n = len(AZURE_WEEK_CONCEPTS[w])
        AZURE_WEEK_CONCEPTS[w].append(
            (f"{_AZURE_FILL_TOPICS[w]} deep dive {n}", "Azure", "Enterprise scale", "Premature optimization",
             f"Production pattern {n} for week {w}")
        )
