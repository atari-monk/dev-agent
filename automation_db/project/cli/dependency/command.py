from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.project.cli.dependency.add import AddCommand
from automation_db.project.cli.dependency.update import UpdateCommand
from automation_db.project.cli.dependency.remove import RemoveCommand

DEPENDENCY_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.PROJECT, 'add_dep'): AddCommand,
    (ModelType.PROJECT, 'update_dep'): UpdateCommand,
    (ModelType.PROJECT, 'remove_dep'): RemoveCommand
}