from pathlib import Path
from tdd_tool.models.task import Task
from tdd_tool.prompts.assumptions import get_standard_assumptions


def generate_feedback(feature_description: str) -> Task:
    return Task(
        element_type="feedback",
        description_template=f"Fix these issues {feature_description}",
        file_path=Path(),
        assumptions=get_standard_assumptions(),
    )

def generate_tests_feedback(feature_description: str) -> Task:
    return Task(
        element_type="tests feedback",
        description_template=f"Tests results:\n{feature_description}",
        file_path=Path(),
        assumptions=get_standard_assumptions(additional=["Respond with only OK and wait for next task"]),
    )