from pathlib import Path
from typing import Protocol, runtime_checkable


@runtime_checkable
class IProjectAgent(Protocol):
    def execute(self, base_path: Path, game_description: str) -> None: ...

    def get_prompt(self, game_description: str) -> str: ...