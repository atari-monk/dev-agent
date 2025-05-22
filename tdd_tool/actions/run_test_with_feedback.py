from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
import pytest


def run_test_with_feedback(file_path: Path) -> str:
    output_buffer = io.StringIO()
    with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
        pytest_exit_code = pytest.main([str(file_path)])
    test_output = output_buffer.getvalue()
    return f"Test Output (exit code: {pytest_exit_code}):\n{test_output.strip()}"