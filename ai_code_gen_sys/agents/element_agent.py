from pathlib import Path
from agents.code_task import CodeTask
from agents.interface.icode_agent import ICodeAgent
from ai_code_gen_sys.models.project import Project
from ai_code_gen_sys.models.element import Element


class ElementAgent:
    def __init__(self, code_agent: ICodeAgent):
        self._agent = code_agent

    def execute(self, base_path: Path) -> None:
        project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
        elements_path = base_path / "docs" / "ai_code_gen_sys" / "elements.yaml"
        
        if not project_path.exists():
            raise FileNotFoundError("Project file not found")
            
        project = Project.load(project_path)
        if not project.is_valid():
            raise ValueError("Invalid project configuration")
        
        task = CodeTask(
            prompt=f"""""",
            output_path=elements_path
        )
        
        self._agent.execute(task)

    def get_prompt(self, project: Project) -> str:
        return f"""You are an element agent that generates elements for a project.
For a project:
{project.__str__()}
Generate elements using this schema:
{Element.prompt()}
Requirements:
- Output valid YAML array of elements
- No comments in YAML
- Include all required fields"""