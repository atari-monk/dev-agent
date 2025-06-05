from pathlib import Path
from automation_scripts.crud import load_automation_from_toml
from automation_scripts.models import Automation

def generate_project_prompt(data: Automation) -> str:
    prompt = [
        f"Project: {data.project.name}",
        "Requirements",
        *[f"- {req}" for req in data.project.requirements],
        "Dependencies",
        *[f"- {dep}" for dep in data.project.dependencies]
    ]
    return "\n".join(prompt)

def main():
    path = Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml")
    automation: Automation = load_automation_from_toml(path)
    print(generate_project_prompt(automation))

if __name__ == "__main__":
    main()