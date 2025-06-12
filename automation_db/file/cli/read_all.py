from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.file.crud import FileCRUD

@dataclass
class ReadAllCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        files = FileCRUD.read_all()
        if not files:
            print("No files found.")
            return
        
        for _i, file in enumerate(files, 1):
            print(f"\nFile name: {file.file_name}")
            print(f"Class name: {file.class_name}")
            print(f"Path: {file.path}")
            print(f"Feature: {file.feature}")
            print(f"Task: {file.task}")
        print()