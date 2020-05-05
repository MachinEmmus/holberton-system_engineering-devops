#!/usr/bin/python3
import json
import requests


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    all_user = {}
    list_dict = []
    dicty = {}
    for item in users:
        response = requests.get(
                        "https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(item['id'])).json()
        for task in response:
            dicty['username'] = item['username']
            dicty['task'] = task['title']
            dicty['completed'] = task['completed']
            list_dict.append(dicty)
            dicty = {}
        all_user[item['id']] = list_dict
        list_dict = []

    all_user = json.dumps(all_user)
    with open('todo_all_employees.json', 'w', newline='') as file:
        file.write(all_user)
