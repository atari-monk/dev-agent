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
    def read_all() -> List[File]:
        data = toml.load(db_config.file.open())
        files: List[File] = []
        for file in data['file']:
            files.append(File(
                id = file['id'],
                feature=file['feature'],
                task=file['task'],
                file_name=file['file_name'],
                class_name=file.get('class_name'),
                path=file['path']
            ))
        return files
    
    @staticmethod
    def read_many_by_feature(feature_name: str) -> List[File]:
        data = toml.load(db_config.file.open())
        files: List[File] = []
        for file in data['file']:
            if file['feature'] == feature_name:
                files.append(File(
                    id = file['id'],
                    feature=file['feature'],
                    task=file['task'],
                    file_name=file['file_name'],
                    class_name=file.get('class_name'),
                    path=file['path']
                ))
        return files
    
    @staticmethod
    def read_many_by_ids(ids: List[int]) -> List[File]:
        items = toml.load(db_config.file.open())
        ids_set = set(ids)
        select_items: List[File] = []
        for item in items['file']:
            if item['id'] in ids_set:
                select_items.append(File(
                    id=item['id'],
                    feature=item['feature'],
                    task=item['task'],
                    file_name=item['file_name'],
                    class_name=item.get('class_name'),
                    path=item['path']
                ))
        return select_items
    
    @staticmethod
    def read_by_feature_and_task(feature_name: str, task_name: str) -> File:
        data = toml.load(db_config.file.open())
        for file in data['file']:
            if file['feature'] == feature_name and file['task'] == task_name:
                return File(
                    id = file['id'],
                    feature=file['feature'],
                    task=file['task'],
                    file_name=file['file_name'],
                    class_name=file.get('class_name'),
                    path=file['path']
                )
        raise ValueError(f"File with feature '{feature_name}' and task '{task_name}' not found")

    @staticmethod
    def update(feature_name: str, task_name: str, updates: dict[str, Any]) -> File:
        data = toml.load(db_config.file.open())
        for file in data['file']:
            if file['feature'] == feature_name and file['task'] == task_name:
                for key, value in updates.items():
                    if key in file:
                        file[key] = value
                with db_config.file.open('w') as f:
                    toml.dump(data, f)
                return File(
                    id = file['id'],
                    feature=file['feature'],
                    task=file['task'],
                    file_name=file['file_name'],
                    class_name=file.get('class_name'),
                    path=file['path']
                )
        raise ValueError(f"FeatureFile with feature '{feature_name}' and task '{task_name}' not found")

    @staticmethod
    def remove(feature_name: str, task_name: str) -> None:
        data = toml.load(db_config.file.open())
        data['file'] = [
            file for file in data['file']
            if not (file['feature'] == feature_name and file['task'] == task_name)
        ]
        with db_config.file.open('w') as f:
            toml.dump(data, f)