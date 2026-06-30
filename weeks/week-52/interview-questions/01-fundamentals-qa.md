# Week 52 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Architecture Portfolio Essentials

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

What essentials belong in an architecture portfolio for principal-level job search?

### Short Answer (30 seconds)

3–5 deep case studies with context, your role, diagrams, trade-offs, and metrics; plus executive summary, principles, tech radar, and contact. Depth beats breadth — anonymize confidential data.

### Detailed Answer (3–5 minutes)

**Portfolio essentials:**
1. **Executive summary (1 page)** — Specialty, impact metrics, target role
2. **Case studies (3–5)** — Each 3–5 pages:
   - Business context and constraints
   - Your role ('I' vs 'we' explicit)
   - C4 L1–L2 diagrams
   - ADR highlights
   - Before/after metrics
   - Lessons learned
3. **Architecture principles** — 5–8 personal principles with examples
4. **Tech radar** — Adopt/trial/assess/hold with rationale
5. **References** — LinkedIn, GitHub, talks, blog

**Format:** PDF primary; optional static site (GitHub Pages).

**Privacy:** Anonymize employer; no confidential revenue or customer names.

**Anti-patterns:** Resume paste; 7 shallow cases; diagrams with live confidential data.

### Architecture Perspective

Portfolio essentials separate serious architect candidates from resume-only applicants.

### Follow-up Questions

1. **How many case studies? — 3 excellent beats 7 shallow — interviewers go deep on one.**
2. **Redacted diagrams? — Generic boxes OK — structure and trade-offs matter most.**

### Common Mistakes in Interviews

- Resume copied as portfolio
- No clarity on personal role in case studies
- Confidential numbers or customer names exposed

---

## Q002: Mock Interview Preparation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

What are the essentials of mock interview preparation before architect job search?

### Short Answer (30 seconds)

Deliberate practice across system design, behavioral STAR, leadership, and estimation. Schedule peer mocks, record and review, track gaps in spreadsheet, simulate full loop in final week.

### Detailed Answer (3–5 minutes)

**4-week essentials plan:**
| Week | Focus | Activities |
|------|-------|------------|
| 1 | System design | 3 mocks: SaaS, payments, scale |
| 2 | Behavioral | 2 STAR sessions; record and critique |
| 3 | Leadership | Exec comms + conflict scenarios |
| 4 | Full loop | 4-hour simulated loop + debrief |

**Practice rules:**
- Speak aloud — reading ≠ interviewing
- Time-box answers (90 sec STAR, 45 min design)
- Debrief every mock: gaps, filler words, diagram clarity
- Max 2 mocks/day — quality degrades beyond that

**Log:** Spreadsheet of missed questions; drill weak areas before next mock.

**Logistics:** Test video, whiteboard tool (Excalidraw), quiet space.

**Resources:** Peer architects, Pramp, optional coach for final polish.

### Architecture Perspective

Mock prep is deliberate practice — schedule it like exam study, not optional cramming.

### Follow-up Questions

1. **Company-specific prep? — Final week tailor stories to target stack and values.**
2. **Only reading — never practicing aloud? — #1 preparation failure.**

### Common Mistakes in Interviews

- Skip behavioral and leadership mocks
- No debrief or gap tracking after sessions
- Cram 5 mocks day before interview

---

## Q003: Personal Architecture Principles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

How articulate personal architecture principles for portfolio and interviews?

### Short Answer (30 seconds)

Define 5–8 principles from your experience; each with rationale, example, and trade-off awareness. Show you prioritize contextually — not parrot frameworks blindly.

### Detailed Answer (3–5 minutes)

**Example personal principle set:**
1. **Simplicity first** — Simplest design meeting NFRs (monolith before microservices)
2. **Evolutionary architecture** — Decide at last responsible moment
3. **Observability by default** — Can't operate what you can't see
4. **Security embedded** — Not bolted on at end
5. **Conway-aware boundaries** — Service splits match team ownership
6. **Managed services** — Unless clear reason not to
7. **Data as product** — Contracts and ownership explicit
8. **Blameless learning** — Incidents improve systems

**Interview use:**
- 'Which principle would you violate here and why?' — show contextual judgment
- Link principles to case studies in portfolio

**Evolution:** Annual reflection — principles should mature with experience.

**Avoid:** 10+ unfocused principles; buzzwords without examples; principles you contradict in stories.

### Architecture Perspective

Personal principles show architectural maturity — not just Microsoft Well-Architected recitation.

### Follow-up Questions

1. **Principles in conflict? — Discuss prioritization by context — strong senior signal.**
2. **Generic only? — Must connect each principle to real project example.**

### Common Mistakes in Interviews

- Buzzword principles without examples
- 10+ principles — unfocused philosophy
- Principles contradicted by your STAR stories

---

## Q004: Tech Radar Curation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

How curate a personal technology radar for architect portfolio and interviews?

### Short Answer (30 seconds)

Use Adopt/Trial/Assess/Hold quadrants with brief rationale per technology. Personalize to your specialty and cloud; update quarterly — dated radar hurts credibility.

### Detailed Answer (3–5 minutes)

**ThoughtWorks-style quadrants:**
- **Adopt** — Production-ready in your context: K8s, OpenTelemetry, Terraform
- **Trial** — Active POC: vector DBs for RAG, WASM on edge
- **Assess** — Watching: eBPF networking, FinOps tooling maturity
- **Hold** — Defer: unproven blockchain for enterprise ledger

**Personalization examples:**
| Specialty | Adopt emphasis | Hold example |
|-----------|----------------|-------------|
| Azure SA | AKS, APIM, Cosmos | Premature multi-cloud abstraction |
| Fintech security | HSM, zero-trust patterns | Experimental crypto schemes |

**Portfolio format:** One-page visual + paragraph on how you update (quarterly review).

**Interview use:** 'Why is X in Trial not Adopt?' — shows judgment, not hype.

**Employer radar conflict? — Personal radar can differ — explain thoughtfully.

### Architecture Perspective

Tech radar shows continuous learning and judgment — not resume keyword stuffing.

### Follow-up Questions

1. **Hold vs reject? — Hold = not now; may revisit — different from permanent rejection.**
2. **Everything in Adopt? — Signals lack of critical evaluation.**

### Common Mistakes in Interviews

- Radar copied unchanged from ThoughtWorks
- No rationale for quadrant placement
- Radar not updated in 12+ months

---

## Q005: Career Planning for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

What essentials belong in a 5-year career plan for solution or principal architect track?

### Short Answer (30 seconds)

Define vision, skills roadmap, experiences, network, milestones, and contingency paths. Review annually — intentionality beats drifting on promotion titles alone.

### Detailed Answer (3–5 minutes)

**5-year plan framework:**
| Year | Focus |
|------|-------|
| 1 | Land role; establish credibility; 1 major delivery |
| 2 | Lead tier-1 program; external visibility (talk/blog) |
| 3 | Principal scope; architecture board; mentor 3+ |
| 4 | Industry recognition; optional course or book |
| 5 | CTO exploration or staff/principal depth |

**Skills roadmap:** FinOps, security architecture, AI/LLM systems — align to market demand.

**Experience targets:**
- Tier-1 program leadership
- Executive stakeholder management
- Published ADRs, talks, or open source contributions

**Contingency paths:**
- IC vs management fork by year 2–3
- Consulting or contracting if market downturn
- Geographic or industry pivot triggers

**Review:** Annual retrospective — adjust plan for life constraints and market shifts.

**Interview use:** 'Where do you see yourself in 5 years?' — specific but flexible.

### Architecture Perspective

Career planning shows intentionality — interviewers assess whether you own your trajectory.

### Follow-up Questions

1. **IC vs management? — Decide by year 2–3; both valid — document triggers for each path.**
2. **Market downturn plan B? — Consulting, broaden stack, fractional architect roles.**

### Common Mistakes in Interviews

- No written plan — drifting on promotions only
- Only title goals — no skill development
- Plan ignores life constraints and sustainability

---

## Q006: Architecture Portfolio Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

How structure architecture portfolio for principal-level job search?

### Short Answer (30 seconds)

3–5 deep case studies with context, constraints, your role, diagrams, trade-offs, outcomes. Plus index, principles, contact.

### Detailed Answer (3–5 minutes)

**Portfolio sections:**
1. **Executive summary** — 1 page: who you are, specialty, impact metrics
2. **Case studies (3–5)** — Each 3–5 pages:
   - Business context & constraints
   - Your role (explicit 'I' vs 'we')
   - Architecture diagrams (C4 L1–L2)
   - ADR highlights
   - Metrics (before/after)
   - Lessons learned
3. **Architecture principles** — Your philosophy
4. **Tech radar** — What you adopt/hold/assess
5. **References & links** — GitHub, blog, talks

**Format:** PDF + optional static site (GitHub Pages).

**Privacy:** Anonymize employers; no confidential numbers.

### Architecture Perspective

Portfolio structure separates serious architect candidates from resume-only.

### Follow-up Questions

1. **How many case studies? — Depth over breadth — 3 excellent > 7 shallow.**
2. **Redacted diagrams? — Generic boxes OK — structure matters.**

### Common Mistakes in Interviews

- Resume paste as portfolio
- No 'my role' clarity
- Confidential data exposed

---

## Q007: Mock Interview Preparation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Plan 4-week mock interview preparation before architect job search.

### Short Answer (30 seconds)

Mix system design, behavioral, leadership, estimation. Peer mocks, recording review, gap tracking.

### Detailed Answer (3–5 minutes)

**Week plan:**
| Week | Focus | Activity |
|------|-------|----------|
| 1 | System design | 3 mocks: URL shortener, payments, SaaS |
| 2 | Behavioral | 2 STAR sessions; record and critique |
| 3 | Leadership | Exec comms + conflict scenarios |
| 4 | Full loop | 4hr simulated loop with debrief |

**Resources:** Peer architects, Pramp, paid coach for final polish.

**Log:** Spreadsheet of questions missed; drill weak areas.

**Logistics:** Test video, whiteboard tool, quiet space.

### Architecture Perspective

Mock prep is deliberate practice — schedule it like exam study.

### Follow-up Questions

1. **Company-specific? — Week 4 tailor to target company stack.**
2. **Fatigue? — Max 2 mocks/day — quality drops.**

### Common Mistakes in Interviews

- Only read — never practice aloud
- Skip behavioral prep
- No debrief after mocks

---

## Q008: Architecture Principles Personal

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Articulate your personal architecture principles for portfolio and interviews.

### Short Answer (30 seconds)

5–8 principles reflecting your experience; each with rationale and example; show trade-off awareness.

### Detailed Answer (3–5 minutes)

**Example personal set:**
1. **Simplicity first** — Simplest design meeting NFRs (example: monolith before microservices)
2. **Evolutionary architecture** — Decide last responsible moment
3. **Observability by default** — Can't operate what you can't see
4. **Security embedded** — Not bolted on at end
5. **Team topology alignment** — Conway-aware boundaries
6. **Managed services** — Unless clear reason not to
7. **Data as product** — Clear ownership and contracts
8. **Blameless learning** — Incidents improve systems

**Interview use:** 'Which principle would you violate here and why?'

### Architecture Perspective

Personal principles show maturity — not parroting Microsoft Well-Architected only.

### Follow-up Questions

1. **Conflict between principles? — Discuss prioritization context.**
2. **Evolve principles? — Annual reflection — growth signal.**

### Common Mistakes in Interviews

- Generic buzzwords without examples
- 10+ principles — unfocused
- Principles you don't follow in stories

---

## Q009: Tech Radar Curation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Curate personal technology radar for architect portfolio.

### Short Answer (30 seconds)

Adopt, trial, assess, hold — with brief rationale per technology; aligned to market and your specialty.

### Detailed Answer (3–5 minutes)

**Quadrants (ThoughtWorks style):**
- **Adopt** — Production-ready for your context: Kubernetes, OpenTelemetry, Terraform
- **Trial** — POC stage: WebAssembly on edge, vector DBs for RAG
- **Assess** — Watching: eBPF networking, FinOps tooling maturity
- **Hold** — Defer: new unproven blockchain for enterprise ledger

**Personalize:** Azure architect radar differs from fintech security architect.

**Update:** Quarterly review — radar dated >1yr hurts credibility.

**Portfolio:** One-page visual + paragraph rationale.

### Architecture Perspective

Tech radar shows continuous learning and judgment — not resume keyword list.

### Follow-up Questions

1. **Hold vs reject? — Hold = not now; may revisit.**
2. **Employer radar conflict? — Personal radar can differ — explain thoughtfully.**

### Common Mistakes in Interviews

- Everything in Adopt
- Radar copied from ThoughtWorks unchanged
- No rationale for placement

---

## Q010: Career Planning Architect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Create 5-year career plan for solution/principal architect track.

### Short Answer (30 seconds)

Vision, skills, experiences, network, milestones, contingency paths.

### Detailed Answer (3–5 minutes)

**Plan framework:**
- **Year 1** — Land role; establish credibility; 1 major delivery
- **Year 2** — Lead tier-1 program; external visibility (talk/blog)
- **Year 3** — Principal scope; architecture board; mentor 3+
- **Year 4** — Industry recognition; optional book/course
- **Year 5** — CTO path exploration or staff/principal depth

**Skills roadmap:** FinOps, security, AI architecture as market demands.

**Contingency:** Management track? Consulting? Document triggers.

**Review:** Annual retrospective against plan.

### Architecture Perspective

Career planning shows intentionality — interviewers ask 5-year goals.

### Follow-up Questions

1. **IC vs management fork? — Decide by year 2–3 typically.**
2. **Market downturn? — Plan B: consulting, broaden stack.**

### Common Mistakes in Interviews

- No written plan — drift
- Only promotion titles — no skill development
- Plan ignores life constraints

---

## Q011: Certification Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Which certifications matter for enterprise architect career in 2025–2026?

### Short Answer (30 seconds)

Align certs to target role and cloud. Azure: AZ-305, SC-100. AWS: SA-Pro. TOGAF for EA formalism. Certs open doors; experience closes.

### Detailed Answer (3–5 minutes)

**By path:**
| Path | Priority certs |
|------|----------------|
| Azure SA | AZ-305, AZ-104, SC-100 |
| AWS SA | SAA, SAP |
| Enterprise EA | TOGAF, Zachman awareness |
| Security architect | CISSP, SC-100 |

**Strategy:**
- Max 2 certs/year while working — burnout risk
- Cert after hands-on — not substitute
- List on LinkedIn; mention in resume skills

**Diminishing returns:** After 3 relevant certs, portfolio > more certs.

### Architecture Perspective

Certification strategy is tactical — match target employers.

### Follow-up Questions

1. **TOGAF still relevant? — Some enterprises require; know framework basics.**
2. **Cert only no experience? — Interview will expose — cert supports not replaces.**

### Common Mistakes in Interviews

- Collecting unrelated certs
- Cert before any cloud hands-on
- Ignore employer's cloud preference

---

## Q012: Networking Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

How build professional network as architect for job opportunities and learning?

### Short Answer (30 seconds)

Architecture guilds, conferences, LinkedIn, open source, alumni, give-before-ask.

### Detailed Answer (3–5 minutes)

**Tactics:**
- **Local guild** — Present quarterly; volunteer organize
- **Conferences** — 1 major/year; hallway track valuable
- **LinkedIn** — Thoughtful comments on architect posts; share learnings
- **Open source** — Contribute to CNCF project docs or samples
- **Mentorship** — Mentor 1–2 juniors — network reciprocity

**Job search:** Warm intros 3× more effective than cold apply.

**Give first:** Answer questions, make intros — before asking favors.

### Architecture Perspective

Networking is long game — start before you need job.

### Follow-up Questions

1. **Introvert strategies? — 1:1 coffee chats over large mixers.**
2. **Online only? — Balance virtual and in-person.**

### Common Mistakes in Interviews

- Transactional networking only when job hunting
- No give — only take
- Ignore local community

---

## Q013: Conference Speaking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Path from zero to conference speaker on architecture topics.

### Short Answer (30 seconds)

Internal talks → meetups → regional → CFP for major conferences. Pick niche; practice; record.

### Detailed Answer (3–5 minutes)

**Ladder:**
1. **Lunch-and-learn** at company
2. **Meetup** — 20 min talk
3. **Regional conf** — 40 min
4. **CFP** — KubeCon, re:Invent builder sessions, local Architect Summit

**Topic:** Lesson learned from production — not hello-world.

**CFP tips:** Clear title, 3 takeaways, speaker bio with credibility.

**Prep:** Rehearse 5×; backup slides offline; engage Q&A.

### Architecture Perspective

Conference speaking builds brand — employers notice.

### Follow-up Questions

1. **Rejection? — Normal — iterate CFP abstract.**
2. **Co-present? — Pair with mentor first talk.**

### Common Mistakes in Interviews

- Theory-only talk no production story
- Read slides verbatim
- Never submitted CFP

---

## Q014: Blog Writing Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Start architecture blog that supports job search and learning.

### Short Answer (30 seconds)

Consistent cadence, depth over hype, diagrams, series, cross-post, SEO basics.

### Detailed Answer (3–5 minutes)

**Strategy:**
- **Platform** — Personal site or dev.to + own domain canonical
- **Cadence** — 1 post/2 weeks realistic; series on one topic builds authority
- **Topics** — ADR breakdowns, migration war stories (anonymized), pattern deep dives
- **Quality** — One great post > four shallow
- **Promote** — LinkedIn summary; don't spam

**Portfolio link:** Best 3 posts featured.

**Avoid:** AI-generated fluff without personal experience.

### Architecture Perspective

Blog demonstrates communication — architects write for living.

### Follow-up Questions

1. **First post topic? — 'What I learned migrating X' — concrete.**
2. **Stop/start? — Series commitment beats sporadic.**

### Common Mistakes in Interviews

- Hype-driven content only
- No diagrams in architecture blog
- Employer confidential details

---

## Q015: Open Source Contribution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Occasional |

### Question

Meaningful open source contribution strategy for architects (not just code).

### Short Answer (30 seconds)

Docs, samples, ADRs in CNCF projects, issue triage, reference architectures. Align to your stack.

### Detailed Answer (3–5 minutes)

**Contribution types:**
- **Documentation** — Fix unclear K8s docs — high impact
- **Samples** — Azure/cross-cloud reference arch repos
- **Issues** — Reproduce bugs; thoughtful feature proposals
- **Talks** — Present OSS you use

**Time:** 2–4 hr/month sustainable.

**Resume:** 'Contributor to X' with link to merged PR.

**Pick project:** What you use in production — authenticity.

### Architecture Perspective

OSS contribution signals community engagement — docs count.

### Follow-up Questions

1. **First PR? — Start with typo fix or doc clarification.**
2. **Maintainer burden? — Don't promise more than you deliver.**

### Common Mistakes in Interviews

- Claim contributor without merged work
- Only star repos
- Random projects unrelated to expertise

---

## Q016: Personal Brand

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Define and build personal brand as architect without cringe.

### Short Answer (30 seconds)

Consistent niche, authentic voice, value-first content, professional boundaries.

### Detailed Answer (3–5 minutes)

**Brand elements:**
- **Niche** — 'Azure platform architect for regulated finance'
- **Proof** — Portfolio, talks, certs aligned to niche
- **Voice** — Practical, not guru; admit unknowns
- **Channels** — LinkedIn + blog + optional Twitter/X
- **Boundaries** — Employer IP separate; opinions yours

**Anti-cringe:** No humble brag spam; engage genuinely.

**Measure:** Inbound recruiter quality; peer recognition.

### Architecture Perspective

Personal brand is reputation at scale — consistency matters.

### Follow-up Questions

1. **Rebrand? — OK annually as focus sharpens.**
2. **Employer conflict? — Check social media policy.**

### Common Mistakes in Interviews

- Generic 'thought leader' with no niche
- Controversy for attention
- Neglect LinkedIn hygiene

---

## Q017: Salary Negotiation Architect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Negotiate architect compensation package effectively.

### Short Answer (30 seconds)

Research bands, total comp focus, multiple offers, negotiate after offer, written confirmation.

### Detailed Answer (3–5 minutes)

**Preparation:**
- **Research** — levels.fyi, Glassdoor, recruiter intel for level
- **Total comp** — Base + bonus + equity + benefits + signing
- **Anchoring** — Let them offer first if possible
- **Leverage** — Competing offer (ethical)
- **Negotiate** — 'I'm excited; can we discuss base/equity to align with market for principal?'

**Non-salary:** Remote, title, learning budget, conference budget.

**Walk away:** Know minimum — architect market varies by region.

### Architecture Perspective

Salary negotiation is skill — practice script aloud.

### Follow-up Questions

1. **First offer accept? — Almost always room — polite negotiate.**
2. **Title negotiation? — Principal vs senior affects next hop.**

### Common Mistakes in Interviews

- No market research
- Negotiate before offer
- Burn bridges with ultimatum

---

## Q018: IC vs Management Track

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Decide between IC architect and engineering management track.

### Short Answer (30 seconds)

Assess energy from activities: design vs people ops. Both valid; switch possible but costly. Principal IC = deep impact without direct reports.

### Detailed Answer (3–5 minutes)

**IC architect joys:** Technical depth, ADRs, standards, cross-org influence without perf reviews.

**Management joys:** Team building, hiring, career growth of others, org design.

**IC path levels:** Senior → Staff → Principal → Distinguished.

**Decision framework:**
- Energy from 1:1s and perf cycles? → Management
- Energy from deep technical problems and writing? → IC
- Try: Acting tech lead 6 months before committing

**Hybrid:** Architect with dotted lines — clarify expectations.

### Architecture Perspective

IC vs management is major fork — interviewers probe self-awareness.

### Follow-up Questions

1. **Can switch back? — Harder after 3+ years management — plan intentionally.**
2. **Principal not available? — Some companies — target employers with IC ladder.**

### Common Mistakes in Interviews

- Management only path to seniority myth
- IC because afraid of people — wrong reason
- No conversation with manager on ladder

---

## Q019: Principal Architect Path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

What distinguishes principal architect from senior architect?

### Short Answer (30 seconds)

Org-wide impact, executive trust, ambiguity navigation, multiplier effect, external representation.

### Detailed Answer (3–5 minutes)

**Principal expectations:**
- Influence without authority across company
- Set direction for domain or platform
- Resolve highest-stakes technical conflicts
- Represent company externally
- Grow other architects

**Evidence for promotion:**
- 2+ tier-1 programs delivered
- Measurable org metrics moved (DORA, cost, uptime)
- Exec sponsor relationship
- Architecture board chair or equivalent

**Timeline:** Typically 5–10 years post-senior — varies by company.

### Architecture Perspective

Principal path clarity shows ambition aligned to role.

### Follow-up Questions

1. **Principal vs staff? — Company-dependent — read rubric.**
2. **No principals at company? — Target org with IC growth or define role.**

### Common Mistakes in Interviews

- Principal = best coder only
- No org-wide impact stories
- Ignore soft skills at principal level

---

## Q020: Enterprise Architect Path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Enterprise architect career path vs solution architect — differences and preparation.

### Short Answer (30 seconds)

EA: strategy, portfolio, standards, governance across enterprise. SA: solution delivery for specific programs. EA more abstract; SA more hands-on.

### Detailed Answer (3–5 minutes)

**Enterprise architect:**
- TOGAF/business capability mapping
- Application portfolio rationalization
- Technology standards and roadmaps
- Board and CIO stakeholder

**Solution architect:**
- Program-specific designs
- Hands-on with teams
- Delivery accountability

**Transition:** Senior SA → domain EA → chief architect.

**Prep:** Business acumen, finance, strategy courses; less coding over time.

### Architecture Perspective

EA vs SA path choice depends on business vs technical energy.

### Follow-up Questions

1. **TOGAF required? — Helpful not mandatory everywhere.**
2. **EA disconnected from delivery? — Danger — stay connected to production.**

### Common Mistakes in Interviews

- EA as PowerPoint only stereotype
- SA forever without growth plan
- Ignore business strategy skills for EA

---

## Q021: Solution Architect Path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Build career as solution architect in cloud consulting or product company.

### Short Answer (30 seconds)

Breadth across stack, customer communication, presales optional, delivery excellence, specialization.

### Detailed Answer (3–5 minutes)

**Consulting SA:**
- Client-facing; travel; broad exposure; presales
- Skills: workshops, estimations, proposals

**Product SA:**
- Deep product domain; internal teams; less travel
- Skills: roadmap partnership, scale patterns

**Growth:** SA → senior SA → principal → CTO (product) or practice lead (consulting).

**Portfolio:** Customer stories (anonymized); reference architectures.

### Architecture Perspective

Solution architect path suits breadth lovers and customer interaction.

### Follow-up Questions

1. **Presales required? — Consulting often — product optional.**
2. **Specialize? — Vertical (health) or horizontal (integration) by year 3.**

### Common Mistakes in Interviews

- Jack of all trades no depth
- Poor communication skills unaddressed
- Ignore cloud hands-on labs

---

## Q022: Continuous Learning Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Design continuous learning plan for architect staying current.

### Short Answer (30 seconds)

70-20-10 model: experience, exposure, education. Quarterly goals, budget, time allocation.

### Detailed Answer (3–5 minutes)

**Annual plan:**
- **70% experience** — Lead project in new domain (e.g., AI platform)
- **20% exposure** — Conferences, guilds, peer architects
- **10% education** — Courses, certs, books

**Quarterly:** 1 book, 1 course module, 1 conference or deep blog series.

**Budget:** $2–5K/yr employer L&D — use it.

**Track:** Learning log in Notion — interview evidence.

**Avoid:** Random tutorial hopping without application.

### Architecture Perspective

Continuous learning plan prevents obsolescence — architects must model it.

### Follow-up Questions

1. **AI era? — Allocate 20% to LLM/RAG/security implications.**
2. **Learning in public? — Blog reinforces retention.**

### Common Mistakes in Interviews

- No allocated time — 'too busy'
- Only certs no building
- Chase every hype cycle

---

## Q023: Community Involvement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Ways architects give back to professional community.

### Short Answer (30 seconds)

Mentoring, OSS, meetups, teaching, standards bodies, pro bono nonprofits.

### Detailed Answer (3–5 minutes)

**Options:**
- **Code mentoring** — CodePath, Rewriting the Code
- **Meetup organizer** — Cloud native group
- **Standards** — IETF, W3C working groups (niche)
- **Teaching** — Adjunct or bootcamp guest lecturer
- **Nonprofit** — Architecture for social good orgs

**Benefits:** Network, skills, fulfillment.

**Boundaries:** 2–4 hr/month sustainable during job search.

### Architecture Perspective

Community involvement differentiates passionate architects.

### Follow-up Questions

1. **Employer support? — Some offer volunteer days.**
2. **Resume section? — 'Community' — brief with impact.**

### Common Mistakes in Interviews

- Overcommit and burn out
- Community only for resume
- No long-term commitment

---

## Q024: Reference Letter Prep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Prepare references for architect job search.

### Short Answer (30 seconds)

Identify 5 references: manager, peer architect, cross-functional, skip-level optional, customer optional. Brief them; provide resume and role target.

### Detailed Answer (3–5 minutes)

**Reference set:**
1. **Direct manager** — Required almost always
2. **Senior architect peer** — Technical collaboration
3. **Engineering director** — Leadership scope
4. **Product or business partner** — Cross-functional
5. **Optional customer** — Consulting roles

**Prep package for each:**
- Resume and target role description
- 3 bullets they might speak to (projects you led)
- Heads-up on recruiter call timing

**Never:** Surprise reference with cold call.

### Architecture Perspective

Reference prep prevents lukewarm or misaligned references.

### Follow-up Questions

1. **Former manager conflict? — Use skip-level or director instead.**
2. **LinkedIn rec? — Nice supplement not substitute for phone reference.**

### Common Mistakes in Interviews

- Only friends as references
- Surprise references without briefing
- No manager reference without explanation

---

## Q025: LinkedIn Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Common |

### Question

Optimize LinkedIn profile for architect recruiter discovery and credibility.

### Short Answer (30 seconds)

Keyword-rich headline, impact bullets in experience, featured section, recommendations, activity.

### Detailed Answer (3–5 minutes)

**Checklist:**
- **Headline** — 'Principal Architect | Azure | Platform Engineering' not just title
- **About** — 3 paragraphs: specialty, impact metrics, what you seek
- **Experience** — CAR bullets: Context, Action, Result with numbers
- **Featured** — Portfolio link, best talk, blog post
- **Skills** — Endorsements for top 5 skills
- **Recommendations** — Request 2 from collaborators
- **Open to work** — Recruiter-only mode if employed

**Activity:** 1 thoughtful post/month minimum during search.

### Architecture Perspective

LinkedIn is recruiter funnel — optimize for search keywords.

### Follow-up Questions

1. **Photo and banner? — Professional — increases profile views.**
2. **Connection spam? — Personalized notes to architects you admire.**

### Common Mistakes in Interviews

- Job title only headline
- Wall of buzzwords no metrics
- Inactive profile during search

---

## Q026: Interview Loop Preparation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Prepare for full architect interview loop at FAANG or enterprise.

### Short Answer (30 seconds)

Map loop components, company research, story bank, questions to ask, logistics rehearsal.

### Detailed Answer (3–5 minutes)

**Typical loop:**
- Recruiter → HM → 2× system design → behavioral → architecture discussion → leadership (director+)

**Prep:**
- **Company** — Tech blog, engineering principles, recent launches
- **Stories** — 10 STAR stories mapped to competencies
- **Design** — 5 mocks in their domain (fintech, retail, etc.)
- **Questions** — 'How does architecture guild govern?' — show interest
- **Logistics** — Rest day before; materials ready

**Day-of:** Whiteboard tool tested; water; notes sheet allowed?

### Architecture Perspective

Full loop prep is project management — checklist driven.

### Follow-up Questions

1. **Bar raiser round? — Extra behavioral depth — prepare failure story.**
2. **Virtual onsite fatigue? — Request breaks between sessions.**

### Common Mistakes in Interviews

- Wing loop day without mocks
- No questions for interviewers
- Ignore company-specific stack

---

## Q027: System Design Practice Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

12-week system design practice plan for architect interviews.

### Short Answer (30 seconds)

Progressive difficulty, timed mocks, pattern library, weak area drills.

### Detailed Answer (3–5 minutes)

**Weeks 1–4:** Fundamentals — URL shortener, rate limiter, cache, queue
**Weeks 5–8:** Intermediate — Twitter feed, Uber, Dropbox
**Weeks 9–10:** Advanced — Multi-tenant SaaS, payment system, search
**Weeks 11–12:** Company-specific + failure mode drills

**Per session (90 min):** 45 design + 15 review against rubric + 30 drill weak area.

**Rubric:** Requirements, estimation, API, data model, scale, NFRs, trade-offs.

**Log:** Patterns used; mistakes repeated.

### Architecture Perspective

System design practice is muscle memory — timed repetition essential.

### Follow-up Questions

1. **Diagram tool? — Excalidraw muscle memory before interview.**
2. **Partner mocks? — Week 8+ essential for feedback.**

### Common Mistakes in Interviews

- Watch videos only never draw
- Untimed practice only
- Skip estimation and NFRs

---

## Q028: Behavioral Practice Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

8-week behavioral interview practice plan for architect roles.

### Short Answer (30 seconds)

Story bank, recording, competency mapping, director-level probes.

### Detailed Answer (3–5 minutes)

**Week 1–2:** Draft 12 STAR stories (leadership, conflict, failure, influence)
**Week 3–4:** Record 2-min delivery; cut filler words
**Week 5–6:** Mock with peer; practice follow-up probes
**Week 7:** 'Why architect?' 'Why leave?' 'Why us?'
**Week 8:** Full behavioral mock with debrief

**Competency map:** Amazon LP, Microsoft growth mindset, generic leadership dimensions.

**Tip:** Same story adapts to multiple prompts — know flexible angles.

### Architecture Perspective

Behavioral practice prevents rambling — timer discipline.

### Follow-up Questions

1. **Failure story? — Mandatory — prepare authentic one.**
2. **Over-rehearsed robotic? — Bullet outline not word script.**

### Common Mistakes in Interviews

- No story bank written
- Only technical prep
- Stories without metrics

---

## Q029: 90-Day Job Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Draft 90-day plan for starting new architect role.

### Short Answer (30 seconds)

Listen, learn, deliver quick win, relationships, avoid redesigning everything day one.

### Detailed Answer (3–5 minutes)

**Days 1–30 — Learn:**
- Stakeholder 1:1s (manager, peers, product, ops)
- Read ADRs, incident history, roadmap
- Map architecture and pain points

**Days 31–60 — Contribute:**
- Lead one architecture review
- Identify quick win (doc gap, standard clarification)
- Join on-call shadow if applicable

**Days 61–90 — Lead:**
- Own small initiative end-to-end
- Present findings to guild
- Propose one roadmap item with business case

**Avoid:** 'Everything is wrong' first impression.

### Architecture Perspective

90-day plan question common in architect interviews — show you've thought about onboarding.

### Follow-up Questions

1. **Remote start? — Over-index relationship building early.**
2. **Consulting vs FTE? — Consulting: deliverable by day 90 critical.**

### Common Mistakes in Interviews

- Redesign entire architecture day 1
- No stakeholder listening phase
- No measurable 90-day outcome

---

## Q030: Graduation Presentation Rubric

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Graduation Capstone |
| **Frequency** | Very Common |

### Question

Present graduation capstone: 30-min architecture portfolio review against program rubric.

### Short Answer (30 seconds)

Demonstrate mastery across technical depth, leadership, communication, and program completion. Panel evaluates holistically.

### Detailed Answer (3–5 minutes)

**Presentation (30 min):**
1. **Introduction** — Journey and specialty (3 min)
2. **Portfolio walkthrough** — 2 case studies deep (15 min)
3. **Live whiteboard** — Extend one case study (7 min)
4. **Lessons & next steps** — Career plan (5 min)

**Rubric dimensions (pass ≥70% each):**
| Dimension | Criteria |
|-----------|----------|
| Technical depth | Trade-offs, NFRs, scale |
| Leadership | Influence, stakeholder stories |
| Communication | Clarity, exec-appropriate |
| Completeness | 52-week program artifacts |
| Growth | Self-awareness, improvement plan |

**Deliverables submitted:** Portfolio PDF, learning log, mock interview reflection.

**Panel:** Peer architect + program mentor.

### Architecture Perspective

Graduation rubric caps 52-week program — treat as job interview finale.

### Follow-up Questions

1. **Fail one dimension? — Remediation presentation option.**
2. **Nerves? — Same prep as mock loop — you've trained for this.**

### Common Mistakes in Interviews

- Read slides 30 minutes
- Skip leadership dimension entirely
- No portfolio submitted before presentation

---
