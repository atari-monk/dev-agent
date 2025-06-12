from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.project.cli.project.create import CreateCommand
from automation_db.project.cli.project.read import ReadCommand
from automation_db.project.cli.project.update import UpdateCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.PROJECT, 'create'): CreateCommand,
    (ModelType.PROJECT, 'read'): ReadCommand,
    (ModelType.PROJECT, 'update'): UpdateCommand
}