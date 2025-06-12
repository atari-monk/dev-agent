from pathlib import Path
from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.db.config import db_config
from automation_db.project.crud import ProjectCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('dependency', help='Dependency to remove')

    @staticmethod
    def handle(args: argparse.Namespace, config_path: Path = db_config.project) -> None:
        _ = ProjectCRUD.remove_dependency(args.dependency)
        print(f"Removed dependency at {config_path}")