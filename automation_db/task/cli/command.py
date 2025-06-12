from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.task.cli.task.command import COMMAND
from automation_db.task.cli.requirement.command import REQUIREMENT_COMMAND

TASK_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {}

TASK_COMMAND.update(COMMAND)
TASK_COMMAND.update(REQUIREMENT_COMMAND)