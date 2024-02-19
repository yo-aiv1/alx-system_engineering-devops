#!/usr/bin/python3
""" fetch data from a REST API """
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com"
    users = "{}/users/{}".format(api, id)
    todos = "{}/todos?userId={}".format(api, id)

    UserRes = requests.get(users)
    UserTasks = requests.get(todos)

    UserObj = UserRes.json()
    TasksObj = UserTasks.json()

    FileName = "{}.json".format(id)
    UserDict = {id: []}
    for task in TasksObj:
        data = {}
        data["task"] = task.get("title")
        data["completed"] = task.get("completed")
        data["username"] = UserObj.get("username")
        UserDict[id].append(data)

    with open(FileName, "w") as f:
        json.dump(UserDict, f)
