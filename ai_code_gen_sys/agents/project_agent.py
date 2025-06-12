from pathlib import Path
from agents.code_task import CodeTask
from agents.interface.icode_agent import ICodeAgent
from ai_code_gen_sys.agents.interface.iproject_agent import IProjectAgent
from ai_code_gen_sys.models.project import Project


class ProjectAgent(IProjectAgent):
    def __init__(self, base_path: Path, code_agent: ICodeAgent):
        self.project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
        self._agent = code_agent

    def open(self) -> None:
        self._agent.open()

    def close(self) -> None:
        self._agent.close()
        
    def execute(self, game_description: str) -> None:
        task = CodeTask(
            prompt=self.get_prompt(game_description),
            output_path=self.project_path,
            delay_seconds=30, overwrite=False
        )
        self._agent.execute(task)
        self._agent.close()

    def get_prompt(self, game_description: str) -> str:
        return f"""
You are a Project Architect Agent. Convert this game description into a structured project blueprint that will be processed by the System Designer Agent.

# Game Description
{game_description}

# Full Schema
{Project.format()}

# Output Rules
1. This YAML will be DIRECTLY CONSUMED by the System Designer Agent to generate technical components
2. Format: Strict YAML (no comments, no Markdown, no trailing commas)
3. Required Fields:
   - id: lowercase_snake_case (e.g. "pygame_racer")
   - name: Title Case (max 100 chars)
   - description: 1-3 sentences summarizing core gameplay (used for component generation)
   - status: Always "draft"
   - metadata: Must contain these System Designer-critical subfields:
     mvp_requirements: List of playable game mechanics (will become components/elements)
     technical_constraints: List of key tech limits (guides implementation approach)
     assets_required: List of needed resources (will create asset loader components)
   - default_language: Always "python"

# System Designer Agent Requirements
- Metadata must be machine-parsable for component generation
- mvp_requirements should map 1:1 to major systems (e.g. "Collision system" → PhysicsSystem)
- Include implied interfaces (e.g. "Lap time tracking" implies ITimer interface)

# Example Output (YAML only):
id: pygame_racer
name: Pygame Racer
description: "2D top-down racing game with AI opponents and lap timing"
status: draft
default_language: python
metadata:
  mvp_requirements:
    - Player car with acceleration/steering  # Will become InputSystem
    - AI opponents with basic pathfinding    # Will become AISystem
    - Collision system for track boundaries  # Will become PhysicsSystem
    - Lap time tracking                     # Will become TimingSystem
  technical_constraints:
    - Must use Pygame 2.5+                  # Will constrain component implementations
    - 60 FPS target                         # Will generate performance monitoring
  assets_required:
    - Race track sprite                     # Will create AssetLoader component
    - Vehicle sprites                       # Will create SpriteManager
"""