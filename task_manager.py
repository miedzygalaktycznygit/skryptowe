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
            "deadline" : deadline
        }
        if any(t["task_name"] == task["task_name"] for t in self.tasks):
            print("this task is arleady in list")
        else:
            self.tasks.append(task)
            self._save_tasks()

    def list_tasks(self):
        for i in range(len(self.tasks)):
            print(self.tasks[i])

    def get_tasks_due_today(self):
        time = date.today()
        for task in self.tasks:
            if task["deadline"]:
                try:
                    deadline_date = datetime.fromisoformat(task["deadline"]).date()
                    if deadline_date == time:
                        print("Those are Your tasks for today:\n")
                        print(task)
                except ValueError:
                    print("Valid usage of module")

    def delete_task(self, index):
        removed = self.tasks.pop(index)
        self._save_tasks()
        print("You deleted this task: ")
        print(removed)
        print("List after removal:")
        self.list_tasks()

    def mark_done(self, index):
        self.tasks[index]["is_done"] = True
    
            
    
