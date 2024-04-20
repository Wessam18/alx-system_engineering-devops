#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    req_user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    user_todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos/")

    employee_name = req_user.json().get("name")
    number_tasks = 0
    total_tasks = 0

    for x in user_todo.json():
        if x.get("userId") == int(argv[1]):
            total_tasks += 1
            if x.get("completed"):
                number_tasks += 1

    employee = f"Employee {employee_name} is done with tasks({number_tasks}/{total_tasks}):"
    
    print(employee)

    for x in user_todo.json():
        if x.get("userId") == int(argv[1]):
            if x.get("completed") is True:
                print("\t {}".format(x.get("title")))
