from pathlib import Path
from typing import List, Optional
import tomli
from automation_scripts.models import Automation, Feature

def load_automation_from_toml(filepath: Path) -> Automation:
    with open(filepath, "rb") as f:
        data = tomli.load(f)
    return Automation.model_validate(data)

def get_active_feature(features: List[Feature]) -> Optional[Feature]:
    return next((f for f in features if f.status == "pending"), None)

if __name__ == "__main__":
    path = Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml")
    project = load_automation_from_toml(path)
    print(project)
