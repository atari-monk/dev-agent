from pathlib import Path
from tdd_tool.models.task import Task
from tdd_tool.prompts.assumptions import get_standard_assumptions


def generate_empty_class(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        element_type="class",
        description_template=f"Implement empty python class for {feature_description}",
        file_path=base_path / file_name / f"{file_name}.py",
        assumptions=get_standard_assumptions(additional=["output only class code", "implement the interface", "import interface from dir of class file", "functions empty with pass"]),
    )