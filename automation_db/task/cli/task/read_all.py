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
        items = TaskCRUD.read_all()
        if not items:
            print("No tasks found.")
            return
        
        for _i, item in enumerate(items, 1):
            print(f"\nTask: {item.name}")
            print(f"Feature: {item.feature}")
            print(f"Status: {item.status}")
            print(f"Assigned to: {item.assigned_to}")
            print(f"Requirements: {', '.join(item.requirements)}")
            print(f"Files: {', '.join(map(str, item.context_files))}")
            print(f"Save File: {item.save_file}")
        print()