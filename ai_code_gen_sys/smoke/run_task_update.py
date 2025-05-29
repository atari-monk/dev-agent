from pathlib import Path
from typing import Any, Dict
from ai_code_gen_sys.models.task import Task, TaskStatus

test_task = Task(
    id="test_123",
    element_id="elem_456",
    title="Smoke Test Task",
    prompt="Verify task update functionality",
    generated_code="",
    status=TaskStatus.NOT_IMPLEMENTED
)
test_task2 = Task(
    id="test_124",
    element_id="elem_457",
    title="Smoke Test Task 2",
    prompt="Verify task update functionality 2",
    generated_code="",
    status=TaskStatus.NOT_IMPLEMENTED
)

test_file = Path("test_task.yaml")

Task.save_many(test_file, [test_task, test_task2])

assert test_file.exists()

loaded_tasks = Task.load_many(test_file)
assert len(loaded_tasks) == 2
assert any(task.id == "test_123" for task in loaded_tasks)
assert any(task.id == "test_124" for task in loaded_tasks)

input("Saved tasks, Check file and Press Enter to continue...")

update_data: Dict[str, Any] = {
    "status": TaskStatus.IMPLEMENTED,
    "generated_code": "print('smoke test passed')",
    "metadata": {"test": True}
}

Task.update_task_in_file(test_file, "test_123", update_data)

updated_tasks = Task.load_many(test_file)
updated_task = next(task for task in updated_tasks if task.id == "test_123")

assert updated_task.status == TaskStatus.IMPLEMENTED
assert updated_task.generated_code == "print('smoke test passed')"
assert updated_task.metadata.get("test") is True
assert updated_task.updated_at > test_task.created_at

input("Updated task, Check file and Press Enter to continue...")

test_file.unlink()