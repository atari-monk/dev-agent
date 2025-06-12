from typing import Any
import toml
from automation_db.db.config import db_config
from automation_db.agent.model import Agent

class AgentCRUD:
    @staticmethod
    def create(agent: Agent) -> None:
        path = db_config.agent
        data: dict[str, list[dict[str, object]]] = {'agent': []}
        if path.exists():
            data = toml.load(path.open())
            if 'agent' not in data:
                data['agent'] = []
        
        data['agent'].append({
            'role': agent.role,
            'requirements': agent.requirements
        })
        
        with path.open('w') as f:
            toml.dump(data, f)

    @staticmethod
    def read(role: str) -> Agent:
        path = db_config.agent
        data = toml.load(path.open())
        for agent_data in data['agent']:
            if agent_data['role'] == role:
                return Agent(
                    role=agent_data['role'],
                    requirements=agent_data['requirements']
                )
        raise ValueError(f"Agent with role '{role}' not found")

    @staticmethod
    def update(role: str, updates: dict[str, Any]) -> Agent:
        data = toml.load(db_config.agent.open())
        for agent_data in data['agent']:
            if agent_data['role'] == role:
                if 'role' in updates:
                    agent_data['role'] = updates['role']
                with db_config.agent.open('w') as f:
                    toml.dump(data, f)
                return Agent(
                    role=agent_data['role'],
                    requirements=agent_data['requirements']
                )
        raise ValueError(f"Agent with role '{role}' not found")

    @staticmethod
    def add_requirement(role: str, requirement: str) -> Agent:
        data = toml.load(db_config.agent.open())
        for agent_data in data['agent']:
            if agent_data['role'] == role:
                agent_data['requirements'].append(requirement)
                with db_config.agent.open('w') as f:
                    toml.dump(data, f)
                return Agent(
                    role=agent_data['role'],
                    requirements=agent_data['requirements']
                )
        raise ValueError(f"Agent with role '{role}' not found")

    @staticmethod
    def update_requirement(role: str, old: str, new: str) -> Agent:
        data = toml.load(db_config.agent.open())
        for agent_data in data['agent']:
            if agent_data['role'] == role:
                if old in agent_data['requirements']:
                    index = agent_data['requirements'].index(old)
                    agent_data['requirements'][index] = new
                with db_config.agent.open('w') as f:
                    toml.dump(data, f)
                return Agent(
                    role=agent_data['role'],
                    requirements=agent_data['requirements']
                )
        raise ValueError(f"Agent with role '{role}' not found")

    @staticmethod
    def remove_requirement(role: str, requirement: str) -> Agent:
        data = toml.load(db_config.agent.open())
        for agent_data in data['agent']:
            if agent_data['role'] == role:
                if requirement in agent_data['requirements']:
                    agent_data['requirements'].remove(requirement)
                with db_config.agent.open('w') as f:
                    toml.dump(data, f)
                return Agent(
                    role=agent_data['role'],
                    requirements=agent_data['requirements']
                )
        raise ValueError(f"Agent with role '{role}' not found")

    @staticmethod
    def remove(role: str) -> None:
        data = toml.load(db_config.agent.open())
        data['agent'] = [agent for agent in data['agent'] if agent['role'] != role]
        with db_config.agent.open('w') as f:
            toml.dump(data, f)