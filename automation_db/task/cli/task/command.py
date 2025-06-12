from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.task.cli.task.create import CreateCommand
from automation_db.task.cli.task.read_all import ReadAllCommand
from automation_db.task.cli.task.read_by_feature_and_name import ReadByFeatureAndNameCommand
from automation_db.task.cli.task.update import UpdateCommand
from automation_db.task.cli.task.remove import RemoveCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.TASK, 'create'): CreateCommand,
    (ModelType.TASK, 'read_all'): ReadAllCommand,
    (ModelType.TASK, 'read_by_feature_and_name'): ReadByFeatureAndNameCommand,
    (ModelType.TASK, 'update'): UpdateCommand,
    (ModelType.TASK, 'remove'): RemoveCommand
}