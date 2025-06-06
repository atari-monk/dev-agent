from pathlib import Path
from typing import List
from automation_scripts.crud import load_automation_from_toml
from automation_scripts.models import Automation, Feature, Task
from automation_scripts.prompt.feature import generate_feature_prompt, get_active_feature
from automation_scripts.prompt.project import generate_project_prompt
from automation_scripts.prompt.agent import generate_agent_task_prompt, get_first_pending_task
from automation_scripts.prompt.code_standards import generate_code_standards_prompt
from automation_scripts.prompt.task import generate_task_prompt
from dataclasses import dataclass

@dataclass
class AutomationData:
    automation: Automation
    feature: Feature
    task: Task
    prompt: str

def generate_combined_prompt(data: Automation, feature: Feature, task: Task) -> str:
    prompt_sections: List[str] = []
    
    if project_prompt := generate_project_prompt(data):
        prompt_sections.append(project_prompt)
    
    if feature_prompt := generate_feature_prompt(feature):
        prompt_sections.append(feature_prompt)
    
    if task_prompt := generate_task_prompt(task):
        prompt_sections.append(task_prompt)
    
    if agent_prompt := generate_agent_task_prompt(data):
        prompt_sections.append(agent_prompt)
    
    if standards_prompt := generate_code_standards_prompt(data):
        prompt_sections.append(standards_prompt)
    
    return "\n\n".join(prompt_sections)

def get_active_feature_task() -> AutomationData | None:
    automation = load_automation_from_toml(Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml"))
    feature = get_active_feature(automation.features)
    if not feature:
        print("No active Feature")
        return None
    task = get_first_pending_task(automation)
    if not task:
        print("No pending tasks available")
        return None
    prompt = generate_combined_prompt(automation, feature, task) 
    result = AutomationData(automation, feature, task, prompt)
    return result

def main():
    print(get_active_feature_task())

if __name__ == "__main__":
    main()