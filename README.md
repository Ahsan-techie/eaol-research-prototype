# EAOL - Enterprise Agent Orchestration Layer

Research prototype for a PhD project at Teesside University, supervised by Professor Annalisa Occhipinti, in partnership with MCD Systems.

> **Status:** Phase 0 - design and literature review. Prototype implementation begins in Phase 1.

## Aim

Design, develop, and evaluate the Enterprise Agent Orchestration Layer (EAOL): an architecture for reliable autonomous task management in enterprise software environments.

## Thesis claim

EAOL combines three mechanisms within a single coordination architecture:

1. Hierarchical agent role specialisation
2. Confidence-driven task allocation
3. Lightweight symbolic verification

The claim is that this combination outperforms flat LLM orchestration in task completion rate and failure recovery time under live enterprise production conditions. Baselines: single-agent ReAct, default AutoGen, and a static rule-based workflow.

## Roadmap

See [`ROADMAP.md`](ROADMAP.md).

- **Phase 1 (Months 1–12):** Requirements and architecture design.
- **Phase 2 (Months 10–28):** Prototype build and controlled evaluation.
- **Phase 3 (Months 26–42):** Industrial deployment with MCD Systems.
## Related work

In parallel with this prototype, I maintain a public learning repository
documenting hands-on experiments with LangGraph, multi-agent patterns, and
verification workflows. These experiments inform design decisions in the
EAOL prototype.

→ [agentic-AI](https://github.com/Ahsan-techie/agentic_AI)

## Licence

Apache 2.0.

## Contact

Ahsan (PhD applicant, Teesside University).
