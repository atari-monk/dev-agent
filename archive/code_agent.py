from pathlib import Path
from agents.chatgpt_agent import ChatGPTAgent
from archive.task_prompt import TaskPrompt

def main():
    t = TaskPrompt()
    t.get_task("46210739-c4e6-463f-844f-21a278df5533")
    prompt = t.generate_prompt()
    print(prompt)
    
    c = ChatGPTAgent()
    c.send_prompt(prompt)
    c.save_code(Path("data/fibonacci.py"))
    c.close()

if __name__ == "__main__":
    main()
