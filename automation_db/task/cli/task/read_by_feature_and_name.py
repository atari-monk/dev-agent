from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.task.crud import TaskCRUD

@dataclass
class ReadByFeatureAndNameCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        task = TaskCRUD.read_by_feature_and_name(args.feature, args.name)
        print(f"\nTask: {task.name}")
        print(f"Status: {task.status}")
        print(f"Assigned to: {task.assigned_to}")
        print(f"Requirements: {', '.join(task.requirements)}")
        print(f"Feature: {task.feature}")
        print()