#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
from sys import argv
import requests

if __name__ == "__main__":
    user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()
    tasks = requests.get(
            "https://jsonplaceholder.typicode.com/todos/").json()

    with open(f"{argv[1]}.csv", "w", newline="") as f:
        x = csv.writer(f)
        x.writerow(["USER_ID", "USERNAME", "COMPLETED", "TASK_TITLE"])
        for task in tasks:
            x.writerow([(argv[1]), user.get("username"),
                        task.get("completed"), task.get("title")])
