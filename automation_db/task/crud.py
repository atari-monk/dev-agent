import toml
from automation_db.task.model import Task
from typing import Any

from automation_db.db.config import db_config

class TaskCRUD:
    @staticmethod
    def create(task: Task) -> None:
        data: dict[str, list[dict[str, object]]] = {'task': []}
        if db_config.task.exists():
            data = toml.load(db_config.task.open())
            if 'task' not in data:
                data['task'] = []
        
        data['task'].append({
            'feature': task.feature,
            'name': task.name,
            'requirements': task.requirements,
            'assigned_to': task.assigned_to,
            'status': task.status
        })
        
        with db_config.task.open('w') as f:
            toml.dump(data, f)

    @staticmethod
    def read_all() -> list[Task]:
        data = toml.load(db_config.task.open())
        return [
            Task(
                feature=task_data['feature'],
                name=task_data['name'],
                requirements=task_data['requirements'],
                assigned_to=task_data['assigned_to'],
                status=task_data['status'])
            for task_data in data['task']
        ]
    
    @staticmethod
    def read_by_feature_and_name(feature: str, name: str) -> Task:
        data = toml.load(db_config.task.open())
        for task_data in data['task']:
            if task_data['feature'] == feature and task_data['name'] == name:
                return Task(
                    feature=task_data['feature'],
                    name=task_data['name'],
                    requirements=task_data['requirements'],
                    assigned_to=task_data['assigned_to'],
                    status=task_data['status']
                )
        raise ValueError(f"Task with feature '{feature}' and name '{name}' not found")

    @staticmethod
    def read_by_status(status: str = 'pending') -> Task | None:
        data = toml.load(db_config.task.open())
        for task_data in data['task']:
            if task_data['status'] == status:
                return Task(
                    feature=task_data['feature'],
                    name=task_data['name'],
                    requirements=task_data['requirements'],
                    assigned_to=task_data['assigned_to'],
                    status=task_data['status']
                )
        return None

    @staticmethod
    def update(feature: str, name: str, updates: dict[str, Any]) -> Task:
        data = toml.load(db_config.task.open())
        for task_data in data['task']:
            if task_data['feature'] == feature and task_data['name'] == name:
                for key, value in updates.items():
                    if key in task_data:
                        task_data[key] = value
                with db_config.task.open('w') as f:
                    toml.dump(data, f)
                return Task(
                    feature=task_data['feature'],
                    name=task_data['name'],
                    requirements=task_data['requirements'],
                    assigned_to=task_data['assigned_to'],
                    status=task_data['status']
                )
        raise ValueError(f"Task with feature '{feature}' and name '{name}' not found")

    @staticmethod
    def remove(feature: str, name: str) -> None:
        data = toml.load(db_config.task.open())
        data['task'] = [task for task in data['task'] if not (task['feature'] == feature and task['name'] == name)]
        with db_config.task.open('w') as f:
            toml.dump(data, f)

    @staticmethod
    def add_requirement(feature: str, name: str, requirement: str) -> Task:
        current = TaskCRUD.read_by_feature_and_name(feature, name)
        current.requirements.append(requirement)
        updates = {'requirements': current.requirements}
        return TaskCRUD.update(feature, name, updates)

    @staticmethod
    def update_requirement(feature: str, name: str, old: str, new: str) -> Task:
        current = TaskCRUD.read_by_feature_and_name(feature, name)
        if old in current.requirements:
            index = current.requirements.index(old)
            current.requirements[index] = new
        updates = {'requirements': current.requirements}
        return TaskCRUD.update(feature, name, updates)

    @staticmethod
    def remove_requirement(feature: str, name: str, requirement: str) -> Task:
        current = TaskCRUD.read_by_feature_and_name(feature, name)
        if requirement in current.requirements:
            current.requirements.remove(requirement)
        updates = {'requirements': current.requirements}
        return TaskCRUD.update(feature, name, updates)