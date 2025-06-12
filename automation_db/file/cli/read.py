from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.file.crud import FileCRUD

@dataclass
class ReadCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature_name', help='Feature name')
        parser.add_argument('task_name', help='Task name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        feature_file = FileCRUD.read(args.feature_name, args.name)
        print("Current feature file:")
        print(f"Feature: {feature_file.feature}")
        print(f"Task: {feature_file.task}")
        print(f"File name: {feature_file.file_name}")
        print(f"Class name: {feature_file.class_name}")
        print(f"Path: {feature_file.path}")