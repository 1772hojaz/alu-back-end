#!/usr/bin/python3


"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

def fetch_employee_tasks(emp_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_resp = requests.get(user_url)
    user_data = user_resp.json()
    username = user_data.get("username", "Unknown")

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    tasks_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed", False),
            "username": username
        }
        tasks_list.append(task_dict)

    with open(f"{emp_id}.json", "w") as jsonfile:
        json.dump({emp_id: tasks_list}, jsonfile, indent=4)

if __name__ == "__main__":
    emp_id = sys.argv[1]
    fetch_employee_tasks(emp_id)