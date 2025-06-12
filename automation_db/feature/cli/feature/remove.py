from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.feature.crud import FeatureCRUD

@dataclass
class RemoveCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Feature name to remove')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        FeatureCRUD.remove(args.name)
        print(f"Removed feature at {db_config.feature}")