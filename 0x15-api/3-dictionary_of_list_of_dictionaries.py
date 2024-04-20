#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    users = requests.get(
            f"https://jsonplaceholder.typicode.com/users/").json()
    tasks = requests.get(
            "https://jsonplaceholder.typicode.com/todos/").json()

    #all_employee = {}

    for user in users:
        all_tasks = []
        for task in tasks:
            if task.get("userId") == user.get("id"):
                user_task = {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                all_tasks.append(user_task)
        #all_employee[user.get("id")] = all_tasks
        export_data = {user.get("id"): all_tasks}

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(export_data, jsonfile)
