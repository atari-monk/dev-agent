from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.agent.cli.agent.command import COMMAND
from automation_db.agent.cli.requirement.command import REQUIREMENT_COMMAND

AGENT_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {}

AGENT_COMMAND.update(COMMAND)
AGENT_COMMAND.update(REQUIREMENT_COMMAND)