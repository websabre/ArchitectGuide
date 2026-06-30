# Week 50 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Stakeholder Management Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

What are stakeholder management fundamentals every architect must master?

### Short Answer (30 seconds)

Identify all stakeholders, map power and interest, align work to business OKRs, communicate proactively, document decisions, and escalate with data when deadlocked. Architecture ships through people — not diagrams alone.

### Detailed Answer (3–5 minutes)

**Core fundamentals:**
1. **Discovery** — Who wins/loses from this change? Interview sponsors early
2. **Map** — Power/interest grid: manage closely, keep satisfied, consult, monitor
3. **Align** — Tie initiatives to company OKRs — not architecture preferences
4. **Engage** — Cadence per stakeholder type (weekly tech leads, biweekly sponsors)
5. **Decide transparently** — RACI + decision log; no back-channel surprises
6. **Escalate** — Present options with cost/risk when priorities conflict

**Stakeholder map example:**
| Stakeholder | Power | Interest | Strategy |
|-------------|-------|----------|----------|
| CTO | High | High | Manage closely |
| CFO | High | Low | Cost dashboard, brief updates |
| Team leads | Low | High | Consult on contracts |
| Legacy team | Medium | Low | Co-opt as migration leads |

**Artifacts:** Stakeholder map, RACI, decision log, steering deck.

**Architect trap:** Designing perfect solution that key sponsor never bought into.

### Architecture Perspective

Stakeholder fundamentals are prerequisite to every leadership scenario — neglect them and perfect architecture stalls.

### Follow-up Questions

1. **Sponsor vs champion? — Sponsor has budget authority; champion drives daily adoption.**
2. **Silent stakeholder risk? — Proactively engage neutrals — silence becomes veto at steering.**

### Common Mistakes in Interviews

- Designing without sponsor alignment
- Treating all stakeholders with same cadence
- No written decision record after conflict

---

## Q032: Conflict Resolution for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

What conflict resolution approaches should architects use when teams disagree on technical direction?

### Short Answer (30 seconds)

Separate people from problem, agree on decision criteria, timebox debate, use POC when needed, record ADR, escalate by deadline. Focus on requirements and data — not rank or volume of opinions.

### Detailed Answer (3–5 minutes)

**Resolution process:**
1. **Restate problem** — Shared understanding of business need and NFRs
2. **Criteria** — Latency, coupling, team skills, ops burden, cost — written list both sides accept
3. **Options** — At least two viable paths with honest trade-offs
4. **Evidence** — POC with success metrics (1 week max) or reference architecture precedent
5. **Decision** — ADR with rejected alternative and revisit trigger
6. **Commit** — Disagree and commit; assign ownership on chosen path

**Facilitation techniques:**
- Round-robin input before debate
- 'What would change your mind?' question
- Architecture board as tie-breaker with strategic lens

**People dimension:** Acknowledge contributions from both sides; 1:1 repair after heated sessions.

**When to escalate:** Deadline missed, compliance risk, or deadlock on criteria themselves.

### Architecture Perspective

Conflict resolution is core architect leadership — process beats charisma or seniority.

### Follow-up Questions

1. **Consensus vs consent? — Consent = no principled objection — faster at scale than full consensus.**
2. **Relationship repair? — Brief 1:1 after resolution — 'disagree and commit' ritual.**

### Common Mistakes in Interviews

- Defaulting to senior engineer's preference
- Endless debate without timebox or POC
- No ADR — same conflict repeats next quarter

---

## Q033: Influencing Without Authority

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How do architects influence autonomous teams without direct management authority?

### Short Answer (30 seconds)

Make the right path the easy path: golden paths, templates, pilot wins, champions, data on adoption, and executive air cover. Respect team autonomy — influence through value, not mandates.

### Detailed Answer (3–5 minutes)

**Influence levers:**
| Lever | Tactic |
|-------|--------|
| Ease | Secure CI template faster than rolling your own |
| Proof | Pilot team shows 80% CVE reduction — tell story |
| Data | Adoption % correlated with incident rate |
| Champions | Tech lead per tribe advocates standard |
| Air cover | CTO: 'expected default for new services' |

**Gradual adoption curve:**
```
Opt-in → Recommended → Required for new services only
```

**Avoid:** Email mandates from ivory tower; standards as PDF without tooling; shaming holdouts.

**Listen to resistance:** Often edge case reveals gap in standard — adapt before enforcing.

**When mandate is OK:** Regulatory audit finding, security incident, contractual obligation — pair with tooling enforcement.

### Architecture Perspective

Influence without authority defines architect role — platforms and proof beat policies.

### Follow-up Questions

1. **When escalate to mandate? — After opt-in fails and compliance risk is material.**
2. **Holdout team? — 1:1 to understand friction — fix template before forcing.**

### Common Mistakes in Interviews

- Standards email without golden path tooling
- Architecture team disconnected from stream pain
- Treating resistance as ignorance not signal

---

## Q034: Executive Communication Skills

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

What executive communication skills must architects develop beyond technical depth?

### Short Answer (30 seconds)

BLUF, business metrics first, one visual, risk honesty, clear ask, no jargon, rehearsed timing. Executives decide on outcomes, dollars, and dates — not container orchestration details.

### Detailed Answer (3–5 minutes)

**Skill checklist:**
1. **BLUF** — Bottom line up front in first 30 seconds
2. **Business language** — Revenue, risk, cost, time-to-market — not tech stack
3. **One diagram** — Simplified current → target; appendix for depth
4. **Status discipline** — Green/yellow/red with early yellow preferred
5. **Risks** — Top 2 with mitigations; no surprise bad news in Q&A
6. **Ask** — Specific decision, budget, or resource — every meeting
7. **Timing** — 10-minute slot means 8 minutes content + 2 buffer

**10-minute template:**
```
Headline → Progress (3 bullets) → Business impact → One diagram → Risks → Ask
```

**Preparation:** Rehearse aloud; anticipate cost, timeline, competitive questions.

**Common failure:** Technical deep dive unprompted — loses executive attention in 90 seconds.

### Architecture Perspective

Executive communication is a distinct skill — senior architects practice it deliberately.

### Follow-up Questions

1. **Managing up to technical CTO? — Lead with metrics and code-level credibility — still BLUF.**
2. **Board vs exec committee? — Board wants risk, audit, materiality — less operational detail.**

### Common Mistakes in Interviews

- Opening with acronyms and architecture patterns
- No ask at end of presentation
- Surprise bad news first time in exec forum

---

## Q035: Prioritization Frameworks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

What prioritization frameworks help architects rank competing initiatives with limited capacity?

### Short Answer (30 seconds)

WSJF, RICE, value/effort matrix, and OKR alignment — applied transparently with steering ratification. Architect owns the 'no' — document deferred items with reason.

### Detailed Answer (3–5 minutes)

**Framework comparison:**
| Framework | Formula / method | Best for |
|-----------|------------------|----------|
| WSJF | (BV + TC + RR) / Job size | SAFe / portfolio |
| RICE | Reach × Impact × Confidence / Effort | Product-style ranking |
| Value/Effort 2×2 | Plot initiatives | Quick visual triage |
| OKR tie-break | Align to company objectives | Executive deadlock |

**WSJF components:**
- **Business value** — Revenue, cost save, risk reduction
- **Time criticality** — Regulatory deadline, competitive window
- **Risk reduction** — Unblocks other work, reduces outage risk
- **Job size** — Engineering estimate in person-weeks

**Process:**
1. Inventory initiatives with one-line outcome
2. Collaborative scoring — avoid architect solo ranking
3. Fit top N into squad capacity
4. Publish ranked backlog; dissent documented
5. Revisit quarterly or when OKRs shift

**Say no explicitly:** Bottom items deferred with reason — prevents zombie priorities.

### Architecture Perspective

Prioritization frameworks show strategic discipline — transparent criteria beat HIPPO (highest paid person's opinion).

### Follow-up Questions

1. **Local vs global optimum? — Platform work ranks low locally — exec override may be needed.**
2. **Cost of delay? — WSJF time criticality captures regulatory deadlines.**

### Common Mistakes in Interviews

- 40 items all marked P0
- Architect scores alone without stakeholder input
- No re-prioritization cadence when context shifts

---

## Q036: Stakeholder Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How do you manage conflicting stakeholder priorities on a platform migration?

### Short Answer (30 seconds)

Map stakeholders, align to business OKRs, transparent prioritization framework, regular steering, document decisions. Escalate with data — not opinions.

### Detailed Answer (3–5 minutes)

**Approach:**
1. **Discover** — Interview sponsors; understand success metrics per VP
2. **Align** — Tie work to company OKRs; show trade-off matrix
3. **Prioritize** — RICE or WSJF in steering committee
4. **Communicate** — Weekly status; no surprises on delays
5. **Escalate** — When deadlock, present options with cost/risk to exec sponsor

**Example:** VP Sales wants CRM first; VP Ops wants inventory. OKR tie-break: revenue impact → CRM wave 1 with inventory read-only integration.

**Artifacts:** RACI, decision log, stakeholder map.

### Architecture Perspective

Stakeholder management separates architects who ship from those who diagram.

### Follow-up Questions

1. **Sponsor unavailable? — Identify delegate with decision authority.**
2. **Silent stakeholders? — Proactively engage — silence becomes veto later.**

### Common Mistakes in Interviews

- Pick favorites without transparent criteria
- Avoid conflict until too late
- No written decision record

---

## Q037: Managing Up

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Describe how you manage up to a CTO who is technically hands-on and skeptical of architecture overhead.

### Short Answer (30 seconds)

Earn trust with outcomes, speak their language, bring options not problems, respect their time, demonstrate ROI of architecture activities.

### Detailed Answer (3–5 minutes)

**Tactics:**
- **Lead with results** — 'Deploy time 4hr → 22min' before process talk
- **Brevity** — One-page exec summary; appendix for depth
- **Involve early** — Preview ADRs before review; no surprises
- **Speak code** — Reference concrete PRs and metrics they can verify
- **Align agenda** — Ask 'what keeps you up at night?' quarterly

**Avoid:** Jargon-heavy decks, blocking delivery for perfect architecture, going around them.

**Long-term:** Become trusted advisor on hard calls — they delegate more.

### Architecture Perspective

Managing up is trust-building — especially with technical executives.

### Follow-up Questions

1. **Disagree with CTO? — Disagree and commit once decided — or exit if ethical.**
2. **Skip-level risk? — Use carefully — only with transparency to direct manager.**

### Common Mistakes in Interviews

- Architecture theater without delivery impact
- Ambush in exec meeting with new proposal
- Ignore CTO's technical passion — feel patronized

---

## Q038: Conflict Resolution Tech

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Two senior engineers disagree on event-driven vs REST for integration. How do you resolve?

### Short Answer (30 seconds)

Facilitate decision process: requirements, POC criteria, timebox, ADR. Focus on criteria not personalities; escalate if no resolution by deadline.

### Detailed Answer (3–5 minutes)

**Steps:**
1. **Restate problem** — Integration needs: latency, coupling, team skills
2. **Criteria** — Document NFRs both agree on
3. **Options analysis** — Event: loose coupling, complexity. REST: simple, sync coupling
4. **POC** — 1-week spike with success metrics
5. **ADR** — Record decision, rejected alternative, revisit trigger

**If stuck:** Architecture board or eng director breaks tie using strategic fit.

**People:** Acknowledge both contributions; assign ownership on chosen path.

### Architecture Perspective

Technical conflict resolution uses process and data — not rank alone.

### Follow-up Questions

1. **Consensus vs consent? — Consent = no principled objection — faster at scale.**
2. **Relationship repair? — 1:1 after — 'disagree and commit' ritual.**

### Common Mistakes in Interviews

- Pick senior person's preference by default
- Endless debate without timebox
- No ADR — conflict repeats next quarter

---

## Q039: Influencing Without Authority

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How influence 12 autonomous product teams to adopt your security standards without mandating?

### Short Answer (30 seconds)

Build coalition, make easy path (templates), show wins, measure adoption, executive air cover, respect autonomy.

### Detailed Answer (3–5 minutes)

**Levers:**
- **Golden path** — Secure CI template faster than rolling own
- **Pilot success** — Team A reduced CVEs 80% — tell story
- **Data** — Dashboard: adoption % vs incident rate correlation
- **Champions** — Tech lead per tribe advocates
- **Air cover** — CTO message: 'expected default'

**Avoid:** Mandates without tooling; shame for non-adopters.

**Gradual:** Opt-in → recommended → required for new services only.

### Architecture Perspective

Influence without authority is core architect skill — platforms beat policies.

### Follow-up Questions

1. **When mandate? — Regulated industry, audit finding — then enforce with tooling.**
2. **Resistance source? — Listen — maybe standard doesn't fit edge case — adapt.**

### Common Mistakes in Interviews

- Email mandate from architecture ivory tower
- No templates — standards are PDF only
- Ignore feedback from holdout teams

---

## Q040: Executive Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How structure a 10-minute architecture update for executive committee?

### Short Answer (30 seconds)

BLUF (bottom line up front), business impact, one visual, risks, ask. Practice 10 min hard stop.

### Detailed Answer (3–5 minutes)

**Template:**
1. **Headline** — 'Checkout modernization on track; risk on payment cert delay'
2. **Progress** — 3 bullets vs milestones (green/yellow/red)
3. **Business impact** — Revenue enabled, outage risk reduced
4. **One diagram** — Current state → target (simplified)
5. **Risks & mitigations** — Top 2 only
6. **Ask** — Decision or resource needed

**Rules:** No acronyms; dollars and dates; rehearse aloud.

**Q&A prep:** Anticipate cost, timeline, competitive questions.

### Architecture Perspective

Executive communication is a distinct skill — practice timing and BLUF.

### Follow-up Questions

1. **Yellow status honesty? — Executives prefer early yellow over late red.**
2. **Visual clutter? — One diagram — appendix for depth.**

### Common Mistakes in Interviews

- Technical deep dive unprompted
- No ask — missed opportunity for decision
- Surprise bad news first time in exec forum

---

## Q041: Prioritization Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

What framework prioritize 40 architecture initiatives competing for 3 squad capacity?

### Short Answer (30 seconds)

WSJF or value/risk matrix aligned to OKRs. Transparent scoring, steering committee ratification, quarterly re-prioritization.

### Detailed Answer (3–5 minutes)

**WSJF:** (Business value + Time criticality + Risk reduction) / Job size

**Process:**
1. Inventory initiatives with one-line outcome
2. Score collaboratively — avoid architect solo scoring
3. Plot on 2×2: value vs effort — quick wins first for momentum
4. Capacity fit top 6 into 3 squads
5. Publish ranked backlog — dissent documented

**Revisit:** Quarterly or when OKRs shift.

**Say no:** Bottom 20 items explicitly deferred with reason.

### Architecture Perspective

Prioritization framework shows strategic discipline — architects own the 'no'.

### Follow-up Questions

1. **Local vs global optimum? — Platform work may rank low locally — exec override.**
2. **Cost of delay? — WSJF time criticality — regulatory deadline boosts score.**

### Common Mistakes in Interviews

- HIPPO prioritization (highest paid person)
- 40 items all P0
- No re-prioritization cadence

---

## Q042: Saying No to Features

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Product VP demands new feature requiring 3-month architecture detour. How say no constructively?

### Short Answer (30 seconds)

Acknowledge goal, explain cost/trade-off, offer alternatives, escalate with data if needed, document decision.

### Detailed Answer (3–5 minutes)

**Script:**
'I understand launch Q4 is critical. The requested custom cache breaks our standard and adds 3 months plus ongoing ops burden. Alternatives: (A) use platform Redis — 2 weeks, (B) defer to Q1 for custom — hit Q4 with A. Recommend A — here's risk comparison.'

**If insist:** Escalate to CTO with trade-off matrix — feature date vs platform integrity vs tech debt.

**Relationship:** Follow up 1:1 — stay partner not gatekeeper.

### Architecture Perspective

Saying no is offering better yes — alternatives required.

### Follow-up Questions

1. **When yes to detour? — Strategic differentiator with exec signed tech debt paydown.**
2. **Document 'no'? — ADR prevents relitigation.**

### Common Mistakes in Interviews

- Flat no without alternatives
- Passive yes then slow-walk
- Public no humiliating PM in meeting

---

## Q043: Technical Vision Articulation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How articulate 3-year technical vision that inspires engineers without being vague?

### Short Answer (30 seconds)

North star metaphor, capability milestones, principles, what we won't do, connect to product roadmap.

### Detailed Answer (3–5 minutes)

**Structure:**
1. **North star** — 'Every team deploys safely in 15 minutes'
2. **Why** — Customer speed + engineer satisfaction
3. **Capabilities** — Self-service platform, observable, secure by default
4. **Milestones** — Year 1 foundation, year 2 scale, year 3 optimize
5. **Anti-goals** — 'We won't microservice the monolith prematurely'
6. **Invitation** — How teams participate

**Delivery:** Tech all-hands with demo, not deck-only.

**Measure:** DORA metrics trend as vision scorecard.

### Architecture Perspective

Vision articulation balances aspiration and credibility — milestones ground it.

### Follow-up Questions

1. **Vision vs roadmap? — Vision stable years; roadmap quarterly.**
2. **Skeptical engineers? — Show quick win in 30 days post-announcement.**

### Common Mistakes in Interviews

- Buzzword vision without milestones
- Vision changes monthly
- No connection to product strategy

---

## Q044: Building Consensus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Eight teams must agree on API style guide. How build consensus?

### Short Answer (30 seconds)

Working group, draft RFC, comment period, pilot, ratify, automate enforcement in CI.

### Detailed Answer (3–5 minutes)

**Process:**
1. **Charter working group** — 1 rep per team, architect facilitates
2. **Baseline** — Industry standard (Zalando REST guidelines) as start
3. **RFC 2 weeks** — Async comments in Git
4. **Resolve** — Facilitate remaining disputes with decision matrix
5. **Pilot** — 2 teams adopt 1 month
6. **Ratify** — Architecture board approval
7. **Enforce** — Spectral/OpenAPI lint in CI — gentle then required

**Dissent:** Document minority opinion in ADR appendix.

### Architecture Perspective

Consensus is process design — not unanimous happiness.

### Follow-up Questions

1. **Veto rights? — Security and compliance retain veto on standards.**
2. **Stale standard? — Annual review RFC — living document.**

### Common Mistakes in Interviews

- Architect dictates standard in isolation
- No enforcement mechanism
- Endless RFC without decision deadline

---

## Q045: Cross-functional Leadership

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Lead cross-functional initiative: app, infra, security, data, legal for GDPR data deletion.

### Short Answer (30 seconds)

Single thread owner (you), weekly sync, RACI, shared milestone plan, exec sponsor, unified status report.

### Detailed Answer (3–5 minutes)

**RACI snapshot:**
| Task | App | Infra | Security | Legal |
|------|-----|-------|----------|-------|
| Delete API | R | C | C | I |
| Audit log | C | I | R | C |
| DPA review | I | I | C | R |

**Cadence:** Weekly 30 min standup; Slack channel; shared Confluence dashboard.

**Risks:** Legal delay — parallelize technical spike while DPA reviews.

**Success:** Right-to-erasure E2E in 30 days SLA — measured in prod.

### Architecture Perspective

Cross-functional leadership is program management with technical credibility.

### Follow-up Questions

1. **DRI vs committee? — One DRI — you — escalates blockers.**
2. **Remote cross-functional? — Over-communicate written status.**

### Common Mistakes in Interviews

- No single owner — diffusion of responsibility
- Skip legal until launch
- Teams work in silos without shared milestones

---

## Q046: Mentoring Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

How mentor two senior engineers transitioning to architect roles?

### Short Answer (30 seconds)

Individual development plan, shadow reviews, delegate decisions with feedback, reading list, safe-to-fail ownership.

### Detailed Answer (3–5 minutes)

**Plan per mentee:**
- **Strengths/gaps** — 360 or self-assessment
- **Goals** — Lead ADR in Q2; present at guild Q3
- **Activities** — Shadow architecture reviews; co-facilitate then solo
- **Feedback** — Biweekly 1:1; specific on communication gaps
- **Stretch** — Own integration design with you as backup

**Avoid:** Doing their work; only technical mentoring ignoring influence skills.

**Success:** Mentee leads review without you in room.

### Architecture Perspective

Mentoring architects develops organizational capacity — multiplier effect.

### Follow-up Questions

1. **Coach vs mentor? — Coach asks questions; mentor shares experience — blend both.**
2. **When mentee not ready? — Honest conversation — delay promo case.**

### Common Mistakes in Interviews

- Promote best coder without communication coaching
- No delegated ownership
- Mentorship without measurable goals

---

## Q047: Feedback Delivery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Give constructive feedback to peer architect whose designs consistently over-engineer.

### Short Answer (30 seconds)

SBI model (Situation-Behavior-Impact), private, specific examples, collaborative improvement plan.

### Detailed Answer (3–5 minutes)

**Example:**
'In last Tuesday's review (S), you proposed 5 new services for a feature needing one API extension (B). That added 6-week estimate and team pushed back (I). I'd like to pair on simpler options first — can we try constraint of max 1 new service unless ADR justifies?'

**Follow-up:** Offer to co-review their next design.

**Avoid:** Public criticism, personality labels ('you're a maximalist').

### Architecture Perspective

Feedback delivery skill signals emotional intelligence — senior interviews probe this.

### Follow-up Questions

1. **Receiving feedback? — Model openness when given feedback yourself.**
2. **Written feedback? — Follow verbal with email summary for clarity.**

### Common Mistakes in Interviews

- Vague 'you need to simplify'
- Public call-out in architecture review
- No offer to help improve

---

## Q048: Difficult Conversation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Need to tell VP their preferred vendor fails technical evaluation. Approach?

### Short Answer (30 seconds)

Prepare data, private meeting, acknowledge their input, present criteria-based result, offer path forward.

### Detailed Answer (3–5 minutes)

**Approach:**
1. **Pre-wire** — Share evaluation criteria before outcome
2. **Private** — 1:1 not group ambush
3. **Data** — Scorecard against agreed criteria
4. **Acknowledge** — 'I know you have relationship with Vendor X'
5. **Recommend** — Vendor Y with conditions
6. **Path** — Pilot option if they need more proof

**If override:** Document dissent; commit to making chosen option work — or exit if unethical.

**Tone:** Respectful, firm on facts.

### Architecture Perspective

Difficult conversations test courage and diplomacy — architects deliver bad news often.

### Follow-up Questions

1. **Written follow-up? — Email summary post-meeting for alignment.**
2. **Political fallout? — Engage exec sponsor as buffer if needed.**

### Common Mistakes in Interviews

- Blindsiding VP in steering committee
- Personal attack on vendor choice
- No objective criteria shared upfront

---

## Q049: Team Psychological Safety

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How foster psychological safety in architecture guild where juniors fear speaking up?

### Short Answer (30 seconds)

Model vulnerability, rotate facilitation, anonymous input channels, blameless postmortems, praise questions.

### Detailed Answer (3–5 minutes)

**Practices:**
- **Leader models** — 'I missed this risk in v1 — thanks for catching'
- **Round-robin** — Everyone speaks in reviews
- **Anonymous** — Pre-review async comments in doc
- **No interrupt** — Facilitator enforces
- **Celebrate learning** — Postmortem focuses system not person

**Measure:** Guild survey quarterly; track participation ratio.

**Architect role:** Senior voices dominate by default — actively invite juniors.

### Architecture Perspective

Psychological safety enables better architecture — silent room hides risks.

### Follow-up Questions

1. **Safety vs accountability? — Safe to raise mistakes; still accountable to fix.**
2. **Remote safety? — Cameras optional; chat questions welcomed.**

### Common Mistakes in Interviews

- Senior architects dominate every review
- Blame in incident reviews
- Dismiss 'dumb' questions publicly

---

## Q050: Leading Through Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

You are incident commander for SEV1 outage. Leadership behaviors in first 30 minutes?

### Short Answer (30 seconds)

Calm tone, clear roles, stakeholder comms cadence, avoid heroics, document timeline, support IC doing technical work.

### Detailed Answer (3–5 minutes)

**First 30 min:**
1. **Announce IC** — 'I'm IC; Maria tech lead; Tom comms'
2. **Severity confirm** — SEV1 criteria met
3. **Bridge etiquette** — Mute unless speaking; status every 10 min
4. **Comms** — Tom posts customer status page update
5. **No blame** — 'What do we know? What next?'
6. **Escalate resources** — Pull experts without ego

**Avoid:** IC debugging database while bridge chaos.

**After:** Thank team; schedule postmortem within 48hr.

### Architecture Perspective

Incident leadership is coordination — not being fastest debugger.

### Follow-up Questions

1. **IC rotation? — IC doesn't have to be deepest expert.**
2. **Customer comms? — Honest ETA ranges — under-promise.**

### Common Mistakes in Interviews

- IC deep in logs ignoring bridge
- Blame during active incident
- No comms role assigned

---

## Q051: Post-Incident Leadership

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Facilitate blameless postmortem for architect-visible systemic failure.

### Short Answer (30 seconds)

Timeline, root cause (5 whys), contributing factors, action items with owners, share widely, track to completion.

### Detailed Answer (3–5 minutes)

**Facilitation:**
- **Blameless ground rule** — Signed at start
- **Timeline** — UTC, facts only
- **Root cause** — Systemic: 'No load test gate on deploy pipeline'
- **Actions** — SMART: 'Add load test to CI by June 15 — Owner: Platform'
- **Publish** — Internal blog within 1 week

**Architect angle:** Link to ADR or principle gap.

**Follow-up:** Review action items in guild 30 days — no orphan actions.

### Architecture Perspective

Post-incident leadership turns pain into organizational learning.

### Follow-up Questions

1. **5 whys depth? — Stop at actionable system fix — not 'human error'.**
2. **Customer postmortem? — Separate external summary — careful wording.**

### Common Mistakes in Interviews

- Name individual as root cause
- Actions without owners
- Postmortem not shared — lesson lost

---

## Q052: Budget Justification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Justify $500K architecture platform budget to CFO.

### Short Answer (30 seconds)

ROI, TCO comparison, risk cost avoidance, phased spend, benchmarks, align to financial metrics.

### Detailed Answer (3–5 minutes)

**Case:**
- **Spend** — $500K (6 FTE + tooling)
- **Save** — $300K/yr license consolidation + $400K/yr engineer time (deploy automation)
- **Avoid** — $2M outage risk (historical 2 SEV1 × $1M)
- **Payback** — 9 months

**Phasing:** $200K Q1 pilot proving metrics; $300K Q2–Q4 scale.

**CFO language:** NPV, payback, opex vs capex treatment.

**Risk of not funding:** Competitor velocity; talent retention (developer experience).

### Architecture Perspective

Budget justification speaks finance — architects need ROI fluency.

### Follow-up Questions

1. **Intangible benefits? — Label assumptions; don't mix with hard savings.**
2. **Underspend credibility? — Track actuals vs forecast quarterly.**

### Common Mistakes in Interviews

- Technical features list without dollars
- ROI without baseline measurement
- All upfront spend — no milestone gates

---

## Q053: Hiring Senior Engineers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Design interview loop for senior platform engineer reporting to you.

### Short Answer (30 seconds)

Structured rubric: system design, coding (practical), architecture trade-offs, collaboration, values. Diverse panel; avoid trivia.

### Detailed Answer (3–5 minutes)

**Loop:**
1. **Recruiter screen** — Scope, comp alignment
2. **Hiring manager** — Leadership, motivation (45 min)
3. **System design** — Platform problem: CI/CD or K8s (60 min)
4. **Coding** — Realistic script or API task (60 min)
5. **Architecture discussion** — Review their past ADR (45 min)
6. **Values/collaboration** — Cross-functional scenario (30 min)

**Rubric:** Strong hire = independent design + clear communication + culture add.

**Debrief:** Calibrated scores; no single veto without evidence.

### Architecture Perspective

Hiring loop design shows leadership maturity — rubric over gut.

### Follow-up Questions

1. **Bar raiser? — Senior architect outside team for calibration.**
2. **Career level? — Same loop signals adjusted rubric for senior vs staff.**

### Common Mistakes in Interviews

- Leetcode hard as filter for platform role
- No architecture discussion
- Homogeneous panel bias

---

## Q054: Performance Review Architect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Write performance review themes for architect who excels technically but weak stakeholder communication.

### Short Answer (30 seconds)

Balanced: specific strengths, measurable improvement areas, examples, development plan, no surprises.

### Detailed Answer (3–5 minutes)

**Review structure:**
- **Strengths** — 'Led payment ADR adopted org-wide; reduced integration defects 40%'
- **Growth area** — 'Steering committee feedback: updates too detailed; missed exec ask on Q3'
- **Examples** — Feb board deck; May escalation delay
- **Plan** — Exec comms coaching; shadow you on 3 presentations
- **Goals** — Next quarter: lead initiative with documented stakeholder sign-off

**Rating:** Meets on tech; developing on leadership — overall meets with growth plan.

**No surprises** — Feedback given realtime through year.

### Architecture Perspective

Performance reviews for architects weight influence not just technical depth.

### Follow-up Questions

1. **PIP threshold? — PIP only after clear documented coaching — rare for architects.**
2. **Self-review alignment? — Compare self vs manager before final.**

### Common Mistakes in Interviews

- Vague 'communicate better'
- Surprise negative rating
- Technical-only evaluation ignoring leadership

---

## Q055: Delegation Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

How delegate architecture decisions across team without becoming bottleneck?

### Short Answer (30 seconds)

Decision rights matrix, delegate ADRs by domain, review not author, coaching on close calls.

### Detailed Answer (3–5 minutes)

**RACI for decisions:**
| Decision type | Responsible | Accountable |
|---------------|-------------|-------------|
| Tier-3 service design | Team architect | You inform |
| Tier-1 payment change | You | You |
| Style guide exception | Delegate | You approve |

**Practices:**
- **Template ADRs** — Consistent quality
- **Office hours** — 2hr/week for questions
- **Async review** — 48hr SLA on delegated ADRs

**Avoid:** Rubber stamp without reading; reverse delegation ('you decide but tell me first').

### Architecture Perspective

Delegation scales architecture practice — matrix clarifies autonomy.

### Follow-up Questions

1. **Delegate vs abdicate? — You remain accountable — spot-check quality.**
2. **New delegate? — First 3 ADRs paired review.**

### Common Mistakes in Interviews

- Approve everything personally
- Delegate without context or standards
- Blame delegate when decision fails publicly

---

## Q056: RACI for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How use RACI when architects lead cross-team initiatives?

### Short Answer (30 seconds)

Architect Accountable for design quality; teams Responsible for implementation; Consulted early; Informed via steering — document in decision log.

### Detailed Answer (3–5 minutes)

**Example RACI:**
| Activity | Architect | Stream teams | Security | PM |
|----------|-----------|--------------|----------|----|
| ADR | A/R | C | C | I |
| Implementation | C | R | C | I |
| Launch gate | A | R | R | C |

**Rules:** One A per row; avoid all C.

**Update:** RACI lives with initiative charter.

### Architecture Perspective

RACI clarifies architect accountability without owning all execution.

### Follow-up Questions

1. **Responsible vs Accountable? — R does work; A answers for outcome.**
2. **RACI stale? — Review each phase gate.**

### Common Mistakes in Interviews

- Architect R on every row
- No single Accountable per decision
- RACI never shared with teams

---

## Q057: Managing Up BLUF

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Write a one-paragraph managing-up update to a skeptical CTO.

### Short Answer (30 seconds)

BLUF outcome, metric proof, one risk, one ask — respect their time; attach depth only if requested.

### Detailed Answer (3–5 minutes)

**Example:**
'Checkout modernization is on track for M2 (June 15): deploy time 4hr→22min across 3 pilot teams. Risk: payment cert renewal may slip 1 week — mitigation owner Maria. Ask: approve 2 platform engineers through Q3 to hit 50% adoption.'

**Rules:** Verifiable metrics; no jargon; honest yellow.

### Architecture Perspective

Managing up is concise credibility building with technical executives.

### Follow-up Questions

1. **Weekly vs ad hoc? — Regular rhythm prevents surprise escalations.**
2. **Bad news timing? — Early in 1:1 not Friday exec email.**

### Common Mistakes in Interviews

- Three-page essay update
- Bury bad news at bottom
- No specific ask

---

## Q058: Facilitation Techniques

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

What facilitation techniques help architects resolve technical conflict?

### Short Answer (30 seconds)

Round-robin input, 'what would change your mind?', silent brainstorming, dot voting, timeboxed POC criteria.

### Detailed Answer (3–5 minutes)

**Techniques:**
| Technique | When |
|-----------|------|
| Round-robin | Equal airtime |
| Dot voting | Many options |
| Silent brainstorm | Senior voices dominate |
| Pre-mortem | Risk identification |
| Decision matrix | Objective criteria agreed |

**Facilitator:** Architect stays neutral on outcome until decision point.

### Architecture Perspective

Facilitation separates architect from loudest engineer in room.

### Follow-up Questions

1. **Parking lot? — Capture tangents without losing agenda.**
2. **Timebox? — 45 min decision meeting hard stop.**

### Common Mistakes in Interviews

- Debate until loudest wins
- No written criteria before debate
- Facilitator advocates own design throughout

---

## Q059: Coalition Building Steps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Steps to build coalition for org-wide architecture standard without mandate?

### Short Answer (30 seconds)

Find pain, recruit champions, pilot win, publish metrics, expand opt-in, exec air cover, phased enforcement for new work only.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Interview teams — find shared pain (CVEs, deploy time)
2. Recruit 2 champions from respected squads
3. Pilot golden path — measure DORA delta
4. Internal case study blog
5. CTO message: recommended default
6. CI lint required for new repos only

**Timeline:** 6 months influence → adoption.

### Architecture Perspective

Coalition building is influence playbook for staff architects.

### Follow-up Questions

1. **Holdout team? — Listen — adapt standard if valid edge case.**
2. **Mandate timing? — After 50% voluntary adoption usually.**

### Common Mistakes in Interviews

- Email mandate day one
- No pilot before org-wide push
- Champions unpaid extra work forever

---

## Q060: Executive Ask Crafting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

How craft a specific executive ask at end of architecture presentation?

### Short Answer (30 seconds)

One decision, dollar amount or headcount, deadline, consequence of no decision, alternative if rejected.

### Detailed Answer (3–5 minutes)

**Template:**
'Ask: Approve $400K Q3 platform budget and 2 FTE by Friday so we hit Black Friday readiness. Without it, checkout scale test fails — 30% outage risk per risk register.'

**Avoid:** Vague 'support needed'.

**Prep:** Pre-wire finance on numbers.

### Architecture Perspective

Specific asks get decisions — vague asks get nod-and-forget.

### Follow-up Questions

1. **Multiple asks? — Max two — prioritized.**
2. **Pre-wire? — Share ask with sponsor 48h before meeting.**

### Common Mistakes in Interviews

- No ask at end
- Ask without dollar or headcount
- Five competing asks in one meeting

---

## Q061: WSJF for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Apply WSJF to rank architecture initiatives with steering committee.

### Short Answer (30 seconds)

Score business value, time criticality, risk reduction; divide by job size; transparent spreadsheet; dissent recorded.

### Detailed Answer (3–5 minutes)

**WSJF = (BV + TC + RR) / Job size**

**Example:**
| Initiative | BV | TC | RR | Size | WSJF |
|------------|----|----|-----|------|------|
| Identity std | 8 | 9 | 7 | 13 | 1.85 |
| Observability | 7 | 6 | 8 | 8 | 2.63 |

**Process:** Committee scores together — not architect alone.

**Output:** Ranked backlog published.

### Architecture Perspective

WSJF makes prioritization discussable with executives.

### Follow-up Questions

1. **Job size estimate? — T-shirt then refine top items.**
2. **Local optimum? — Platform work may need exec override.**

### Common Mistakes in Interviews

- Architect scores alone
- All items same priority
- No job size denominator

---

## Q062: Saying No Scripts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Give three scripts for saying no to architecture scope creep.

### Short Answer (30 seconds)

Acknowledge goal, state trade-off, offer alternatives, escalate with matrix if needed — partner tone not gatekeeper.

### Detailed Answer (3–5 minutes)

**Scripts:**
1. **Defer:** 'Valid goal — not in Q3 capacity. Queue for WSJF scoring next steering.'
2. **Alternative:** 'Custom cache 3 months — platform Redis 2 weeks meets launch.'
3. **Escalate:** 'If Q4 launch mandatory, here's risk acceptance doc for CTO.'

**Tone:** Curious partner — 'help me understand constraint.'

### Architecture Perspective

Saying no scripts keep relationships while protecting integrity.

### Follow-up Questions

1. **Written no? — ADR prevents relitigation next quarter.**
2. **When yes to creep? — Exec-signed strategic bet with debt paydown.**

### Common Mistakes in Interviews

- Flat no in public meeting
- Passive yes then slow-walk
- No alternatives offered

---

## Q063: Vision Storytelling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

How tell technical vision as a story engineers remember?

### Short Answer (30 seconds)

Before/after protagonist (developer), conflict (deploy fear), resolution (golden path), demo not deck-only.

### Detailed Answer (3–5 minutes)

**Story arc:**
'Remember 4-hour deploy Fridays? We lost entire weekends. North star: deploy at 2pm Friday with confidence. Here's Maria demoing 12-minute deploy yesterday.'

**Elements:** Real names, real metrics, emotional hook, call to action.

**All-hands:** Live demo > 40 slides.

### Architecture Perspective

Vision storytelling complements milestone roadmaps for inspiration.

### Follow-up Questions

1. **Customer in story? — Tie engineer pain to customer outage impact.**
2. **Repeat vision? — Quarterly — consistency builds memory.**

### Common Mistakes in Interviews

- Buzzword vision deck only
- No demo or proof point
- Vision changes every month

---

## Q064: Consent vs Consensus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Explain consent-based decision making for architecture standards.

### Short Answer (30 seconds)

Consent = no principled objection — not everyone loves it. Faster than unanimous consensus at scale.

### Detailed Answer (3–5 minutes)

**Process:**
1. Present proposal with objection criteria
2. Round: 'Principled objections only?'
3. Integrate valid objections — revise
4. Second round — consent or escalate

**Document:** Dissenting view in ADR appendix.

**vs Consensus:** Unanimous enthusiasm rare at 15 teams.

### Architecture Perspective

Consent models show mature governance for large orgs.

### Follow-up Questions

1. **Principled objection? — Must cite criteria violation — not preference.**
2. **Escalate when? — Objection on compliance/safety — arch board decides.**

### Common Mistakes in Interviews

- Require unanimous enthusiasm
- Veto without principled reason
- No dissent documentation

---

## Q065: Cross-functional DRI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Role of single DRI in cross-functional architecture programs.

### Short Answer (30 seconds)

One throat to choke for delivery; DRI coordinates, escalates blockers, owns status — not doing all technical work.

### Detailed Answer (3–5 minutes)

**DRI responsibilities:**
- Unified milestone plan
- Weekly status to sponsor
- Escalation within 24hr of blocker
- RACI clarity
- Decision log maintenance

**Not DRI job:** Write all code, all ADRs alone.

**Architect as DRI:** Common for compliance, migration, platform launches.

### Architecture Perspective

DRI model prevents diffusion of responsibility in cross-functional work.

### Follow-up Questions

1. **Co-DRI? — Avoid — splits accountability.**
2. **DRI rotation? — Per phase OK — handoff doc required.**

### Common Mistakes in Interviews

- Committee ownership
- DRI does all technical work
- No escalation when blocked

---

## Q066: Mentoring IDP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Create individual development plan for engineer → architect transition.

### Short Answer (30 seconds)

Strengths/gaps assessment, quarterly goals, shadowing, delegated ownership, communication coaching, promotion evidence.

### Detailed Answer (3–5 minutes)

**IDP template:**
| Quarter | Goal | Activity | Evidence |
|---------|------|----------|----------|
| Q1 | ADR authorship | Co-write 2 ADRs | Merged ADRs |
| Q2 | Facilitation | Lead guild session | Recording |
| Q3 | Exec comms | Present steering | Feedback |
| Q4 | Solo review | Tier-2 review lead | Sign-off |

**Biweekly 1:1:** Track IDP not just status.

### Architecture Perspective

IDP shows structured mentoring beyond ad hoc advice.

### Follow-up Questions

1. **Promotion case? — IDP evidence feeds calibration doc.**
2. **Not ready? — Honest conversation — delay with plan.**

### Common Mistakes in Interviews

- Promote best coder without IDP
- No delegated ownership
- Only technical goals in IDP

---

## Q067: SBI Feedback Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Apply SBI feedback model to peer architect over-engineering.

### Short Answer (30 seconds)

Situation-Behavior-Impact privately; specific; collaborative improvement plan.

### Detailed Answer (3–5 minutes)

**SBI example:**
'In Tuesday review (S), you proposed 5 services for one API extension (B), adding 6 weeks and team pushback (I). Can we pair on max-1-new-service constraint next design?'

**Follow-up:** Co-review next RFC.

**Avoid:** Labels ('maximalist') and public criticism.

### Architecture Perspective

SBI is interview-ready framework for feedback questions.

### Follow-up Questions

1. **Receive feedback? — Model openness when given SBI yourself.**
2. **Written summary? — Email after verbal for alignment.**

### Common Mistakes in Interviews

- Vague you need to simplify
- Public call-out in review
- No offer to help improve

---

## Q068: Pre-wire Difficult News

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Pre-wire difficult conversation with VP before steering committee.

### Short Answer (30 seconds)

Share criteria and outcome 48h early; private 1:1; acknowledge relationship; offer pilot if needed; never blindside in group.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Schedule 1:1 before group meeting
2. Share evaluation criteria used
3. Deliver outcome with data
4. Offer path (pilot, revisit)
5. Confirm group meeting approach together

**If angry:** Pause — schedule follow-up — don't debate in hallway.

### Architecture Perspective

Pre-wire preserves relationships on bad news delivery.

### Follow-up Questions

1. **Email pre-read? — Data pack before conversation.**
2. **Political ally? — Engage exec sponsor as buffer if high stakes.**

### Common Mistakes in Interviews

- Blindsiding VP in steering
- Personal attack on preference
- No objective criteria shared

---

## Q069: Psych Safety Survey

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Measure psychological safety in architecture guild quarterly.

### Short Answer (30 seconds)

Anonymous survey 5 questions, participation ratio, act on results publicly, track trend.

### Detailed Answer (3–5 minutes)

**Sample questions:**
1. I can raise concerns without retaliation
2. Mistakes are discussed blamelessly
3. Juniors are heard in reviews
4. I understand decision rationale
5. I would recommend guild to peers

**Act:** Share top action item from results next guild.

**Trend:** Quarter over quarter comparison.

### Architecture Perspective

Measuring safety shows commitment beyond platitudes.

### Follow-up Questions

1. **Low score action? — Facilitation training, rotate leads.**
2. **Anonymous channel? — Async RFC comments option.**

### Common Mistakes in Interviews

- Survey without acting on results
- Senior domination unchecked
- Blame in postmortems

---

## Q070: Incident Comms Cadence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Set stakeholder communication cadence during SEV1 as incident leader.

### Short Answer (30 seconds)

Customer status page 30 min; internal exec 60 min; engineering bridge 10 min; single comms DRI — no conflicting messages.

### Detailed Answer (3–5 minutes)

**Cadence table:**
| Audience | Channel | Frequency | Owner |
|----------|---------|-----------|-------|
| Customers | Status page | 30 min | Comms DRI |
| Exec | Email/slack | 60 min | IC or delegate |
| Engineering | Bridge | 10 min | IC |

**Message:** Facts, impact, ETA range, next update time.

**Avoid:** Multiple leaders giving different ETAs.

### Architecture Perspective

Incident comms cadence is architect IC leadership staple.

### Follow-up Questions

1. **ETA honesty? — Under-promise range — update if slips.**
2. **All-clear message? — Confirm resolution + monitoring period.**

### Common Mistakes in Interviews

- IC gives customer updates while debugging
- No comms DRI assigned
- Conflicting ETAs from leaders

---
