from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.code_style.cli.code_style.create import CreateCommand
from automation_db.code_style.cli.code_style.read import ReadCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.CODE_STYLE, 'create'): CreateCommand,
    (ModelType.CODE_STYLE, 'read'): ReadCommand,
}