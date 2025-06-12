from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.task.cli.requirement.add import AddCommand
from automation_db.task.cli.requirement.update import UpdateCommand
from automation_db.task.cli.requirement.remove import RemoveCommand

REQUIREMENT_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.TASK, 'add_req'): AddCommand,
    (ModelType.TASK, 'update_req'): UpdateCommand,
    (ModelType.TASK, 'remove_req'): RemoveCommand
}