from typing import ClassVar, Dict, Any, List, cast
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from ai_code_gen_sys.models.element_type import ElementType
import yaml
from pathlib import Path
from typing import ClassVar, Dict, Any

class Element(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="Unique identifier for the element")
    project_id: str = Field(..., description="ID of the parent project")
    name: str = Field(..., max_length=50, description="Name of the element")
    description: str = Field(..., description="Purpose and functionality of the element")
    element_type: ElementType = Field(..., description="Type of element")
    dependencies: List[str] = Field(default_factory=list, description="List of element IDs this element depends on")
    created_at: datetime = Field(default_factory=datetime.now, description="When the element was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional element metadata")

    @classmethod
    def load(cls, file_path: Path) -> 'Element':
        with open(file_path, 'r') as f:
            raw = yaml.safe_load(f)
            data = cast(Dict[str, Any], raw)
        return cls(**data)
    
    @classmethod
    def load_many(cls, file_path: Path) -> List['Element']:
        with open(file_path, 'r') as f:
            raw = yaml.safe_load(f)
            if raw is None:
                return []
            if isinstance(raw, dict):
                data: Dict[str, Any] = cast(Dict[str, Any], raw)
                return [cls(**data)]
            return [cls(**cast(Dict[str, Any], data)) for data in raw]
        
    def save(self, file_path: Path) -> None:
        with open(file_path, 'w') as f:
            yaml.dump(self.model_dump(), f, sort_keys=False)

    @classmethod
    def save_many(cls, file_path: Path, elements: List['Element']) -> None:
        with open(file_path, 'w') as f:
            yaml.dump([element.model_dump(mode='json') for element in elements], f, sort_keys=False)

    def full_description(self) -> str:
        return (
            f"id: {self.id}\n"
            f"project_id: {self.project_id}\n"
            f"name: {self.name}\n"
            f"description: {self.description}\n"
            f"element_type: {self.element_type.value}\n"
            f"dependencies: {self.dependencies}\n"
            f"created_at: {self.created_at.isoformat()}\n"
            f"updated_at: {self.updated_at.isoformat()}\n"
            f"metadata: {self.metadata}\n"
        )
    
    def __str__(self) -> str:
        return self.full_description()
    
    __schema__: ClassVar[str] = """
id: str
project_id: str
name: str
description: str
element_type: ElementType
dependencies: List[str]
created_at: datetime
updated_at: datetime
metadata: Dict[str, Any]
"""
    
    @classmethod
    def format(cls) -> str:
        return f"""
Element Schema:
{cls.__schema__}

Defaults:
element_type: (module, class, function, component, api_endpoint, database_model, configuration, test)

Key Relationships:
- Components depend on interfaces
- Systems depend on utility modules
- Tests match component naming

Metadata Standards:
- is_interface: Marks abstraction contracts
- test_coverage: Guides test generation
- task_hints: Suggested implementation steps
""" 

    def is_valid(self) -> bool:
        try:
            return all([
                self.id.strip(),
                self.project_id.strip(),
                self.name.strip(),
                self.description.strip(),
                self.created_at <= self.updated_at,
            ])
        except Exception:
            return False