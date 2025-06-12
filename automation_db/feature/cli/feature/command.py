from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.feature.cli.feature.create import CreateCommand
from automation_db.feature.cli.feature.read import ReadCommand
from automation_db.feature.cli.feature.update import UpdateCommand
from automation_db.feature.cli.feature.remove import RemoveCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.FEATURE, 'create'): CreateCommand,
    (ModelType.FEATURE, 'read'): ReadCommand,
    (ModelType.FEATURE, 'update'): UpdateCommand,
    (ModelType.FEATURE, 'remove'): RemoveCommand
}