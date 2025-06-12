from pathlib import Path
import time
from colorama import Fore, Style
from chatgpt_utils.chatgpt_automation import (
    save_code_block,
    send_prompt,
)
from chrome_utils.chrome_automation import open_chrome_with_profile
from utils.colorama_utils import color_print
from selenium import webdriver


def open_chatgpt_session(
    page: str, config_Path: str, detach: bool, delay_seconds: int
) -> webdriver.Chrome | None:
    message = f"Initializing Chrome with profile... ({delay_seconds} seconds delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    driver = open_chrome_with_profile(page, config_Path, detach=detach)
    time.sleep(delay_seconds)
    return driver


def send_chatgpt_prompt(driver: webdriver.Chrome, prompt: str, delay_seconds: int, printPrompt:bool=False) -> None:
    message = f"Sending Prompt... ({delay_seconds} seconds delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    if printPrompt:
        print(prompt)
    send_prompt(driver, prompt)
    time.sleep(delay_seconds)


def save_chatgpt_code_block(
    driver: webdriver.Chrome, output_file_path: Path, delay_seconds: int, json: bool = False, printResponse:bool=False, overwrite:bool=False
):
    message = f"Saving Response... ({delay_seconds} second delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    response = save_code_block(driver, output_file_path, wait_time=60, json=json, overwrite=overwrite)
    if printResponse:
        print("Response:")
        print(response)
    time.sleep(delay_seconds)
    return response
