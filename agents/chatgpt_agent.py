from pathlib import Path
from chatgpt_utils.chatgpt_cli import (
    open_chatgpt_session,
    save_chatgpt_code_block,
    send_chatgpt_prompt,
)

class ChatGPTAgent:
    def __init__(self):
        self.driver = None
        self.open()

    def open(self):
        if self.driver is not None:
            self.driver.quit()
        self.driver = open_chatgpt_session(
            page="https://chat.openai.com/",
            config_Path=r"C:\atari-monk\code\apps-data-store\chrome_profiles.json",
            detach=True,
            delay_seconds=5,
        )

    def close(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def send_prompt(self, prompt:str, delay_seconds:int=25):
        if self.driver is None:
            raise Exception("ChatGPT session is not open.")
        send_chatgpt_prompt(self.driver, prompt, delay_seconds)

    def save_code(self, output_file_path: Path, delay_seconds:int=1, json: bool = False):
        if self.driver is None:
            raise Exception("ChatGPT session is not open.")
        save_chatgpt_code_block(self.driver, output_file_path, delay_seconds, json=json)


def main():
    assumptions = "Dont use comments in code. Do not wrtie anything but code. Asume strict typing."
    function = f"Python function that calculates the Fibonacci sequence."
    test = f"Write pytest unit test for {function}. Only test, dont implement the function yet, import it from same directory."
    task = f"Write a {function} passing all tests." 
    
    codeFilePath = Path("data/fibonacci.py")
    testFilePath = Path("data/fibonacci.test.py")

    c = ChatGPTAgent()
    c.send_prompt(f"{assumptions} {test}")
    c.save_code(Path(testFilePath))
    
    c.send_prompt(task)
    c.save_code(Path(codeFilePath))
    c.close()

if __name__ == "__main__":
    main()
