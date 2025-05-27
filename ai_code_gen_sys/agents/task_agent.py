from pathlib import Path
from typing import List
import yaml
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from ai_code_gen_sys.models.task import Task
from ai_code_gen_sys.models.element import Element

class TaskAgent:
    def __init__(self, persist_session: bool = False):
        self._agent = CodeAgent(persist_session=persist_session)

    def execute(self, base_path: Path, element_id: str) -> None:
        elements_path = base_path / "docs" / "ai_code_gen_sys" / "elements.yaml"
        tasks_path = base_path / "docs" / "ai_code_gen_sys" / "tasks.yaml"
        
        if not elements_path.exists():
            raise FileNotFoundError("Elements file not found")
            
        with open(elements_path, 'r') as f:
            elements: List[Element] = [Element(**e) for e in yaml.safe_load(f)]
        
        target_element = next((e for e in elements if e.id == element_id), None)
        if not target_element:
            raise ValueError(f"Element {element_id} not found")
        
        if not target_element.is_valid():
            raise ValueError(f"Element {element_id} is invalid")
        
        task = CodeTask(
            prompt=f"""Element Context:
{target_element.full_description()}

Generate tasks for this element using schema:
{Task.to_prompt()}

Requirements:
- Output valid YAML array of tasks
- Each task must reference element_id: {element_id}
- No comments in YAML""",
            output_path=tasks_path
        )
        
        self._agent.execute(task)