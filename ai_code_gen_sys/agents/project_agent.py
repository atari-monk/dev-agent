from pathlib import Path
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from ai_code_gen_sys.models.project import Project


class ProjectAgent:
    def __init__(self):
        self._agent = CodeAgent()

    def execute(self, base_path: Path, prompt: str) -> None:
        project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
        
        if project_path.exists():
            project = Project.load(project_path)
            if project.is_valid():
                print(f"Project already exists: {project.__str__()}")
                return
            
        task = CodeTask(
            prompt=f"{prompt}\n\nFor this game, generate yamal\n{Project.prompt()}\nDont use comments in the yaml; Write only the yaml",
            output_path=project_path
        )
        self._agent.execute(task)
