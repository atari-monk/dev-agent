import types
from typing import List, Optional, Type
from agents.code_task import CodeTask
from agents.interface.ichatgpt_agent import IChatGPTAgent
from agents.interface.icode_agent import ICodeAgent

class CodeAgent(ICodeAgent):
    def __init__(self, chatgpt_agent: IChatGPTAgent):
        self._agent = chatgpt_agent

    def execute(self, task: CodeTask) -> str | None:
        self._agent.send_prompt(task.prompt, task.delay_seconds)
        return self._agent.save_code(task.output_path, 2)

    def batch_execute(self, tasks: List[CodeTask]) -> List[Optional[str]]:
        result: List[Optional[str]] = []
        for task in tasks:
            result.append(self.execute(task))
        return result

    def open(self):
        self._agent.open()

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