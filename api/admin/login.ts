import type { VercelRequest, VercelResponse } from '@vercel/node'
import { loginValid } from '../lib/auth'
import { kvConfigured } from '../lib/storage'

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  if (!process.env.ADMIN_PASSWORD) {
    return res.status(503).json({ error: 'ADMIN_PASSWORD not configured on server' })
  }

  if (!loginValid(req.body)) {
    return res.status(401).json({ error: 'Invalid password' })
  }

  return res.status(200).json({
    token: process.env.ADMIN_PASSWORD,
    kvReady: kvConfigured(),
  })
}
