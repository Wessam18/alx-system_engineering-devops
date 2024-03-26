#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
from sys import argv
import requests


if __name__ == "__main__":

    params = {"userId": argv[1]}
    user_req = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                                                            argv[1])).json()
    task_req = requests.get(
        "https://jsonplaceholder.typicode.com/todos/", params=params).json()

    with open(f"{argv[1]}.csv", "w", newline="") as file:
        line = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in task_req:
            line.writerow([argv[1], user_req.get("username"),
                        task.get('completed'), task.get('title')])
