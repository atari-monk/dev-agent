from pathlib import Path
from automation_scripts.models import Automation
from automation_scripts.crud import load_automation_from_toml

def generate_code_standards_prompt(data: Automation) -> str:
    prompt = [
        "Code Standards",
        *[f"- {req}" for req in data.code_requirements.requirements],
    ]
    return "\n".join(prompt)

if __name__ == "__main__":
    path = Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml")
    automation = load_automation_from_toml(path)
    print(generate_code_standards_prompt(automation))