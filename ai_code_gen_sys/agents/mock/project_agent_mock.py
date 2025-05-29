from pathlib import Path
from agents.code_task import CodeTask
from agents.interface.icode_agent import ICodeAgent
from ai_code_gen_sys.agents.interface.iproject_agent import IProjectAgent
from ai_code_gen_sys.models.project import Project


class ProjectAgentMock(IProjectAgent):
    def __init__(self, code_agent: ICodeAgent):
        self._agent = code_agent

    def execute(self, base_path: Path, game_description: str) -> None:
        project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
                        
        task = CodeTask(
            prompt=self.get_prompt(game_description),
            output_path=project_path
        )
        self._agent.execute(task)
        self._agent.close()

    def get_prompt(self, game_description:str) -> str:
        return f"""You are a project agent that creates a project file for the AI Code Generation System.
For a game: {game_description}
Generate a YAML file with schema: {Project.format()}Requirements:
- Use metadata to store the game requirements, which define playable game mechanic MVP (Minimum Viable Product).
- Dont use comments in the yaml.
- Write only the yaml."""