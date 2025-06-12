from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.feature.crud import FeatureCRUD

@dataclass
class AddCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Feature name')
        parser.add_argument('requirement', help='Requirement to add')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = FeatureCRUD.add_requirement(args.name, args.requirement)
        print(f"Added requirement at {db_config.feature}")