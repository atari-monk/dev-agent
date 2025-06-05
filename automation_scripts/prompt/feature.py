from pathlib import Path
from typing import List, Optional
from automation_scripts.crud import load_automation_from_toml
from automation_scripts.models import Automation, Feature, FeatureFile

def get_active_feature(features: List[Feature]) -> Optional[Feature]:  
    return next(  
        (feature for feature in features if feature.status == "pending"),  
        None  
    )    

def generate_file_prompt(file_key: str, file_obj: FeatureFile) -> str:
    file_prompt = [
        f"- {file_key}:",
        f"  - File: {file_obj.file}",
        f"  - Path: {file_obj.path}",
    ]
    if file_obj.class_:
        file_prompt.append(f"  - Class: {file_obj.class_}")
    return "\n".join(file_prompt)

def generate_feature_prompt(feature: Feature, include_files: bool = False) -> str:
    prompt = [
        f"Feature: {feature.name}",
        "Requirements",
        *[f"- {req}" for req in feature.requirements],
    ]
    
    if include_files and feature.files:
        prompt.extend(["Files"])
        for file_key, file_obj in feature.files.items():
            prompt.append(generate_file_prompt(file_key, file_obj))
    
    return "\n".join(prompt)

def main():
    path = Path(r"C:\atari-monk\code\race-track-game\docs\automation.toml")
    automation: Automation = load_automation_from_toml(path)
    feature = get_active_feature(automation.features)
    if not feature:
        print("Warning: No active feature found")
        return
    print(generate_feature_prompt(feature, True))

if __name__ == "__main__":
    main()