from pathlib import Path
from agents.code_task import CodeTask
from agents.interface.icode_agent import ICodeAgent
from ai_code_gen_sys.agents.interface.ielement_agent import IElementAgent
from ai_code_gen_sys.models.project import Project
from ai_code_gen_sys.models.element import Element
from pathlib import Path

class ElementAgent(IElementAgent):
    def __init__(self, base_path: Path, code_agent: ICodeAgent):
        self.elements_path = base_path / "docs" / "ai_code_gen_sys" / "elements.yaml"
        self._agent = code_agent

    def open(self) -> None:
        self._agent.open()

    def close(self) -> None:
        self._agent.close()

    def execute(self, project:Project) -> None:        
        task = CodeTask(
            prompt=self.get_prompt(project),
            output_path=self.elements_path,
            delay_seconds=80,
            overwrite=False
        )
        self._agent.execute(task)
        self._agent.close()

    def get_prompt(self, project: Project) -> str:
        return f"""
You are a System Designer Agent. Transform this project into technical elements that will be processed by the Task Planner Agent.

# Project Context (From Project Architect Agent)
{project.__str__()}

# Task Planner Agent Preparation
Your output will DIRECTLY feed the Task Planner Agent which will:
1. Create implementation tasks for each element
2. Establish task dependencies based on your element dependencies
3. Use your metadata to prioritize work

# Output Requirements
1. Format: Strict YAML array (no comments, no Markdown)
2. Required Fields:
   - id: lowercase_snake_case (e.g. 'physics_system')
   - project_id: Always '{project.id}'
   - name: Human-readable name (max 50 chars)
   - description: Implementation-focused 1-2 sentences
   - element_type: From schema below
   - dependencies: List of element IDs or []
   - metadata: Must include:
     * task_hints: List of suggested task titles (e.g. ["Implement collision detection", "Create unit tests"])

{Element.format()}

# System Design Rules
- Create 5-15 elements covering ALL project requirements
- Ensure dependency closure (if A → B, B must exist)
- Follow these patterns:
  * Interfaces: prefix with 'I' (e.g. 'ICollidable')
  * Components: suffix with 'System' (e.g. 'PhysicsSystem')
  * Tests: suffix with '_tests' (e.g. 'physics_tests')
- Metadata must contain:
  is_interface: (true/false)
  test_coverage: (unit/integration/none)
  stability: (experimental/stable/deprecated)

# Example Output (YAML only):
- id: input_system
  project_id: proj_123
  name: Input System
  description: "Handles player controls and input mapping"
  element_type: component
  dependencies: [message_bus]
  metadata:
    is_interface: false
    test_coverage: unit
    task_hints: ["Implement keyboard controls", "Create input mapping config"]
- id: irenderable
  project_id: proj_123
  name: IRenderable
  description: "Interface for renderable game objects"
  element_type: interface
  dependencies: []
  metadata:
    is_interface: true
    task_hints: ["Define render contract", "Implement for PlayerCar"]
"""