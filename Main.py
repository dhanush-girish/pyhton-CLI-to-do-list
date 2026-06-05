import json
import os
import argparse

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(description): pass

def list_tasks(): pass  

def main():
    parser = argparse.ArgumentParser(description="my python cli to do list")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")

    list_parser = subparsers.add_parser("list", help="List all tasks")
    args = parser.parse_args()
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
