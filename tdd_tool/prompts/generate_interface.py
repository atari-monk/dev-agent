from pathlib import Path
from tdd_tool.models.task import Task
from tdd_tool.prompts.assumptions import get_standard_assumptions
from utils.string_utils import snake_to_camel


def generate_interface(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        element_type="interface",
        description_template=f"Implement python Protocol based pure {{element_type}} for {feature_description}",
        file_path=base_path / file_name / f"{file_name}_interface.py",
        assumptions=get_standard_assumptions(additional=["Output only interface code", f"Interface name I{snake_to_camel(file_name)}"]),
)