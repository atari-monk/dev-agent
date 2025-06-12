import toml
from typing import Any, List
from automation_db.db.config import db_config
from automation_db.file.model import File

class FileCRUD:
    @staticmethod
    def create(file: File) -> None:
        data: dict[str, list[dict[str, object]]] = {'file': []}
        if db_config.file.exists():
            data = toml.load(db_config.file.open())
            if 'file' not in data:
                data['file'] = []
        
        data['file'].append({
            'feature': file.feature,
            'task': file.task,
            'file_name': file.file_name,
            'class_name': file.class_name,
            'path': file.path
        })
        
        with db_config.file.open('w') as f:
            toml.dump(data, f)

    @staticmethod
    def read(feature_name: str, task_name: str) -> File:
        data = toml.load(db_config.file.open())
        for file in data['file']:
            if file['feature'] == feature_name and file['task'] == task_name:
                return File(
                    feature=file['feature'],
                    task=file['task'],
                    file_name=file['file_name'],
                    class_name=file.get('class_name'),
                    path=file['path']
                )
        raise ValueError(f"File with feature '{feature_name}' and task '{task_name}' not found")
    
    @staticmethod
    def read_list(feature_name: str) -> List[File]:
        data = toml.load(db_config.file.open())
        files: List[File] = []
        for file in data['file']:
            if file['feature'] == feature_name:
                files.append(File(
                    feature=file['feature'],
                    task=file['task'],
                    file_name=file['file_name'],
                    class_name=file.get('class_name'),
                    path=file['path']
                ))
        return files
    
    @staticmethod
    def update(feature_name: str, name: str, updates: dict[str, Any]) -> File:
        data = toml.load(db_config.file.open())
        for file in data['file']:
            if file['feature'] == feature_name and file['name'] == name:
                for key, value in updates.items():
                    if key in file:
                        file[key] = value
                with db_config.file.open('w') as f:
                    toml.dump(data, f)
                return File(
                    feature=file['feature'],
                    task=file['name'],
                    file_name=file['file_name'],
                    class_name=file.get('class_name'),
                    path=file['path']
                )
        raise ValueError(f"FeatureFile with feature '{feature_name}' and name '{name}' not found")

    @staticmethod
    def remove(feature_name: str, task_name: str) -> None:
        data = toml.load(db_config.file.open())
        data['file'] = [
            file for file in data['file']
            if not (file['feature'] == feature_name and file['task'] == task_name)
        ]
        with db_config.file.open('w') as f:
            toml.dump(data, f)