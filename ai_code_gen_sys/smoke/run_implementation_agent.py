from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.implementation_agent import ImplementationAgent
from ai_code_gen_sys.models.element import Element

def smoke_test(base_path: Path, elements_path:Path) -> None:
    agent = ImplementationAgent(CodeAgent(ChatGPTAgent()))
    elements = Element.load_many(elements_path)
    for element in elements:
        agent.open()
        agent.execute(base_path, element)
        agent.close()

def mock_smoke_test(base_path: Path, elements_path:Path) -> None:
    agent = ImplementationAgent(CodeAgentMock(ChatGPTAgentMock()))
    elements = Element.load_many(elements_path)
    for element in elements:
        agent.open()
        agent.execute(base_path, element)
        agent.close()

def main(mock: bool = False) -> None:
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    elements_path = base_path / "docs" / "ai_code_gen_sys" / "elements.yaml"
    if not mock:
        smoke_test(base_path, elements_path)
    else:
        mock_smoke_test(base_path, elements_path)
        
if __name__ == "__main__":
    main()