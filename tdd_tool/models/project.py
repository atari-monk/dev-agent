from pydantic import BaseModel


from pathlib import Path
from typing import List


class Project(BaseModel):
    project_name: str
    repo_base_path: Path
    repo_name: str
    assumptions: List[str]

    @property
    def repo_path(self) -> Path:
        return self.repo_base_path / self.repo_name