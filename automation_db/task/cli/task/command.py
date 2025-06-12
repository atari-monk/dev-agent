from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.task.cli.task.create import CreateCommand
from automation_db.task.cli.task.read import ReadCommand
from automation_db.task.cli.task.update import UpdateCommand
from automation_db.task.cli.task.remove import RemoveCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.TASK, 'create'): CreateCommand,
    (ModelType.TASK, 'read'): ReadCommand,
    (ModelType.TASK, 'update'): UpdateCommand,
    (ModelType.TASK, 'remove'): RemoveCommand
}