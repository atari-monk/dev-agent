from pathlib import Path
from typing import Protocol, runtime_checkable


@runtime_checkable
class IChatGPTAgent(Protocol):
    def open(self) -> None:
        ...

    def close(self) -> None:
        ...

    def send_prompt(self, prompt: str, delay_seconds: int) -> None:
        ...

    def save_code(
        self,
        output_file_path: Path,
        delay_seconds: int
    ) -> str | None:
        ...