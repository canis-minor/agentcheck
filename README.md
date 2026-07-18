# Agent Tester

Regression testing and continuous evaluation for AI agents.

Agent Tester treats prompts, tools, policies, models, and memory changes as
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

## Core capabilities

- Declarative test scenarios
- Deterministic and model-based evaluators
- Baseline-versus-candidate comparison
- Cost and latency budgets
- Flakiness tracking
- CI-friendly pass/fail reports

## Example

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
agent-tester run examples/suite.yaml
```

## Research questions

1. How can evaluation sampling reduce cost without hiding regressions?
2. How should confidence intervals affect deployment gates?
3. How do we separate model variance from real regressions?
4. Which trajectory-level signals best predict task failure?

## Status

CLI and evaluation contract scaffold.
