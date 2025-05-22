from pathlib import Path
from typing import List
from game_tool.models.element import Element
from game_tool.models.project import Project
from game_tool.models.task import Task
from game_tool.prompts.generate_test_task import generate_test_task
from game_tool.prompts.generate_unit_test import generate_unit_test
from game_tool.prompts.generate_empty_class import generate_empty_class
from game_tool.prompts.generate_interface import generate_interface
from utils.files import ensure_init_py_in_parents

project = Project(
    project_name="Race Track Game",
    repo_name="race-track-game",
    repo_base_path=Path("C:/atari-monk/code"),
    assumptions=["2d game", "Python", "Pygame", "racing game"],
    #elements=["race track", "ai car opponent", "player car", "collision detection"]
)

elements = [
    Element(name="game loop", description="class with main loop of the game that handles events, updates game state, and renders graphics.", requirements=["pygame", "game state management", "game menu", "game over", "restart game", "start game", "pause game", ])]

tasks: List[Task] = []

for element in elements:
    tasks.append(generate_interface(project.repo_path, element.snake_case_name, element.description_with_requirements)) 
    tasks.append(generate_empty_class(project.repo_path, element.snake_case_name, element.description_with_requirements))
    tasks.append(generate_unit_test(project.repo_path, element.snake_case_name, element.description_with_requirements))
    tasks.append(generate_test_task(project.repo_path, element.snake_case_name, element.description_with_requirements))

for task in tasks:
    task.file_path.parent.mkdir(parents=True, exist_ok=True)
    ensure_init_py_in_parents(task.file_path)

def getTasks():
    return tasks