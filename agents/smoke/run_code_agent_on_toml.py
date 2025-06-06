from pathlib import Path
from typing import Union
from agents.chatgpt_agent import ChatGPTAgent
from agents.code_agent import CodeAgent
from agents.code_task import CodeTask
from automation_scripts.prompt.combined_prompt import get_active_feature_task

def ensure_path_exists(path: Union[str, Path], is_file: bool = False) -> Path:
    path = Path(path)
    if is_file:
        path.parent.mkdir(parents=True, exist_ok=True)
    else:
        path.mkdir(parents=True, exist_ok=True)
    return path

def run_code_agent_on_toml():
    result = get_active_feature_task()
    if not result:
        return
    repo_path = Path(result.automation.project.path)
    feature_file = result.feature.files[result.task.file]
    output_path = repo_path / feature_file.path / feature_file.file 
    ensure_path_exists(output_path, is_file=True)

    task = CodeTask(
        prompt=result.prompt,
        delay_seconds=40,
        output_path=output_path,
        json_output=False,
    )

    agent = CodeAgent(ChatGPTAgent())
    agent.open()
    agent.execute(task)
    agent.close()

if __name__ == "__main__":
    run_code_agent_on_toml()