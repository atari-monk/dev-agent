from pathlib import Path
from dataclasses import dataclass
from selenium import webdriver

@dataclass
class CodeBlockConfig:
    driver: webdriver.Chrome
    output_file_path: Path
    delay_seconds: int
    json: bool = False
    printResponse:bool=False
    overwrite:bool=False