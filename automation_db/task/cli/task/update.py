from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.task.crud import TaskCRUD

@dataclass
class UpdateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')
        parser.add_argument('--new_feature', help='New task feature')
        parser.add_argument('--new_name', help='New task name')
        parser.add_argument('--assigned_to', help='New task assigned to')
        parser.add_argument('--status', help='New task status')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        updates: dict[str, str] = {}
        if args.new_feature: updates['feature'] = args.new_feature
        if args.new_name: updates['name'] = args.new_name
        if args.assigned_to: updates['assigned_to'] = args.assigned_to
        if args.status: updates['status'] = args.status
        _ = TaskCRUD.update(args.feature,  args.name, updates)
        print(f"Updated task at {db_config.task}")