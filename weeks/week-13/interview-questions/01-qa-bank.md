# Week 13 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Networking | **Count:** 50

---


## Q001: Hub-Spoke Network Topology

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Design hub-spoke for 3 application teams on Azure.

### Short Answer (30 seconds)

Hub: firewall, VPN/ExpressRoute gateway, DNS, optional Bastion. Spokes: team VNets peered to hub — no spoke-to-spoke without hub.

### Detailed Answer (3–5 minutes)

**Traffic:** spoke → hub firewall → internet or on-prem. **UDR:** default route 0.0.0.0/0 to firewall private IP.

**Architect:** Azure Firewall or NVA in hub — centralized egress control and logging.

### Architecture Perspective

Hub-spoke is enterprise Azure networking default.

### Follow-up Questions

1. **VWAN vs manual hub? — Virtual WAN simplifies many spokes at scale.**
2. **Peering transitive? — Non-transitive — spoke cannot reach spoke direct.**

### Common Mistakes in Interviews

- Full mesh spoke peering chaos
- No centralized egress filtering
- Overlapping IP address spaces

---

## Q002: Private Link vs Service Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Private Endpoint vs Service Endpoint for Azure SQL?

### Short Answer (30 seconds)

Private Endpoint: SQL gets private IP in your VNet, traffic stays private, strongest isolation. Service Endpoint: route to Azure backbone, simpler, less isolation.

### Detailed Answer (3–5 minutes)

**Architect prod default:** Private Link for SQL, Storage, Key Vault.

**DNS:** private DNS zone `privatelink.database.windows.net` linked to VNet.

### Architecture Perspective

Private Link is interview answer for secure PaaS access.

### Follow-up Questions

1. **DNS private resolver? — Hybrid DNS resolution for on-prem.**
2. **Dual-stack? — Private endpoint for inbound, service endpoint legacy — prefer PE.**

### Common Mistakes in Interviews

- Public SQL endpoint prod
- Private endpoint without DNS zone
- Assume service endpoint stops all exfiltration

---

## Q003: Application Gateway vs Azure Front Door

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Regional App Gateway vs global Front Door?

### Short Answer (30 seconds)

App Gateway: regional L7 load balancer + WAF, VMs/internal apps in one region. Front Door: global anycast, multi-region, CDN-like edge, global WAF.

### Detailed Answer (3–5 minutes)

**Pattern:** Front Door → regional App Gateway/App Service for global users + regional origin.

**Architect:** Front Door for internet-facing multi-region; App Gateway for hub VNet internal apps.

### Architecture Perspective

L7 product selection maps to user geography.

### Follow-up Questions

1. **WAF mode? — Detection then prevention after tuning false positives.**
2. **SSL termination? — At edge — certificate management at Front Door.**

### Common Mistakes in Interviews

- App Gateway for global users single region
- No WAF on public endpoints
- Wrong tier WAF (regional vs global)

---

## Q004: Network Security Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

NSG design for 3-tier app (web, app, data)?

### Short Answer (30 seconds)

Web subnet: allow 443 inbound from App Gateway/Front Door. App subnet: allow from web only. Data subnet: allow SQL port from app only. Deny all else implicit.

### Detailed Answer (3–5 minutes)

**Micro-segmentation:** NSG + ASG (application security groups) for cleaner rules — `WebServers` ASG to `AppServers` ASG port 443.

**Architect:** Default deny mindset — explicit allow rules only.

### Architecture Perspective

NSG rules are defense in depth.

### Follow-up Questions

1. **NSG flow logs? — Send to Log Analytics — traffic analysis.**
2. **Service tags? — `Sql`, `Storage` — simplify PaaS rules.**

### Common Mistakes in Interviews

- Allow all internal VNet inbound
- NSG on subnet and NIC conflicting
- No logging on deny rules

---

## Q005: ExpressRoute vs VPN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Connect on-prem datacenter to Azure — VPN or ExpressRoute?

### Short Answer (30 seconds)

VPN: quick, lower cost, internet/IPsec — moderate bandwidth. ExpressRoute: dedicated private connection, predictable latency, higher bandwidth, compliance.

### Detailed Answer (3–5 minutes)

**Architect:** VPN for pilot/dev hybrid. ExpressRoute production with redundant circuits (provider diversity).

**ExpressRoute Gateway:** required in hub VNet.

### Architecture Perspective

Hybrid connectivity is common enterprise requirement.

### Follow-up Questions

1. **ExpressRoute FastPath? — Data plane bypass gateway for performance.**
2. **Dual VPN active-active? — Possible for resilience — lower than ER.**

### Common Mistakes in Interviews

- Single VPN circuit production no backup
- No bandwidth planning
- Assume ExpressRoute immune to outages

---

## Q006: Azure DNS Private Zones

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Common |

### Question

Why private DNS zone for private endpoints?

### Short Answer (30 seconds)

Public DNS resolves SQL to public IP. Private zone linked to VNet resolves `sqlserver.database.windows.net` to private IP — apps use same connection string name.

### Detailed Answer (3–5 minutes)

**Split-horizon:** different resolution internal vs external.

**Architect:** Central DNS zone in hub, linked to all spokes.

### Architecture Perspective

DNS is overlooked until private link breaks apps.

### Follow-up Questions

1. **Auto-registration? — VM DNS in Azure — private zones manual A records or auto.**
2. **Conditional forwarding? — On-prem DNS forward Azure private zones.**

### Common Mistakes in Interviews

- Private endpoint without DNS config
- Hardcode private IPs in connection strings
- Forget hub-spoke DNS linking

---

## Q007: User-Defined Routes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Routing |
| **Frequency** | Common |

### Question

Force all spoke internet egress through hub firewall?

### Short Answer (30 seconds)

UDR on spoke subnet: `0.0.0.0/0` → Virtual Appliance (firewall private IP). Disable BGP route override if needed.

### Detailed Answer (3–5 minutes)

**Asymmetric routing:** ensure return path through firewall — SNAT on firewall.

**Architect:** Test with Network Watcher — verify effective routes on VM.

### Architecture Perspective

UDR mistakes cause subtle connectivity failures.

### Follow-up Questions

1. **Service endpoints and UDR? — May need specific routes — test PaaS connectivity.**
2. **Route Server? — BGP between firewall and VNet — advanced hub.**

### Common Mistakes in Interviews

- Spoke direct internet bypass firewall
- UDR without effective route validation
- Blackhole routing misconfiguration

---

## Q008: Bastion and Jump Hosts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Secure admin access to VMs without public RDP?

### Short Answer (30 seconds)

Azure Bastion in hub — RDP/SSH over HTTPS through portal, no public VM IP. Or private jump box with JIT access.

### Detailed Answer (3–5 minutes)

**Architect:** No public IPs on servers. PIM + Bastion + logging.

**Just-in-time:** Defender opens port temporarily for approved admin.

### Architecture Perspective

Admin access architecture is security review item.

### Follow-up Questions

1. **Bastion SKU? — Basic vs Standard — session recording Standard.**
2. **Session recording compliance? — Store logs for audit.**

### Common Mistakes in Interviews

- Public RDP for convenience
- Shared admin password
- Jump box without MFA

---

## Q009: DDoS Protection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

When enable Azure DDoS Network Protection?

### Short Answer (30 seconds)

Public-facing endpoints with revenue impact — Front Door origin, public IPs. DDoS IP Protection per protected resource or Network Protection per VNet.

### Detailed Answer (3–5 minutes)

**Architect:** Pair with WAF at edge. DDoS alerts to SOC.

**Cost:** Network Protection fixed monthly — justify for critical internet properties.

### Architecture Perspective

DDoS is availability architecture.

### Follow-up Questions

1. **DDoS vs WAF? — DDoS volume attacks; WAF application layer.**
2. **Telemetry? — DDoS diagnostic logs during attack.**

### Common Mistakes in Interviews

- No DDoS on public ecommerce
- Assume Front Door alone stops all attacks
- No runbook for DDoS event

---

## Q010: VNet Peering Data Transfer Cost

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Hub-spoke peering cost consideration?

### Short Answer (30 seconds)

Peering ingress/egress charged within same region (minimal) — cross-region peering costs more. Egress to internet expensive — centralize through firewall with monitoring.

### Detailed Answer (3–5 minutes)

**Architect:** Model data flow — heavy spoke-to-spoke via hub doubles hub traffic.

**Optimize:** private endpoints reduce internet egress for Azure PaaS.

### Architecture Perspective

Network architecture affects monthly bill.

### Follow-up Questions

1. **VWAN hub routing? — May simplify billing complexity at scale.**
2. **Same region deployment? — Keep peering same region when possible.**

### Common Mistakes in Interviews

- Unnecessary cross-region peering
- Ignore egress in architecture review
- Chatty microservices across regions

---

## Q011: VNet Peering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Design VNet peering for two workloads in the same region — what must you validate before peering?

### Short Answer (30 seconds)

Non-overlapping address spaces, no transitive routing, peering is not gateway transit by default. Validate DNS resolution and effective routes after peering.

### Detailed Answer (3–5 minutes)

**Pre-peering checklist:**
- CIDR ranges must not overlap (10.0.0.0/16 vs 10.0.1.0/24 fails)
- Decide `allowForwardedTraffic` and `allowGatewayTransit` / `useRemoteGateways`
- Plan DNS — linked private zones or custom DNS forwarders

**Architect:** Peering is non-transitive — if VNet A peers to Hub and Hub to VNet B, A cannot reach B without UDR or hub routing.

**Cost:** Same-region peering data transfer is low cost but not free at scale — model chatty cross-VNet traffic.

### Architecture Perspective

Peering mistakes cause day-one connectivity failures in landing zones.

### Follow-up Questions

1. **Can you peer overlapping VNets? — No — must redesign IP plan or use NAT/proxy.**
2. **Global VNet peering? — Cross-region peering with higher latency and transfer cost.**

### Common Mistakes in Interviews

- Assuming peering enables transitive routing
- Overlapping IP ranges discovered after deploy
- No post-peering effective route validation

---

## Q012: Hub-Spoke Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Compare hub-spoke vs mesh for 15 application teams on Azure.

### Short Answer (30 seconds)

Hub-spoke: centralized firewall, VPN/ER gateway, DNS, Bastion in hub; spokes peer to hub only. Mesh does not scale — 15 teams = 105 peering pairs and no central egress control.

### Detailed Answer (3–5 minutes)

**Hub contains:** Azure Firewall or NVA, ExpressRoute/VPN gateway, Private DNS resolver, optional DDoS-protected public IPs.

**Spoke rules:** Default route 0.0.0.0/0 → firewall private IP via UDR. No direct spoke-to-spoke peering.

**Architect:** Hub-spoke is the enterprise default for policy enforcement, logging, and hybrid connectivity. Virtual WAN is the managed evolution at 50+ sites.

### Architecture Perspective

Hub-spoke demonstrates centralized governance thinking.

### Follow-up Questions

1. **When mesh is acceptable? — Small estates (<5 VNets) with low security requirements.**
2. **Shared hub across subscriptions? — Yes — peering and RBAC at subscription scope.**

### Common Mistakes in Interviews

- Full mesh peering between all team VNets
- Spoke internet egress bypassing hub firewall
- Hub without redundant gateway for production hybrid

---

## Q013: Azure Firewall

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

When choose Azure Firewall vs NSG for egress control?

### Short Answer (30 seconds)

Azure Firewall: centralized FQDN filtering, threat intel, TLS inspection (Premium), DNAT, forced tunneling — hub appliance. NSG: subnet/NIC stateful L3-L4 rules — micro-segmentation.

### Detailed Answer (3–5 minutes)

**Azure Firewall use cases:**
- Central egress allow-list by FQDN (`*.microsoft.com`)
- SNAT for spoke outbound with logging to Log Analytics
- Application rules for HTTP/HTTPS without opening all ports

**Architect:** Firewall Policy (hierarchical) for enterprise — parent policy in platform team, child policies per environment. Premium SKU for IDPS and TLS inspection when compliance requires.

### Architecture Perspective

Firewall vs NSG is a classic Azure architect layering question.

### Follow-up Questions

1. **Firewall vs third-party NVA? — Azure Firewall is fully managed; NVA when deep packet inspection vendor required.**
2. **Firewall in forced tunneling mode? — All internet via on-prem — UDR + BGP configuration.**

### Common Mistakes in Interviews

- Replacing NSG entirely with firewall only
- Basic SKU when FQDN filtering required
- No diagnostic logs to Log Analytics

---

## Q014: NSG vs ASG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Explain NSG vs Application Security Group — how combine for 3-tier app?

### Short Answer (30 seconds)

NSG: L3-L4 rules on subnet or NIC. ASG: logical grouping of NICs — rules reference ASG not IP. Combine: `WebServers` ASG → `AppServers` ASG port 443.

### Detailed Answer (3–5 minutes)

**Example rules:**
- Inbound 443 to `WebServers` ASG from App Gateway subnet
- Inbound 443 to `AppServers` ASG from `WebServers` ASG
- Inbound 1433 to `SqlServers` ASG from `AppServers` ASG only

**Architect:** ASG rules survive VM reprovisioning — no IP churn in rule sets. Implicit deny remains — last rule is not explicit allow-all.

### Architecture Perspective

ASG shows micro-segmentation maturity beyond IP-based NSG.

### Follow-up Questions

1. **NSG on subnet vs NIC? — Both possible — avoid conflicting rules; prefer subnet for consistency.**
2. **ASG across VNets? — ASG is VNet-scoped only.**

### Common Mistakes in Interviews

- Hardcoded VM IPs in NSG rules
- Allow all VNet inbound for convenience
- NSG on subnet and NIC with contradictory rules

---

## Q015: Route Tables UDR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Spoke VMs reach internet without going through hub firewall — diagnose with UDR.

### Short Answer (30 seconds)

Check effective routes on NIC: `0.0.0.0/0` may point to Internet via system route overriding intent. Associate UDR on subnet, disable BGP route propagation if needed, verify firewall as next hop.

### Detailed Answer (3–5 minutes)

**Common causes:**
- UDR not associated to subnet
- System route preferred over custom (wrong next hop type)
- `0.0.0.0/0` on firewall but asymmetric return path

**Architect:** Use Network Watcher 'Effective routes' before and after UDR changes. Document route table per spoke tier (web, app, data).

### Architecture Perspective

UDR debugging separates senior network architects from beginners.

### Follow-up Questions

1. **Service endpoint routes and UDR? — May need `Microsoft.Storage` routes — test PaaS after UDR.**
2. **Route Server for BGP? — Hub firewall advertises routes via BGP to spokes.**

### Common Mistakes in Interviews

- UDR on wrong subnet (app tier not web tier)
- Forgot to disable BGP propagation when required
- Asymmetric routing without firewall SNAT

---

## Q016: VPN Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

Design site-to-site VPN for hybrid Azure — SKU and redundancy?

### Short Answer (30 seconds)

VpnGw2+ for production throughput. Active-active dual tunnels from on-prem to Azure VPN gateway in hub VNet. Use route-based (BGP optional) VPN.

### Detailed Answer (3–5 minutes)

**Design:**
- Gateway subnet `/27` minimum in hub VNet
- Local network gateway represents on-prem CIDR
- Connection with shared key or IKEv2

**Architect:** VPN for dev/pilot or backup to ExpressRoute. Plan bandwidth — VpnGw3 ~1.25 Gbps aggregate. Always second tunnel or second on-prem device for HA.

### Architecture Perspective

VPN is the fast path to hybrid — architects know limits.

### Follow-up Questions

1. **Policy-based vs route-based VPN? — Route-based only for most Azure scenarios.**
2. **Point-to-site VPN? — Developer remote access — separate from site-to-site.**

### Common Mistakes in Interviews

- Gateway subnet too small (/28)
- Single tunnel production with no failover
- VPN as primary without bandwidth planning

---

## Q017: ExpressRoute

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

ExpressRoute architecture for production hybrid — what components required?

### Short Answer (30 seconds)

ExpressRoute circuit (provider), ExpressRoute gateway in hub VNet, routing via BGP, optional ExpressRoute FastPath for data plane performance.

### Detailed Answer (3–5 minutes)

**Redundancy:** Dual circuits from diverse peering locations or providers — Microsoft requires diverse for SLA.

**Architect:** ExpressRoute for predictable latency, high bandwidth, and private connectivity (not over public internet). Pair with VPN as Microsoft → 'ExpressRoute with VPN failover' pattern.

**Peering types:** Private (to VNet), Microsoft (to M365/Azure PaaS public endpoints), Public (legacy).

### Architecture Perspective

ExpressRoute is enterprise hybrid default for critical workloads.

### Follow-up Questions

1. **ExpressRoute Direct? — 100 Gbps dedicated port at peering location.**
2. **Circuit provider vs Microsoft peering? — You buy circuit from Equinix/AT&T etc.; Microsoft provides ER gateway.**

### Common Mistakes in Interviews

- Single circuit production
- Wrong peering type for workload (Public vs Private)
- No VPN backup for circuit maintenance window

---

## Q018: ExpressRoute Global Reach

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

When use ExpressRoute Global Reach?

### Short Answer (30 seconds)

Connect two on-prem datacenters via Azure backbone using ExpressRoute circuits — traffic hairpins through Microsoft global network without traversing corporate WAN.

### Detailed Answer (3–5 minutes)

**Use case:** Merger integration — Datacenter A and B each have ER to Azure; Global Reach links them via Azure.

**Architect:** Requires premium circuit SKUs at both ends. Alternative: VPN between on-prem sites + Azure as hub.

**Not for:** General Azure VNet-to-VNet — use peering or Virtual WAN.

### Architecture Perspective

Global Reach shows advanced hybrid routing knowledge.

### Follow-up Questions

1. **Global Reach vs VNet peering? — Global Reach is on-prem to on-prem via Azure ER; peering is Azure VNet to VNet.**
2. **Bandwidth limits? — Depends on circuit SKU — validate with provider.**

### Common Mistakes in Interviews

- Using Global Reach for Azure VNet connectivity
- Single region ER without Global Reach planning
- No route filtering between on-prem sites

---

## Q019: Virtual WAN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Virtual WAN vs manual hub-spoke — when migrate to vWAN?

### Short Answer (30 seconds)

vWAN when 20+ branch sites, SD-WAN integration, automated spoke onboarding, or global transit hub needed. Manual hub-spoke fine for centralized Azure-only estate.

### Detailed Answer (3–5 minutes)

**vWAN components:** Virtual hub (managed), VPN/ExpressRoute gateways, Azure Firewall in hub, branch connections.

**Architect:** vWAN reduces operational toil — spokes connect via `Virtual network connection` not manual peering matrix. Hub routing intent policies control inter-spoke traffic.

**Trade-off:** Less granular control than DIY NVA; cost model differs from manual hub.

### Architecture Perspective

vWAN is the scale answer for multi-site Azure networking.

### Follow-up Questions

1. **vWAN secure hub? — Built-in Azure Firewall deployment in vWAN hub.**
2. **SD-WAN CPE integration? — Partner devices connect as branch to vWAN.**

### Common Mistakes in Interviews

- vWAN for 3 VNets only — over-engineering
- Manual peering alongside vWAN without plan
- Ignoring vWAN routing policy for spoke isolation

---

## Q020: Azure DNS Private Zones

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Very Common |

### Question

Design private DNS zones for private endpoints across hub-spoke.

### Short Answer (30 seconds)

Central private DNS zones in hub (`privatelink.database.windows.net`, `privatelink.blob.core.windows.net`). Link zones to all spoke VNets or use Private DNS Resolver.

### Detailed Answer (3–5 minutes)

**Split-horizon:** Same FQDN resolves to private IP inside VNet, public IP outside.

**Architect:** Auto-registration optional for VMs; private endpoints require A record (manual or via Terraform/Bicep). Document zone ownership — platform team manages all privatelink zones.

### Architecture Perspective

Private DNS is mandatory for private endpoint success.

### Follow-up Questions

1. **Multiple zones same name linked to VNets? — One zone linked to many VNets — central model.**
2. **Fallback to public DNS? — Conditional forwarder from on-prem for hybrid resolution.**

### Common Mistakes in Interviews

- Private endpoint without DNS zone link
- Per-team duplicate private zones
- Hardcoding private IPs in connection strings

---

## Q021: DNS Forwarding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Common |

### Question

Hybrid DNS — on-prem resolves Azure private endpoints. Architecture?

### Short Answer (30 seconds)

Azure Private DNS Resolver inbound endpoint in hub; on-prem DNS conditional forwarders send `database.windows.net` to resolver IP. Outbound endpoint forwards to on-prem for internal names.

### Detailed Answer (3–5 minutes)

**Flow:** VM in Azure → Azure DNS → private zone. On-prem client → forward to Resolver inbound → Azure private zone.

**Architect:** Avoid split-brain — document which zones live where. Test resolution from both sides before cutover.

### Architecture Perspective

Hybrid DNS breaks more migrations than compute.

### Follow-up Questions

1. **Resolver vs custom DNS VM? — Managed Resolver preferred over IaaS DNS servers.**
2. **DNS private resolver rulesets? — Forward specific domains to on-prem or internet.**

### Common Mistakes in Interviews

- No conditional forwarding from on-prem
- Public DNS cache serving stale records after private link
- Single DNS server with no redundancy

---

## Q022: Traffic Manager

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Traffic Manager vs Front Door for global routing?

### Short Answer (30 seconds)

Traffic Manager: DNS-based load balancing, any endpoint (on-prem, Azure, external). Front Door: HTTP(S) reverse proxy at edge with WAF, caching, TLS.

### Detailed Answer (3–5 minutes)

**Traffic Manager profiles:** Priority (active-passive DR), Weighted (canary), Performance (lowest latency), Geographic (compliance routing).

**Architect:** Traffic Manager for non-HTTP (custom ports, legacy) or multi-cloud endpoints. Front Door for modern web APIs with WAF requirement.

### Architecture Perspective

DNS vs anycast routing — know when each applies.

### Follow-up Questions

1. **Traffic Manager health probes? — HTTP/TCP probes remove unhealthy endpoints from DNS.**
2. **Nested profiles? — Combine geographic + priority for complex DR.**

### Common Mistakes in Interviews

- Traffic Manager for single-region app only
- TTL too high during failover (600s+)
- No health probe — stale DNS to dead endpoint

---

## Q023: Front Door vs CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Azure Front Door vs Azure CDN — when use each?

### Short Answer (30 seconds)

Front Door: global L7 load balancer + WAF + routing to origins (App Service, AKS, on-prem). CDN (Standard/Premium): cache static assets at edge — often behind Front Door.

### Detailed Answer (3–5 minutes)

**Pattern:** Front Door → CDN endpoint for static (`/assets/*`) → App Service for dynamic API.

**Architect:** Front Door Premium for Private Link origins, advanced WAF, bot protection. CDN alone when only static content acceleration needed without origin load balancing.

### Architecture Perspective

Edge architecture layers CDN caching on Front Door routing.

### Follow-up Questions

1. **Front Door vs App Gateway? — Front Door global; App Gateway regional — often combined.**
2. **Caching rules? — CDN cache TTL vs dynamic API no-cache.**

### Common Mistakes in Interviews

- CDN for dynamic API responses incorrectly cached
- Front Door without WAF on public endpoints
- Origin exposed publicly when Private Link available

---

## Q024: Private Link Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Expose internal PaaS or IaaS service to consumers via Private Link Service?

### Short Answer (30 seconds)

Provider creates Private Link Service on Standard ILB fronting your service; consumers create private endpoints in their VNets. Cross-tenant and cross-subscription supported.

### Detailed Answer (3–5 minutes)

**Use case:** SaaS platform on Azure offering private connectivity to enterprise customers without public IPs.

**Architect:** Approve connection requests manually or via automation. NAT IP mapping for SNAT. Document DNS — consumers need private DNS for your service FQDN.

### Architecture Perspective

Private Link Service is the B2B private connectivity pattern.

### Follow-up Questions

1. **Private Link Service vs Private Endpoint? — Service is provider side; endpoint is consumer side.**
2. **On-premises access? — ExpressRoute/VPN + private endpoint in connected VNet.**

### Common Mistakes in Interviews

- Auto-approve all connection requests
- No ILB health probes on backend pool
- Consumer DNS not documented

---

## Q025: Private Endpoint DNS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Very Common |

### Question

Private endpoint created but app still connects to public SQL IP — fix?

### Short Answer (30 seconds)

Create A record in `privatelink.database.windows.net` zone linked to VNet, or use `zoneGroup` on private endpoint for auto DNS. Verify `nslookup` from VM returns 10.x private IP.

### Detailed Answer (3–5 minutes)

**Common gaps:**
- Zone exists but not linked to VM's VNet
- `hostNameInCertificate` mismatch when using custom DNS
- App caches connection string resolved at startup

**Architect:** Integrate private endpoint + private DNS in IaC template — never manual post-deploy.

### Architecture Perspective

DNS is the #1 private endpoint failure mode.

### Follow-up Questions

1. **Integrate with on-prem DNS? — Conditional forward via Private DNS Resolver.**
2. **Multiple endpoints same service? — Separate A records or CNAME chain.**

### Common Mistakes in Interviews

- Private endpoint without private DNS zone
- Testing DNS from laptop not from VNet VM
- Disabling public endpoint while DNS still public

---

## Q026: NAT Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

When NAT Gateway vs Azure Firewall SNAT for outbound internet?

### Short Answer (30 seconds)

NAT Gateway: scalable outbound SNAT for subnet — no FQDN filtering, simple, high SNAT ports. Firewall: filtered egress with logging and threat intel.

### Detailed Answer (3–5 minutes)

**Architect:** NAT Gateway on spoke subnet when outbound-only internet needed (Windows updates, package repos) and hub firewall handles filtered traffic separately. Avoid mixing default routes — one SNAT path per subnet.

**SNAT exhaustion:** NAT Gateway scales ports automatically; LB SNAT limited to 1024 ports per IP.

### Architecture Perspective

SNAT architecture prevents mysterious outbound failures.

### Follow-up Questions

1. **NAT Gateway vs LB outbound rule? — NAT Gateway preferred for subnet-level outbound; LB SNAT for load-balanced VMs.**
2. **IPv4 only? — NAT Gateway is IPv4 outbound.**

### Common Mistakes in Interviews

- LB SNAT exhaustion at scale
- NAT Gateway and firewall both as 0.0.0.0/0 next hop
- No monitoring of SNAT failed connections

---

## Q027: Bastion Host

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Secure VM admin access without public RDP/SSH?

### Short Answer (30 seconds)

Deploy Azure Bastion in hub VNet — admin connects via portal/CLI over HTTPS. VMs have no public IPs. Standard SKU for session recording.

### Detailed Answer (3–5 minutes)

**Alternatives:** JIT access via Defender for Cloud, private jump box with PIM.

**Architect:** Bastion subnet `AzureBastionSubnet` /26 minimum. NSG rules per Microsoft requirements. Integrate with Entra ID for conditional access on portal access.

### Architecture Perspective

Bastion eliminates public management plane exposure.

### Follow-up Questions

1. **Bastion vs VPN jump box? — Bastion zero inbound ports; jump box needs VNet connectivity design.**
2. **Native client support? — Bastion Standard supports native RDP/SSH clients.**

### Common Mistakes in Interviews

- Public RDP 'temporarily' for troubleshooting
- Bastion in spoke without hub connectivity to VMs
- Shared local admin credentials

---

## Q028: DDoS Protection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

DDoS Network Protection vs IP Protection — when enable?

### Short Answer (30 seconds)

Network Protection: protects all public IPs in VNet. IP Protection: per protected IP. Enable for revenue-critical public endpoints with DDoS telemetry to SOC.

### Detailed Answer (3–5 minutes)

**Layers:** DDoS (volumetric L3-L4) + WAF (L7) + rate limiting at APIM.

**Architect:** DDoS Protection Plan associated to VNet. Alert thresholds in Monitor. Runbook for attack — Microsoft scrubs traffic automatically on protected resources.

### Architecture Perspective

DDoS is availability architecture not optional for public commerce.

### Follow-up Questions

1. **DDoS vs WAF overlap? — Complementary — volumetric vs application attacks.**
2. **Simulation testing? — Contact Microsoft for DDoS simulation prior to go-live.**

### Common Mistakes in Interviews

- Public ecommerce without DDoS plan
- Assume Front Door alone stops all attacks
- No runbook for DDoS alert escalation

---

## Q029: Network Watcher

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Key Network Watcher capabilities for architects?

### Short Answer (30 seconds)

Topology view, NSG flow logs, connection monitor, packet capture, VPN troubleshoot, next hop analysis, IP flow verify.

### Detailed Answer (3–5 minutes)

**Architect workflow:**
1. IP flow verify — is traffic allowed?
2. Next hop — where does packet route?
3. Connection troubleshoot — end-to-end latency and path

Enable flow logs to Storage or Log Analytics for traffic analytics and anomaly detection.

### Architecture Perspective

Network Watcher is first-line hybrid connectivity debug tool.

### Follow-up Questions

1. **Flow logs vs NSG diagnostics? — Flow logs are long-term traffic records; diagnostic settings for audit.**
2. **Traffic analytics? — Log Analytics solution on flow logs.**

### Common Mistakes in Interviews

- Debugging routing without effective routes check
- Flow logs disabled to save cost on prod
- Packet capture left running indefinitely

---

## Q030: Packet Capture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Occasional |

### Question

When use Network Watcher packet capture vs NSG flow logs?

### Short Answer (30 seconds)

Packet capture: deep debug specific VM NIC — short duration, high detail. Flow logs: continuous metadata (5-tuple, allow/deny) for all NSG-associated traffic.

### Detailed Answer (3–5 minutes)

**Capture limits:** Storage account for `.cap` files — analyze in Wireshark. Stop capture after issue reproduced — storage and performance impact.

**Architect:** Packet capture for 'connection reset' mysteries; flow logs for baseline and compliance. Require change ticket for production capture.

### Architecture Perspective

Right diagnostic tool for network triage.

### Follow-up Questions

1. **Filters on packet capture? — Filter by IP/port to reduce capture size.**
2. **Mirror vs capture? — Azure does local NIC capture not SPAN port.**

### Common Mistakes in Interviews

- Permanent packet capture on production NIC
- Capture without storage account lifecycle policy
- Confusing flow logs with full packet capture

---

## Q031: Connection Troubleshoot

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Connection troubleshoot reports 'Unreachable' between VM and SQL private endpoint — steps?

### Short Answer (30 seconds)

Verify NSG/ASG allow path, UDR next hop, private DNS resolution to 10.x, private endpoint NIC in correct subnet, SQL firewall disabled (private link only).

### Detailed Answer (3–5 minutes)

**Network Watcher connection troubleshoot** tests TCP from VM to destination — reports hop failures.

**Architect:** Document connectivity matrix (source subnet → destination → port → rule). Automate validation in deployment pipeline with test VM.

### Architecture Perspective

Systematic connectivity debug impresses in incident scenarios.

### Follow-up Questions

1. **User-defined route blocking? — Effective routes show blackhole.**
2. **Private endpoint in wrong subnet? — Must be dedicated subnet recommended.**

### Common Mistakes in Interviews

- Testing from developer laptop not VNet
- Public SQL firewall rule left enabled masking DNS issue
- Skip DNS verification step

---

## Q032: IP Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Azure Firewall IP Groups — use case?

### Short Answer (30 seconds)

Named collections of IP ranges/CIDRs referenced in firewall rules — simplify management of on-prem datacenter ranges, partner networks, banned IPs.

### Detailed Answer (3–5 minutes)

**Example:** `OnPrem-Datacenters` IP Group in allow rules instead of 20 individual CIDR entries.

**Architect:** Central platform team maintains IP Groups; application teams reference in child Firewall Policies. Update group once — all rules inherit.

### Architecture Perspective

IP Groups reduce firewall rule sprawl.

### Follow-up Questions

1. **IP Groups vs ASG? — IP Groups for firewall/NVA external CIDRs; ASG for Azure NIC grouping.**
2. **Cross-policy reference? — IP Groups are regional resource referenced by policies.**

### Common Mistakes in Interviews

- Hardcoded CIDRs in every firewall rule
- Stale IP Group after datacenter migration
- No ownership for IP Group updates

---

## Q033: Service Tags

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Use service tags in NSG and Firewall rules — example?

### Short Answer (30 seconds)

Service tags represent Azure service IP prefixes — `Sql`, `Storage`, `AzureKeyVault`, `AzureActiveDirectory`. Rule: allow outbound to `Sql` from app subnet without maintaining Microsoft IP list.

### Detailed Answer (3–5 minutes)

**Architect:** Prefer service tags over `0.0.0.0/0` for PaaS access. Combine with Private Link — service tag rules become fallback or unnecessary when all traffic is private.

**Regional tags:** `Sql.WestEurope` when scoping to region.

### Architecture Perspective

Service tags show Azure-native rule authoring.

### Follow-up Questions

1. **Service tag updates? — Microsoft maintains — rules auto-update unlike manual IP lists.**
2. **Service tags on-prem? — Available for hybrid allow rules to Azure services.**

### Common Mistakes in Interviews

- Allow all internet because PaaS IPs change
- Service tag when Private Link should be used
- Wrong regional service tag scope

---

## Q034: Forced Tunneling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Force all Azure internet egress through on-prem firewall — design?

### Short Answer (30 seconds)

UDR default route to NVA/firewall OR ExpressRoute with forced tunneling — internet breakout via on-prem inspection before exiting.

### Detailed Answer (3–5 minutes)

**Azure Firewall forced tunneling:** Firewall learns default route via BGP from on-prem; SNAT on-prem or on firewall per design.

**Architect:** Watch asymmetric routing and hairpin latency. Document exception paths for Azure PaaS service tags that must not tunnel.

### Architecture Perspective

Forced tunneling satisfies 'all egress inspected' compliance.

### Follow-up Questions

1. **Split tunnel exceptions? — Route Azure service tag prefixes direct to Azure backbone.**
2. **Performance impact? — All internet RTT adds on-prem hop — model latency.**

### Common Mistakes in Interviews

- Forced tunnel without bandwidth sizing
- Asymmetric routing breaking TCP sessions
- No break-glass direct egress path

---

## Q035: Active-Active VPN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Active-active VPN gateway configuration benefits?

### Short Answer (30 seconds)

Two public IPs on Azure VPN gateway, two tunnels from on-prem — aggregate throughput and redundancy. On-prem requires dual VPN devices or dual tunnels.

### Detailed Answer (3–5 minutes)

**Architect:** Active-active for production hybrid backup to ExpressRoute or primary VPN at scale. BGP over VPN for dynamic route exchange.

**Failover:** One tunnel down — traffic flows remaining tunnel; monitor both.

### Architecture Perspective

Active-active shows HA hybrid design.

### Follow-up Questions

1. **Active-active vs active-passive? — Active-active uses both paths simultaneously.**
2. **Policy-based with active-active? — Route-based required.**

### Common Mistakes in Interviews

- Single tunnel labeled 'active-active'
- No monitoring per tunnel status
- Asymmetric routing with dual paths unplanned

---

## Q036: BGP with ExpressRoute

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

How BGP works with ExpressRoute gateway?

### Short Answer (30 seconds)

Microsoft and customer exchange routes via BGP sessions over private peering — Azure advertises VNet prefixes; customer advertises on-prem prefixes. Enables dynamic routing without static UDRs.

### Detailed Answer (3–5 minutes)

**Architect:** Set connection weight for primary/backup paths. Route filters limit prefixes advertised. AS path prepending for traffic engineering.

**Warning:** Overlapping prefixes between on-prem and Azure cause blackholes — IP plan governance critical.

### Architecture Perspective

BGP is how hybrid routing scales beyond static routes.

### Follow-up Questions

1. **BGP vs static UDR? — BGP for dynamic failover; UDR for forced default route to firewall.**
2. **ExpressRoute Microsoft peering BGP? — Separate session for Office 365/Azure public prefixes.**

### Common Mistakes in Interviews

- Overlapping BGP advertised prefixes
- No route filter on large prefix advertisements
- Static routes conflicting with BGP learned routes

---

## Q037: VNet Encryption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Azure VNet encryption — what does it protect?

### Short Answer (30 seconds)

Encrypts VNet traffic between VMs within a VNet (and peered VNets with encryption enabled) using MACsec-like capability on Azure infrastructure — defense against physical layer interception within Azure datacenter.

### Detailed Answer (3–5 minutes)

**Architect:** Enable at VNet creation (cannot enable later on existing in some cases — verify current docs). Performance overhead minimal for most workloads. Complements TLS in transit at app layer — not replacement.

### Architecture Perspective

VNet encryption is defense-in-depth for regulated workloads.

### Follow-up Questions

1. **VNet encryption vs TLS? — VNet encryption is network fabric; TLS is application payload.**
2. **Peering with encryption? — Both VNets must enable for encrypted peering traffic.**

### Common Mistakes in Interviews

- VNet encryption replaces application TLS
- Enable on existing VNet without validation
- Assume encryption covers internet egress

---

## Q038: MACsec

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

MACsec on ExpressRoute Direct — when required?

### Short Answer (30 seconds)

Layer 2 encryption between customer router and Microsoft edge on ExpressRoute Direct — financial/regulated workloads requiring link-layer encryption beyond IPsec.

### Detailed Answer (3–5 minutes)

**Architect:** MACsec on ER Direct physical port — complementary to IPsec/Private Peering BGP routes. Plan key exchange and cipher suites with network team.

**Not available:** Standard provider-based ExpressRoute shared ports — Direct only.

### Architecture Perspective

MACsec shows deep compliance networking knowledge.

### Follow-up Questions

1. **MACsec vs IPsec VPN? — MACsec is L2 on dedicated link; IPsec is L3 tunnel.**
2. **Key rotation MACsec? — Follow Microsoft ER Direct MACsec key lifecycle.**

### Common Mistakes in Interviews

- MACsec on standard ExpressRoute circuit
- MACsec as only encryption layer for data at rest
- No network team coordination for Direct

---

## Q039: Load Balancer Outbound SNAT

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Standard LB outbound SNAT exhaustion — symptoms and fixes?

### Short Answer (30 seconds)

Symptoms: intermittent outbound TCP failures, 'Cannot assign requested address'. Cause: 1024 ports per frontend IP shared across backend pool VMs.

### Detailed Answer (3–5 minutes)

**Fixes:**
1. Add backend VMs to reduce ports-per-VM (counterintuitive — more VMs share pool)
2. Dedicated outbound rule with extra public IPs
3. NAT Gateway on subnet (recommended for new designs)

**Architect:** Allocate min 40 ports per VM guideline — calculate `ports = 1024 / VM count` for planning.

### Architecture Perspective

SNAT exhaustion is classic Azure VM outbound mystery.

### Follow-up Questions

1. **Outbound rules vs default SNAT? — Explicit outbound rule with multiple IPs scales ports.**
2. **Connection idle timeout? — Reduce long-lived idle connections consuming ports.**

### Common Mistakes in Interviews

- Ignore SNAT in architecture review
- Single public IP large VM scale set
- No alert on SNAT failed metric

---

## Q040: Cross-Subscription Peering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

VNet peering across subscriptions — permissions and design?

### Short Answer (30 seconds)

User needs Network Contributor on both VNets. Peering created in both directions (initiator + accepter). Use for platform hub in connectivity subscription, spokes in app subscriptions.

### Detailed Answer (3–5 minutes)

**Architect:** RBAC at subscription — platform team owns hub subscription. Automate peering via pipeline with managed identity. Document subscription ID mapping in landing zone.

### Architecture Perspective

Cross-subscription peering is standard landing zone pattern.

### Follow-up Questions

1. **Cross-tenant peering? — Possible with B2B guest access and peering request.**
2. **Global peering cross-subscription? — Supported — watch data transfer billing.**

### Common Mistakes in Interviews

- Insufficient RBAC on one subscription side
- Peering only one direction
- Assuming policy inherits across subscription boundary

---

## Q041: IPv6 Dual Stack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Occasional |

### Question

Dual-stack IPv4/IPv6 on Azure VNet — considerations?

### Short Answer (30 seconds)

Azure supports IPv6 on VNets, LB, App Service (limited), Public IP dual stack. Not all PaaS services IPv6-native — verify per service.

### Detailed Answer (3–5 minutes)

**Architect:** IPv6 for internet-facing apps where mobile/carrier IPv6 required. Internal east-west often IPv4-only sufficient. DNS AAAA records required. NSG rules must include IPv6 address space.

### Architecture Perspective

Dual-stack when business requires IPv6 client reachability.

### Follow-up Questions

1. **IPv6 only VNet? — Rare — dual stack is typical migration path.**
2. **ExpressRoute IPv6? — Supported on private peering — verify provider.**

### Common Mistakes in Interviews

- IPv6 public without NSG hardening
- Forgot AAAA DNS records
- Assumed all Azure PaaS supports IPv6

---

## Q042: Network Segmentation Zero Trust

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Implement Zero Trust network segmentation on Azure?

### Short Answer (30 seconds)

Assume breach — verify explicitly. Micro-segment with NSG/ASG, Private Link for PaaS, Conditional Access, no flat VNet trust, JIT admin access, continuous monitoring.

### Detailed Answer (3–5 minutes)

**Principles:**
- Never trust VNet membership alone for authorization
- Identity + network + app layer checks
- Least privilege east-west traffic

**Architect:** Segment by data classification — PCI subnet isolated with separate firewall policy.

### Architecture Perspective

Zero Trust is identity + network + data — not product name only.

### Follow-up Questions

1. **Zero Trust vs traditional perimeter? — Perimeter still exists but not sole control.**
2. **Microsoft Zero Trust deployment guide? — Map to CA, Defender, Purview pillars.**

### Common Mistakes in Interviews

- Flat VNet — all subnets talk freely
- Network location as sole trust signal
- Zero Trust without identity verification

---

## Q043: Micro-Segmentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Micro-segmentation strategy for microservices on AKS?

### Short Answer (30 seconds)

Azure CNI with network policies (Calico/Cilium), NSG on node subnet, service mesh mTLS optional, Private Link to backing stores.

### Detailed Answer (3–5 minutes)

**Layers:**
- Deny all between namespaces by default
- Allow explicit namespace-to-namespace on ports
- Ingress controller WAF for north-south

**Architect:** Start with Kubernetes NetworkPolicy — add service mesh when mTLS and L7 policy required.

### Architecture Perspective

Micro-segmentation beyond coarse subnet NSG.

### Follow-up Questions

1. **Service mesh vs network policy? — Policy is L3-L4 K8s; mesh adds L7 and mTLS.**
2. **AKS Azure CNI required? — Network policies need Azure CNI (not kubenet).**

### Common Mistakes in Interviews

- All pods in cluster flat network
- NSG allow all within VNet
- Micro-segmentation without observability on denied flows

---

## Q044: Application Security Groups Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Refactor 200 IP-based NSG rules to ASGs — approach?

### Short Answer (30 seconds)

Inventory VMs by tier role, create ASGs (`WebTier`, `AppTier`, `DataTier`), assign NICs to ASGs, replace IP rules with ASG-to-ASG rules, decommission IP rules.

### Detailed Answer (3–5 minutes)

**Migration:** Enable in audit mode with flow logs — verify traffic patterns before removing old rules.

**Architect:** ASG naming standard in landing zone policy. Automate ASG assignment in VM deployment template.

### Architecture Perspective

ASG migration reduces operational toil at scale.

### Follow-up Questions

1. **Multiple ASGs per NIC? — Yes — NIC can belong to multiple ASGs.**
2. **ASG with scale sets? — Apply ASG to scale set NIC configuration.**

### Common Mistakes in Interviews

- Big-bang rule cutover without flow log validation
- ASG per VM instead of per tier
- Forgetting to assign new VMs to ASG

---

## Q045: Firewall Policy DNAT

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Publish internal web server via Azure Firewall DNAT?

### Short Answer (30 seconds)

Firewall public IP + DNAT rule: external 443 → internal 10.0.1.4:443. Source filter restrict to known IPs if possible.

### Detailed Answer (3–5 minutes)

**Architect:** Prefer Front Door/App Gateway for web publishing with WAF — use Firewall DNAT for non-HTTP or hub-centric designs. Log all DNAT hits to Log Analytics.

**SNAT return path:** Firewall performs SNAT for return — internal server sees firewall IP as source.

### Architecture Perspective

DNAT is hub ingress pattern — know alternatives.

### Follow-up Questions

1. **DNAT vs ILB? — DNAT through firewall for inspected ingress.**
2. **Multiple DNAT rules same IP different ports? — Supported — map ports to different internals.**

### Common Mistakes in Interviews

- DNAT without WAF for public HTTP
- Any source on DNAT rule
- Internal server default gateway wrong for asymmetric

---

## Q046: TLS Inspection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Azure Firewall Premium TLS inspection — trade-offs?

### Short Answer (30 seconds)

Decrypt HTTPS for IDPS and URL filtering — requires corporate CA cert deployed to clients/servers. Privacy and compliance implications.

### Detailed Answer (3–5 minutes)

**Architect:** Enable only where policy mandates — exclude banking/health categories. Document exception list. Performance overhead on firewall SKU.

**Alternative:** East-west mTLS within app layer without central TLS break.

### Architecture Perspective

TLS inspection is compliance decision not default enable.

### Follow-up Questions

1. **Certificate pinning apps? — Break with inspection — maintain bypass list.**
2. **Outbound vs inbound inspection? — Both configurable in Premium policy.**

### Common Mistakes in Interviews

- Enable TLS inspection without legal/compliance review
- Default CA not deployed to all clients
- Inspect all traffic including Azure service tags unnecessarily

---

## Q047: Proxy Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Design explicit proxy for outbound internet from Azure workloads?

### Short Answer (30 seconds)

Squid/NVA or Azure Firewall as forward proxy — apps configured with `HTTP_PROXY` env var. UDR forces traffic to proxy; direct internet blocked.

### Detailed Answer (3–5 minutes)

**Architect:** Central proxy enables URL categorization, authentication, logging. Container egress via proxy sidecar or cluster-wide policy.

**PaaS exception:** App Service regional VNet integration may need service endpoints/Private Link instead of proxy for Azure services.

### Architecture Perspective

Explicit proxy for regulated egress filtering.

### Follow-up Questions

1. **Transparent vs explicit proxy? — Explicit requires app config; transparent uses UDR redirect.**
2. **Proxy HA? — Scale proxy VMSS behind ILB in hub.**

### Common Mistakes in Interviews

- Proxy as single VM SPOF
- Apps not configured for proxy — bypass fails open
- No proxy logging to SIEM

---

## Q048: Egress Filtering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Egress filtering strategy for PCI subnet on Azure?

### Short Answer (30 seconds)

Default deny outbound from PCI subnet UDR — allow explicit FQDN via Azure Firewall application rules, deny direct internet, Private Link to required PaaS only.

### Detailed Answer (3–5 minutes)

**Allow list:** Package repos (nuget.org via mirror), Microsoft Update service tags, specific API partners.

**Architect:** Log all denied egress — tune rules monthly. Break-glass rule with approval workflow for emergency domains.

### Architecture Perspective

Egress control prevents data exfiltration architecture.

### Follow-up Questions

1. **Egress vs ingress focus? — Architects often neglect outbound — attackers use egress.**
2. **FQDN tag AzureBackup? — Allow required service tag rules for backup agents.**

### Common Mistakes in Interviews

- Allow all outbound from app subnet
- Egress filter without logging
- Block Azure service tags breaking PATCH operations

---

## Q049: Hybrid DNS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Very Common |

### Question

End-to-end hybrid DNS for Active Directory integrated zones?

### Short Answer (30 seconds)

Domain controllers on-prem authoritative for `corp.contoso.com`; Azure VMs join domain via VPN/ER. Azure Private DNS Resolver bridges Azure-specific privatelink zones.

### Detailed Answer (3–5 minutes)

**Architect:** Avoid split-brain AD DNS — single authoritative source. Azure DCs in hub if Azure-native DR for AD required.

**Test:** `nslookup` internal names from Azure VM and from on-prem client.

### Architecture Perspective

Hybrid DNS + AD is common enterprise migration path.

### Follow-up Questions

1. **Azure AD DS vs AD DS DNS? — Managed domain has own DNS — different pattern.**
2. **DNS forwarder on Azure VM? — Prefer Private DNS Resolver managed.**

### Common Mistakes in Interviews

- Duplicate AD DNS zones Azure and on-prem
- Dynamic DNS updates blocked by firewall
- No DNS monitoring on resolution failures

---

## Q050: Network Monitoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Network monitoring architecture for Azure landing zone?

### Short Answer (30 seconds)

NSG flow logs → Log Analytics Traffic Analytics, Connection Monitor synthetic probes, Azure Monitor alerts on VPN/ER gateway metrics, Firewall diagnostic logs, DDoS alerts.

### Detailed Answer (3–5 minutes)

**Dashboards:** Cross-region latency, top talkers, denied flow trends, VPN tunnel status.

**Architect:** Define SLO for hub connectivity — alert ER BGP session down within 1 minute. Integrate Sentinel for correlation with security events.

### Architecture Perspective

Network observability prevents long MTTR on hybrid incidents.

### Follow-up Questions

1. **SNMP on Azure? — Limited — use platform metrics and flow logs.**
2. **Packet capture automation? — Logic App triggered on alert for brief capture.**

### Common Mistakes in Interviews

- No flow logs in production
- Alerts without runbook links
- Monitoring only Azure not on-prem path

---
