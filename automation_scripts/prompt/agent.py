from pathlib import Path
from typing import Optional
from automation_scripts.crud import load_automation_from_toml
from automation_scripts.models import Automation, Task

def get_first_pending_task(data: Automation) -> Optional[Task]:
    for feature in data.features:
        if feature.tasks:
            for task in feature.tasks:
                if task.status == "pending":
                    return task
    return None

def generate_agent_task_prompt(data: Automation) -> Optional[str]:
    task = get_first_pending_task(data)
    if not task:
        return None
    
    agent = next((a for a in data.agents if a.role == task.assigned_to), None)
    if not agent:
        return None
    
    prompt = [
        f"Agent: {agent.role}",
        *[f"- {spec}" for spec in agent.requirements]
    ]
    return "\n".join(prompt)

if __name__ == "__main__":
    automation = load_automation_from_toml(Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml"))
    print(generate_agent_task_prompt(automation))