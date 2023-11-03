#!/usr/bin/python3
"""
Module: fetch_employee_tasks

This module provides functionality to fetch and print details about an
employee's tasks from the
placeholder API (https://jsonplaceholder.typicode.com).
The module can be used as a standalone script
or imported into other Python programs.
"""

import requests
import sys


def fetch_employee_tasks(emp_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_resp = requests.get(user_url)
    user_data = user_resp.json()
    employee_name = user_data.get("name", "Unknown")

    t_ul = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todo_response = requests.get(t_ul)
    todos = todo_response.json()

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed", False)]
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{})".format(employee_name, \
number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t", task.get("title", "Unknown Task"))


if __name__ == "__main__":
    # Taking input from the command line
    emp_id = sys.argv[1]
    # Calling the fetch_employee function
    fetch_employee_tasks(emp_id)
