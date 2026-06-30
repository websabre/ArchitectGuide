# Week 50 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Remote Team Leadership

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Lead distributed architecture team across US, EU, APAC. Practices?

### Short Answer (30 seconds)

Overlap hours, async-first docs, recorded sessions, inclusive meetings, intentional social, clear written decisions.

### Detailed Answer (3–5 minutes)

**Practices:**
- **Handbook** — Architecture decisions in Git not hallway
- **Overlap** — 2hr EU-US daily; APAC async review
- **Meetings** — Rotate time zones; record; agenda 24hr ahead
- **Whiteboard** — Miro persistent; not ephemeral
- **1:1s** — Biweekly each direct
- **On-site** — Quarterly 2-day summit for relationship

**Inclusion:** Don't schedule critical decisions only at US morning.

### Architecture Perspective

Remote leadership requires documentation discipline — architects should excel here.

### Follow-up Questions

1. **Async RFC default? — 48hr comment window before sync decision.**
2. **Timezone fairness? — Track meeting load per zone quarterly.**

### Common Mistakes in Interviews

- Hallway decisions excluding remote
- Always-on video culture causing burnout
- No written record of architecture decisions

---

## Q072: Vendor Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Manage strategic relationship with cloud vendor during contract renewal.

### Short Answer (30 seconds)

Multi-year TCO model, competitive leverage, SLA credits, escalation contacts, technical account team engagement.

### Detailed Answer (3–5 minutes)

**Renewal playbook:**
1. **Usage audit** — Right-size commitments; reserved vs on-demand
2. **Benchmark** — AWS/GCP quote for leverage (even if staying)
3. **SLA review** — Historical credits owed?
4. **Roadmap alignment** — Features you need on vendor roadmap
5. **Negotiate** — EDP discount, training credits, support tier
6. **Relationship** — Quarterly QBR with TAM

**Architect role:** Technical validation of vendor commitments; not sole negotiator.

### Architecture Perspective

Vendor management blends technical and commercial — architects inform TCO.

### Follow-up Questions

1. **Multi-cloud threat credible? — Need real workload portability assessment.**
2. **Lock-in acceptable? — Sometimes — document as conscious ADR.**

### Common Mistakes in Interviews

- Renew without usage analysis
- Ignore SLA breach history in negotiation
- Architect signs commercial terms alone

---

## Q073: Negotiation Skills

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Negotiate deadline extension for architecture review blocking product launch.

### Short Answer (30 seconds)

Understand interests, trade offers, document scope reduction, escalate with options, preserve relationship.

### Detailed Answer (3–5 minutes)

**Preparation:**
- **Their interest** — Launch date for revenue
- **Your interest** — Security/compliance gate
- **Options:**
  A) Launch with feature flag limited scope — full review parallel
  B) Delay 2 weeks — complete review
  C) Phased launch geography — US after review, EU week later

**Negotiate:** Offer A with signed risk acceptance from exec if review finds P2 only.

**BATNA:** They launch without you — reputational risk for both — avoid stating hostile.

### Architecture Perspective

Negotiation is interest-based problem solving — architects trade scope and time.

### Follow-up Questions

1. **Principal negotiation? — Separate people from problem; objective criteria.**
2. **Document agreement? — Email recap — scope, risk owner, review date.**

### Common Mistakes in Interviews

- Binary ultimatum without options
- Capitulate on security for friendship
- Negotiate in public Slack channel

---

## Q074: Career Growth Architect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

How plan career growth from senior to principal architect over 2 years?

### Short Answer (30 seconds)

Scope expansion, organizational impact, external visibility, competency gaps, sponsor, measurable milestones.

### Detailed Answer (3–5 minutes)

**Dimensions:**
- **Scope** — Team → domain → enterprise
- **Impact** — Measurable outcomes (DORA, cost, revenue enablement)
- **Influence** — Exec trust, cross-org initiatives
- **Technical depth** — T-shaped; 1–2 specialties

**2-year plan:**
- Y1: Lead tier-1 program; mentor 2 architects; speak internally
- Y2: Architecture board member; industry talk; principal promotion case

**Sponsor:** VP Eng advocates in calibration.

**Evidence:** Promotion doc with STAR stories and metrics.

### Architecture Perspective

Career growth planning shows self-awareness — interviewers ask 'where in 3 years?'

### Follow-up Questions

1. **Principal vs staff? — Company-specific — map rubric early.**
2. **IC track commitment? — Explicit — avoid ambiguous management pressure.**

### Common Mistakes in Interviews

- Promotion by tenure not impact
- No sponsor relationship
- Only technical growth ignoring influence

---

## Q075: Leadership STAR Stories

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Prepare STAR story demonstrating architecture leadership for director-level interview.

### Short Answer (30 seconds)

Structure Situation, Task, Action, Result with metrics. 2-minute delivery; authentic; shows influence and trade-offs.

### Detailed Answer (3–5 minutes)

**Example prompt:** 'Tell me about driving architectural change.'

**STAR:**
- **S** — Monolith deploy blocking 12 teams; 3 outages/quarter
- **T** — Lead extraction of payment service without revenue impact
- **A** — Strangler plan, coalition with 4 leads, ADR series, weekly steering, load test gate
- **R** — Deploy 4hr→18min; outages 3→0 in 2 quarters; adopted as golden path

**Tips:** Use 'I' for your actions; credit team; quantify; 2 min then pause for follow-up.

**Bank:** Prepare 8 stories covering conflict, failure, influence, technical depth.

### Architecture Perspective

Leadership STAR stories are interview currency — rehearse aloud with timer.

### Follow-up Questions

1. **Weak result? — Still share if learning clear — failure story variant.**
2. **Overlong STAR? — Director level wants brevity — details on request.**

### Common Mistakes in Interviews

- Team 'we' only — unclear your role
- No metrics in result
- Fabricated story — follow-ups expose

---

## Q076: Stakeholder Pre-mortem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Run stakeholder pre-mortem before major platform launch.

### Short Answer (30 seconds)

Imagine launch failed — enumerate reasons; mitigate top 5; assign owners; update risk register.

### Detailed Answer (3–5 minutes)

**Workshop (60 min):**
1. 'Launch failed spectacularly — why?' silent brainstorm
2. Cluster themes: adoption, perf, security, comms
3. Top 5 mitigations with owners
4. Link to launch checklist

**Include:** Skeptical stakeholders — their fears are data.

### Architecture Perspective

Pre-mortem is advanced stakeholder risk management.

### Follow-up Questions

1. **Post-launch pre-mortem? — Retrospective compares predicted vs actual.**
2. **Remote pre-mortem? — Miro + anonymous sticky notes.**

### Common Mistakes in Interviews

- Only architects in room
- Findings not tracked
- Skip skeptical voices

---

## Q077: Managing Up During Crisis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Manage up to CEO during week-long SEV1 program outage.

### Short Answer (30 seconds)

Daily BLUF, business impact $, customer count, ETA range, no jargon, don't hide uncertainty, single spokesperson.

### Detailed Answer (3–5 minutes)

**Daily CEO brief:**
1. Status color
2. Customers/revenue impacted
3. Root cause progress (plain language)
4. ETA range with confidence
5. What we need from CEO (usually nothing)

**Rules:** Same time daily; no surprise in board meeting.

**Architect role:** Technical accuracy behind comms DRI.

### Architecture Perspective

Crisis managing up tests composure and translation under pressure.

### Follow-up Questions

1. **Overpromise ETA? — Damages trust worse than honest range.**
2. **CEO in bridge? — Usually counterproductive — exec summary only.**

### Common Mistakes in Interviews

- Technical jargon to CEO daily
- Different story than customer status
- Hide worsening status

---

## Q078: Mediation Between VPs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Mediate architecture deadlock between two VPs with equal power.

### Short Answer (30 seconds)

Private sessions, shared criteria doc, options matrix, exec sponsor tie-break, document dissent.

### Detailed Answer (3–5 minutes)

**Mediation steps:**
1. 1:1 each VP — interests not positions
2. Shared NFR/criteria list both sign
3. Joint session — options scoring
4. If deadlock — escalate to CEO with recommendation
5. Decision log + commit ritual

**Architect:** Neutral facilitator — disclose any bias upfront.

### Architecture Perspective

VP mediation is principal architect political scenario.

### Follow-up Questions

1. **BATNA for each? — Understand walk-away options.**
2. **Relationship repair dinner? — Optional culture-dependent follow-up.**

### Common Mistakes in Interviews

- Pick side in public
- No criteria document
- Endless mediation without deadline

---

## Q079: Influence Metrics Dashboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Build influence metrics dashboard for architecture standards adoption.

### Short Answer (30 seconds)

Adoption %, defect correlation, deploy frequency by adopters vs holdouts, survey NPS, time-to-compliance for new services.

### Detailed Answer (3–5 minutes)

**Dashboard metrics:**
| Metric | Adopters | Holdouts |
|--------|----------|----------|
| Integration defects/mo | 2 | 11 |
| Deploy frequency | 10/wk | 2/wk |
| CVE open >30d | 0 | 8 |

**Story:** Data convinces holdouts and execs.

**Ethics:** No public shame leaderboard — aggregate teams.

### Architecture Perspective

Influence dashboard turns soft power into evidence.

### Follow-up Questions

1. **Causation vs correlation? — Honest — pilot A/B when possible.**
2. **Publish internally? — Guild + steering — not all-hands shame.**

### Common Mistakes in Interviews

- Mandate without measuring adoption
- Public team ranking shaming
- Cherry-picked metrics only

---

## Q080: Exec Committee Political Landmine

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Navigate political landmine when your architecture recommendation embarrasss a powerful VP's past decision.

### Short Answer (30 seconds)

Focus on forward-looking criteria, no blame, offer face-saving path (wrap not rewrite), private pre-wire.

### Detailed Answer (3–5 minutes)

**Approach:**
1. Never say 'your system failed' — say 'current state constraints'
2. Pre-wire VP 1:1 with respect for past context
3. Recommend evolution path honoring sunk work where possible
4. ADR forward-looking language

**If hostile:** Escalate to neutral exec sponsor.

### Architecture Perspective

Political landmines test maturity — blame destroys influence.

### Follow-up Questions

1. **Face-saving option? — Wrap legacy as phase 1 — not rip-and-replace headline.**
2. **Private respect public neutrality? — Don't humiliate in steering.**

### Common Mistakes in Interviews

- Blame VP's project in steering
- Ambush recommendation
- No private pre-wire

---

## Q081: Prioritization Deadlock OKR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Break prioritization deadlock using company OKRs.

### Short Answer (30 seconds)

Map initiatives to OKR key results, quantify contribution, steering ratifies, document deferred items with OKR misalignment reason.

### Detailed Answer (3–5 minutes)

**Process:**
1. List active OKRs with weights
2. Score each initiative OKR contribution 0-3
3. Sum weighted scores
4. Tie-break with risk reduction or regulatory deadline

**Communicate:** Deferred items explicitly 'does not advance OKR 2'.

### Architecture Perspective

OKR tie-break shows business alignment over politics.

### Follow-up Questions

1. **Local team OKR vs company? — Company wins at steering.**
2. **OKR change mid-quarter? — Re-prioritize emergency session.**

### Common Mistakes in Interviews

- HIPPO overrides without OKR discussion
- Initiatives not mapped to OKRs
- Deferred work invisible — zombie projects

---

## Q082: Technical Vision Pushback

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Engineers push back that vision is 'more platform bureaucracy' — respond?

### Short Answer (30 seconds)

Listen to specific pain, show quick win in 30 days, co-design with skeptics, measure before/after, adjust vision language.

### Detailed Answer (3–5 minutes)

**Response:**
1. Office hours — hear bureaucracy concerns
2. Kill worst friction point in 2 weeks (template fix)
3. Invite skeptic to pilot squad
4. Publish DORA before/after from pilot
5. Revise vision to emphasize autonomy + guardrails

**Credibility:** Actions before slides.

### Architecture Perspective

Vision pushback handled with empathy and proof — not dismissal.

### Follow-up Questions

1. **Kill initiative? — If data shows negative value — intellectual honesty.**
2. **Skeptic champion? — Convert loudest critic — powerful story.**

### Common Mistakes in Interviews

- Dismiss feedback as resistance
- Mandate without fixing friction
- Vision never updated from feedback

---

## Q083: Consensus Deadlock Escalation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

API style guide consensus deadlock after 4 weeks RFC — escalate how?

### Short Answer (30 seconds)

Summarize unresolved issues, decision deadline, architecture board tie-break, ADR with dissent, revisit trigger 6 months.

### Detailed Answer (3–5 minutes)

**Escalation pack:**
- Options A/B with criteria scores
- Unresolved objections listed
- Recommendation with rationale
- Board decision requested by date

**Post-decision:** Disagree and commit; dissent in ADR appendix.

**Revisit:** Trigger if adoption <30% in 6 months.

### Architecture Perspective

Consensus deadlock requires decision mechanism — timebox is kindness.

### Follow-up Questions

1. **Architecture board charter? — Tie-break authority documented.**
2. **Minority opinion? — Preserved — not erased.**

### Common Mistakes in Interviews

- RFC open indefinitely
- Architect imposes without board
- No revisit trigger

---

## Q084: Cross-functional Blocker Escalation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Legal team blocks GDPR launch 2 weeks before deadline — escalate as DRI?

### Short Answer (30 seconds)

Quantify risk of delay vs launch, parallel paths, exec sponsor engagement, scope reduction option, daily sync until resolved.

### Detailed Answer (3–5 minutes)

**Escalation:**
1. Document legal concern precisely
2. Options: delay launch, limited geography launch, feature scope cut
3. CEO/CTO decision with risk acceptance
4. Daily 15 min tripartite sync

**Architect:** Technical spikes continue where legal allows.

**Relationship:** Legal as partner — not obstacle.

### Architecture Perspective

Blocker escalation with options is DRI core skill.

### Follow-up Questions

1. **Bypass legal? — Never — career-ending and wrong.**
2. **Document risk acceptance? — Signed for scoped launch.**

### Common Mistakes in Interviews

- Hope legal resolves silently
- Blame legal in engineering channel
- No exec engagement on deadline

---

## Q085: Mentoring Failure Adaptation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Mentee fails first solo architecture review — adapt mentoring approach?

### Short Answer (30 seconds)

Debrief blamelessly, identify gap (comms vs technical), adjust IDP, pair on next review, maybe delay promotion timeline with clarity.

### Detailed Answer (3–5 minutes)

**Debrief:**
- What went well
- Specific gaps observed
- Revised plan: co-facilitate next 2 reviews
- Additional exec comms coaching

**Honesty:** Promotion case delayed with clear criteria to proceed.

**Avoid:** Public disappointment or withdrawing sponsorship abruptly.

### Architecture Perspective

Mentoring adaptation shows leadership maturity beyond cheerleading.

### Follow-up Questions

1. **Mentee mismatch? — Rare — try adapted approach before giving up.**
2. **360 input? — Ask review participants for feedback on mentee.**

### Common Mistakes in Interviews

- Abandon mentee after failure
- Blame mentee publicly
- No adjusted development plan

---

## Q086: Radical Candor Feedback

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Apply radical candor (care personally, challenge directly) to underperforming architect peer.

### Short Answer (30 seconds)

Private, specific behaviors, impact on teams, offer support, clear expectations, follow-up date.

### Detailed Answer (3–5 minutes)

**Conversation:**
'I care about your success and the guild's credibility (care). Your last three reviews ran 90 minutes without decision (challenge). Teams are avoiding review. Let's pair on facilitation next month — I'll share my outline.'

**Follow-up:** Scheduled check-in with measurable goal.

### Architecture Perspective

Radical candor advanced feedback for peer leadership scenarios.

### Follow-up Questions

1. **Ruinous empathy? — Avoiding hard truth hurts peer and org.**
2. **Obnoxious aggression? — Challenge without care destroys trust.**

### Common Mistakes in Interviews

- Public criticism of peer
- Vague performance concerns
- No follow-up scheduled

---

## Q087: Difficult Conversation HR Partner

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Occasional |

### Question

When involve HR in difficult architecture leadership conversation?

### Short Answer (30 seconds)

HR when policy violation, harassment, discrimination, or PIP pathway — not for normal technical disagreement.

### Detailed Answer (3–5 minutes)

**HR appropriate:**
- Hostile behavior in reviews
- Discrimination concerns
- Formal performance plan

**HR not needed:**
- Technical disagreement
- Vendor preference conflict

**Architect:** Document facts; consult HR manager privately before accusatory conversations.

### Architecture Perspective

Knowing HR boundaries shows organizational savvy.

### Follow-up Questions

1. **Document timeline? — Factual notes before HR meeting.**
2. **Retaliation fear? — HR confidential intake first.**

### Common Mistakes in Interviews

- HR for every technical dispute
- Skip HR on harassment report
- Undocumented accusatory emails

---

## Q088: Psych Safety After Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Rebuild psychological safety after blameful post-incident meeting.

### Short Answer (30 seconds)

Apologize for tone if leader, re-run blameless postmortem, leader models vulnerability, publish learning-focused report.

### Detailed Answer (3–5 minutes)

**Recovery steps:**
1. Leader acknowledges harmful meeting
2. Reschedule postmortem with signed ground rules
3. Focus on systems — 5 whys to fixable causes
4. Thank people who spoke up
5. Guild discussion on safety norms

**Long-term:** Incident facilitator training for ICs.

### Architecture Perspective

Safety recovery after blame is advanced incident leadership.

### Follow-up Questions

1. **Scapegoating firing? — Toxic — drives hiding future issues.**
2. **Anonymous reporting? — Optional channel for safety concerns.**

### Common Mistakes in Interviews

- Pretend blame meeting didn't happen
- Same facilitator repeats blame
- No published learning report

---

## Q089: SEV1 IC Delegation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

As incident commander, what must you delegate vs do personally in SEV1?

### Short Answer (30 seconds)

Delegate technical investigation, comms, scribe; IC coordinates, timing, resources, stakeholder alignment — do not deep debug.

### Detailed Answer (3–5 minutes)

**Delegate:**
- Tech lead: root cause investigation
- Comms DRI: status page + exec updates
- Scribe: timeline doc
- Liaison: customer support sync

**IC keeps:**
- Bridge facilitation
- Severity calls
- Resource escalation
- All-clear decision

**Anti-pattern:** IC debugging DB while bridge chaos.

### Architecture Perspective

IC delegation advanced topic — coordination not heroics.

### Follow-up Questions

1. **IC training? — Practice in game days quarterly.**
2. **Rotation? — IC need not be deepest expert.**

### Common Mistakes in Interviews

- IC alone in logs
- No roles assigned
- Multiple unofficial ICs

---

## Q090: Budget Zero-based Pitch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Zero-based budget justification for architecture team annual request.

### Short Answer (30 seconds)

Every line item tied to OKR, alternative cheaper options considered, last year actuals vs forecast, cut scenario impact.

### Detailed Answer (3–5 minutes)

**Structure:**
| Line | OKR link | Last yr | Request | Cut impact |
|------|----------|---------|---------|------------|
| Platform FTE | OKR2 deploy | 4 | 6 | Slower adoption |
| Tooling | OKR3 observe | $80K | $100K | Blind spots |

**Narrative:** Not 'last year +10%' — justify from zero.

**CFO respect:** Show cut scenario honestly.

### Architecture Perspective

Zero-based pitch advanced FinOps leadership for architects.

### Follow-up Questions

1. **Multi-year? — Show trajectory not just annual.**
2. **Benchmark? — Industry DORA peer comparison if available.**

### Common Mistakes in Interviews

- Line items without OKR mapping
- Only growth scenario presented
- Inflated numbers without actuals

---

## Q091: Hiring Loop Debrief Calibration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Calibrate hiring loop debrief for senior architect candidate with split panel.

### Short Answer (30 seconds)

Review rubric scores, probe disagreement, evidence not gut, bar raiser tie-break, no affinity bias, document decision.

### Detailed Answer (3–5 minutes)

**Debrief process:**
1. Each interviewer states hire/no-hire with evidence
2. Probe 2+2 split — what did each see?
3. Bar raiser challenges thin evidence
4. Decision: strong hire, hire, no hire — no 'weak hire' for architect
5. Document in ATS

**Split resolution:** More evidence needed = another focused interview.

### Architecture Perspective

Calibration advanced hiring leadership — split panels common.

### Follow-up Questions

1. **Affinity bias? — 'Culture add' not 'culture fit' homogeneity.**
2. **Leetcode split? — Relevance to architect role questioned.**

### Common Mistakes in Interviews

- Gut feeling hire
- Split ignored — majority rules without probe
- No rubric scores recorded

---

## Q092: Delegation Failure Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Delegated ADR decision failed in production — recover without blaming delegate?

### Short Answer (30 seconds)

Blameless postmortem, you own accountability as delegator, coaching not punishment, improve review SLA, adjust decision rights matrix.

### Detailed Answer (3–5 minutes)

**Recovery:**
1. Fix production — delegate leads with your support
2. Postmortem — system gaps in review quality
3. 1:1 — coaching on gap identified
4. Process fix — paired review for next 3 ADRs
5. Public — you accountable to steering

**Matrix update:** Tier-1 stays with you until delegate ready.

### Architecture Perspective

Delegation failure recovery tests leadership under accountability.

### Follow-up Questions

1. **Revoke all delegation? — Overcorrection — adjust tiering.**
2. **Spot-check quality? — Random ADR audits quarterly.**

### Common Mistakes in Interviews

- Public blame of delegate
- Revoke delegation permanently
- No process improvement

---

## Q093: Remote Conflict Resolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Resolve heated architecture conflict on remote video call.

### Short Answer (30 seconds)

Pause if needed, private breakout rooms, shared doc for criteria, async follow-up if emotions high, camera-optional after initial.

### Detailed Answer (3–5 minutes)

**Techniques:**
- Call 5-min break — cool down
- 1:1 breakout with each party
- Shared Google doc criteria — silent write then discuss
- Summarize agreement in chat before end
- Schedule follow-up if unresolved — don't force bad decision tired

**Inclusion:** Chat questions for those who won't interrupt on video.

### Architecture Perspective

Remote conflict needs explicit facilitation — harder than in-person.

### Follow-up Questions

1. **Record meeting? — Only with consent — for notes not surveillance.**
2. **Timezone fairness? — Don't always favor US morning for decision.**

### Common Mistakes in Interviews

- Force decision while shouting on mute
- No written summary after
- Ignore chat from quiet participants

---

## Q094: Vendor Negotiation Technical Redlines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Define technical redlines before cloud contract renewal negotiation.

### Short Answer (30 seconds)

Data export API, SLA credits, support tier, region availability, security certifications, exit notice period — walk if violated.

### Detailed Answer (3–5 minutes)

**Redlines:**
1. 90-day data export on request
2. SLA <99.95% with meaningful credits
3. 24/7 support with 15min P1 ack
4. Required regions available
5. SOC2 Type II current
6. 12-month exit notice max

**Architect validates:** Technical feasibility of redlines.

**Legal owns:** Contract signature.

### Architecture Perspective

Technical redlines inform negotiation — architect not sole signer.

### Follow-up Questions

1. **Multi-cloud leverage? — Credible only with portability assessment.**
2. **Lock-in discount trap? — Deep discount for 5yr — model exit cost.**

### Common Mistakes in Interviews

- Accept any SLA without credits
- No data export requirement
- Architect signs commercial terms alone

---

## Q095: Interest-based Negotiation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Apply interest-based negotiation to architecture review deadline vs launch date.

### Short Answer (30 seconds)

Uncover interests behind positions, invent options for mutual gain, use objective criteria, document agreement.

### Detailed Answer (3–5 minutes)

**Positions → Interests:**
- PM position: launch Friday
- Architect position: 2-week review
- PM interest: Q4 revenue
- Architect interest: no SEV1 from security gap

**Options:** Limited launch scope Friday + full review parallel; phased geo launch.

**Criteria:** Risk matrix, regulatory requirements.

**Document:** Email recap with owners.

### Architecture Perspective

Interest-based negotiation advanced — positions are not interests.

### Follow-up Questions

1. **BATNA? — Know walk-away without burning bridge.**
2. **Principal negotiation? — Separate people from problem.**

### Common Mistakes in Interviews

- Binary launch vs delay only
- Capitulate security for friendship
- Negotiate in public Slack

---

## Q096: Succession Planning Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Occasional |

### Question

Succession plan when principal architect may leave — document what?

### Short Answer (30 seconds)

Decision rights matrix, ADR index, stakeholder map, in-flight initiative status, mentee bench, 30-60-90 acting plan.

### Detailed Answer (3–5 minutes)

**Succession doc:**
1. Tier-1 decision delegates named
2. ADR catalog with status
3. Steering relationships intro list
4. Initiative RAID log
5. Recommended acting architect + support

**Review:** Quarterly with manager — not only on resignation.

**Knowledge:** Guild recordings, diagram repo.

### Architecture Perspective

Succession planning shows organizational leadership maturity.

### Follow-up Questions

1. **Bus factor? — Minimum two people per critical domain.**
2. **Exit interview architecture? — Handoff week structured.**

### Common Mistakes in Interviews

- Knowledge only in principal's head
- No named delegates
- Succession plan starts on resignation notice

---

## Q097: Leadership 360 Gaps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Act on 360 feedback showing weak executive communication — 90-day plan?

### Short Answer (30 seconds)

Exec coach or mentor, rehearse BLUF updates, shadow exec presentations, record and review, measure steering feedback.

### Detailed Answer (3–5 minutes)

**90-day plan:**
| Week | Action |
|------|--------|
| 1-2 | Coach engagement |
| 3-6 | Weekly BLUF practice with mentor |
| 7-10 | Shadow 3 exec presentations |
| 11-12 | Present steering solo — survey feedback |

**Measure:** Sponsor NPS or qualitative feedback.

### Architecture Perspective

Acting on 360 shows growth mindset — director interviews probe this.

### Follow-up Questions

1. **Coach vs mentor? — Coach external; mentor internal exec.**
2. **Technical 360 gap? — Different plan — courses, RFC practice.**

### Common Mistakes in Interviews

- Dismiss 360 as politics
- No measurable development plan
- Same communication style unchanged

---

## Q098: Ethical Override Request

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Occasional |

### Question

VP requests architecture sign-off violating security policy — response?

### Short Answer (30 seconds)

Decline sign-off, document concern, escalate to CISO and exec, offer alternatives, protect team from pressure.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Clarify specific policy violation
2. Decline politely with written rationale
3. Escalate to CISO — parallel notify your manager
4. Offer compliant alternatives
5. Document in risk register if exec override proceeds

**Line:** Never sign what you believe unsafe — reputational and ethical.

### Architecture Perspective

Ethical override scenarios test integrity — senior interview staple.

### Follow-up Questions

1. **Retaliation? — HR pathway if pressure continues.**
2. **Document dissent? — ADR or email trail essential.**

### Common Mistakes in Interviews

- Sign to avoid conflict
- Verbal override without documentation
- Team pressured to implement quietly

---

## Q099: Org Design Recommendation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Recommend org design change to fix Conway misalignment — present to CTO.

### Short Answer (30 seconds)

Data on lead time and cross-team tickets, stream-aligned proposal, transition plan, retention risks, 6-month metrics.

### Detailed Answer (3–5 minutes)

**Presentation:**
1. Problem data — lead time up 40%, 60% features cross 3 teams
2. Current vs proposed org chart
3. Conway explanation plain language
4. Phased transition — 6 months
5. Risks — talent, short-term velocity dip
6. Ask — approve reorg pilot for Checkout domain

**Evidence:** DORA and ticket data — not opinion.

### Architecture Perspective

Org design recommendation is apex architect influence scenario.

### Follow-up Questions

1. **Pilot reorg? — One stream before enterprise-wide.**
2. **Change management? — Comms plan and retention bonuses.**

### Common Mistakes in Interviews

- Reorg diagram without data
- Surprise announcement
- Ignore retention risk

---

## Q100: Negotiate Architecture Capacity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

Negotiate 20% architecture capacity for platform work with product org.

### Short Answer (30 seconds)

Show opportunity cost of not investing, defect/outage data, phased capacity ramp, measurable outcomes in 90 days, exec sponsor support.

### Detailed Answer (3–5 minutes)

**Offer:**
- Start 10% Q1 with measured outcomes
- Ramp 20% Q2 if deploy frequency improves 2×
- Platform team delivers golden path reducing stream effort net

**Data:** Historical outage $ + velocity drag quantified.

**Exec sponsor:** CTO endorses capacity trade.

### Architecture Perspective

Capacity negotiation balances product pressure and platform health.

### Follow-up Questions

1. **Stealing engineers? — Frame as net velocity gain — not poaching.**
2. **Capacity reversion? — If metrics don't improve — honest review.**

### Common Mistakes in Interviews

- Demand 50% without proof
- Permanent capacity without outcomes
- No exec air cover for trade

---
