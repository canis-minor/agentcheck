from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Scenario:
    name: str
    input: str
    expected: dict[str, Any] = field(default_factory=dict)
    budgets: dict[str, float] = field(default_factory=dict)


@dataclass(slots=True)
class EvaluationResult:
    scenario: str
    passed: bool
    scores: dict[str, float]
    cost_usd: float = 0.0
    latency_ms: float = 0.0
    notes: list[str] = field(default_factory=list)
