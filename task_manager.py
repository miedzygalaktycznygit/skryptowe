import json
from datetime import datetime, date
from pathlib import Path

class TaskManager:
    def __init__ (self, filename = "tasks.json"):
        self.filename = Path(filename)
        self.tasks = []
        self._load_tasks()

    def _load_tasks(self):
        if self.filename.exists():
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def _save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, deadline = None):
        task = {
            "task_name" : description,
            "is_done" : False,
            "created" : datetime.now().isoformat(),
            "dateline" : deadline
        }
        if any(t["task_name"] == task["task_name"] for t in self.tasks):
            print("this task is arleady in list")
        else:
            self.tasks.append(task)
            self._save_tasks()

    def list_tasks(self):
        for i in range(len(self.tasks)):
            print(self.tasks[i])
