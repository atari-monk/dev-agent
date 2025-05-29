from pathlib import Path
from typing import Dict, Any, List
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from ai_code_gen_sys.models.task import Task
from ai_code_gen_sys.models.task_status import TaskStatus

class ImplementationAgent:
    def __init__(self) -> None:
        self._code_agent = CodeAgent()

    def load_tasks(self, tasks_path: Path, element_id: str) -> List[Task]:
        if not tasks_path.exists():
            return []
        tasks = Task.load_many(tasks_path)
        return [t for t in tasks if t.element_id == element_id and t.status == TaskStatus.NOT_IMPLEMENTED]

    def implement_task(self, task: Task, output_path: Path) -> Dict[str, Any]:
        existing_content = ""
        if output_path.exists():
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()

        prompt = f"""
        {task.__str__()}
        
        Existing code:
        {existing_content}

        Requirements:
        - Build upon existing code
        - No comments
        - SRP functions
        - Strict typing
        - Latest Python
        - SOLID/DRY/KISS/YAGNI
        - Output only code
        """
        code_task = CodeTask(prompt=prompt, output_path=output_path, overwrite=True)
        code = self._code_agent.execute(code_task)
        return {"status": TaskStatus.IMPLEMENTED, "generated_code": code}

    def execute(self, base_path: Path, element_id: str) -> None:
        tasks_path = base_path / "docs" / "ai_code_gen_sys" / "tasks.yaml"
        tasks = self.load_tasks(tasks_path, element_id)
        for task in tasks:
            implementation_path = base_path / "src" / f"{task.element_id}.py"
            update_data = self.implement_task(task, implementation_path)
            Task.update_task_in_file(tasks_path, task.id, update_data)
        self._code_agent.close()