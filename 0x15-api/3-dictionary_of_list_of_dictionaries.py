#!/usr/bin/python3
""" fetch data from a REST API """
import json
import requests


if __name__ == "__main__":
    count = 1
    UsersDict = {}
    while True:
        id = count
        api = "https://jsonplaceholder.typicode.com"
        users = "{}/users/{}".format(api, id)
        todos = "{}/todos?userId={}".format(api, id)

        UserRes = requests.get(users)
        if UserRes.status_code == 404:
            break

        UserTasks = requests.get(todos)

        UserObj = UserRes.json()
        TasksObj = UserTasks.json()

        UsersDict[id] = []
        for task in TasksObj:
            data = {}
            data["username"] = UserObj.get("username")
            data["task"] = task.get("title")
            data["completed"] = task.get("completed")
            UsersDict[id].append(data)

        count += 1

    with open("todo_all_employees.json", "w") as f:
        json.dump(UsersDict, f)
