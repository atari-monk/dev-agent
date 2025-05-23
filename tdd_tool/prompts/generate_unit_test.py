from pathlib import Path
from tdd_tool.models.task import Task
from tdd_tool.prompts.assumptions import get_standard_assumptions


def generate_unit_test(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        element_type="unit test",
        description_template=f"Implement python pytest {{element_type}} for {feature_description}",
        file_path=base_path / file_name / f"test_{file_name}.py",
        assumptions=get_standard_assumptions(additional=["Output ONLY unit test code", "use the interface", "inject tested code", "import interface and tested code from dir of test file", "It is TDD test", "Initially all test should fail due to lack of implementation", "test features/requirements of code under test"]),
)