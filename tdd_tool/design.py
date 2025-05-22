from pathlib import Path
from typing import List
from tdd_tool.models.element import Element
from tdd_tool.models.project import Project
from tdd_tool.models.task import Task
from tdd_tool.prompts.generate_unit_test import generate_unit_test
from tdd_tool.prompts.generate_empty_class import generate_empty_class
from tdd_tool.prompts.generate_interface import generate_interface
from utils.files import ensure_init_py

project = Project(
    project_name="Race Track Game",
    repo_name="race-track-game",
    repo_base_path=Path("C:/atari-monk/code"),
    assumptions=["2d game", "Python", "Pygame", "racing game"],
    #elements=["race track", "ai car opponent", "player car", "collision detection"]
)

elements = [
    Element(name="game loop", description="class with main loop of the game that handles events, updates game state, and renders graphics.", requirements=["pygame", "game state management", "game menu", "game over", "restart game", "start game", "pause game", ])]

code_generation: List[Task] = []

for element in elements:
    code_generation.append(generate_interface(project.repo_path, element.snake_case_name, element.description_with_requirements)) 
    code_generation.append(generate_empty_class(project.repo_path, element.snake_case_name, element.description_with_requirements))
    code_generation.append(generate_unit_test(project.repo_path, element.snake_case_name, element.description_with_requirements))

    element_path = project.repo_path / element.snake_case_name
    element_path.mkdir(parents=True, exist_ok=True)
    ensure_init_py(element_path)

def getTasks() -> List[Task]:
    return code_generation