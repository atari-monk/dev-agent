from pathlib import Path
from game_tool.models.task import Task
from game_tool.models.task_type import TaskType
from game_tool.prompts.assumptions import get_standard_assumptions


def generate_interface(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        assumptions=get_standard_assumptions(additional=["Output only interface code"]),
        description=f"Implement python Protocol based pure interface for {feature_description}",
        file_path=base_path / file_name / f"{file_name}_interface.py",
        task_type=TaskType.Code,
)