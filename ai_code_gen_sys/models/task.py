from pathlib import Path
from typing import ClassVar, List, Optional, Dict, Any, cast
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

import yaml
from ai_code_gen_sys.models.task_status import TaskStatus
from ai_code_gen_sys.models.code_language import CodeLanguage

class Task(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="Unique identifier for the task")
    element_id: str = Field(..., description="ID of the parent element")
    title: str = Field(..., max_length=100, description="Short description of the task")
    prompt: str = Field(..., description="Detailed prompt for AI code generation")
    status: TaskStatus = Field(default=TaskStatus.NOT_IMPLEMENTED, description="Current status of the task")
    generated_code: Optional[str] = Field(None, description="AI-generated code for this task")
    code_language: CodeLanguage = Field(default=CodeLanguage.PYTHON, description="Programming language for this task")
    dependencies: List[str] = Field(default_factory=list, description="List of task IDs this task depends on")
    created_at: datetime = Field(default_factory=datetime.now, description="When the task was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional task metadata")

    def update_status(self, new_status: TaskStatus):
        self.status = new_status
        self.updated_at = datetime.now()

    @classmethod
    def load(cls, file_path: Path) -> 'Task':
        with open(file_path, 'r') as f:
            raw = yaml.safe_load(f)
            data = cast(Dict[str, Any], raw)
        return cls(**data)

    @classmethod
    def load_many(cls, file_path: Path) -> List['Task']:
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
            yaml.dump(self.model_dump(mode='json'), f, sort_keys=False)
    
    @classmethod
    def save_many(cls, file_path: Path, tasks: List['Task']) -> None:
        with open(file_path, 'w') as f:
            yaml.dump([task.model_dump(mode='json') for task in tasks], f, sort_keys=False)

    def update_task(self, file_path: Path, update_data: Dict[str, Any]) -> None:
        task = Task.load(file_path)
        for field, value in update_data.items():
            if field in Task.model_fields:
                setattr(task, field, value)
        task.updated_at = datetime.now()
        task.save(file_path)

    @classmethod
    def update_task_in_file(cls, file_path: Path, task_id: str, update_data: Dict[str, Any]) -> None:
        tasks = cls.load_many(file_path)
        updated = False
        
        for task in tasks:
            if task.id == task_id:
                for field, value in update_data.items():
                    if field in Task.model_fields:
                        setattr(task, field, value)
                task.updated_at = datetime.now()
                updated = True
                break
        
        if not updated:
            raise ValueError(f"Task with id {task_id} not found in file")
        
        cls.save_many(file_path, tasks)

    def full_description(self) -> str:
        return (
            f"id: {self.id}\n"
            f"element_id: {self.element_id}\n"
            f"title: {self.title}\n"
            f"prompt: {self.prompt}\n"
            f"status: {self.status.value}\n"
            f"code_language: {self.code_language.value}\n"
            f"generated_code: {self.generated_code}\n"
            f"dependencies: {self.dependencies}\n"
            f"created_at: {self.created_at.isoformat()}\n"
            f"updated_at: {self.updated_at.isoformat()}\n"
            f"metadata: {self.metadata}\n"
        )
    
    def __str__(self) -> str:
        return self.full_description()
    
    __schema__: ClassVar[str] = """
    id: str
    element_id: str
    title: str
    prompt: str
    status: TaskStatus
    generated_code: Optional[str]
    code_language: CodeLanguage
    dependencies: List[str]
    created_at: datetime
    updated_at: datetime
    metadata: Dict[str, Any]
    """

    @classmethod
    def format(cls) -> str:
        return f"""
Task Schema:
{cls.__schema__}

Defaults:
status: (pending)
code_language: (python)

Required Metadata Fields:
- complexity: (low|medium|high)
- estimated_steps: (integer)
- requires_review: (true|false)

Common Task Types:
1. Implementation (prefix with 'implement_')
2. Testing (prefix with 'test_')
3. Interface Definition (prefix with 'define_')
4. Integration (prefix with 'integrate_')
"""

    def is_valid(self) -> bool:
        try:
            return all([
                self.id.strip(),
                self.element_id.strip(),
                self.title.strip(),
                self.prompt.strip(),
                self.created_at <= self.updated_at,
            ])
        except Exception:
            return False