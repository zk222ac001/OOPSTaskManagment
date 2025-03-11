class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.assigned_to = None
        self.completed = False

    def assign_to(self, user):
        self.assigned_to = user

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        assigned = f"Assigned to: {self.assigned_to}" if self.assigned_to else "Unassigned"
        return f"Task: {self.title}\nDescription: {self.description}\nStatus: {status}\n{assigned}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def assign_task(self, task, user):
        if user in self.users:
            task.assign_to(user)
        else:
            print(f"User {user} not found.")

    def complete_task(self, task):
        task.mark_completed()

    def display_tasks(self):
        for task in self.tasks:
            print(task)
            print("-" * 40)

# Example Usage
if __name__ == "__main__":
    # Create a TaskManager instance
    manager = TaskManager()

    # Create users
    user1 = User("Alice")
    user2 = User("Bob")
    manager.add_user(user1)
    manager.add_user(user2)

    # Create tasks
    task1 = manager.create_task("Implement Login", "Implement user login functionality.")
    task2 = manager.create_task("Design Dashboard", "Design the user dashboard UI.")

    # Assign tasks to users
    manager.assign_task(task1, user1)
    manager.assign_task(task2, user2)

    # Mark a task as completed
    manager.complete_task(task1)

    # Display all tasks
    manager.display_tasks()
