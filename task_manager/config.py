import os

DEFAULT_TASKS_FILE = "tasks.json"

def get_tasks_file():
    return os.getenv("TASKS_FILE_PATH", DEFAULT_TASKS_FILE)