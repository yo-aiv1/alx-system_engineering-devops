#!/usr/bin/python3
""" fetch data from a REST API """
import csv
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

    FileName = "{}.csv".format(id)
    with open(FileName, mode="w", newline='') as f:
        for task in TasksObj:
            user = [UserObj.get("id"), UserObj.get("username")]
            user.append(str(task.get("completed")))
            user.append(task.get("title"))
            write = csv.writer(f,
                               delimiter=',',
                               quotechar='"',
                               quoting=csv.QUOTE_ALL)
            write.writerow(user)
