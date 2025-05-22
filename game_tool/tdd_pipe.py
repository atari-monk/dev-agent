from typing import List
from agents.chatgpt_agent import ChatGPTAgent
from game_tool.actions.run_test_with_feedback import run_test_with_feedback
from game_tool.design import getTasks
from game_tool.models.task import Task
from game_tool.models.task_type import TaskType


def tdd_pipe(tasks: List[Task]):
    c = ChatGPTAgent()

    for task in tasks:
        if task.task_type == TaskType.Code:
            c.send_prompt(task.generate_prompt())
            c.save_code(task.file_path)
        if task.task_type == TaskType.Test:
            run_test_with_feedback(task)
            c.send_prompt(task.generate_prompt())
            c.save_code(task.file_path)

    #c.close()

if __name__ == "__main__":
    tdd_pipe(tasks=getTasks())