# Vercel KV + Admin Analytics — Setup Guide

Step-by-step documentation for connecting **Upstash for Redis** (Vercel’s KV storage) to the **ArchitectGuide** project, enabling the password-protected `/admin` analytics dashboard.

**Live site:** [architectguide.vercel.app](https://architectguide.vercel.app)  
**Admin dashboard:** [architectguide.vercel.app/admin](https://architectguide.vercel.app/admin)

See also: [admin-analytics.md](admin-analytics.md) for what is tracked and privacy notes.

---

## 1. Starting problem

The admin dashboard showed:

> **Vercel KV not connected**  
> Add a KV store in Vercel → Storage → Connect to project.

That warning appears when the API reports `kvReady: false`. The check lives in `api/lib/storage.ts`:

```ts
export function kvConfigured(): boolean {
  return Boolean(process.env.KV_REST_API_URL && process.env.KV_REST_API_TOKEN)
}
```

`ADMIN_PASSWORD` may already be set, but **without a linked KV store** events are dropped silently and the dashboard warns you.

---

## 2. Architecture

```
Browser (React SPA)
  │
  ├─ AnalyticsTracker ──POST──► /api/track ──► Upstash Redis (analytics:events list)
  │
  └─ AdminPage ──POST──► /api/admin/login
              └──GET───► /api/admin/stats ──► Upstash Redis
```

| Layer | Role |
|--------|------|
| Root `vercel.json` | Builds `site/dist`, rewrites `/api/*` to serverless functions, SPA fallback |
| Root `package.json` | `@vercel/kv`, `@vercel/node` for `/api` routes |
| `api/lib/storage.ts` | Redis list `analytics:events`, max 10,000 events |
| **Upstash for Redis** | Vercel marketplace integration (replaces legacy “Vercel KV” UI) |

**Deploy from the repo root**, not `site/` alone — API functions live at `/api`.

---

## 3. Vercel CLI access

We used the **Vercel CLI**, which authenticates with your stored login token (no manual bearer token unless using `vercel api` directly).

```bash
vercel whoami
# → websabre
```

### Link the project locally

```bash
cd /path/to/ArchitectGuide
vercel link --yes --project architectguide
```

This writes `.vercel/repo.json` with project and team IDs:

| Field | Example value |
|--------|----------------|
| Project ID | `prj_77obw2VYFWQUNEJZ56HK1D1vv2Ms` |
| Team ID | `team_IOgF14zsKprNxZygcjfB4N6s` |
| Team slug | `websabres-projects` |

After linking, `vercel env pull` syncs environment variables into `.env.local`.

---

## 4. Discovering storage options

Vercel no longer exposes a `vercel storage` CLI command. Storage is provisioned via **marketplace integrations**:

```bash
vercel integration discover kv
vercel integration discover redis
```

Relevant products:

| Product | Slug | Notes |
|---------|------|--------|
| **Upstash for Redis** | `upstash/upstash-kv` | Used for this project; sets `KV_REST_API_*` |
| **Redis (official)** | `redis` | Alternative; also requires marketplace terms |

Check existing resources:

```bash
vercel integration list architectguide
# Before setup: No resources found
```

---

## 5. Provisioning KV (CLI — recommended)

```bash
vercel integration add upstash/upstash-kv \
  -n architectguide-kv \
  -e production \
  -e preview
```

| Flag | Meaning |
|------|---------|
| `-n architectguide-kv` | Resource name in Vercel |
| `-e production -e preview` | Inject env vars into those environments |

**On success:**

1. Upstash Redis store `architectguide-kv` is provisioned
2. Store is connected to project `architectguide`
3. `vercel env pull` updates `.env.local`

Confirm:

```bash
vercel integration list architectguide
```

```
architectguide-kv  ● Available  Upstash for Redis  upstash-kv  architectguide
```

---

## 6. Environment variables (auto-injected)

```bash
vercel env ls
```

| Variable | Purpose |
|----------|---------|
| `KV_REST_API_URL` | Upstash REST endpoint — **required by our code** |
| `KV_REST_API_TOKEN` | Auth token — **required by our code** |
| `KV_REST_API_READ_ONLY_TOKEN` | Read-only token |
| `KV_URL` | Redis connection URL |
| `REDIS_URL` | Alternate Redis URL |
| `ADMIN_PASSWORD` | Admin login (set manually in project settings) |

`@vercel/kv` reads `KV_REST_API_URL` and `KV_REST_API_TOKEN` at runtime in serverless functions.

**Important:** Env vars exist on the project immediately, but **running deployments do not pick them up until you redeploy**.

### Set admin password (if not done)

```bash
vercel env add ADMIN_PASSWORD
# Select Production and Preview when prompted
```

Or: Vercel Dashboard → **architectguide** → **Settings** → **Environment Variables**.

---

## 7. Production redeploy

```bash
vercel --prod
```

Build flow (from `vercel.json`):

1. `npm ci` at repo root (API dependencies)
2. `cd site && npm ci` (frontend)
3. `site/scripts/prepare-site.mjs` — copy markdown + generate `navigation.json`
4. `vite build` → `site/dist`
5. Deploy `/api/*.ts` as serverless functions with KV env vars

---

## 8. Verification

### Track API (no auth)

```bash
curl -s -X POST "https://architectguide.vercel.app/api/track" \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test-setup","path":"/test-kv-connection","referrer":""}'
# → {"ok":true}
```

Note: if KV is missing, `appendEvent()` logs a warning and returns without throwing — track still returns `{"ok":true}`. Always **redeploy after connecting KV**.

### Admin dashboard

1. Open [architectguide.vercel.app/admin](https://architectguide.vercel.app/admin)
2. Sign in with `ADMIN_PASSWORD`
3. `kvReady: true` — amber “KV not connected” banner disappears
4. Browse the site — events appear in the live feed

---

## 9. Vercel REST API (optional / automation)

The CLI wraps `https://api.vercel.com`. For scripted provisioning **after** a marketplace installation exists:

```bash
vercel api list | rg -i "kv|redis|storage|integration"
```

Useful endpoints:

| Endpoint | Purpose |
|----------|---------|
| `POST /v1/storage/stores/integration/direct` | Create integration store |
| `POST /v1/integrations/installations/{icfg}/resources/{id}/connections` | Connect resource to project |
| `GET /v1/integrations/integration/{slug}/products/{product}/plans` | Billing plans |

### Example: create store (requires `icfg_*` installation ID)

```bash
vercel api /v1/storage/stores/integration/direct -X POST \
  -F slug=websabres-projects \
  -F name=architectguide-kv \
  -F integrationProductIdOrSlug=upstash-kv \
  -F integrationConfigurationId=icfg_XXXXX
```

You need a real `icfg_*` from an accepted marketplace installation.

### API errors encountered during exploration

| Attempt | Result |
|---------|--------|
| `GET /v1/integrations/configurations` | **404** — no installations yet |
| `GET .../upstash/products/upstash-kv/plans` | **404** — needs valid installation context |
| `POST .../integration/direct` with `integrationConfigurationId=upstash` | **400** — must match `^icfg_[a-zA-Z0-9]+$` |

**Takeaway:** use `vercel integration add` first; it creates the installation, provisions the store, connects the project, and pulls env vars in one flow.

### Inspect env vars locally

```bash
vercel env pull .env.vercel.tmp --environment=production --yes
# Delete the temp file after — it contains secrets
```

---

## 10. Exceptions and blockers

### A. Marketplace terms acceptance (main blocker)

First `vercel integration add` attempt returns:

```json
{
  "status": "action_required",
  "reason": "integration_terms_acceptance_required",
  "verification_uri": "https://vercel.com/websabres-projects/~/integrations/accept-terms/upstash?source=cli"
}
```

The CLI does **not** wait for browser acceptance in non-interactive mode.

**Fix:** open the verification URI in a browser where you are logged into Vercel:

```bash
open "https://vercel.com/websabres-projects/~/integrations/accept-terms/upstash?source=cli"
```

Accept Upstash marketplace terms, then retry:

```bash
vercel integration add upstash/upstash-kv \
  -n architectguide-kv \
  -e production \
  -e preview
```

The same blocker applies to `vercel integration add redis`.

### B. No `vercel storage` CLI

```text
Error: "storage" is not a valid target directory or subcommand.
```

Storage is managed through **marketplace integrations**, not a top-level `vercel storage` command.

### C. Earlier deploy issues (same project)

| Error | Cause | Fix |
|-------|--------|-----|
| `npm ci` failed on Vercel | No root `package-lock.json` | Added root lockfile |
| Thousands of git changes | Root `node_modules/` not gitignored | Fixed `.gitignore` |
| Week pages 404 | Missing SPA fallback | `BrowserRouter` + rewrites in `vercel.json` |

### D. `@vercel/kv` deprecation warning

Build log may show:

```text
npm warn deprecated @vercel/kv@3.0.0: Vercel KV is deprecated...
```

It still works with Upstash-injected `KV_*` env vars. Long-term migration: `@upstash/redis` with `Redis.fromEnv()` (supports both `KV_*` and `UPSTASH_REDIS_REST_*`).

### E. Silent event drop when KV is missing

If `KV_REST_API_URL` / `KV_REST_API_TOKEN` are unset, `appendEvent()` warns and returns — no HTTP 500. The admin UI exposes `kvReady` so you can see the problem.

---

## 11. Repeatable checklist

```bash
# 1. Auth + link
vercel whoami
vercel link --yes --project architectguide

# 2. Admin password (if not set)
vercel env add ADMIN_PASSWORD

# 3. Accept marketplace terms (one-time, in browser)
open "https://vercel.com/websabres-projects/~/integrations/accept-terms/upstash?source=cli"

# 4. Provision + connect KV
vercel integration add upstash/upstash-kv \
  -n architectguide-kv \
  -e production -e preview

# 5. Confirm
vercel integration list architectguide
vercel env ls

# 6. Redeploy (required)
vercel --prod

# 7. Smoke test
curl -X POST https://architectguide.vercel.app/api/track \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test","path":"/","referrer":""}'
```

---

## 12. API routes in production

| Route | File | Auth |
|-------|------|------|
| `POST /api/track` | `api/track.ts` | None (public) |
| `POST /api/admin/login` | `api/admin/login.ts` | `ADMIN_PASSWORD` |
| `GET /api/admin/stats` | `api/admin/stats.ts` | Bearer token from login |

Storage: Redis list key `analytics:events`, trimmed to 10,000 entries via `LPUSH` + `LTRIM`.

---

## 13. Local development

```bash
# From repo root — site + API
npx vercel dev
```

Pull env vars from Vercel:

```bash
vercel env pull .env.local
```

See `.env.example` for required variable names.

---

## 14. Summary

| Step | Tool | Outcome |
|------|------|---------|
| Identify gap | `vercel env ls`, `vercel integration list` | KV missing; `ADMIN_PASSWORD` may already exist |
| Discover product | `vercel integration discover kv` | `upstash/upstash-kv` |
| Blocked | CLI terms gate | Browser acceptance required |
| Unblock | `open` verification URL | Terms accepted |
| Provision | `vercel integration add upstash/upstash-kv` | Store + env vars + project link |
| Activate | `vercel --prod` | Functions receive KV credentials |
| Verify | `curl /api/track`, `/admin` login | Analytics live |

For first-time KV setup, **`vercel integration add`** plus browser terms acceptance is the practical path. Use the REST API (`POST /v1/storage/stores/integration/direct`) only when you already have an `icfg_*` installation ID for automation.
