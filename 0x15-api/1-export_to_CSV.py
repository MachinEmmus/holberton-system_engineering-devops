#!/usr/bin/python3
"""API https://jsonplaceholder.typicode.com/"""
import csv
import requests
import sys


if __name__ == "__main__":
    """API"""
    id = sys.argv[1]
    r = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    response = requests.get(r).json()

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json()
    username = user['username']

    with open(id + '.csv', 'w', newline='') as csvfile:
        for item in response:
            spamwriter = csv.writer(
                                    csvfile, delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            spamwriter.writerow(
                                [item['userId']] +
                                [username] +
                                [item['completed']] +
                                [item['title']])
