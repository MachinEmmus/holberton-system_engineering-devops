#!/usr/bin/python3
"""API"""
import requests
import sys


if __name__ == "__main__":
    """API"""
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    name_employee = response_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    number_tasks = len(todos_json)

    task_completed = 0
    task_list = ""

    for task in todos_json:
        if task.get("completed") is True:
            task_completed += 1
            task_list += "     {}\n".format(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name_employee,
                                                          task_completed,
                                                          number_tasks))
    print(task_list[:-1])
