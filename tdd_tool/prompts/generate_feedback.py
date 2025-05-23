from pathlib import Path
from tdd_tool.models.task import Task
from tdd_tool.prompts.assumptions import get_standard_assumptions


def generate_feedback(feature_description: str) -> Task:
    return Task(
        element_type="Code feedback",
        description_template=f"{{element_type}}:\n{feature_description}",
        file_path=Path(),
        assumptions=get_standard_assumptions(),
    )

def generate_tests_feedback(feature_description: str) -> Task:
    return Task(
        element_type="Tests feedback",
        description_template=f"{{element_type}}:\n{feature_description}",
        file_path=Path(),
        assumptions=get_standard_assumptions(additional=["Respond with only OK and wait for next task"]),
    )