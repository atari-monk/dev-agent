from pathlib import Path
from ai_code_gen_sys.agents.task_agent import TaskAgent


def task_agent_smoke_test():
    agent = TaskAgent()
    agent.execute(Path(r"C:\atari-monk\code\race-track-game"), "game_loop_module")


if __name__ == "__main__":
    task_agent_smoke_test()