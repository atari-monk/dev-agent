from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from ai_code_gen_sys.models.task_status import TaskStatus
from ai_code_gen_sys.models.code_language import CodeLanguage

class Task(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="Unique identifier for the task")
    element_id: str = Field(..., description="ID of the parent element")
    title: str = Field(..., max_length=100, description="Short description of the task")
    prompt: str = Field(..., description="Detailed prompt for AI code generation")
    status: TaskStatus = Field(default=TaskStatus.PENDING, description="Current status of the task")
    generated_code: Optional[str] = Field(None, description="AI-generated code for this task")
    code_language: CodeLanguage = Field(default=CodeLanguage.PYTHON, description="Programming language for this task")
    dependencies: List[str] = Field(default_factory=list, description="List of task IDs this task depends on")
    created_at: datetime = Field(default_factory=datetime.now, description="When the task was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional task metadata")

    def update_status(self, new_status: TaskStatus):
        self.status = new_status
        self.updated_at = datetime.now()