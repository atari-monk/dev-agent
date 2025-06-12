# AI Code Generation System

## Models

I want to define project, elements, tasks data models in pydanticV2  
to define elements with i will generte code in ai, prompts from tasks  
will be used to generate code, project will be used to generate its elements  
then tasks are steps to implement element with code, can u propose such a structure

### Pydantic V2 Data Models for AI Code Generation System

Here's a proposed structure for your project using Pydantic V2 models. This design organizes projects into elements, and elements into tasks, with clear relationships between them for AI-powered code generation.

```python
from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class CodeLanguage(str, Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    CPP = "cpp"
    GO = "go"
    RUST = "rust"
    # Add more as needed

class Task(BaseModel):
    """Represents a single actionable step to implement part of an element"""
    model_config = ConfigDict(extra='forbid')  # Strict validation
    
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
        """Helper method to update status and timestamp"""
        self.status = new_status
        self.updated_at = datetime.now()

class ElementType(str, Enum):
    MODULE = "module"
    CLASS = "class"
    FUNCTION = "function"
    COMPONENT = "component"  # For UI frameworks
    API_ENDPOINT = "api_endpoint"
    DATABASE_MODEL = "database_model"
    CONFIG = "configuration"
    TEST = "test"

class Element(BaseModel):
    """Represents a component or building block of the project"""
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="Unique identifier for the element")
    project_id: str = Field(..., description="ID of the parent project")
    name: str = Field(..., max_length=50, description="Name of the element")
    description: str = Field(..., description="Purpose and functionality of the element")
    element_type: ElementType = Field(..., description="Type of element")
    tasks: List[Task] = Field(default_factory=list, description="Tasks needed to implement this element")
    dependencies: List[str] = Field(default_factory=list, description="List of element IDs this element depends on")
    created_at: datetime = Field(default_factory=datetime.now, description="When the element was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional element metadata")

    def add_task(self, task: Task):
        """Add a new task to this element"""
        if task.element_id != self.id:
            raise ValueError("Task's element_id must match the element's id")
        self.tasks.append(task)
        self.updated_at = datetime.now()

class ProjectStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class Project(BaseModel):
    """Top-level container for elements and tasks"""
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="Unique identifier for the project")
    name: str = Field(..., max_length=100, description="Name of the project")
    description: str = Field(..., description="Project purpose and scope")
    status: ProjectStatus = Field(default=ProjectStatus.DRAFT, description="Current status of the project")
    elements: List[Element] = Field(default_factory=list, description="Elements that make up this project")
    created_at: datetime = Field(default_factory=datetime.now, description="When the project was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional project metadata")
    default_language: CodeLanguage = Field(default=CodeLanguage.PYTHON, description="Default code language for this project")

    def add_element(self, element: Element):
        """Add a new element to this project"""
        if element.project_id != self.id:
            raise ValueError("Element's project_id must match the project's id")
        self.elements.append(element)
        self.updated_at = datetime.now()

    def find_element(self, element_id: str) -> Optional[Element]:
        """Find an element by its ID"""
        for element in self.elements:
            if element.id == element_id:
                return element
        return None

    def find_task(self, task_id: str) -> Optional[Task]:
        """Find a task by its ID across all elements"""
        for element in self.elements:
            for task in element.tasks:
                if task.id == task_id:
                    return task
        return None
```

### Key Features of This Structure:

1. **Hierarchical Organization**:
   - Project contains Elements
   - Elements contain Tasks

2. **Strict Typing**:
   - Enums for statuses, element types, and languages
   - Field validation with Pydantic V2

3. **AI Code Generation Support**:
   - Each Task has a `prompt` field for AI instructions
   - `generated_code` field stores the output
   - Language specification at both project and task levels

4. **Tracking Metadata**:
   - Creation and update timestamps
   - Custom metadata dictionaries at all levels
   - Status tracking for progress monitoring

5. **Relationship Management**:
   - Dependencies between tasks and elements
   - Helper methods for finding and adding items

### Example Usage:

```python
# Create a project
project = Project(
    id="proj_123",
    name="AI Chatbot",
    description="A conversational AI chatbot with natural language processing",
    default_language=CodeLanguage.PYTHON
)

# Add an element
chatbot_element = Element(
    id="elem_1",
    project_id=project.id,
    name="Chatbot Core",
    description="Main chatbot logic and conversation handling",
    element_type=ElementType.MODULE
)
project.add_element(chatbot_element)

# Add tasks to the element
init_task = Task(
    id="task_1",
    element_id=chatbot_element.id,
    title="Initialize chatbot class",
    prompt="Create a Python class called Chatbot with basic initialization that takes a configuration dictionary",
    code_language=CodeLanguage.PYTHON
)

nlp_task = Task(
    id="task_2",
    element_id=chatbot_element.id,
    title="Add NLP processing",
    prompt="Add natural language processing methods to the Chatbot class using the NLTK library",
    code_language=CodeLanguage.PYTHON,
    dependencies=["task_1"]  # Depends on the initialization task
)

chatbot_element.add_task(init_task)
chatbot_element.add_task(nlp_task)
```

This structure gives you a solid foundation for managing AI-generated code projects with clear relationships between components and proper tracking of the generation process.