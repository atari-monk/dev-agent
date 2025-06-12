from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.feature.cli.feature.command import COMMAND
from automation_db.feature.cli.requirement.command import REQUIREMENT_COMMAND

FEATURE_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {}

FEATURE_COMMAND.update(COMMAND)
FEATURE_COMMAND.update(REQUIREMENT_COMMAND)