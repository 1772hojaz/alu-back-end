#!/usr/bin/python3

"""
Python script to export data in the CSV format.
"""


import requests
import sys
import csv


def fetch_employee_tasks(emp_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_resp = requests.get(user_url)
    user_data = user_resp.json()
    username = user_data.get("username", "Unknown")

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    with open(f"{emp_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([emp_id, username, task.get("completed", False), task.get("title")])

if __name__ == "__main__":
    emp_id = sys.argv[1]
    fetch_employee_tasks(emp_id)