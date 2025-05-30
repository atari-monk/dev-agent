from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.element_agent import ElementAgent


def smoke_test(base_path: Path) -> None:
    print("Running Element Agent smoke test")
    agent = ElementAgent(base_path, CodeAgent(ChatGPTAgent()))
    agent.execute()

def mock_smoke_test(base_path: Path) -> None:
    print("Running Mock Element Agent smoke test")
    agent = ElementAgent(base_path, CodeAgentMock(ChatGPTAgentMock()))
    agent.execute()

def main(mock: bool = False) -> None:
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    if not mock:
        smoke_test(base_path)
    else:
        mock_smoke_test(base_path)

if __name__ == "__main__":
    main(True)