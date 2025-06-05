from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class FeatureFile(BaseModel):
    file: str
    path: str
    class_: Optional[str] = Field(default=None, alias="class")

class Task(BaseModel):
    id: str
    status: str
    assigned_to: str
    requirements: List[str]
    files: List[str]
    depends_on: Optional[List[str]] = None

class Feature(BaseModel):
    name: str
    status: Optional[str] = "pending"
    requirements: List[str]
    files: Dict[str, FeatureFile]
    tasks: Optional[List[Task]] = None

class Agent(BaseModel):
    role: str
    requirements: List[str]

class Project(BaseModel):
    name: str
    path: str
    dependencies: List[str]
    requirements: List[str]

class CodeRequirements(BaseModel):
    requirements: List[str]

class Automation(BaseModel):
    project: Project
    code_requirements: CodeRequirements
    agents: List[Agent]
    features: List[Feature]
