from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.task.model import Task
from automation_db.task.crud import TaskCRUD
from automation_db.cli.command import Command

@dataclass
class CreateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('feature', help='Task feature')
        parser.add_argument('name', help='Task name')
        parser.add_argument('assigned_to', help='Task assigned to')
        parser.add_argument('reqs', nargs='+', help='Task requirements (at least one required)')
        parser.add_argument('--status', default='pending', choices=['pending'], help='Initial status of the feature (default: %(default)s)')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        task = Task(
            feature=args.feature,
            name=args.name,
            requirements=args.reqs,
            assigned_to=args.assigned_to,
            status=args.status
        )
        TaskCRUD.create(task)
        print(f"Created task at {db_config.task}")