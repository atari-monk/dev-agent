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
        parser.add_argument('old', help='Old requirement')
        parser.add_argument('new', help='New requirement')

    @staticmethod
    def handle(args: argparse.Namespace, config_path: Path = db_config.project) -> None:
        _ = ProjectCRUD.update_requirement(args.old, args.new)
        print(f"Updated requirement at {config_path}")