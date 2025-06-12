from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.feature.cli.feature.create import CreateCommand
from automation_db.feature.cli.feature.read_all import ReadAllCommand
from automation_db.feature.cli.feature.read_by_name import ReadByNameCommand
from automation_db.feature.cli.feature.update import UpdateCommand
from automation_db.feature.cli.feature.remove import RemoveCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.FEATURE, 'create'): CreateCommand,
    (ModelType.FEATURE, 'read_all'): ReadAllCommand,
    (ModelType.FEATURE, 'read_by_name'): ReadByNameCommand,
    (ModelType.FEATURE, 'update'): UpdateCommand,
    (ModelType.FEATURE, 'remove'): RemoveCommand
}