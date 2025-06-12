from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.file.cli.create import CreateCommand
from automation_db.file.cli.read import ReadCommand
from automation_db.file.cli.update import UpdateCommand
from automation_db.file.cli.remove import RemoveCommand

FILE_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {}

FILE_COMMAND.update({
    (ModelType.FILE, 'create'): CreateCommand,
    (ModelType.FILE, 'read'): ReadCommand,
    (ModelType.FILE, 'update'): UpdateCommand,
    (ModelType.FILE, 'remove'): RemoveCommand
})