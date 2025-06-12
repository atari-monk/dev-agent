from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.code_style.cli.code_style.command import COMMAND
from automation_db.code_style.cli.requirement.command import REQUIREMENT_COMMAND

CODE_STYLE_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {}

CODE_STYLE_COMMAND.update(COMMAND)
CODE_STYLE_COMMAND.update(REQUIREMENT_COMMAND)
