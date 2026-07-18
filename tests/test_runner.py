from agentcheck.models import Scenario
from agentcheck.runner import run_scenario


def test_passing_scenario() -> None:
    scenario = Scenario(name="basic", input="hello")
    result = run_scenario(scenario, lambda _: {"task_success": True})
    assert result.passed
