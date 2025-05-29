from pathlib import Path
from ai_code_gen_sys.agents.implementation_agent import ImplementationAgent


def implementation_agent_smoke_test():
    agent = ImplementationAgent()
    agent.execute(Path(r"C:\atari-monk\code\race-track-game"), "game_loop")


if __name__ == "__main__":
    implementation_agent_smoke_test()