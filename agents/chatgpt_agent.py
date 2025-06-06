from pathlib import Path
from agents.interface.ichatgpt_agent import IChatGPTAgent
from chatgpt_utils.chatgpt_cli import (
    open_chatgpt_session,
    save_chatgpt_code_block,
    send_chatgpt_prompt,
)

class ChatGPTAgent(IChatGPTAgent):
    def __init__(self):
        self.driver = None

    def open(self):
        if self.driver is not None:
            self.driver.quit()
        self.driver = open_chatgpt_session(
            page="https://chat.openai.com/",
            config_Path=r"C:\atari-monk\code\apps-data-store\chrome_profiles.json",
            detach=True,
            delay_seconds=10)

    def close(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def send_prompt(self, prompt:str, delay_seconds:int=45):
        if self.driver is None:
            raise Exception("ChatGPT session is not open.")
        send_chatgpt_prompt(self.driver, prompt, delay_seconds)

    def save_code(self, output_file_path: Path, delay_seconds:int=1, json: bool = False, overwrite:bool=False) -> str | None:
        if self.driver is None:
            raise Exception("ChatGPT session is not open.")
        return save_chatgpt_code_block(self.driver, output_file_path, delay_seconds, json=json, overwrite=overwrite)