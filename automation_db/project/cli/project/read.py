from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.project.crud import ProjectCRUD

@dataclass
class ReadCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        project = ProjectCRUD.read()
        print(f"\nProject: {project.name}")
        print(f"Path: {project.path}")
        print(f"Dependencies: {', '.join(project.dependencies)}")
        print(f"Requirements: {', '.join(project.requirements)}\n")