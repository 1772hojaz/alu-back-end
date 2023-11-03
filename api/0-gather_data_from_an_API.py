#!/usr/bin/python3
import requests
import sys

#fetching employee tasks
def fetch_employee_tasks(employee_id):

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_resp = requests.get(user_url)
    user_data = user_resp.json()
    employee_name = user_data.get("name", "Unknown")

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed", False)]
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{})".format(employee_name, number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t", task.get("title", "Unknown Task"))

if __name__ == "__main__":
#taking input from the command line
    employee_id = sys.argv[1]
#calling the fetch_employee funtion
    fetch_employee_tasks(employee_id)

