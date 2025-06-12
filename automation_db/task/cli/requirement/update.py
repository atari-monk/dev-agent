from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.task.crud import TaskCRUD
from automation_db.cli.command import Command

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')
        parser.add_argument('old', help='Old requirement')
        parser.add_argument('new', help='New requirement')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = TaskCRUD.update_requirement(args.feature, args.name, args.old, args.new)
        print(f"Updated requirement in task at {db_config.task}")