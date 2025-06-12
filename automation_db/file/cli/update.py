from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.file.crud import FileCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature_name', help='Feature name')
        parser.add_argument('task_name', help='Task name')
        parser.add_argument('--file_name', help='New file name')
        parser.add_argument('--class_name', help='New class name')
        parser.add_argument('--path', help='New path')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        updates: dict[str, str] = {}
        if args.file_name: updates['file_name'] = args.file_name
        if args.class_name: updates['class_name'] = args.class_name
        if args.path: updates['path'] = args.path
        _ = FileCRUD.update(args.feature_name, args.name, updates)
        print(f"Updated feature file at {db_config.file}")