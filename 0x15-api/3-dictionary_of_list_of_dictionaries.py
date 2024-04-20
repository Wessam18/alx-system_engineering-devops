#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users/").json()
    tasks = requests.get(
            "https://jsonplaceholder.typicode.com/todos/").json()

    for use in user:
        id = use.get("id")
        username = use.get("username")

        tasks_data = []

        for task in tasks:
            task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": use.get("username")
            }
            tasks_data.append(task_info)

    export_data = {use.get("id"): tasks_data}

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(export_data, jsonfile)
