from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from ai_code_gen_sys.agents.implementation_agent import ImplementationAgent
from ai_code_gen_sys.models.element import Element

def smoke_test():
    agent = ImplementationAgent(CodeAgent(ChatGPTAgent()))
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    elements_path = base_path / "docs" / "ai_code_gen_sys" / "elements.yaml"
    elements = Element.load_many(elements_path)
    for element in elements:
        agent.execute(base_path, element)

if __name__ == "__main__":
    smoke_test()