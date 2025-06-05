import os
import sys
from pathlib import Path
from typing import List, Set

DEFAULT_IGNORES: Set[str] = {'.git', '__pycache__', '.idea', '.vscode', 'venv', 'env', 'node_modules', '__init__.py'}

def get_all_files(directory: Path, ignores: Set[str] = DEFAULT_IGNORES) -> List[Path]:
    file_list: List[Path] = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignores]
        for file in files:
            if file not in ignores:
                file_list.append(Path(root) / file)
    return file_list

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No folder path provided")
        print(f"Usage: {sys.argv[0]} <folder_path>")
        print(f"Ignored folders/files: {', '.join(DEFAULT_IGNORES)}")
        sys.exit(1)
    
    folder_path = Path(sys.argv[1])
    if not folder_path.exists():
        print(f"Error: Path '{folder_path}' does not exist")
        sys.exit(1)
    if not folder_path.is_dir():
        print(f"Error: '{folder_path}' is not a directory")
        sys.exit(1)
    
    files = get_all_files(folder_path)
    with open('temp.txt', 'w', encoding='utf-8') as f:
        for file in files:
            f.write(f"{file}\n")
    
    print(f"File paths written to temp.txt ({len(files)} entries)")