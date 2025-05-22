from contextlib import redirect_stderr, redirect_stdout
import io
import pytest
from game_tool.models.task import Task
from game_tool.models.task_type import TaskType


def run_test_with_feedback(task: Task) -> None:
    if task.task_type != TaskType.Test:
        raise ValueError("Can only run tests on Test tasks")

    output_buffer = io.StringIO()
    with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
        pytest_exit_code = pytest.main([str(task.file_path)])
    test_output = output_buffer.getvalue()

    task.description = (
        f"{task.description}\n\n"
        f"Test Output (exit code: {pytest_exit_code}):\n{test_output.strip()}"
    )