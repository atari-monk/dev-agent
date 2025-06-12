from typing import Dict, Tuple, Type
from automation_db.cli.model_type import ModelType
from automation_db.cli.command import Command
from automation_db.agent.cli.agent.create import CreateCommand
from automation_db.agent.cli.agent.read_all import ReadAllCommand
from automation_db.agent.cli.agent.read_by_role import ReadByRoleCommand
from automation_db.agent.cli.agent.update import UpdateCommand
from automation_db.agent.cli.agent.remove import RemoveCommand

COMMAND: Dict[Tuple[ModelType, str], Type[Command]] = {
    (ModelType.AGENT, 'create'): CreateCommand,
    (ModelType.AGENT, 'read_all'): ReadAllCommand,
    (ModelType.AGENT, 'read_by_role'): ReadByRoleCommand,
    (ModelType.AGENT, 'update'): UpdateCommand,
    (ModelType.AGENT, 'remove'): RemoveCommand
}