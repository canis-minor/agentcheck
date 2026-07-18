from collections.abc import Callable
from typing import Any

from .models import EvaluationResult, Scenario

AgentCallable = Callable[[str], dict[str, Any]]


def run_scenario(scenario: Scenario, agent: AgentCallable) -> EvaluationResult:
    output = agent(scenario.input)
    success = bool(output.get("task_success", False))
    return EvaluationResult(
        scenario=scenario.name,
        passed=success,
        scores={"task_success": float(success)},
        cost_usd=float(output.get("cost_usd", 0.0)),
        latency_ms=float(output.get("latency_ms", 0.0)),
    )
