from typing import List, Optional


def get_standard_assumptions(additional: Optional[List[str]] = None) -> List[str]:
    base_assumptions = [
        "No comments in code", 
        "Strict typing",
        "Generate only one code block, when new or fixed as a unit",
    ]
    return base_assumptions + (additional if additional else [])
