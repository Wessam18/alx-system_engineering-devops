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
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()
    tasks= requests.get(
            "https://jsonplaceholder.typicode.com/todos/").json()
    
    #url = "https://jsonplaceholder.typicode.com/"
    #user_id = sys.argv[1]

    #user = requests.get(url + "users/{}".format(user_id)).json()
    #tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    username = user.get("username")

    with open(f"{argv[1]}.json", "w") as jsonfile:
        json.dump({user.get("id"): [
            {"task": task.get("title"),
            "completed": task.get("completed"),
            "username": username} for task in tasks]}, jsonfile)
