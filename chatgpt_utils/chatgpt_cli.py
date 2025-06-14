import time
from colorama import Fore, Style
from chatgpt_utils.code_block_config import CodeBlockConfig
from chatgpt_utils.prompt_config import PromptConfig
from chatgpt_utils.chatgpt_config import ChatGPTConfig
from chatgpt_utils.chatgpt_automation import (
    save_code_block,
    send_prompt,
)
from chrome_utils.chrome_automation import open_chrome_with_profile
from utils.colorama_utils import color_print
from selenium import webdriver

def open_chatgpt_session(config: ChatGPTConfig) -> webdriver.Chrome | None:
    message = f"Initializing Chrome with profile... ({config.delay_seconds} seconds delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    driver = open_chrome_with_profile(config)
    time.sleep(config.delay_seconds)
    return driver

def send_chatgpt_prompt(config: PromptConfig) -> None:
    message = f"Sending Prompt... ({config.delay_seconds} seconds delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    if config.printPrompt:
        print(config.prompt)
    send_prompt(config)
    time.sleep(config.delay_seconds)

def save_chatgpt_code_block(config: CodeBlockConfig):
    message = f"Saving Response... ({config.delay_seconds} second delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    response = save_code_block(config)
    if config.printResponse:
        print("Response:")
        print(response)
    time.sleep(config.delay_seconds)
    return response
