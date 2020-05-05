#!/usr/bin/python3
"""API"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json["name"]

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    todos = requests.get(url)
    todos_json = todos.json()
    number_tasks = len(todos_json)

    task_compleated = 0
    task_list = ""

    with open(user_id + ".csv", "a") as fd:
        for todo in todos_json:
            completed = todo.get("completed")
            title = todo.get("title")
            data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(user_id,
                                                          employee_name,
                                                          completed, title)
            fd.write(data)
