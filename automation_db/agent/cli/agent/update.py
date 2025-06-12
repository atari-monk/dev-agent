from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.agent.crud import AgentCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('role', help='Agent role to look up')
        parser.add_argument('new_role', help='New agent role')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        updates: dict[str, str] = {}
        if args.new_role:
            updates['role'] = args.new_role
        _ = AgentCRUD.update(args.role, updates)
        print(f"Updated agent at {db_config.agent}")