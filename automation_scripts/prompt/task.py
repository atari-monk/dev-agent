from pathlib import Path
from automation_scripts.crud import load_automation_from_toml
from automation_scripts.models import Automation, Task

def get_first_pending_task(data: Automation) -> Task | None:
    for feature in data.features:
        if feature.tasks:
            for task in feature.tasks:
                if task.status == "pending":
                    return task
    return None

def generate_task_prompt(task: Task) -> str:
    prompt_lines = [
        f"Task: {task.id}",
        "Requirements:",
        *[f"- {req}" for req in task.requirements]
    ]
    
    if task.depends_on:
        prompt_lines.extend([
            "",
            "Dependencies:",
            *[f"- {dep}" for dep in task.depends_on]
        ])
    
    return "\n".join(prompt_lines)

def main():
    path = Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml")
    automation = load_automation_from_toml(path)
    task = get_first_pending_task(automation)
    if not task:
        return "No pending tasks available"
    print(generate_task_prompt(task))

if __name__ == "__main__":
    main()