from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.agent.crud import AgentCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('role', help='Agent role')
        parser.add_argument('old', help='Old requirement')
        parser.add_argument('new', help='New requirement')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = AgentCRUD.update_requirement(args.role, args.old, args.new)
        print(f"Updated requirement at {db_config.agent}")