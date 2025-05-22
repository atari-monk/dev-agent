from pathlib import Path
from game_tool.models.task import Task
from game_tool.models.task_type import TaskType
from game_tool.prompts.assumptions import get_standard_assumptions


def generate_test_task(base_path: Path, file_name: str, feature_description: str
    ) -> Task:
        file_path = base_path / file_name / f"test_{file_name}.py"
        
        assumptions = get_standard_assumptions(additional=[
            "Output ONLY unit test code",
            "import interface and class from dir of test file"
        ])

        description = (
            f"Implement python pytest unit test for {feature_description} use the interface, "
            f"inject the class, and test the class."
        )

        return Task(
            assumptions=assumptions,
            description=description,
            file_path=file_path,
            task_type=TaskType.Test,
        )