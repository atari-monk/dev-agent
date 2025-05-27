from pathlib import Path
from ai_code_gen_sys.agents.element_agent import ElementAgent


def element_agent_smoke_test():
    agent = ElementAgent(persist_session=False)
    agent.execute(Path(r"C:\atari-monk\code\race-track-game"))


if __name__ == "__main__":
    element_agent_smoke_test()