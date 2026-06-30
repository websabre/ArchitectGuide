# Admin Analytics Setup

Password-protected dashboard at **`/admin`** on your deployed site.

**Full Vercel KV / Upstash setup guide (CLI, API, troubleshooting):** [vercel-kv-setup.md](vercel-kv-setup.md)

## 1. Storage (Upstash for Redis / KV)

Vercel’s legacy “KV” UI is replaced by the **Upstash for Redis** marketplace integration. Our code uses `@vercel/kv`, which reads `KV_REST_API_URL` and `KV_REST_API_TOKEN`.

### Option A — CLI (recommended)

```bash
vercel link --yes --project architectguide

# One-time: accept marketplace terms in browser if prompted
open "https://vercel.com/websabres-projects/~/integrations/accept-terms/upstash?source=cli"

vercel integration add upstash/upstash-kv \
  -n architectguide-kv \
  -e production -e preview

vercel --prod
```

### Option B — Dashboard

1. [Vercel Dashboard](https://vercel.com) → **architectguide** → **Storage** or **Integrations**
2. Add **Upstash for Redis** → connect to the project
3. Redeploy

Env vars `KV_REST_API_URL` and `KV_REST_API_TOKEN` are added automatically.

## 2. Admin password

**Settings → Environment Variables** → add:

| Name | Value |
|------|--------|
| `ADMIN_PASSWORD` | A strong secret (used for login + API auth) |

Or via CLI: `vercel env add ADMIN_PASSWORD`

Redeploy after adding or changing variables.

## 3. Access

Open: [https://architectguide.vercel.app/admin](https://architectguide.vercel.app/admin)

Sign in with `ADMIN_PASSWORD`.

## What is tracked

| Field | Source |
|-------|--------|
| Page path | Client route changes |
| Session ID | Anonymous UUID in `localStorage` |
| IP address | `x-forwarded-for` |
| City / country | Vercel geo headers (`x-vercel-ip-city`, etc.) |
| Referrer, user agent | Browser |
| Timestamp | Server |

Last **10,000** events kept in KV.

## Local development

```bash
# From repo root — runs site + API
npx vercel dev
```

Set `.env.local` with `ADMIN_PASSWORD` and KV vars, or pull from Vercel:

```bash
vercel env pull .env.local
```

See `.env.example` at repo root.

## Privacy

Inform visitors if required by your jurisdiction (GDPR, etc.). IP collection may need a privacy notice on the public site.
