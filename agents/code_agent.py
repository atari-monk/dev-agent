import types
from typing import List, Optional, Type
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_task import CodeTask


class CodeAgent:
    def __init__(self):
        self._agent = ChatGPTAgent()

    def execute(self, task: CodeTask) -> str | None:
        self._agent.send_prompt(task.prompt, task.delay_seconds)
        return self._agent.save_code(task.output_path, json=task.json_output, overwrite=task.overwrite)

    def batch_execute(self, tasks: List[CodeTask]) -> List[Optional[str]]:
        result: List[Optional[str]] = []
        for task in tasks:
            result.append(self.execute(task))
        return result

    def close(self) -> None:
        self._agent.close()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[types.TracebackType],
    ) -> None:
        self._agent.close()