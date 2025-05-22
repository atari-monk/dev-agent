import os
from pathlib import Path
from typing import List

def get_py_files(folder_path: Path) -> list[Path]:
    py_files: List[Path] = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                full_path = Path(root) / file
                py_files.append(full_path)
    return py_files

def ensure_init_py_in_parents(file_path: Path, stop_at: Path | None = None) -> None:
    stop_at = Path.cwd() if stop_at is None else stop_at.resolve()
    parent = file_path.parent.resolve()
    
    if stop_at not in parent.parents and parent != stop_at:
        return

    while parent != stop_at:
        (parent / "__init__.py").touch(exist_ok=True)
        parent = parent.parent
        
if __name__ == "__main__":
    home_path = Path.home()
    python_files = get_py_files(home_path)
    for file in python_files:
        print(file)
