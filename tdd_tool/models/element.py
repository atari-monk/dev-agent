from pydantic import BaseModel


from typing import List


class Element(BaseModel):
    name: str
    description: str
    requirements: List[str]

    @property
    def snake_case_name(self) -> str:
        return self.name.lower().replace(' ', '_')

    @property
    def requirements_text(self) -> str:
        return "; ".join(self.requirements)

    @property
    def description_with_requirements(self) -> str:
        requirements_part = f"Requirements: {self.requirements_text}" if self.requirements else ""
        return f"{self.description}\n{requirements_part}".strip()