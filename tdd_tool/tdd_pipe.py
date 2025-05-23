from typing import List
from agents.chatgpt_agent import ChatGPTAgent
from tdd_tool.actions.run_test_with_feedback import run_test_with_feedback
from tdd_tool.design import getTasks
from tdd_tool.models.task import Task
from tdd_tool.prompts.generate_feedback import generate_feedback
from utils.py_syntax_utils import has_issues, validate_python_code, validation_results_to_str
from utils.py_type_utils import validate_types


def code_generation_phase(chat: ChatGPTAgent, tasks: List[Task]):
    for task in tasks:
        chat.send_prompt(task.generate_prompt())
        chat.save_code(task.file_path)

        if task.skipValidation:
            print("Skipping validation for this task.")
            continue
        print(f"Validating {task.file_path}")
        syntax_counter = 0
        syntax = validate_python_code(task.file_path)
        while has_issues(syntax) and syntax_counter < 2:
            print("Syntax errors found.")
            fix_task = generate_feedback(validation_results_to_str(syntax))
            chat.send_prompt(fix_task.generate_prompt())
            chat.save_code(task.file_path)
            syntax = validate_python_code(task.file_path)
            syntax_counter += 1
        else:
            if syntax_counter >= 2:
                print("Maximum syntax fix attempts reached.")
            else:
                print("No syntax errors.")
            
        type_counter = 0
        types = validate_types(task.file_path)
        while has_issues(types) and type_counter < 2:
            print("Type errors found.")
            fix_task = generate_feedback(validation_results_to_str(types))
            chat.send_prompt(fix_task.generate_prompt())
            chat.save_code(task.file_path)
            types = validate_types(task.file_path)
            type_counter += 1
        else:
            if type_counter >= 2:
                print("Maximum type fix attempts reached.")
            else:
                print("No type errors.")

def fail_tests_phase(tasks: List[Task]):
    last_task = tasks[-1]

    output, all_failed = run_test_with_feedback(last_task.file_path)
    if all_failed:
        print("All tests failed!")
        print(output)
    else:
        print("Some tests passed or there were other issues")
        print(output)
   
def tdd_pipe(tasks: List[Task]):
    chat = ChatGPTAgent()
    code_generation_phase(chat, tasks)
    fail_tests_phase(tasks)
    #c.close()

if __name__ == "__main__":
    tdd_pipe(tasks=getTasks())