from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.file.crud import FileCRUD
from automation_db.file.model import File

@dataclass
class CreateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('id', help='Id')
        parser.add_argument('feature', help='Feature')
        parser.add_argument('task', help='Task')
        parser.add_argument('file_name', help='File name')
        parser.add_argument('path', help='Path')
        parser.add_argument('--class_name', help='Class name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        feature_file = File(
            id=args.id,
            feature=args.feature,
            task=args.task,
            file_name=args.file_name,
            class_name=args.class_name,
            path=args.path
        )
        FileCRUD.create(feature_file)
        print(f"Created feature file at {db_config.file}")