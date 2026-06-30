# How to Use This Guide

## Repository Conventions

### Week Folders (`weeks/week-XX/`)

Each week is self-contained:

```
weeks/week-01/
├── README.md              # Week overview, objectives, schedule
├── theory/                # Theory notes (01-fundamentals.md, 02-intermediate.md, etc.)
├── diagrams/              # Mermaid/C4 architecture diagrams
├── labs/                  # Step-by-step hands-on labs
├── exercises/             # Coding and design exercises
├── interview-questions/   # Q&A banks (split by difficulty)
├── case-studies/          # Real-world scenarios
├── assessments/           # Weekly quiz and rubric
└── common-mistakes.md     # Pitfalls and anti-patterns
```

### Module Folders (`modules/`)

Deep-dive reference libraries that span multiple weeks. Use modules when you need exhaustive coverage of a single topic.

### Cross-Cutting Topics (`docs/cross-cutting/`)

Topics that integrate across the program (security, networking, FinOps). Reference these whenever a week touches the topic.

**Hub:** [docs/README.md](../README.md) | [cross-cutting index](../cross-cutting/README.md)

---

## Weekly Workflow

### Day 1–2: Theory
Read theory files in order: `01-fundamentals` → `02-intermediate` → `03-advanced` → `04-expert`.

**Don't just read.** For each section:
- Draw the diagram yourself before looking at ours
- Write a one-paragraph summary in your own words
- List 3 trade-offs the section mentions

### Day 3: Lab
Complete the hands-on lab. Labs use real tools (Azure, Docker, .NET CLI). Document what broke and why.

### Day 4: Exercises
Complete coding or design exercises. Design exercises should produce a diagram + written trade-off analysis.

### Day 5: Interview Q&A
Practice 20–30 questions from `interview-questions/`. **Speak answers aloud** — architects are evaluated on communication.

### Day 6: Case Study
Work through the case study. Compare your solution to the reference solution.

### Day 7: Assessment
Take the weekly assessment. Score yourself honestly using the rubric.

---

## How to Read Theory Sections

Each theory file follows this structure:

```markdown
# Topic — Level

## Learning Objectives
## Core Concepts
## Architecture Perspective (why architects care)
## Production Examples
## Trade-offs
## Common Mistakes
## Best Practices
## Further Reading
```

The **Architecture Perspective** section is the most important — it bridges code knowledge to architect thinking.

---

## How to Practice Interview Questions

1. **Read the question** — don't peek at the answer
2. **Set a 3-minute timer** — answer aloud as in an interview
3. **Compare** with the detailed answer
4. **Note gaps** — add to your personal weak-areas list
5. **Revisit** weak areas in spaced repetition (Day 7 reviews)

For scenario questions, structure answers as:

```
1. Clarify requirements (ask 2-3 questions)
2. State assumptions
3. High-level design (draw while talking)
4. Deep dive on 1-2 components
5. Discuss trade-offs and alternatives
6. Address failure modes and scale
```

---

## Diagrams

Diagrams use **Mermaid** (renders in GitHub, VS Code, Cursor) and **C4 Model** notation.

Practice redrawing diagrams from memory weekly. In interviews, you will draw — not paste.

---

## Templates

Use [templates/](../../templates/) when creating your own notes, ADRs, or case study solutions:

- `module-template.md` — new topic module
- `interview-qa-template.md` — new interview Q&A entry
- `case-study-template.md` — case study solution
- `adr-template.md` — Architecture Decision Record
- `weekly-assessment-template.md` — self-assessment

---

## Tracking Progress

Create a local file `progress/my-tracker.md` (gitignored) with:

```markdown
# My Progress

| Week | Theory | Lab | Exercises | Q&A | Case Study | Assessment | Score |
|------|--------|-----|-----------|-----|------------|------------|-------|
| 01   | ✅     | ✅  | ✅        | 🔄  | ⬜         | ⬜         | —     |
```

---

## When to Skip Ahead

**Don't skip Phase 1 (Months 1–2)** even if you're a senior developer. The architect lens on C#, patterns, and data is different from day-to-day coding.

You may accelerate if you can pass the week's assessment at 80%+ without studying.

---

## Getting Help

- Re-read the **Trade-offs** and **Common Mistakes** sections — they answer most "but why?" questions
- Cross-reference [docs/reference/glossary.md](../reference/glossary.md) for terminology
- Use [docs/reference/decision-frameworks.md](../reference/decision-frameworks.md) when stuck between options

---

## Study Tools

| Tool | Purpose |
|------|---------|
| [Progress tracker](../../templates/progress-tracker.md) | Track weeks, mocks, capstones, weak areas |
| [MkDocs site](../../mkdocs.yml) | Browse the guide locally: `pip install mkdocs-material && mkdocs serve` |
| [Link checker](../../scripts/check_links.py) | CI validates internal links: `python3 scripts/check_links.py` |

---

Next: [prerequisites.md](prerequisites.md) → [Week 01](../../weeks/week-01/README.md)
