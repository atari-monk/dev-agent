from pathlib import Path
from pydantic import BaseModel
from typing import List
from game_tool.models.task_type import TaskType


class Task(BaseModel):
    assumptions: List[str]
    description: str
    file_path: Path
    task_type: TaskType

    def generate_prompt(self) -> str:
        assumptions_text = "; ".join(self.assumptions)
        return (
            f"{assumptions_text}. "
            f"{self.description}. "
        )