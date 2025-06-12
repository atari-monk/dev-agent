from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.project.cli.project.command import COMMAND
from automation_db.project.cli.dependency.command import DEPENDENCY_COMMAND
from automation_db.project.cli.requirement.command import REQUIREMENT_COMMAND

PROJECT_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {}

PROJECT_COMMAND.update(COMMAND)
PROJECT_COMMAND.update(DEPENDENCY_COMMAND)
PROJECT_COMMAND.update(REQUIREMENT_COMMAND)