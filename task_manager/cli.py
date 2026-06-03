import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description")
    add_parser.add_argument("--priority", default="medium")

    # List
    subparsers.add_parser("list", help="List all tasks")

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.description, args.priority)
        print(f"Added task #{task['id']}")

    elif args.command == "list":
        tasks = list_tasks()
        for t in tasks:
            print(f"{t['id']} - {t['description']} ({t['priority']})")

    elif args.command == "delete":
        delete_task(args.task_id)
        print("Task deleted")


if __name__ == "__main__":
    main()