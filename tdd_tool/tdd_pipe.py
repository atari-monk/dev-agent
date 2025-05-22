from typing import List
from agents.chatgpt_agent import ChatGPTAgent
from tdd_tool.actions.run_test_with_feedback import run_test_with_feedback
from tdd_tool.design import getTasks
from tdd_tool.models.task import Task
from tdd_tool.prompts.generate_feedback import generate_feedback, generate_tests_feedback
from utils.py_syntax_utils import has_issues, validate_python_code, validation_results_to_str
from utils.py_type_utils import validate_types


def code_generation_phase(chat: ChatGPTAgent, tasks: List[Task]):
    for task in tasks:
        chat.send_prompt(task.generate_prompt())
        chat.save_code(task.file_path)

        syntax = validate_python_code(task.file_path)
        while has_issues(syntax):
            print("Syntax errors found.")
            fix_task = generate_feedback(validation_results_to_str(syntax))
            chat.send_prompt(fix_task.generate_prompt())
            chat.save_code(task.file_path)
        else:
            print("No syntax errors.")
            
        types = validate_types(task.file_path)
        while has_issues(types):
            print("Type errors found.")
            fix_task = generate_feedback(validation_results_to_str(types))
            chat.send_prompt(fix_task.generate_prompt())
            chat.save_code(task.file_path)
        else:
            print("No type errors.")

def tests_phase(chat: ChatGPTAgent, tasks: List[Task]):
    last_task = tasks[-1]
    fix_task = generate_tests_feedback(run_test_with_feedback(last_task.file_path))
    chat.send_prompt(fix_task.generate_prompt())
    for task in tasks:
        chat.send_prompt(task.generate_fix_prompt())
        chat.save_code(task.file_path)

def tdd_pipe(tasks: List[Task]):
    chat = ChatGPTAgent()
    code_generation_phase(chat, tasks)
    tests_phase(chat, tasks)
    #c.close()

if __name__ == "__main__":
    tdd_pipe(tasks=getTasks())