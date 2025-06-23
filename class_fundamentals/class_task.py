"""
You're creating a task management system. Create a Task class that tracks completion 
status, due dates, and provides task summary reports.

Your task: Create a Task class for project management
Test with:
task = Task("Complete report", "2024-06-30", "high")
print(task.is_overdue("2024-07-01"))  # Should print True
task.mark_complete()
print(task.get_status())  # Should show completed status
"""

class Task:
    def __init__(self, name, due_date, priority, status = "Pending"):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = status
    
    def get_status(self):
        return self.status

    def mark_complete(self):
        self.status = "Completed"
    
    def is_overdue(self, current_date):
        return current_date > self.due_date

task = Task("Complete report", "2024-06-30", "high")
print(task.is_overdue("2024-07-01"))  # Should print True
task.mark_complete()
print(task.get_status())  # Should show completed status