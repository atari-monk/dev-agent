from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.project_agent import ProjectAgent

def smoke_test(base_path: Path, game_description:str) -> None:
    print("Running Project Agent smoke test")
    agent =  ProjectAgent(base_path, CodeAgent(ChatGPTAgent()))
    agent.open()
    agent.execute(game_description)
    agent.close()

def mock_smoke_test(base_path: Path, game_description:str) -> None:
    print("Running Mocked Project Agent smoke test")
    agent = ProjectAgent(base_path, CodeAgentMock(ChatGPTAgentMock()))
    agent.open()
    agent.execute(game_description)
    agent.close()
        
def main(mock: bool = False) -> None:
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    game_description = """Goal: Generate a minimal runnable Pygame racing game with:
A 800x600 black window.
A player car (red rectangle) controllable with arrow keys (up/down/left/right).
Basic game loop (60 FPS) with exit-on-close.
Constraints:
No track, AI, or collisions yet.
Use Pygame (pygame.init(), pygame.display.set_mode()).
Player car must be a class (PlayerCar) with draw() and move() methods.
Code must run without errors when executed.
"""
    if not mock:
        smoke_test(base_path, game_description)
    else:
        mock_smoke_test(base_path, game_description)

if __name__ == "__main__":
    main()