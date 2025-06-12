from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.feature.cli.requirement.add import AddCommand
from automation_db.feature.cli.requirement.update import UpdateCommand
from automation_db.feature.cli.requirement.remove import RemoveCommand

REQUIREMENT_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.FEATURE, 'add_req'): AddCommand,
    (ModelType.FEATURE, 'update_req'): UpdateCommand,
    (ModelType.FEATURE, 'remove_req'): RemoveCommand
}