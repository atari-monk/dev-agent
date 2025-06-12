from pathlib import Path
from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.db.config import db_config
from automation_db.project.crud import ProjectCRUD

@dataclass
class AddCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('dependency', help='Dependency to add')

    @staticmethod
    def handle(args: argparse.Namespace, config_path: Path = db_config.project) -> None:
        _ = ProjectCRUD.add_dependency(args.dependency)
        print(f"Added dependency at {config_path}")