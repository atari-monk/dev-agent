from typing import List, Optional


def get_standard_assumptions(additional: Optional[List[str]] = None) -> List[str]:
    base_assumptions = [
        "No comments in code", 
        "Strict typing"
    ]
    return base_assumptions + (additional if additional else [])
