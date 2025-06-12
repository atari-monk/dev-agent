from pathlib import Path
from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.db.config import db_config
from automation_db.project.crud import ProjectCRUD
from automation_db.project.model import Project

@dataclass
class CreateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Project name')
        parser.add_argument('path', type=Path, help='Project path')
        parser.add_argument('--deps', nargs='+', default=[], help='Dependencies')
        parser.add_argument('--reqs', nargs='+', default=[], help='Requirements')

    @staticmethod
    def handle(args: argparse.Namespace, config_path: Path = db_config.project) -> None:
        project = Project(
            name=args.name,
            path=args.path,
            dependencies=args.deps,
            requirements=args.reqs
        )
        ProjectCRUD.create(project)
        print(f"Created at {config_path}")