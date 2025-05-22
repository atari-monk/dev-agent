from pathlib import Path
from game_tool.models.task import Task
from game_tool.models.task_type import TaskType
from game_tool.prompts.assumptions import get_standard_assumptions


def generate_empty_class(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        assumptions=get_standard_assumptions(additional=["Output only class code"]),
        description=f"Implement empty python class for {feature_description} implementing the interface",
        file_path=base_path / file_name / f"{file_name}.py",
        task_type=TaskType.Code,
    )