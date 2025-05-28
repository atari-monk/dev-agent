from pathlib import Path
from typing import Optional
import yaml
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from ai_code_gen_sys.models.task import Task
from ai_code_gen_sys.models.task_status import TaskStatus

class ImplementationAgent:
    def __init__(self, persist_session: bool = False):
        self._code_agent = CodeAgent(persist_session=persist_session)

    def load_task(self, tasks_path: Path) -> Optional[Task]:
        if not tasks_path.exists():
            return None
            
        with open(tasks_path, 'r') as f:
            tasks = [Task(**t) for t in yaml.safe_load(f)]
            
        return next((t for t in tasks if t.status == TaskStatus.NOT_IMPLEMENTED), None)

    def implement_task(self, task: Task, output_path: Path) -> None:
        existing_content = ""
        if output_path.exists():
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()

        prompt = f"""
        {task.__str__()}
        
        Existing code:
        {existing_content}

        Requirements:
        - Build upon the existing code if present
        - Do not use any type of comments in the code.
        - Do SRP functions and methods named to be self documenting.
        - Strict python typing.
        - Use latest python version.
        - Use latest python libraries.
        - Use latest python best practices.
        - Use latest python idioms.
        - Use latest python design patterns.
        - Output only the code.
        - Use SOLID principles.
        - Use DRY principles.
        - Use KISS principles.
        - Use YAGNI principles.
        - If something is not SRP, implemtnt it in a separate function or class and use di to use in main implementation.
        """
        code_task = CodeTask(
            prompt=prompt,
            output_path=output_path
        )
        self._code_agent.execute(code_task)
        task.status = TaskStatus.IMPLEMENTED

    def save_task(self, task: Task, tasks_path: Path) -> None:
        with open(tasks_path, 'r+') as f:
            tasks = [Task(**t) for t in yaml.safe_load(f)]
            updated_tasks = [t if t.id != task.id else task for t in tasks]
            yaml.safe_dump([{k: v.value if hasattr(v, 'value') else v for k, v in t.model_dump().items()} for t in updated_tasks], f)

    def execute(self, base_path: Path) -> None:
        tasks_path = base_path / "docs" / "ai_code_gen_sys" / "tasks.yaml"
        
        task = self.load_task(tasks_path)
        if not task:
            return
        
        implementation_path = base_path / "src" / f"{task.element_id}.py"
        self.implement_task(task, implementation_path)
        self.save_task(task, tasks_path)