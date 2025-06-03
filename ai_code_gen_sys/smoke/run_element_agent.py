from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.element_agent import ElementAgent
from ai_code_gen_sys.models.project import Project

def smoke_test(base_path: Path) -> None:
    print("Running Element Agent smoke test")
    agent = ElementAgent(base_path, CodeAgent(ChatGPTAgent()))
    agent.open()
    agent.execute(get_project(base_path))
    agent.close()

def get_project(base_path: Path):
    project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
    if not project_path.exists():
        raise FileNotFoundError("Project file not found")
    project = Project.load(project_path)
    if not project.is_valid():
        raise ValueError("Invalid project configuration")
    return project

def mock_smoke_test(base_path: Path) -> None:
    print("Running Mock Element Agent smoke test")
    agent = ElementAgent(base_path, CodeAgentMock(ChatGPTAgentMock()))
    agent.open()
    agent.execute(get_project(base_path))
    agent.close()

def main(mock: bool = False) -> None:
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    if not mock:
        smoke_test(base_path)
    else:
        mock_smoke_test(base_path)

if __name__ == "__main__":
    main()