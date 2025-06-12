from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.task.crud import TaskCRUD

@dataclass
class AddCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')
        parser.add_argument('requirement', help='Requirement to add')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = TaskCRUD.add_requirement(args.feature, args.name, args.requirement)
        print(f"Added requirement to task at {db_config.task}")