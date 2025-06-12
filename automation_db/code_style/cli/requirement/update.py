from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.code_style.crud import CodeStyleCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('old', help='Old requirement')
        parser.add_argument('new', help='New requirement')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        _ = CodeStyleCRUD.update_requirement(args.old, args.new)
        print(f"Updated requirement at {db_config.code_style}")