"""
Create a TaskTracker class with these features:

1. Initialize with an empty list of tasks
2. Add a task (string) to the list
3. Mark a task as completed (remove it from the list)
4. Get the count of remaining tasks
5. Display all current tasks

Example usage:
tracker = TaskTracker()
tracker.add_task("Write documentation")
tracker.add_task("Review code")
print(tracker.task_count())  # Should print: 2
tracker.complete_task("Write documentation")
print(tracker.show_tasks())  # Should show remaining tasks
"""

class TaskTracker:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def complete_task(self, task):
        self.tasks.remove(task)
    
    def task_count(self):
        return len(self.tasks)

    def show_tasks(self):
        return self.tasks