from dataclasses import dataclass
import argparse
from automation_db.agent.crud import AgentCRUD
from automation_db.cli.command import Command

@dataclass
class ReadByRoleCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument('role', help='Agent role to look up')

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        agent = AgentCRUD.read_by_role(args.role)
        print("Current agent:")
        print(f"Role: {agent.role}")
        print(f"Requirements: {', '.join(agent.requirements)}")