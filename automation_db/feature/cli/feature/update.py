from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.feature.crud import FeatureCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Feature name to update')
        parser.add_argument('--new_name', help='New feature name')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        updates: dict[str, object] = {}
        if args.new_name: updates['name'] = args.new_name
        _ = FeatureCRUD.update(args.name, updates)
        print(f"Updated at {db_config.feature}")