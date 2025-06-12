from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.feature.crud import FeatureCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Feature name')
        parser.add_argument('requirement', help='Requirement to remove')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = FeatureCRUD.remove_requirement(args.name, args.requirement)
        print(f"Removed requirement at {db_config.feature}")