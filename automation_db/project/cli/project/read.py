from pathlib import Path
from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.db.config import db_config
from automation_db.project.crud import ProjectCRUD

@dataclass
class ReadCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace, config_path: Path = db_config.project) -> None:
        config = ProjectCRUD.read()
        print("Current project:")
        print(f"Name: {config.name}")
        print(f"Path: {config.path}")
        print(f"Dependencies: {', '.join(config.dependencies)}")
        print(f"Requirements: {', '.join(config.requirements)}")