#!/usr/bin/python3
"""API https://jsonplaceholder.typicode.com/"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    r = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    response = requests.get(r).json()

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json()
    username = user['username']
    dicty = {}
    listy = []

    for i in response:
        dicty['task'] = i['title']
        dicty['completed'] = i['completed']
        dicty['username'] = username
        listy.append(dicty)
        dicty = {}

    dicty[id] = listy
    dicty = json.dumps(dicty)
    with open(id + '.json', 'w', newline='') as file:
        file.write(dicty)
