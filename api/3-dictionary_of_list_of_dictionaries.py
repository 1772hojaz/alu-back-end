#!/usr/bin/python3


""" 
Python script to export data in the JSON format.
"""
import json
import requests

def get_json_from_url(url):
    response = requests.get(url)
    return response.json()

def fetch_data():
    users = get_json_from_url("https://jsonplaceholder.typicode.com/users")
    todos = get_json_from_url("https://jsonplaceholder.typicode.com/todos")

    tasks_by_user = {}

    for todo in todos:
        user_id = str(todo["userId"])
        if user_id not in tasks_by_user:
            user = next(
                user for user in users if user["id"] == todo["userId"])
            tasks_by_user[user_id] = []

        task = {
            "username": user["username"],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        
        tasks_by_user[user_id].append(task)

    return tasks_by_user

def main():
    data = fetch_data()
    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
