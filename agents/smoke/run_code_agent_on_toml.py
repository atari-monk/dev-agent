from pathlib import Path
from typing import Union
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from automation_db.automation.model import AutomationContext

def ensure_path_exists(path: Union[str, Path], is_file: bool = False) -> Path:
    path = Path(path)
    if is_file:
        path.parent.mkdir(parents=True, exist_ok=True)
    else:
        path.mkdir(parents=True, exist_ok=True)
    return path

def get_code_task(prompt: str, path:Path):
    return CodeTask(
        prompt=prompt,
        delay_seconds=40,
        output_path=path,
        json_output=False,
        overwrite=True)

def main():
    agent = CodeAgent(ChatGPTAgent())
    agent.open()
    context = AutomationContext()
    is_pending = context.load()
    if not is_pending:
        print('\nNo pending task\n')
        return
    while is_pending:
        context.generate_prompt()
        ensure_path_exists(context.path, True)
        task = get_code_task(context.prompt, context.path)
        agent.execute(task)
        context.update_task()
        is_pending = context.load()
        if not is_pending:
            print('\nNo pending task\n')
            return
    agent.close()
    
if __name__ == "__main__":
    main()