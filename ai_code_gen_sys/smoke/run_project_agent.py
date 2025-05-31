from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.mock.chatgpt_agent_mock import ChatGPTAgentMock
from agents.mock.code_agent_mock import CodeAgentMock
from ai_code_gen_sys.agents.project_agent import ProjectAgent

def smoke_test(base_path: Path, game_description:str) -> None:
    print("Running Project Agent smoke test")
    agent =  ProjectAgent(base_path, CodeAgent(ChatGPTAgent()))
    agent.execute(game_description)

def mock_smoke_test(base_path: Path, game_description:str) -> None:
    print("Running Mocked Project Agent smoke test")
    agent = ProjectAgent(base_path, CodeAgentMock(ChatGPTAgentMock()))
    agent.execute(game_description)
        
def main(mock: bool = False) -> None:
    base_path = Path(r"C:\atari-monk\code\race-track-game")
    project_path = base_path / "docs" / "ai_code_gen_sys" / "project.yaml"
    if project_path.exists():
        print("Project already exists. Skipping generation.")
        return
    game_description = """Modular 2D Racing Game (Pygame)
Core Architecture:
Decoupled Design - Uses Dependency Injection (DI) via interfaces for clean, testable components.
Event-Driven - Message bus system for modular communication between systems.
State Machine - Manages game flow (menus, race, pause, etc.) cleanly.
Component-Based - Easy to extend or modify features without tight coupling.
SOLID Principles - Emphasizes SRP, DI, and interface-based dependencies.
Game Features:
Player Car - Responsive controls with acceleration, braking, and steering.
AI Opponents - Basic racing behaviors (overtaking, collision avoidance).
Elliptical Track - Smooth 2D racing with collision detection.
Lap Timing - Tracks lap times and race progress.
"""
    if not mock:
        smoke_test(base_path, game_description)
    else:
        mock_smoke_test(base_path, game_description)

if __name__ == "__main__":
    main()