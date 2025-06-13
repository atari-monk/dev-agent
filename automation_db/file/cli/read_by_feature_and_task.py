from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.file.crud import FileCRUD

@dataclass
class ReadByFeatureAndTaskCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature_name', help='Feature name')
        parser.add_argument('task_name', help='Task name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        file = FileCRUD.read_by_feature_and_task(args.feature_name, args.name)
        print(f"\nFile name: {file.file_name}")
        print(f"Class name: {file.class_name}")
        print(f"Path: {file.path}")
        print(f"Feature: {file.feature}")
        print(f"Task: {file.task}")
        print(f"Id: {file.id}")