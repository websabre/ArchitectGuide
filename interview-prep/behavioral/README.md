# Behavioral Interview Preparation

## STAR Story Bank Template

Document 20+ stories before Week 50. Each story should demonstrate architect-level impact.

### Story Categories (aim for 3+ per category)

| Category | Example Prompt |
|----------|---------------|
| Technical leadership | "Tell me about a time you drove an architecture decision" |
| Conflict resolution | "Describe disagreeing with a tech lead" |
| Stakeholder management | "Explain a complex decision to non-technical executives" |
| Failure & learning | "Tell me about an architecture that didn't work" |
| Mentoring | "How have you grown senior developers into architects?" |
| Delivery under pressure | "Describe delivering under a tight deadline" |
| Cost optimization | "Tell me about reducing cloud costs" |
| Security incident | "Describe handling a security vulnerability" |

### Story Template

```markdown
## Story [N]: [Title]

**Category:** Technical Leadership
**Role level demonstrated:** Solution Architect

### Situation
[Business context — 2-3 sentences with scale/impact numbers]

### Task
[Your specific responsibility — what was expected of YOU]

### Action
[What YOU did — specific technical and leadership actions]
- Held architecture review with...
- Wrote ADR proposing...
- Prototyped two approaches and measured...

### Result
[Measurable outcome]
- Reduced latency by 40%
- Saved $120K/year in cloud costs
- Team adopted pattern across 5 services

### Architect Lessons
[What you'd do differently; what you learned]

### Follow-up Questions Ready
- "What alternatives did you consider?" → [Answer]
- "How did you handle pushback?" → [Answer]
```

---

## Sample Story: Architecture Migration

**Prompt:** "Tell me about a significant architecture decision you made."

**STAR Answer:**

**Situation:** At a fintech company, our payment monolith on .NET Framework was deploying monthly with 4-hour maintenance windows. The business needed daily releases for regulatory compliance.

**Task:** As the lead architect, I was asked to propose a migration strategy that enabled daily deployments without a 12-month rewrite.

**Action:** I proposed a strangler fig pattern. I wrote an ADR comparing big-bang rewrite vs incremental extraction. We identified the payment notification module — highest change frequency, clearest boundary. I designed an event-driven extraction using Azure Service Bus, created a parallel-run period with feature flags, and mentored two senior devs on the new service's Clean Architecture structure.

**Result:** Payment notifications extracted in 8 weeks. Deployment frequency went from monthly to daily for that module. Zero downtime during migration. The pattern was replicated for 3 more modules over the following year.

---

## Common Behavioral Questions for Architects

1. How do you handle disagreement with a principal engineer?
2. Describe a time you had to say "no" to a feature for architectural reasons.
3. How do you balance speed of delivery with architectural quality?
4. Tell me about influencing without authority.
5. How do you onboard a team to a new architecture pattern?
6. Describe your approach to technical debt prioritization.
7. How do you communicate architecture to C-level executives?
8. Tell me about a production incident you led the response for.
9. How do you evaluate build vs buy decisions?
10. Describe mentoring someone into an architect role.

---

## Practice Protocol

1. Write the story (use template above)
2. Practice aloud — 3 minutes max
3. Record yourself — check for jargon and clarity
4. Peer review with study group
5. Refine based on feedback

Target: **20 polished stories** by Week 50.
