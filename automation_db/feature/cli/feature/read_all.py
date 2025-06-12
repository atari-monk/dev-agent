from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.feature.crud import FeatureCRUD

@dataclass
class ReadAllCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        features = FeatureCRUD.read_all()
        if not features:
            print("No features found.")
            return
        
        for _i, feature in enumerate(features, 1):
            print(f"\nFeature: {feature.name}")
            print(f"Requirements: {', '.join(feature.requirements)}")
        print()