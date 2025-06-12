from pathlib import Path
from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.db.config import db_config
from automation_db.project.crud import ProjectCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('--name', help='Update project name')
        parser.add_argument('--path', type=Path, help='Update project path')

    @staticmethod
    def handle(args: argparse.Namespace, config_path: Path = db_config.project) -> None:
        updates: dict[str, object] = {}
        if args.name: updates['name'] = args.name
        if args.path: updates['path'] = args.path
        _ = ProjectCRUD.update(updates)
        print(f"Updated at {config_path}")