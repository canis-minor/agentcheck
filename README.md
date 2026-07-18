> This repository is part of the **[Reliable Long-Running Agents (RLRA)](https://github.com/canis-minor)** research initiative.

# AgentCheck

**Regression testing, evaluation, and quality gates for AI agents.**

![status: research prototype](https://img.shields.io/badge/status-research%20prototype-orange)

> Siblings in the RLRA stack —
> [TypedMem](https://github.com/canis-minor/typedmem) ·
> **AgentCheck** ·
> [AgentTrace](https://github.com/canis-minor/agenttrace) ·
> [ReliAgent Bench](https://github.com/canis-minor/reliagent-bench) ·
> [AgentLab](https://github.com/canis-minor/agentlab)

AgentCheck treats prompts, tools, policies, models, and memory changes as
versioned software changes. It runs repeatable scenarios and compares quality,
cost, latency, and reliability before a change reaches production.

## Vision

```text
agent change
    ↓
scenario suite
    ↓
execution traces
    ↓
evaluators
    ↓
quality gate
```

## Planned capabilities

- Declarative test scenarios
- Deterministic and model-based evaluators
- Baseline-versus-candidate comparison
- Cost and latency budgets
- Flakiness tracking
- CI-friendly pass/fail reports
- Safety / policy checks

## Example scenario

```yaml
name: password-reset
input: "Help me reset my password"
expect:
  task_success: true
  forbidden_actions: []
budgets:
  max_cost_usd: 0.05
  max_latency_ms: 5000
```

## Quick start

```bash
pip install -e .
agentcheck run examples/suite.yaml
```

## Research questions

1. How can evaluation sampling reduce cost without hiding regressions?
2. How should confidence intervals affect deployment gates?
3. How do we separate model variance from real regressions?
4. Which trajectory-level signals best predict task failure?

## Status

**Research prototype.** CLI and evaluation-contract scaffold only — the runner loads a
scenario file and reports counts. Evaluators, budgets, and comparison are not yet
implemented. Designed to consume traces from
[AgentTrace](https://github.com/canis-minor/agenttrace) and run task sets from
[ReliAgent Bench](https://github.com/canis-minor/reliagent-bench).
