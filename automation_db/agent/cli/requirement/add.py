from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.agent.crud import AgentCRUD

@dataclass
class AddCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('role', help='Agent role to look up')
        parser.add_argument('requirement', help='Requirement to add')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = AgentCRUD.add_requirement(args.role, args.requirement)
        print(f"Added requirement at {db_config.agent}")