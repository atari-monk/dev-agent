from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.code_style.crud import CodeStyleCRUD

@dataclass
class ReadCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        code_style = CodeStyleCRUD.read()
        print(f"\nCode Style: {', '.join(code_style.requirements)}\n")