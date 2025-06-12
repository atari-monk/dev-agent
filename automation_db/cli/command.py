import argparse
from typing import Protocol

class Command(Protocol):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        ...

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        ...