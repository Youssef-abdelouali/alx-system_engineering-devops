#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            y.get("id"): [{
                "task": tas.get("title"),
                "completed": tas.get("completed"),
                "username": y.get("username")
            } for tas in requests.get(url + "todos",
                                    params={"userId": y.get("id")}).json()]
            for y in users}, jsonfile)
