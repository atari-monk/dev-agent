import re

def clean_code(code: str) -> str:
    code = code.strip()
    code = code.replace('\r\n', '\n').replace('\r', '\n')
    code = re.sub(r'\n{3,}', '\n\n', code)
    return code
