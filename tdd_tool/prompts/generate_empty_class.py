from pathlib import Path
from tdd_tool.models.task import Task
from tdd_tool.prompts.assumptions import get_standard_assumptions
from utils.string_utils import snake_to_camel


def generate_empty_class(base_path: Path, file_name: str, feature_description: str) -> Task:
    return Task(
        element_type="class",
        description_template=f"Implement empty python {{element_type}} for {feature_description}",
        file_path=base_path / file_name / f"{file_name}.py",
        assumptions=get_standard_assumptions(
            additional=[
                f"class name: {snake_to_camel(file_name)}",
                "implement the interface",
                "empty functions must raise NotImplementedError",
                "import interface: ",
                f"from {file_name}.{file_name}_interface.py import I{snake_to_camel(file_name)}",
                "implement class in a way that makes test syntax valid",
                "implement class in a way that makes test fail, as first step of tdd",
                "output only class code", 
                ]),
    )