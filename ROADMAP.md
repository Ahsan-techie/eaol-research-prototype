# EAOL Roadmap

This roadmap mirrors the methodology in the research proposal. It will be revised as the supervisor reviews and Phase 1 findings update the plan.

## Phase 1: Requirements and architecture design (Months 1–12)

- Months 1–3: Ethics approval. GDPR data-sharing agreement with MCD Systems. Systematic literature review begins.
- Months 4–8: Structured interviews with MCD Systems teams across ERP, CRM, document management, and SQL-based legacy environments.
- Months 6–12: Formal artefact design (agent model, task schema, contract-net bidding, fast-path/verified-path classifier, PDDL verification layer, interruptibility interface, UML documentation, baseline calibration).
- Month 6 review: Supervisor agreement on the simulation-fallback contingency for Phase 3.

## Phase 2: Prototype and controlled evaluation (Months 10–28)

Months 10–12 overlap with Phase 1.

- Build the EAOL prototype on LangGraph or AutoGen.
- Evaluate against three baselines: single-agent ReAct, default AutoGen, static rule-based.
- 50 episodes per condition for 80% statistical power (α = 0.05).
- Ablations: each of the three innovations removed independently.
- SUS usability evaluation with 10 MCD Systems participants (5 technical, 5 operational), threshold 68.

## Phase 3: Industrial deployment (Months 26–42)

- Shadow-mode evaluation, then controlled live execution under fast-path / verified-path.
- High-risk tasks behind human approval gates. Audit logs and rollback checkpoints throughout.
- Longitudinal SUS: same participants from Phase 2 complete a second assessment.
- Production metrics: latency, throughput, error rates, API cost per task.
- Contingency: if live access is unavailable by Month 28, the thesis pivots to a simulation-validated EAOL.

## Year 4: Thesis and dissemination

Thesis write-up. Papers drafted progressively across Phases 1–3 (target: 2–3 papers). Apache 2.0 release of the framework and evaluation harness.
