from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    feature: str
    name: str
    requirements: List[str]
    assigned_to: str
    status: str

