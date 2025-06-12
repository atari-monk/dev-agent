from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.file.crud import FileCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature_name', help='Feature name')
        parser.add_argument('task_name', help='Task name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        FileCRUD.remove(args.feature_name, args.task_name)
        print(f"Removed feature file at {db_config.file}")