import ast
from pathlib import Path
from typing import Dict, List, Optional, TypedDict, Union


class IssueDict(TypedDict):
    type: str
    message: str
    detail: str
    line: str
    code: str


Issue = IssueDict
ValidationResults = Dict[str, List[Issue]]


def print_results(results: ValidationResults) -> None:
    if not results:
        print("No issues found!")
        return

    for file_path, issues in results.items():
        if file_path == "error":
            for error in issues:
                print(f"\n\033[91mERROR: {error['message']}\033[0m")
            continue

        print(f"\n\033[1mFile: {file_path}\033[0m")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. \033[91m{issue['type']}\033[0m:")
            print(f"     Line: {issue['line']}")
            print(f"     {issue['message']}")
            if issue['detail']:
                print(f"     \033[90m{issue['detail']}\033[0m")
        print(f"Total issues found: {len(issues)}")


def validation_results_to_str(results: ValidationResults) -> str:
    if not results:
        return "No issues found!"

    lines: List[str] = []
    for file_path, issues in results.items():
        if file_path == "error":
            for error in issues:
                lines.append(f"\nERROR: {error['message']}")
            continue

        lines.append(f"\nFile: {file_path}")
        for i, issue in enumerate(issues, 1):
            lines.append(f"  {i}. {issue['type']}:")
            lines.append(f"     Line: {issue['line']}")
            lines.append(f"     {issue['message']}")
            if issue['detail']:
                lines.append(f"     {issue['detail']}")
        lines.append(f"Total issues found: {len(issues)}")
    
    return "\n".join(lines)


def validate_python_code(path: Union[str, Path], recursive: bool = False) -> ValidationResults:
    path = Path(path)
    results: ValidationResults = {}

    files = _get_python_files(path, recursive)
    if not files:
        return {"error": [{"type": "Error", "message": "Invalid path or no Python files found",
                          "detail": "", "line": "", "code": ""}]}

    for file in files:
        issues: List[Issue] = []
        _validate_syntax(file, issues)
        if issues:
            results[str(file)] = issues

    return results


def has_issues(results: ValidationResults, issue_type: Optional[str] = None) -> bool:
    for issues in results.values():
        for issue in issues:
            if issue_type is None or issue["type"] == issue_type:
                return True
    return False


def _get_python_files(path: Path, recursive: bool) -> List[Path]:
    if path.is_file() and path.suffix == ".py":
        return [path]
    elif path.is_dir():
        pattern = "**/*.py" if recursive else "*.py"
        return list(path.glob(pattern))
    return []


def _validate_syntax(file: Path, issues: List[Issue]) -> None:
    try:
        with open(file, "r", encoding="utf-8") as f:
            ast.parse(f.read(), filename=str(file))
    except SyntaxError as e:
        issues.append({
            "type": "SyntaxError",
            "message": e.msg,
            "detail": str(e),
            "line": str(e.lineno) if e.lineno else "",
            "code": ""
        })


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Validate Python code syntax.")
    parser.add_argument("path", type=str, help="Path to the Python file or directory.")
    parser.add_argument("--recursive", action="store_true", help="Recursively check all Python files in the directory.")

    args = parser.parse_args()
    results = validate_python_code(args.path, recursive=args.recursive)
    print_results(results)
