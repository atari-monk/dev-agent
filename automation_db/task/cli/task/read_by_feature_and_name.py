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
        item = TaskCRUD.read_by_feature_and_name(args.feature, args.name)
        print(f"\nTask: {item.name}")
        print(f"Status: {item.status}")
        print(f"Assigned to: {item.assigned_to}")
        print(f"Requirements: {', '.join(item.requirements)}")
        print(f"Files: {', '.join(map(str, item.context_files))}")
        print(f"Save File: {item.save_file}")
        print(f"Feature: {item.feature}")
        print()