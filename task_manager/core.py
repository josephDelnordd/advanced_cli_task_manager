import json
import os
from task_manager.config import get_tasks_file
from task_manager.logger import setup_logger

logger = setup_logger()


def load_tasks():
    tasks_file = get_tasks_file()
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    tasks_file = get_tasks_file()
    with open(tasks_file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(description, priority):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Task added: {description}")
    return task


def list_tasks():
    return load_tasks()


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == len(new_tasks):
        raise ValueError("Task not found")

    save_tasks(new_tasks)
    logger.info(f"Task deleted: {task_id}")