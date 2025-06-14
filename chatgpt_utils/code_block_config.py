from selenium import webdriver


from dataclasses import dataclass
from pathlib import Path


@dataclass
class CodeBlockConfig:
    driver: webdriver.Chrome
    output_file_path: Path
    delay_seconds: int
    json: bool = False
    printResponse:bool=False
    overwrite:bool=False