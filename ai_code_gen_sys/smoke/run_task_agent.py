from pathlib import Path
from typing import List
import yaml
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.task_agent import TaskAgent
from ai_code_gen_sys.models.element import Element

def smoke_test(base_path: Path) -> None:
    print("Running Task Agent smoke test")
    agent = TaskAgent(base_path, CodeAgent(ChatGPTAgent()))
    agent.open()
    run_on_elements(base_path, agent)
    agent.close()

def run_on_elements(base_path: Path, agent: TaskAgent):
    for element in getElement(base_path):
        if not element.is_valid():
            print(f"Element {element.id} is invalid")
            continue
        agent.execute(element)

def getElement(base_path: Path) -> List[Element]:
    elements_path = base_path / "docs" / "ai_code_gen_sys" / "elements.yaml"
    if not elements_path.exists():
        raise FileNotFoundError("Elements file not found")
    with open(elements_path, 'r') as f:
        elements: List[Element] = [Element(**e) for e in yaml.safe_load(f)]
    return elements

def mock_smoke_test(base_path: Path) -> None:
    print("Running Mock Task Agent smoke test")
    agent = TaskAgent(base_path, CodeAgentMock(ChatGPTAgentMock()))
    run_on_elements(base_path, agent)

def main(mock: bool = False) -> None:
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    if not mock:
        smoke_test(base_path)
    else:
        mock_smoke_test(base_path)

if __name__ == "__main__":
    main()