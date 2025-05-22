from pathlib import Path
from pydantic import BaseModel
from typing import List


class Task(BaseModel):
    element_type: str
    description_template: str
    file_path: Path
    assumptions: List[str]

    @property
    def description(self) -> str:
        return self.description_template.format(element_type=self.element_type)
    
    @property
    def assumptions_text(self) -> str:
        return "; ".join(self.assumptions)
    
    def generate_prompt(self) -> str:
        return (
            f"{self.assumptions_text}. "
            f"{self.description}. "
        )
    
    def generate_fix_prompt(self) -> str:
        return (
            f"{self.assumptions_text}. "
            f"Fix test feedback issues in {self.element_type}."
        )