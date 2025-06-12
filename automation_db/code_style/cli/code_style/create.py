from dataclasses import dataclass
import argparse
from automation_db.code_style.crud import CodeStyleCRUD
from automation_db.db.config import db_config
from automation_db.code_style.model import CodeStyle
from automation_db.cli.command import Command

@dataclass
class CreateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('reqs', nargs='+', help='List of requirements for the code style')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        code_style = CodeStyle(
            requirements=args.reqs
        )
        CodeStyleCRUD.create(code_style)
        print(f"Created at {db_config.code_style}")