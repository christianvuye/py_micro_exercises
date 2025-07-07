"""
Create a TaskManager class that tracks tasks across all instances and per instance.

Requirements:
- Class variable all_tasks = [] to track every task created by any instance
- Class variable total_task_count = 0 to count total tasks across all instances
- Instance variable my_tasks = [] to track tasks for this specific instance
- Instance variable instance_id to uniquely identify each instance

Create methods:
- add_task(task_name) that adds to both all_tasks and my_tasks
- get_my_task_count() that returns number of tasks for this instance
- get_global_task_count() that returns total tasks across all instances
- get_all_tasks() that returns the shared list of all tasks

Test your class:
manager1 = TaskManager("Manager1")
manager2 = TaskManager("Manager2")

manager1.add_task("Write code")
manager2.add_task("Review code")
manager1.add_task("Test code")

print(f"Manager1 tasks: {manager1.get_my_task_count()}")  # Should print 2
print(f"Manager2 tasks: {manager2.get_my_task_count()}")  # Should print 1  
print(f"Global tasks: {manager1.get_global_task_count()}")  # Should print 3
print(f"All tasks: {manager1.get_all_tasks()}")  # Should show all 3 tasks

# Here's where it gets interesting...
print(f"Manager2 all tasks: {manager2.get_all_tasks()}")  # What will this show?
"""

class TaskManager:
    all_tasks = []
    #total_task_count = 0 # is this needed, can't we just do len(all_tasks), another tracker could desync the two vars

    def __init__(self, instance_id): # avoid the list as argument: mutable default arguments cause the same list object to be shared
        self.my_tasks = []
        self.instance_id = instance_id

    def add_task(self, task_name):
        self.my_tasks.append(task_name)
        TaskManager.all_tasks.append(task_name)
        # TaskManager.total_task_count += 1 avoid, not needed
    
    def get_my_task_count(self):
        return len(self.my_tasks)
    
    def get_global_task_count(self):
        return len(TaskManager.all_tasks)
    
    def get_all_tasks(self):
        return TaskManager.all_tasks
    
manager1 = TaskManager("Manager1")
manager2 = TaskManager("Manager2")

manager1.add_task("Write code")
manager2.add_task("Review code")
manager1.add_task("Test code")

print(f"Manager1 tasks: {manager1.get_my_task_count()}")  # Should print 2
print(f"Manager2 tasks: {manager2.get_my_task_count()}")  # Should print 1  
print(f"Global tasks: {manager1.get_global_task_count()}")  # Should print 3
print(f"All tasks: {manager1.get_all_tasks()}")  # Should show all 3 tasks

# Here's where it gets interesting...
print(f"Manager2 all tasks: {manager2.get_all_tasks()}")  # What will this show?