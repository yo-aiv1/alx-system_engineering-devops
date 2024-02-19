#!/usr/bin/python3
""" fetch data from a REST API """
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com"
    users = "{}/users/{}".format(api, id)
    todos = "{}/todos?userId={}".format(api, id)

    UserRes = requests.get(users)
    UserName = UserRes.json().get("name")
    print("Employee {} is done with".format(UserName), end="")

    UserTasks = requests.get(todos)
    TasksObj = UserTasks.json()
    CompletedTasks = []
    count = 0
    for task in TasksObj:
        if task.get('completed') is True:
            CompletedTasks.append(task.get("title"))

    print(" ({}/{}):".format(len(CompletedTasks), len(TasksObj)))
    for task in CompletedTasks:
        print("\t {}".format(task))
