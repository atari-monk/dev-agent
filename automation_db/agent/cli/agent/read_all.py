from dataclasses import dataclass
import argparse
from automation_db.cli.command import Command
from automation_db.agent.crud import AgentCRUD

@dataclass
class ReadAllCommand(Command):
    @staticmethod
    def init_parser(parser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def handle(args: argparse.Namespace) -> None:
        agents = AgentCRUD.read_all()
        if not agents:
            print("No agents found.")
            return
            
        for _i, agent in enumerate(agents, 1):
            print(f"\nAgent: {agent.role}")
            print(f"Requirements: {', '.join(agent.requirements)}")
        print()