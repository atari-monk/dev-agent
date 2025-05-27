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
    
    def save(self, file_path: Path) -> None:
        with open(file_path, 'w') as f:
            yaml.dump(self.model_dump(), f, sort_keys=False)

    def element_to_str(self) -> str:
        return (
            f"Element(id={self.id}, name={self.name}, "
            f"element_type={self.element_type.value}, "
            f"project_id={self.project_id})"
        )
    
    def __str__(self) -> str:
        return self.element_to_str()
    
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
    def prompt(cls) -> str:
        return f"""
        Element Schema:
        {cls.__schema__}
        Defaults:
        element_type: (module, class, function, component, api_endpoint, database_model, configuration, test)
        """
    
    def is_valid(self) -> bool:
        return all([
            bool(self.id),
            bool(self.name),
            bool(self.description),
            bool(self.project_id)
        ])