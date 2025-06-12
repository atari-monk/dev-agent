from pathlib import Path
from typing import Any, List
from agents.code_task import CodeTask
from agents.interface.icode_agent import ICodeAgent
from ai_code_gen_sys.models.element import Element
from ai_code_gen_sys.models.task import Task
from ai_code_gen_sys.models.task_status import TaskStatus

class ImplementationAgent:
    def __init__(self, code_agent: ICodeAgent) -> None:
        self._code_agent = code_agent

    def execute(self, base_path: Path, element: Element) -> None:
        tasks_path = base_path / "docs" / "ai_code_gen_sys" / "tasks.yaml"
        tasks = self.load_tasks(tasks_path, element)

        for task in tasks:
            implementation_path = base_path / "src" / f"{task.element_id}.py"
            prompt = self.get_prompt(task, implementation_path)

            code_task = CodeTask(prompt=prompt, output_path=implementation_path, overwrite=False, delay_seconds=30)
            code = self._code_agent.execute(code_task)
            update_data: dict[str, Any] = {"status": TaskStatus.IMPLEMENTED, "generated_code": code}

            Task.update_task_in_file(tasks_path, task.id, update_data)

    def load_tasks(self, tasks_path: Path, element: Element) -> List[Task]:
        if not tasks_path.exists():
            return []
        tasks = Task.load_many(tasks_path)
        return [t for t in tasks if t.element_id == element.id and t.status == TaskStatus.NOT_IMPLEMENTED]

    def get_prompt(self, task: Task, output_path: Path) -> str:
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
        - Strict typing
        - Latest Python
        - SOLID//SRP/DRY/KISS/YAGNI
        - No comments
        - Output only code
        """
        return prompt
    
    def open(self):
        self._code_agent.open()

    def close(self):
        self._code_agent.close()