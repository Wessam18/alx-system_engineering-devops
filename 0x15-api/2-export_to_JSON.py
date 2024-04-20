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
    tasks = requests.get(
            "https://jsonplaceholder.typicode.com/todos/").json()
    
    # Initialize an empty list to hold tasks data
    tasks_data = []

    # Iterate through tasks and populate tasks_data list
    for task in tasks:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        }
        tasks_data.append(task_info)

    # Prepare data for JSON export
    export_data = {user.get("id"): tasks_data}

    # Export data to JSON file
    with open(f"{argv[1]}.json", "w") as jsonfile:
        json.dump(export_data, jsonfile)


    #with open(f"{argv[1]}.json", "w") as jsonfile:
        #json.dump({user.get("id"): [
            #{"task": task.get("title"),
                #"completed": task.get("completed"),
                #"username": user.get("username")} for task in tasks]},
                #jsonfile)
