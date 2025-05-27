from pathlib import Path
from ai_code_gen_sys.agents.project_agent import ProjectAgent


def project_agent_smoke_test():
    agent = ProjectAgent(persist_session=False)
    agent.execute(Path(r"C:\atari-monk\code\race-track-game"), 
        "Create racing game with Pygame featuring: "
        "2D graphics, player car, AI opponents, "
        "collision system and lap timing")


if __name__ == "__main__":
    project_agent_smoke_test()