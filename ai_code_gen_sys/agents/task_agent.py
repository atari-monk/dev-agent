from pathlib import Path
from typing import List
import yaml
from agents.code_task import CodeTask
from agents.interface.icode_agent import ICodeAgent
from ai_code_gen_sys.models.task import Task
from ai_code_gen_sys.models.element import Element

class TaskAgent:
    def __init__(self, code_agent: ICodeAgent):
        self._agent = code_agent

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
            prompt=self.get_prompt(target_element),
            output_path=tasks_path
        )
        
        self._agent.execute(task)

    def get_prompt(self, element: Element) -> str:
        return f"""
You are a Task Planner Agent. Convert this system element into implementable development tasks.

# Element Context
{element.__str__()}

{Task.format()}

# Output Rules
1. Format: Strict YAML array (no comments, no Markdown, no trailing commas)
2. Required Fields:
   - id: lowercase_snake_case (e.g. "implement_collision_check")
   - element_id: Must match parent element '{element.id}'
   - title: Action-oriented verb phrase (max 100 chars)
   - prompt: Detailed implementation requirements including:
     * Inputs/Outputs
     * Edge cases to handle
     * Performance considerations
   - status: Always "not_implemented"
   - code_language: Must match element's context
   - dependencies: List of task IDs or empty array
   - metadata: Must include:
     * complexity: (low/medium/high)
     * estimated_steps: (integer)
     * requires_review: (true/false)

# Task Generation Guidelines
- Create 1-5 tasks per element (more for complex components)
- Order tasks by logical dependency
- Include both implementation and test tasks
- For interfaces:
  * Generate "Define {{InterfaceName}}" task first
  * Follow with "Implement {{InterfaceName}} for {{Component}}"

# Example Output (YAML only):
- id: implement_message_bus
  element_id: message_system
  title: "Implement core MessageBus class"
  prompt: |
    Create a PubSub system with:
    - subscribe(event_name, callback)
    - publish(event_name, data)
    - Thread-safe operation
    - Max 1000 events/sec performance
  status: not_implemented
  code_language: python
  dependencies: []
  metadata:
    complexity: medium
    estimated_steps: 3
    requires_review: true
- id: test_message_bus
  element_id: message_system
  title: "Create MessageBus unit tests"
  prompt: |
    Verify:
    - Subscribers receive correct events
    - Thread safety under load
    - Performance benchmarks
  status: not_implemented
  code_language: python
  dependencies: [implement_message_bus]
  metadata:
    complexity: low
    estimated_steps: 2
    requires_review: false
"""