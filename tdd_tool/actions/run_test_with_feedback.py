import io
from pathlib import Path
from contextlib import redirect_stdout, redirect_stderr
import pytest

def run_test_with_feedback(file_path: Path) -> tuple[str, bool]:
    output_buffer = io.StringIO()
    with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
        pytest_exit_code = pytest.main([str(file_path)])
    
    test_output = output_buffer.getvalue()
    
    all_failed = False
    if pytest_exit_code == 1:
        if "FAILED" in test_output and "passed" not in test_output.lower():
            all_failed = True
    
    output_message = f"Test Output (exit code: {pytest_exit_code}):\n{test_output.strip()}"
    return output_message, all_failed