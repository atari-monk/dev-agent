from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.task.crud import TaskCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        TaskCRUD.remove(args.feature, args.name)
        print(f"Removed task at {db_config.task}")