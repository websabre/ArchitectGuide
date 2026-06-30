# Week 12 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Identity | **Count:** 50

---


## Q001: Entra ID vs Active Directory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Explain Entra ID role in Azure architecture vs on-prem AD.

### Short Answer (30 seconds)

Entra ID: cloud identity provider — users, apps, SSO, Conditional Access. AD DS on VM: legacy LDAP/Kerberos apps. Sync hybrid with Entra Connect for many enterprises.

### Detailed Answer (3–5 minutes)

**Modern apps:** OAuth/OIDC with Entra ID. **Legacy:** AD DS lift or extend.

**Architect:** New apps use Entra — no new AD DS unless required.

### Architecture Perspective

Identity foundation for all Azure designs.

### Follow-up Questions

1. **Entra Domain Services? — Managed AD-compatible — lift legacy LDAP apps.**
2. **B2C vs workforce? — Separate tenant for consumer identities.**

### Common Mistakes in Interviews

- New apps authenticating to on-prem AD directly
- No Conditional Access on admin accounts
- Shared break-glass without procedure

---

## Q002: Managed Identity Types

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

System-assigned vs user-assigned managed identity?

### Short Answer (30 seconds)

System-assigned: lifecycle tied to resource — deleted with App Service. User-assigned: independent, shared across resources (slots, functions).

### Detailed Answer (3–5 minutes)

**Use user-assigned:** same identity across deployment slot swap, multiple apps sharing access.

**Architect:** Default system-assigned for single app; user-assigned for complex slot/failover scenarios.

### Architecture Perspective

MI eliminates secrets — architect standard.

### Follow-up Questions

1. **MI across subscriptions? — Possible with RBAC — cross-subscription grants.**
2. **Local dev without secrets? — DefaultAzureCredential — dev uses VS/Azure CLI.**

### Common Mistakes in Interviews

- SQL connection string password in Key Vault only — still a secret to rotate
- No MI on CI/CD — long-lived SP secret
- MI with excessive RBAC scope

---

## Q003: OAuth 2.0 Flows on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Which OAuth flow for SPA, mobile, and service-to-service?

### Short Answer (30 seconds)

SPA/mobile: Authorization Code + PKCE. Service-to-service: Client Credentials. User context to downstream API: On-Behalf-Of (OBO).

### Detailed Answer (3–5 minutes)

**Never:** implicit flow (deprecated). **API permissions:** least privilege app registration scopes.

**Architect:** APIM validates JWT at edge; services validate audience and issuer.

### Architecture Perspective

OAuth flow selection is security architecture.

### Follow-up Questions

1. **PKCE why? — Public clients cannot store secret — code challenge prevents interception.**
2. **Client secret in mobile app? — Never — use PKCE or native broker.**

### Common Mistakes in Interviews

- Implicit flow for new SPA
- ROPC password grant
- No audience validation on API

---

## Q004: Conditional Access Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design Conditional Access for production admin access.

### Short Answer (30 seconds)

Require MFA, compliant device, block legacy auth, sign-in risk medium+ requires MFA, block non-trusted locations for admins.

### Detailed Answer (3–5 minutes)

**Break-glass accounts:** excluded from CA with monitoring alerts on usage.

**Architect:** CA is Zero Trust enforcement layer — document policies per persona (admin, developer, external).

### Architecture Perspective

CA policies are production security baseline.

### Follow-up Questions

1. **Report-only mode? — Test policy impact before enforcement.**
2. **Continuous access evaluation? — Revoke session when risk changes.**

### Common Mistakes in Interviews

- No MFA on global admin
- CA not applied to service principals appropriately
- Break-glass unmonitored

---

## Q005: Key Vault Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design Key Vault for 10 microservices.

### Short Answer (30 seconds)

Separate vault per environment (prod/nonprod). RBAC not legacy access policies. Soft delete + purge protection prod. References in App Service config.

### Detailed Answer (3–5 minutes)

**Secrets rotation:** automated rotation for SQL passwords, cert renewal alerts.

**Architect:** No secrets in Git — Key Vault references + MI. Pipeline OIDC for deployment secrets.

### Architecture Perspective

Key Vault design prevents secret sprawl.

### Follow-up Questions

1. **Private endpoint Key Vault? — Required for network-isolated workloads.**
2. **HSM-backed keys? — Regulatory requirements — Premium SKU.**

### Common Mistakes in Interviews

- One vault all environments
- Secrets copied to appsettings
- No purge protection — ransomware deletes vault

---

## Q006: App Registration vs Enterprise App

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Difference in Entra app registration?

### Short Answer (30 seconds)

App registration: definition (client ID, permissions, redirect URIs). Enterprise application: instance in tenant (assignment, SSO config, consent).

### Detailed Answer (3–5 minutes)

**Multi-tenant SaaS:** one registration, enterprise apps per customer tenant.

**Architect:** Document app registration ownership and secret rotation owners.

### Architecture Perspective

Entra app model clarity shows identity depth.

### Follow-up Questions

1. **API permissions delegated vs application? — User context vs app-only.**
2. **Admin consent workflow? — Required for application permissions.**

### Common Mistakes in Interviews

- Permissions not granted after registration
- Confuse audience in token
- Over-scoped Microsoft Graph permissions

---

## Q007: On-Behalf-Of Flow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

API A calls API B on behalf of user — pattern?

### Short Answer (30 seconds)

OBO: Client gets user token for API A; API A exchanges for token to API B with user context preserved via `acquireTokenOnBehalfOf`.

### Detailed Answer (3–5 minutes)

**Use when:** downstream API needs user identity/permissions.

**Client credentials when:** background job without user — no OBO.

### Architecture Perspective

OBO is common microservices identity pattern.

### Follow-up Questions

1. **Token cache OBO? — MSAL serializable cache — avoid token request per call.**
2. **Chained OBO depth? — Limit chain — latency and consent complexity.**

### Common Mistakes in Interviews

- Pass user JWT to downstream without validation
- Client credentials when user context needed
- Infinite OBO chain

---

## Q008: Key Vault Reference in App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Common |

### Question

How reference Key Vault secret in App Service without code change?

### Short Answer (30 seconds)

`@Microsoft.KeyVault(SecretUri=https://vault.vault.azure.net/secrets/name/)` in app setting. App Service MI needs GET secret permission.

### Detailed Answer (3–5 minutes)

**Rotation:** update secret version — restart or refresh depending on config.

**Architect:** Bicep deploys references — no manual portal config.

### Architecture Perspective

Configuration externalization best practice.

### Follow-up Questions

1. **Slot setting sticky with KV ref? — Per-slot secrets for staging vs prod.**
2. **Managed identity required? — Yes for reference resolution.**

### Common Mistakes in Interviews

- Secret value pasted in app setting
- KV reference without MI permission
- No rotation process

---

## Q009: Zero Trust on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Implement Zero Trust principles on Azure landing zone?

### Short Answer (30 seconds)

Verify explicitly (CA, MFA), least privilege (RBAC, PIM), assume breach (segment networks, Private Link, Defender, Sentinel).

### Detailed Answer (3–5 minutes)

**Network:** no public PaaS endpoints — private endpoints. **Identity:** managed identities over secrets. **Monitor:** Sentinel analytics, Defender alerts.

### Architecture Perspective

Zero Trust is architecture philosophy not one product.

### Follow-up Questions

1. **Micro-segmentation? — NSG + Azure Firewall application rules.**
2. **Just-in-time VM access? — Defender for Cloud JIT.**

### Common Mistakes in Interviews

- Flat network all resources public
- VPN as only security boundary
- Standing global admin access

---

## Q010: Identity for CI/CD Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

GitHub Actions deploy to Azure without client secret?

### Short Answer (30 seconds)

OIDC federated credential on app registration — GitHub workflow requests token from Entra, deploys with RBAC-scoped role.

### Detailed Answer (3–5 minutes)

**Setup:** `azure/login@v2` with `client-id`, `tenant-id`, `subscription-id`, federated token.

**Architect:** Ban long-lived SP secrets in GitHub — enforce OIDC in platform template.

### Architecture Perspective

Pipeline identity is security-critical architect decision.

### Follow-up Questions

1. **Workload identity federation? — Same pattern Azure DevOps and other CI.**
2. **Scope deploy role? — Resource group level custom role — not subscription Owner.**

### Common Mistakes in Interviews

- SP secret in GitHub secrets 2 years old
- Owner role for pipeline
- No branch protection on workflow files

---

## Q011: Entra ID vs AD DS Deep Comparison

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

When deploy AD Domain Services vs Entra ID for a hybrid enterprise?

### Short Answer (30 seconds)

Entra ID: cloud-native identity for SaaS, OAuth/OIDC apps, Conditional Access. AD DS on VM/IaaS: full LDAP/Kerberos domain control you manage. Entra Domain Services: managed AD-compatible for legacy LDAP lift.

### Detailed Answer (3–5 minutes)

**Decision tree:**
- **New cloud apps:** Entra ID only
- **Legacy LDAP/Kerberos app:** Entra DS or AD DS VM
- **Hybrid users:** Entra Connect sync from on-prem AD

**Architect:** Minimize new AD DS deployments — operational burden (patching, DC HA). Entra DS for GPO/LDAP without VM DCs.

### Architecture Perspective

Hybrid identity architecture balances legacy and modern auth.

### Follow-up Questions

1. **Entra DS limitations? — No domain admin, fixed schema — verify app compatibility.**
2. **Cloud-only org? — Entra ID only — no AD DS needed.**

### Common Mistakes in Interviews

- New SaaS app authenticating Kerberos to AD DS
- Entra DS without understanding schema limits
- No exit plan from on-prem AD

---

## Q012: Managed Identity Types in Depth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Design managed identity strategy for App Service, Functions, and AKS.

### Short Answer (30 seconds)

System-assigned MI per app resource. User-assigned MI shared across slot swap, multiple Functions, AKS pod identity. Prefer user-assigned for production multi-resource scenarios.

### Detailed Answer (3–5 minutes)

**AKS:** Workload Identity (OIDC) replaces deprecated pod identity. Federate K8s SA to user-assigned MI.

**Architect RBAC:** Grant MI least privilege at resource group scope — `Storage Blob Data Contributor` on one account not subscription.

**Dev:** DefaultAzureCredential chain — local VS login, MI in Azure.

### Architecture Perspective

MI strategy prevents secret sprawl across compute types.

### Follow-up Questions

1. **MI across tenants? — Not supported — per-tenant MI.**
2. **Rotate MI? — No secret to rotate — advantage over SP.**

### Common Mistakes in Interviews

- Shared SP credential across 20 microservices
- Subscription Contributor on every MI
- Pod identity on new AKS clusters without migration plan

---

## Q013: Conditional Access Policy Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Layer Conditional Access policies without lockout risk.

### Short Answer (30 seconds)

Start report-only. Baseline: all users MFA, block legacy auth. Layer: admin policies (compliant device + MFA), guest restrictions, sign-in risk policies.

### Detailed Answer (3–5 minutes)

**Policy order matters:** Named locations, filter groups, exclusions documented.

**Architect:** Break-glass accounts excluded with Sentinel alert on sign-in. Separate policies per risk persona — don't one-size-fits-all.

**Test:** What If tool before enforcement.

### Architecture Perspective

CA is Zero Trust enforcement — design carefully to avoid outages.

### Follow-up Questions

1. **Service principal CA? — Conditional Access for workload identities (preview) — know trend.**
2. **Session controls? — App enforced restrictions, sign-in frequency.**

### Common Mistakes in Interviews

- Enforce all policies day one without report-only
- Break-glass in same CA scope as admins
- No exclusion documentation

---

## Q014: PIM Just-in-Time Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Configure PIM for Azure subscription Owner role.

### Short Answer (30 seconds)

Eligible assignment not permanent. Activation requires MFA, justification, ticket ID, max duration 8 hours. Approval workflow for prod subscription.

### Detailed Answer (3–5 minutes)

**Architect:**
- No standing Owner in prod
- Audit activation logs to Log Analytics
- Notification to security on activation

**Emergency access:** Break-glass bypasses PIM — monitored separately.

### Architecture Perspective

PIM converts privileged access from standing to just-in-time.

### Follow-up Questions

1. **PIM for groups? — PIM-enabled Entra groups — scale RBAC management.**
2. **Permanent assignment audit? — Defender Identity recommendations flag.**

### Common Mistakes in Interviews

- Standing Global Administrator prod
- PIM activation without approval prod
- No alert on break-glass usage

---

## Q015: Service Principal vs Managed Identity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Service principal vs managed identity for Azure resource access?

### Short Answer (30 seconds)

Managed identity: Azure-managed, no credential rotation, tied to Azure resource. Service principal: app registration with secret/cert, needed for external systems, CI/CD (prefer federated over secret).

### Detailed Answer (3–5 minutes)

**Use SP when:** GitHub Actions OIDC (federated), third-party SaaS, non-Azure caller.

**Use MI when:** Azure-hosted app accessing Azure APIs.

**Architect:** Eliminate SP secrets — federated workload identity for pipelines.

### Architecture Perspective

Credential type selection is fundamental security architecture.

### Follow-up Questions

1. **SP secret expiry? — App registration credential lifetime policies.**
2. **Multi-tenant SP? — SaaS vendor pattern — careful consent model.**

### Common Mistakes in Interviews

- MI for GitHub Actions (wrong — use federated SP)
- SP secret in ARM template plaintext
- Same SP Owner on all subscriptions

---

## Q016: App Registration vs Enterprise Application

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Multi-tenant SaaS app registration architecture?

### Short Answer (30 seconds)

One multi-tenant app registration (definition). Each customer tenant creates enterprise application instance on admin consent. Per-tenant service principal for API access.

### Detailed Answer (3–5 minutes)

**Architect documents:**
- Redirect URIs per environment
- API exposed scopes and app roles
- Admin consent URL for customer onboarding

**Enterprise app:** SSO blade, user assignment, conditional access targeting.

### Architecture Perspective

SaaS identity model separates definition from tenant instances.

### Follow-up Questions

1. **Publisher verification? — Required for customer trust — MPN ID.**
2. **App roles vs scopes? — App roles for RBAC in API; scopes for delegated permissions.**

### Common Mistakes in Interviews

- Confuse registration object ID with enterprise app ID
- Customer admin consent not documented
- Over-permissioned Graph API scopes

---

## Q017: Entra B2B Guest Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Design B2B collaboration for external consultants.

### Short Answer (30 seconds)

Invite guest users to home tenant. CA policies for guests (MFA, device compliance if enrolled). Restrict guest visibility in directory.

### Detailed Answer (3–5 minutes)

**Architect:**
- Guest access reviews quarterly
- Limit guest to specific apps via assignment
- Cross-tenant sync for partner org auto-provisioning (advanced)

**vs B2C:** B2B for workforce collaboration; B2C for consumer apps.

### Architecture Perspective

B2B extends workforce identity to partners securely.

### Follow-up Questions

1. **Redeem invitation flow? — One-time link — expiry policy.**
2. **Guest can enumerate users? — Restrict in external collaboration settings.**

### Common Mistakes in Interviews

- Guest with same CA as employees without assessment
- Never review guest access
- B2B for customer ecommerce login

---

## Q018: Entra External ID for B2C

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Entra External ID (CIAM) vs legacy Azure AD B2C?

### Short Answer (30 seconds)

External ID is converged CIAM platform — custom sign-up, social IdPs, branded flows. B2C tenants continue; new projects evaluate External ID.

### Detailed Answer (3–5 minutes)

**Architect consumer app:**
- Separate tenant from workforce Entra
- User flows or custom policies (legacy B2C) / native sign-up (External ID)
- Token customization for app claims

**Scale:** Millions of users — no directory object limit concerns with proper architecture.

### Architecture Perspective

Know B2C → External ID evolution for architect roadmap.

### Follow-up Questions

1. **Social identity providers? — Google, Facebook, Apple — configure per app.**
2. **MFA for consumers? — Risk-based — balance UX.**

### Common Mistakes in Interviews

- Workforce and consumer same tenant
- Store consumer PII in workforce directory
- Custom policy complexity without docs

---

## Q019: Passwordless Authentication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Roll out passwordless for enterprise Entra ID users.

### Short Answer (30 seconds)

Windows Hello for Business, FIDO2 security keys, Microsoft Authenticator phone sign-in. Combined registration in Entra — start with security-key pilots.

### Detailed Answer (3–5 minutes)

**Architect rollout:**
1. Enable Combined Registration
2. CA requires MFA → upgrade to passwordless-capable MFA
3. Disable password legacy auth
4. Helpdesk process for lost key

**Phishing-resistant:** FIDO2 and WHfB resist credential theft.

### Architecture Perspective

Passwordless is Microsoft strong auth direction.

### Follow-up Questions

1. **Temporary Access Pass? — Bootstrap passwordless registration.**
2. **Passkeys? — FIDO2 aligned — watch Entra roadmap.**

### Common Mistakes in Interviews

- SMS as only MFA calling it passwordless
- No backup auth method
- Passwordless without CA policy update

---

## Q020: Certificate-Based Authentication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Certificate-based auth for service-to-service on Azure?

### Short Answer (30 seconds)

App registration upload cert (public key) — app uses private cert for client assertion JWT. No client secret.

### Detailed Answer (3–5 minutes)

**vs Federated credential:** CBA for traditional cert PKI; federation for OIDC trust (GitHub, K8s).

**Architect:** Cert expiry monitoring 60 days ahead. Store private cert in Key Vault HSM. Auto-renew with ACME/internal CA integration.

### Architecture Perspective

Certs beat secrets for long-lived service auth when managed properly.

### Follow-up Questions

1. **Mutual TLS? — APIM/API Management client cert validation at gateway.**
2. **Self-signed prod? — Enterprise CA or Key Vault issued preferred.**

### Common Mistakes in Interviews

- Expired cert no monitoring
- Private key in repo
- Cert auth without rotation runbook

---

## Q021: Entra Connect Sync Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

Design Entra Connect sync for hybrid identity.

### Short Answer (30 seconds)

Entra Connect on hardened VM syncs on-prem AD to Entra ID. Password hash sync (PHS) default; PTA or federation for advanced.

### Detailed Answer (3–5 minutes)

**Architect:**
- Staging mode second server for DR
- OU filtering sync scope
- Group writeback if needed
- Monitor sync errors in Entra Connect Health

**Cloud sync:** Lightweight agent alternative for simple scenarios.

### Architecture Perspective

Hybrid sync is critical path — HA and monitoring mandatory.

### Follow-up Questions

1. **PHS vs PTA? — PHS simpler; PTA keeps password on-prem.**
2. **Soft match vs hard match? — UPN alignment prevents duplicate objects.**

### Common Mistakes in Interviews

- Single Connect server no staging
- Sync all OUs including service accounts
- Ignore sync error emails

---

## Q022: Pass-Through Authentication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Pass-through authentication vs password hash sync?

### Short Answer (30 seconds)

PTA: Entra sign-in validated against on-prem AD in real time — password never in cloud. Requires PTA agents on-prem. PHS: hash synced — cloud auth without on-prem dependency.

### Detailed Answer (3–5 minutes)

**Choose PTA when:** policy forbids password hash in cloud, real-time account disable needed.

**Architect:** PTA agents HA (minimum 3). Fallback to PHS documented if agents down.

**Limitation:** PTA agent outage blocks cloud sign-in.

### Architecture Perspective

Auth method affects availability and compliance posture.

### Follow-up Questions

1. **PTA vs Federation AD FS? — PTA simpler; federation for custom auth flows.**
2. **Seamless SSO? — Kerberos ticket for domain-joined devices.**

### Common Mistakes in Interviews

- PTA single agent
- PTA without PHS break-glass fallback plan
- PTA for internet-only users

---

## Q023: Federated Identity AD FS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

When use AD FS federation instead of PHS/PTA?

### Short Answer (30 seconds)

Federation when: custom auth (smart card step-up), third-party IdP integration legacy, claim rules complex. AD FS farm on-prem — higher ops burden.

### Detailed Answer (3–5 minutes)

**Architect:** Microsoft recommends PHS/PTA for new hybrids unless federation requirement clear.

**Modern:** Move to Entra federation with custom IdP via OIDC where possible — retire AD FS long-term.

### Architecture Perspective

Federation is legacy-heavy — justify before designing.

### Follow-up Questions

1. **AD FS WAP? — Web Application Proxy DMZ — don't expose AD FS direct.**
2. **Certificate management AD FS? — Token signing cert rotation critical.**

### Common Mistakes in Interviews

- AD FS for greenfield hybrid
- AD FS without HA farm
- No token signing cert expiry monitoring

---

## Q024: MFA Methods Comparison

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Rank MFA methods for security and usability.

### Short Answer (30 seconds)

Most secure: FIDO2/WHfB (phishing-resistant). Strong: Microsoft Authenticator push with number matching. Weaker: SMS/voice (SIM swap risk).

### Detailed Answer (3–5 minutes)

**Architect CA policy:** Authentication strength — require phishing-resistant for admins.

**Registration:** Combined registration campaign; block weak methods for privileged roles via Authentication methods policy.

### Architecture Perspective

MFA method choice is measurable security difference.

### Follow-up Questions

1. **OATH hardware tokens? — Supported for air-gapped scenarios.**
2. **MFA fatigue attacks? — Number matching + additional context.**

### Common Mistakes in Interviews

- SMS-only MFA for Global Admin
- Allow MFA bypass codes routinely
- No method upgrade path for users

---

## Q025: Entra ID Protection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Use Identity Protection risk signals in architecture.

### Short Answer (30 seconds)

Detects leaked credentials, anonymous IP, atypical travel, malware-linked IP. Risk levels feed Conditional Access (sign-in risk, user risk).

### Detailed Answer (3–5 minutes)

**Architect workflows:**
- Medium sign-in risk → MFA
- High sign-in risk → block or password change
- User risk high → force password reset or block

**License:** Entra ID P2 for full Identity Protection.

### Architecture Perspective

Risk-based auth automates threat response.

### Follow-up Questions

1. **Risk detections export? — Sentinel integration for SOC.**
2. **Disable risk policy on break-glass? — Yes — separate monitoring.**

### Common Mistakes in Interviews

- Ignore Identity Protection alerts
- Risk policy without user communication
- P1 license expecting full risk features

---

## Q026: Risk-Based Conditional Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Design risk-based CA policies for remote workforce.

### Short Answer (30 seconds)

Sign-in risk: require MFA medium+, block high. User risk: require password change for high user risk. Combine with named locations — trusted office IPs lower friction.

### Detailed Answer (3–5 minutes)

**Architect balance:** Productivity vs security — start report-only on new detections.

**Integration:** Defender for Cloud Apps session policies for risky OAuth apps.

### Architecture Perspective

Risk policies adapt to threat without static IP reliance alone.

### Follow-up Questions

1. **Insider risk? — Different product — don't conflate with sign-in risk.**
2. **Continuous Access Evaluation? — Real-time revocation on risk change.**

### Common Mistakes in Interviews

- Block all foreign sign-ins without business justification
- Risk policy no exception for traveling execs
- Never tune false positives

---

## Q027: Workload Identity Federation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Explain workload identity federation without secrets.

### Short Answer (30 seconds)

App registration federated credential trusts external OIDC issuer (GitHub, K8s, other cloud). External workload exchanges OIDC token for Entra access token — no client secret.

### Detailed Answer (3–5 minutes)

**Setup:** Issuer, subject, audience on federated credential. GitHub: `repo:org/repo:ref:refs/heads/main`.

**Architect:** Standard pattern for all CI/CD and K8s — ban secret-based SP auth in platform guardrails.

### Architecture Perspective

Federation is modern SP replacement.

### Follow-up Questions

1. **Multiple federated credentials? — Per repo/environment subject.**
2. **Audit federated sign-ins? — Entra sign-in logs show workload identity.**

### Common Mistakes in Interviews

- Long-lived SP secret for GitHub Actions
- Over-broad subject `repo:org/*:*`
- No branch protection on federated repos

---

## Q028: GitHub OIDC to Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

Configure GitHub Actions OIDC deploy to Azure without secrets.

### Short Answer (30 seconds)

App registration federated credential for GitHub OIDC. Workflow `permissions: id-token: write`. `azure/login@v2` with client-id, tenant-id, subscription-id.

### Detailed Answer (3–5 minutes)

**Architect RBAC:** Grant federated SP `Contributor` on resource group not subscription Owner.

**Environments:** Separate federated credential subject per GitHub environment (prod vs dev).

### Architecture Perspective

OIDC pipeline auth is platform security baseline.

### Follow-up Questions

1. **Azure DevOps equivalent? — Service connection workload identity federation.**
2. **Token theft? — Subject binding prevents other repos using credential.**

### Common Mistakes in Interviews

- AZURE_CREDENTIALS JSON secret
- Owner role for deploy pipeline
- Same credential prod and dev

---

## Q029: Kubernetes SA Token Volume Projection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

AKS workload identity with service account token projection?

### Short Answer (30 seconds)

Kubernetes ServiceAccount annotated with Entra app client ID. Token projected into pod via OIDC — app uses DefaultAzureCredential or SDK token credential.

### Detailed Answer (3–5 minutes)

**Migration:** AKS workload identity replaces legacy pod identity. Enable OIDC issuer on cluster.

**Architect:** One user-assigned MI per workload class; federate via SA annotation. Avoid mounting Azure SP secrets as K8s secrets.

### Architecture Perspective

K8s-native identity is Azure best practice on AKS.

### Follow-up Questions

1. **Token expiration? — Projected token rotates — handle refresh in SDK.**
2. **Multi-tenant K8s? — Namespace isolation + separate MI per namespace.**

### Common Mistakes in Interviews

- Legacy aad-pod-identity on new clusters
- Cluster admin kubeconfig shared
- SP secret in K8s Secret manifest

---

## Q030: Microsoft Entra External ID

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Architect consumer identity with Microsoft Entra External ID.

### Short Answer (30 seconds)

Dedicated workforce vs external tenant separation. External ID provides branded authentication experiences, social and local accounts, MFA for consumers.

### Detailed Answer (3–5 minutes)

**Architect:**
- Custom domains for auth (`login.contoso.com`)
- API connectors for custom logic at sign-up
- Rate limiting and fraud signals

**Integration:** OIDC standard — any mobile/web app.

### Architecture Perspective

External ID is strategic CIAM direction.

### Follow-up Questions

1. **User migration B2C? — Bulk import and gradual cutover patterns.**
2. **Custom extensions? — API connectors call REST endpoints.**

### Common Mistakes in Interviews

- Consumer users in workforce tenant
- No separate CA policy for external users
- Shared app registration workforce and consumer

---

## Q031: Custom Domain in Entra

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Configure custom domain for Entra ID sign-in branding?

### Short Answer (30 seconds)

Verify domain DNS TXT record. Set primary domain for UPN suffix. Custom branding on login page — logo, background, terms link.

### Detailed Answer (3–5 minutes)

**Architect:** Users sign in with `@company.com` not `@tenant.onmicrosoft.com`. Required for federation alignment.

**Email-verified domains for B2C/External ID:** separate DNS verification flow.

### Architecture Perspective

Custom domain is professional identity hygiene.

### Follow-up Questions

1. **Federated domain? — Cannot convert cloud-only managed domain easily.**
2. **Multiple domains? — One primary; aliases supported.**

### Common Mistakes in Interviews

- Permanent onmicrosoft.com UPNs prod
- DNS verification lapsed
- Brand assets not updated phishing risk

---

## Q032: Tenant Isolation Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Isolate production from non-production Entra tenants?

### Short Answer (30 seconds)

Separate Entra tenants for prod vs dev/test — prevents misconfigured CA/policy blast radius. Cross-tenant B2B for admin access if needed.

### Detailed Answer (3–5 minutes)

**Architect:**
- Prod tenant: strict CA, PIM, no experimental apps
- Dev tenant: developer freedom, synthetic data
- No prod data in dev tenant apps

**Alternative:** Single tenant with strict app/CA scoping — harder at scale.

### Architecture Perspective

Tenant boundary is strongest identity isolation.

### Follow-up Questions

1. **Cross-tenant sync? — Partner provisioning — not prod/dev substitute.**
2. **Management group vs tenant? — Azure RBAC vs identity boundary — both needed.**

### Common Mistakes in Interviews

- Prod and dev same tenant same CA
- Prod API app registration in dev tenant
- Global admin shared across tenants same person no PIM

---

## Q033: Cross-Tenant Synchronization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Occasional |

### Question

Use cross-tenant sync for partner user provisioning?

### Short Answer (30 seconds)

Automated provisioning of member users from source tenant to target tenant — B2B alternative for trusted partners needing member (not guest) experience.

### Detailed Answer (3–5 minutes)

**Architect:** Source tenant controls. target tenant one-way sync. Define scope groups. Monitor provisioning logs.

**vs B2B guest:** Member users in target — different CA and licensing implications.

### Architecture Perspective

Cross-tenant sync automates partner onboarding at scale.

### Follow-up Questions

1. **Provisioning conflicts? — Attribute mapping and quarantine review.**
2. **Reverse sync? — Not supported — design one authoritative source.**

### Common Mistakes in Interviews

- Bidirectional sync expectation
- Sync all users not scoped group
- No offboarding sync disable

---

## Q034: Directory Roles vs App Roles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Directory roles vs app roles in API authorization?

### Short Answer (30 seconds)

Directory roles: Entra admin (Global Reader, User Admin) — manage tenant. App roles: defined on app registration, assigned to users/groups/SPs — authorize in your API.

### Detailed Answer (3–5 minutes)

**Architect API:** Validate `roles` claim in JWT — map to permissions. Don't overload directory roles for app RBAC.

**Example app roles:** `Order.Read`, `Order.Admin` assigned via enterprise app.

### Architecture Perspective

Clear role separation prevents authorization model confusion.

### Follow-up Questions

1. **Group vs app role? — Assign group to app role for scale.**
2. **Claims mapping? — Optional claims emit roles in token.**

### Common Mistakes in Interviews

- Global Admin check in application code
- App roles not defined on registration
- Directory role for business permission

---

## Q035: OAuth 2.0 Flows Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Select OAuth 2.0 flow per application type on Azure.

### Short Answer (30 seconds)

Auth code + PKCE: SPA, mobile, native. Client credentials: daemon/service. Auth code (confidential): web server apps with secret/cert. OBO: API calling API with user context. Device code: CLI/IoT constrained input.

### Detailed Answer (3–5 minutes)

**Deprecated:** Implicit flow, ROPC — never new apps.

**Architect:** APIM validates token at edge; backend validates audience, issuer, scopes.

### Architecture Perspective

OAuth flow literacy is identity architecture core.

### Follow-up Questions

1. **Hybrid flow? — Deprecated — use auth code.**
2. **Native redirect URI? — Mobile platform-specific URIs registered.**

### Common Mistakes in Interviews

- Implicit flow new SPA 2024
- ROPC for mobile login
- No PKCE public client

---

## Q036: PKCE for Mobile Apps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Why PKCE mandatory for mobile and SPA on Entra ID?

### Short Answer (30 seconds)

Public clients cannot store client secret. PKCE sends code_challenge with authorize request, code_verifier with token exchange — prevents authorization code interception.

### Detailed Answer (3–5 minutes)

**Architect mobile:** Use MSAL — PKCE automatic. Register redirect URI `msauth://` or app link. Broker auth via Authenticator/Company Portal for SSO.

**No secret in mobile binary — ever.

### Architecture Perspective

PKCE is non-negotiable for public clients.

### Follow-up Questions

1. **S256 vs plain? — S256 required — plain rejected.**
2. **Dynamic client registration? — Not typical Entra — manual app reg.**

### Common Mistakes in Interviews

- Embed client secret in Xamarin app
- Custom OAuth without PKCE
- Token cache unencrypted on device

---

## Q037: Token Lifetime Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Configure refresh and access token lifetime policies.

### Short Answer (30 seconds)

Configurable token lifetime policies (legacy) and continuous access evaluation for session. Default access token ~1 hour; refresh token sliding window.

### Detailed Answer (3–5 minutes)

**Architect:** Short access token + refresh for security. CA sign-in frequency enforces re-auth for sensitive apps.

**Session revocation:** CAE enables near-real-time token invalidation on user disable/risk.

### Architecture Perspective

Token lifetime balances UX and security.

### Follow-up Questions

1. **Refresh token max inactive? — 90 days default single tenant — document.**
2. **Configurable token lifetime retirement? — Moving to CA sign-in frequency.**

### Common Mistakes in Interviews

- Access token 24 hours for convenience
- No sign-in frequency on financial app
- Ignore token lifetime when user disabled

---

## Q038: Refresh Token Rotation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Refresh token rotation and reuse detection in Entra?

### Short Answer (30 seconds)

Single-page apps and native clients get rotating refresh tokens — each use issues new refresh token. Reuse of old token signals theft — revoke family.

### Detailed Answer (3–5 minutes)

**Architect:** MSAL handles rotation. Monitor `invalid_grant` spikes.

**Compromise response:** Revoke all refresh tokens for user + force password reset.

### Architecture Perspective

Rotation limits refresh token theft window.

### Follow-up Questions

1. **Family refresh tokens? — Entire chain invalidated on reuse detection.**
2. **Long-lived refresh without rotation awareness?**

### Common Mistakes in Interviews

- Custom token cache ignoring rotation
- No monitoring anomalous refresh patterns
- Store refresh token in secure storage not localStorage — XSS risk

---

## Q039: Secret vs Certificate Credentials

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

App registration credential strategy — secret or certificate?

### Short Answer (30 seconds)

Certificates preferred for prod SP — longer life, no plaintext secret. Secrets: max 2 years, rotate regularly, store Key Vault only.

### Detailed Answer (3–5 minutes)

**Architect policy:**
- Block secret creation via CA/App governance
- Federated credentials over cert where possible (CI/CD)
- Expiry alerts 30/60/90 days

**HSM:** Premium Key Vault for private key protection.

### Architecture Perspective

Credential type and storage define breach blast radius.

### Follow-up Questions

1. **Secret expiry notification? — App registration owners + automation.**
2. **Multiple active secrets? — Overlap during rotation only.**

### Common Mistakes in Interviews

- Never-rotated 5-year secret
- Secret in terraform state unencrypted
- Cert private key exportable to dev laptop

---

## Q040: Entra Permissions Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Occasional |

### Question

Use Entra Permissions Management for cloud access governance?

### Short Answer (30 seconds)

Discovers permissions across AWS/Azure/GCP (where integrated), right-sizing recommendations, access requests, segregation of duties policies.

### Detailed Answer (3–5 minutes)

**Architect:** Complements PIM — focuses permission analytics and least privilege at scale.

**Workflow:** Over-privileged identity alert → review → downgrade or PIM eligible.

### Architecture Perspective

Permissions Management extends governance beyond Azure RBAC alone.

### Follow-up Questions

1. **SoD policies? — Block toxic combinations (e.g., create VM + reset password).**
2. **Integration Sentinel? — Permission anomaly alerts.**

### Common Mistakes in Interviews

- Ignore over-permissioned SP reports
- No SoD for finance systems
- Manual access reviews only spreadsheets

---

## Q041: LDAP over TLS Hybrid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Secure LDAP (LDAPS) for apps connecting to Entra Domain Services.

### Short Answer (30 seconds)

Entra DS exposes LDAPS on port 636. Apps must trust Entra DS CA chain. Prefer LDAPS over plain LDAP — credentials encrypted.

### Detailed Answer (3–5 minutes)

**Architect:** Private Link to Entra DS VNet. No LDAP over internet. Certificate validation enforced in app config.

**Alternative:** Modernize app to OAuth instead of LDAP bind.

### Architecture Perspective

LDAPS is minimum for legacy directory auth.

### Follow-up Questions

1. **LDAPS vs StartTLS? — Entra DS documents 636 LDAPS.**
2. **Service account LDAP? — Dedicated account least privilege OU.**

### Common Mistakes in Interviews

- Plain LDAP port 389 prod
- LDAP bind account password never rotated
- LDAP app not in VNet with Entra DS

---

## Q042: Hybrid Azure AD Join

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Devices |
| **Frequency** | Common |

### Question

Hybrid Azure AD join vs Entra join for corporate devices?

### Short Answer (30 seconds)

Hybrid join: domain-joined PC synced to Entra via Connect — SSO to cloud apps. Entra join: cloud-first devices registered directly in Entra.

### Detailed Answer (3–5 minutes)

**Architect:**
- Hybrid: existing AD GPO investment, on-prem apps
- Entra join + Autopilot: modern provisioning

**CA:** Require hybrid OR Entra join for resource access.

### Architecture Perspective

Device identity enables device-based CA.

### Follow-up Questions

1. **Co-management Intune? — Hybrid join path to MDM.**
2. **Registration vs join? — Registration alone weaker — join preferred.**

### Common Mistakes in Interviews

- CA device compliance without join
- Hybrid join without Connect health monitoring
- Personal devices hybrid joined

---

## Q043: Continuous Access Evaluation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Implement Continuous Access Evaluation (CAE) in app architecture.

### Short Answer (30 seconds)

CAE-capable apps receive critical event notifications — user disabled, password changed, location change — revoke access in minutes not token TTL.

### Detailed Answer (3–5 minutes)

**Requirements:** MS Graph, Exchange, SharePoint support CAE; custom APIs must implement token validation + CAE protocol.

**Architect:** Enable CAE in MSAL apps. Pair with strict token lifetime and sign-in frequency for custom APIs.

### Architecture Perspective

CAE closes token revocation gap.

### Follow-up Questions

1. **CAE IP address validation? — Critical events on IP mismatch.**
2. **Fallback without CAE? — Standard token lifetime until expiry.**

### Common Mistakes in Interviews

- Assume disable user instant without CAE
- Custom API ignores token revocation events
- CAE not tested in DR user lockout

---

## Q044: Global Secure Access Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

What is Microsoft Global Secure Access (GSA)?

### Short Answer (30 seconds)

Converged SASE offering: Entra Internet Access (SWG) + Entra Private Access (ZTNA) replacing legacy Global Secure Access preview branding.

### Detailed Answer (3–5 minutes)

**Architect:** Entra ID-centric secure access — identity drives access not VPN perimeter.

**Components:** Quick Access apps, forwarding profile on devices, Conditional Access integration.

### Architecture Perspective

GSA is Microsoft's SSE/SASE identity story.

### Follow-up Questions

1. **GSA vs Azure VPN? — VPN perimeter vs identity-based ZTNA.**
2. **Client required? — Global Secure Access client on managed devices.**

### Common Mistakes in Interviews

- VPN only remote access strategy
- Ignore GSA for Zero Trust roadmap
- No CA integration with private access

---

## Q045: Entra Internet Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Entra Internet Access for secure web gateway?

### Short Answer (30 seconds)

Cloud SWG — traffic forwarded from device through Microsoft edge, URL filtering, TLS inspection policies, threat intelligence, integrated with Entra sign-in.

### Detailed Answer (3–5 minutes)

**Architect use cases:**
- Replace legacy proxy for remote workers
- Enforce web policy by Entra group
- Log internet access to Sentinel

**Deploy:** Client forwarding profile + CA requiring compliant device.

### Architecture Perspective

Internet Access is SWG leg of GSA.

### Follow-up Questions

1. **Breakout Office 365? — Bypass rules for optimized paths.**
2. **Third-party SWG coexistence? — Migration period dual stack.**

### Common Mistakes in Interviews

- No web filtering remote users
- TLS inspect without privacy review
- Policy not tied to identity groups

---

## Q046: Entra Private Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Entra Private Access vs traditional VPN for internal apps?

### Short Answer (30 seconds)

Private Access publishes internal apps via Quick Access — users connect through Microsoft ZTNA edge, no full network tunnel. Per-app authorization with Entra ID.

### Detailed Answer (3–5 minutes)

**Architect:** Replace VPN for SaaS-like internal web apps. Connector on-prem or Azure publishes app.

**Benefits:** No lateral movement on full tunnel, CA enforced per session.

### Architecture Perspective

Private Access is ZTNA for private apps.

### Follow-up Questions

1. **Connector HA? — Multiple connectors for resilience.**
2. **On-prem Active Directory apps? — Publish specific URLs not entire VLAN.**

### Common Mistakes in Interviews

- Full VPN for one internal dashboard
- Publish RDP to entire subnet
- No connector monitoring

---

## Q047: Identity Governance Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Design identity lifecycle from joiner to leaver.

### Short Answer (30 seconds)

Automated provisioning (HR-driven), access packages, access reviews, entitlement management, deprovisioning disables account + revokes tokens.

### Detailed Answer (3–5 minutes)

**Architect workflow:**
1. Joiner: Entra ID + group + app assignments via SCIM/Logic Apps
2. Mover: access review trigger role change
3. Leaver: disable account, revoke sessions, transfer ownership

**Target:** <4 hours leaver SLA for prod access removal.

### Architecture Perspective

Lifecycle automation prevents orphaned access.

### Follow-up Questions

1. **Guest leaver? — Same disable — often forgotten.**
2. **SCIM provisioning? — SaaS apps auto user sync.**

### Common Mistakes in Interviews

- Manual ticket for every new hire app access
- Disabled AD user still active Entra
- No leaver checklist

---

## Q048: Access Reviews Configuration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Configure Entra access reviews for group and app assignments.

### Short Answer (30 seconds)

Quarterly review of group membership, app role assignments, PIM activations. Self-review + manager or designated reviewer. Auto-apply remove if no response.

### Detailed Answer (3–5 minutes)

**Architect:**
- Reviews for privileged groups monthly
- Exclude break-glass with separate process
- Export results for audit

**Integration:** Defender Identity access review recommendations.

### Architecture Perspective

Access reviews prove least privilege over time.

### Follow-up Questions

1. **Recurring vs one-time? — Recurring for SOX cadence.**
2. **If reviewer absent? — Fallback reviewer configured.**

### Common Mistakes in Interviews

- Access reviews never auto-apply
- Privileged groups excluded from review
- Annual review only for admins

---

## Q049: Entitlement Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Use entitlement management access packages for project access.

### Short Answer (30 seconds)

Access package bundles groups, apps, SharePoint sites. Request workflow, approval, time-bound assignment, automatic expiration.

### Detailed Answer (3–5 minutes)

**Architect:** Catalog per department. External users via connected org B2B. Policies: max duration 90 days project access.

**vs PIM:** PIM for admin roles; entitlement management for business resource bundles.

### Architecture Perspective

Entitlement management is self-service governance with guardrails.

### Follow-up Questions

1. **Approval workflows? — Single or multi-stage + escalation.**
2. **Assignment customization? — Questions at request time.**

### Common Mistakes in Interviews

- Permanent project group membership
- Manual SharePoint permission grants
- No expiration on vendor package

---

## Q050: PIM Workflow and Audit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

End-to-end PIM activation workflow for production support?

### Short Answer (30 seconds)

Engineer eligible for `Contributor` on prod RG. Activation: MFA, ticket number, 4-hour window, optional approver. Work performed. Activation expires auto. Audit log to Log Analytics + Sentinel rule for after-hours activation.

### Detailed Answer (3–5 minutes)

**Architect:**
- No permanent active assignments prod
- Weekly PIM audit report
- Integration ServiceNow webhook for ticket validation (custom)

**Emergency:** Break-glass outside PIM with C-level approval path.

### Architecture Perspective

PIM workflow demonstrates operational maturity in interviews.

### Follow-up Questions

1. **PIM alerts Sentinel? — KQL on `Add member to role` PIM logs.**
2. **Audit export retention? — Align 7 years compliance.**

### Common Mistakes in Interviews

- PIM activated role never expires bug ignored
- Same person requester and approver
- PIM logs not monitored

---
