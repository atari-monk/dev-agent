from selenium import webdriver
from dataclasses import dataclass

@dataclass
class PromptConfig:
    driver: webdriver.Chrome
    prompt: str
    delay_seconds: int
    printPrompt:bool=False
    input_area_id: str = "prompt-textarea"