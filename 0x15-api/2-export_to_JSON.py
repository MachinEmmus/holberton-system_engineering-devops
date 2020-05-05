#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    task_list = []

    for task in todos_json:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = employee_name
        task_list.append(task_dict)
    todos = {"{}".format(id): task_list}

    with open(id + ".json", "a") as fd:
        json.dump(todos, fd)
