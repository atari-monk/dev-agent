from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.task.crud import TaskCRUD

@dataclass
class ReadCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        task = TaskCRUD.read(args.feature, args.name)
        print("Current task:")
        print(f"Feature: {task.feature}")
        print(f"Name: {task.name}")
        print(f"Requirements: {', '.join(task.requirements)}")
        print(f"Assigned to: {task.assigned_to}")
        print(f"Status: {task.status}")