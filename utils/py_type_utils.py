from mypy import api
from pathlib import Path
from typing import Dict, List, TypedDict, Union

class IssueDict(TypedDict):
    type: str
    message: str
    detail: str
    line: str
    code: str

Issue = IssueDict
ValidationResults = Dict[str, List[Issue]]

def validate_types(path: Union[str, Path], recursive: bool = False) -> ValidationResults:
    path = Path(path)
    results: ValidationResults = {}

    files = _get_python_files(path, recursive)
    if not files:
        return {"error": [{"type": "Error", "message": "Invalid path or no Python files found",
                           "detail": "", "line": "", "code": ""}]}

    for file in files:
        stdout, _, exit_code = api.run([str(file), "--strict"])
        if exit_code != 0:
            issues = _parse_mypy_output(stdout)
            if issues:
                results[str(file)] = issues

    return results

def _get_python_files(path: Path, recursive: bool) -> List[Path]:
    if path.is_file() and path.suffix == ".py":
        return [path]
    elif path.is_dir():
        pattern = "**/*.py" if recursive else "*.py"
        return list(path.glob(pattern))
    return []

def _parse_mypy_output(output: str) -> List[Issue]:
    issues: List[Issue] = []
    for line in output.strip().splitlines():
        parts = line.split(":", 3)
        if len(parts) < 4:
            continue
        file, line_no, _column, message = parts
        issues.append({
            "type": "TypeError",
            "message": message.strip(),
            "detail": "",
            "line": line_no.strip(),
            "code": file.strip()
        })
    return issues
