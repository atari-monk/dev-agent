from pathlib import Path
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from ai_code_gen_sys.models.project import Project


class ProjectAgent:
    def __init__(self):
        self._agent = CodeAgent()

    def execute(self, base_path: Path, game_description: str) -> None:
        project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
        
        if project_path.exists():
            project = Project.load(project_path)
            if project.is_valid():
                print(f"Project already exists: {project.__str__()}")
                print("Skipping project creation.")
                return
                        
        task = CodeTask(
            prompt=self.get_prompt(game_description),
            output_path=project_path
        )
        self._agent.execute(task)
        self._agent.close()

    def get_prompt(self, game_description:str) -> str:
        return f"""
        You are a project agent that creates a project file for the AI Code Generation System.
        For a game:\n\n
        {game_description}\n\n
        You will generate a YAML file:\n\n
        {Project.format()}\n\n
        Requirements:
        - Dont use comments in the yaml.
        - Write only the yaml.
        - Use metadata to store the game requirements.
        - Define playable game mechanic MVP (Minimum Viable Product).
        """