from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.agent.cli.requirement.add import AddCommand
from automation_db.agent.cli.requirement.update import UpdateCommand
from automation_db.agent.cli.requirement.remove import RemoveCommand

REQUIREMENT_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.AGENT, 'add_req'): AddCommand,
    (ModelType.AGENT, 'update_req'): UpdateCommand,
    (ModelType.AGENT, 'remove_req'): RemoveCommand
}