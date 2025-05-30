from typing import ClassVar, Dict, Any, cast
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from ai_code_gen_sys.models.code_language import CodeLanguage
from ai_code_gen_sys.models.project_status import ProjectStatus
import yaml
from pathlib import Path
from typing import ClassVar, Dict, Any

class Project(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="Unique identifier for the project")
    name: str = Field(..., max_length=100, description="Name of the project")
    description: str = Field(..., description="Project purpose and scope")
    status: ProjectStatus = Field(default=ProjectStatus.DRAFT, description="Current status of the project")
    created_at: datetime = Field(default_factory=datetime.now, description="When the project was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional project metadata")
    default_language: CodeLanguage = Field(default=CodeLanguage.PYTHON, description="Default code language for this project")

    @classmethod
    def load(cls, file_path: Path) -> 'Project':
        with open(file_path, 'r') as f:
            raw = yaml.safe_load(f)
            data = cast(Dict[str, Any], raw)
        return cls(**data)

    def save(self, file_path: Path) -> None:
        with open(file_path, 'w') as f:
            yaml.dump(self.model_dump(), f, sort_keys=False)

    def format_metadata(self, indent: int = 2) -> str:
        if not self.metadata:
            return "{}"
        yaml_str = yaml.dump(self.metadata, 
            sort_keys=False, 
            default_flow_style=False,
            indent=indent)
        return yaml_str.strip()

    def full_description(self) -> str:
        return (
            f"id: {self.id}\n"
            f"name: {self.name}\n"
            f"description: {self.description}\n"
            f"status: {self.status.value}\n"
            f"created_at: {self.created_at.isoformat()}\n"
            f"updated_at: {self.updated_at.isoformat()}\n"
            f"metadata: \n{self.format_metadata()}\n"
            f"default_language: {self.default_language.value}"
        )

    def __str__(self) -> str:
        return self.full_description()
    
    __schema__: ClassVar[str] = """
id: str
name: str
description: str
status: ProjectStatus
created_at: datetime
updated_at: datetime
metadata: Dict[str, Any]
default_language: CodeLanguage"""

    @classmethod
    def format(cls, status: ProjectStatus = ProjectStatus.DRAFT, language: CodeLanguage = CodeLanguage.PYTHON) -> str:
        return f"""{cls.__schema__}Defaults:
status: {status.value}
default_language: {language.value}
"""

    def is_valid(self) -> bool:
        try:
            return all([
                self.id.strip(),
                self.name.strip(),
                self.description.strip(),
                self.created_at <= self.updated_at,
            ])
        except Exception:
            return False