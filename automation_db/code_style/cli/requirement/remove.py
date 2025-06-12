from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.code_style.crud import CodeStyleCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('requirement', help='Requirement to remove')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = CodeStyleCRUD.remove_requirement(args.requirement)
        print(f"Removed requirement at {db_config.code_style}")