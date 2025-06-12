from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.feature.model import Feature
from automation_db.feature.crud import FeatureCRUD

@dataclass
class CreateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Feature name')
        parser.add_argument('reqs', nargs='+', help='List of requirements (at least one required)')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        feature = Feature(
            name=args.name,
            requirements=args.reqs
        )
        FeatureCRUD.create(feature)
        print(f"Created at {db_config.feature}")