from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.interface.iproject_agent import IProjectAgent
from ai_code_gen_sys.agents.mock.project_agent_mock import ProjectAgentMock
from ai_code_gen_sys.agents.project_agent import ProjectAgent


def project_agent_smoke_test(mocked: bool = False) -> None:
    agent: IProjectAgent
    if mocked:
        print("Running ProjectAgentMock smoke test")
        agent = ProjectAgentMock(CodeAgentMock(ChatGPTAgentMock()))
    else:
        print("Running ProjectAgent smoke test")
        agent =  ProjectAgent(CodeAgent(ChatGPTAgent()))

    agent.execute(Path(r"C:\atari-monk\code\race-track-game"), 
        "Racing game with Pygame featuring: "
        "2D graphics, player car, AI opponents, circular race track, "
        "collision system and lap timing")


if __name__ == "__main__":
    project_agent_smoke_test(True)