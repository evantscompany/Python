import json
import os
from user import User
from todo import Todo

class Storage:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return {}

        with open(self.filename, "r", encoding="utf-8") as f:
            raw = json.load(f)

        users = {}
        for username, data in raw.items():
            user = User(username, data["password"])

            for t in data["todos"]:
                todo = Todo(
                    t["title"],
                    t["priority"],
                    t["deadline"],
                    t["category"]
                )
                todo.completed = t["completed"]
                user.todos.append(todo)

            users[username] = user

        return users

    def save(self, users):
        result = {}

        for username, user in users.items():
            result[username] = {
                "password": user.password,
                "todos": [
                    {
                        "title": t.title,
                        "priority": t.priority,
                        "deadline": t.deadline,
                        "category": t.category,
                        "completed": t.completed
                    }
                    for t in user.todos
                ]
            }

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
