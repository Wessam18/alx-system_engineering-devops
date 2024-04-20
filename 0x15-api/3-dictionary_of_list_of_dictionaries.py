#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    tasks = requests.get(url + "todos").json()

    all_employee = {}

    for user in users:
        id = user.get("id")
        username = user.get("username")
        all_tasks = []
        for task in tasks:
            user_task = {}
            if task.get("userId") == id:
                user_task["username"] = username
                user_task["task"] = task.get("title")
                user_task["completed"] = task.get("completed")
                all_tasks.append(user_task)
        all_employee[id] = all_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employee, jsonfile)
