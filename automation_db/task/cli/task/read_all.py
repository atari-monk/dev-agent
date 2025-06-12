from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.task.crud import TaskCRUD

@dataclass
class ReadAllCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        tasks = TaskCRUD.read_all()
        if not tasks:
            print("No tasks found.")
            return
        
        for _i, task in enumerate(tasks, 1):
            print(f"\nTask: {task.name}")
            print(f"Feature: {task.feature}")
            print(f"Status: {task.status}")
            print(f"Assigned to: {task.assigned_to}")
            print(f"Requirements: {', '.join(task.requirements)}")
        print()