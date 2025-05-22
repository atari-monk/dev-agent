from pathlib import Path
from game_tool.models.task import Task
from game_tool.models.task_type import TaskType
from game_tool.prompts.assumptions import get_standard_assumptions


def generate_unit_test(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        assumptions=get_standard_assumptions(additional=["Output ONLY unit test code", "import interface and class from dir of test file"]),
        description=f"Implement python pytest unit test for {feature_description} use the interface, inject the class, and test the class",
        file_path=base_path / file_name / f"test_{file_name}.py",
        task_type=TaskType.Code,
)