from dataclasses import dataclass
import argparse
from automation_db.db.config import db_config
from automation_db.cli.command import Command
from automation_db.agent.model import Agent
from automation_db.agent.crud import AgentCRUD

@dataclass
class CreateCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('role', help='Agent role (required)')
        parser.add_argument('reqs', nargs='+', help='Agent requirements (at least one required)')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        agent = Agent(
            role=args.role,
            requirements=args.reqs
        )
        AgentCRUD.create(agent)
        print(f"Created agent at {db_config.agent}")