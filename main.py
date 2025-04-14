from task_manager import TaskManager

manager = TaskManager()

manager.add_task("coś nowego", deadline="2025-04-14")

manager.mark_done(0)

manager.list_tasks()

manager.get_tasks_due_today()

#manager.delete_task(0)
