from typing import Dict, Tuple, Type
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.code_style.cli.requirement.add import AddCommand
from automation_db.code_style.cli.requirement.update import UpdateCommand
from automation_db.code_style.cli.requirement.remove import RemoveCommand

REQUIREMENT_COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.CODE_STYLE, 'add_req'): AddCommand,
    (ModelType.CODE_STYLE, 'update_req'): UpdateCommand,
    (ModelType.CODE_STYLE, 'remove_req'): RemoveCommand
}