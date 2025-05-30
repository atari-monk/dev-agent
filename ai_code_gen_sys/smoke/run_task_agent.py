from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from ai_code_gen_sys.agents.task_agent import TaskAgent


def task_agent_smoke_test():
    agent = TaskAgent(CodeAgent(ChatGPTAgent()))
    agent.execute(Path(r"C:\atari-monk\code\race-track-game"), "game_loop")


if __name__ == "__main__":
    task_agent_smoke_test()