from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.feature.crud import FeatureCRUD

@dataclass
class ReadByNameCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('name', help='Feature name to read')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        feature = FeatureCRUD.read_by_name(args.name)
        print(f"Feature: {feature.name}")
        print(f"Requirements: {', '.join(feature.requirements)}")