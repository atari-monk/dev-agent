import types
from typing import List, Optional, Type
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_task import CodeTask


class CodeAgent:
    def __init__(self, persist_session: bool = False):
        self._agent = ChatGPTAgent()
        self._persist = persist_session

    def execute(self, task: CodeTask) -> None:
        self._agent.send_prompt(task.prompt, task.delay_seconds)
        self._agent.save_code(task.output_path, json=task.json_output)
        if not self._persist:
            self._agent.close()

    def batch_execute(self, tasks: List[CodeTask]) -> None:
        for task in tasks:
            self.execute(task)
        if self._persist:
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