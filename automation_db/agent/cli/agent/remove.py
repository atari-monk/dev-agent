from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.agent.crud import AgentCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('role', help='Agent role')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        AgentCRUD.remove(args.role)
        print(f"Removed agent at {db_config.agent}")