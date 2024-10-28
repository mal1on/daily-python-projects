'''Console-based task manager app where users can add, complete,
 and view tasks'''


class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False
    def mark_completed(self):
        self.is_completed = True


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        description = input("Enter the task description: ")
        self.tasks.append(Task(description))

    def complete_task(self):
        # self.view_tasks()
        task = int(input('Enter the task number to mark as completed: '))
        while task not in range(len(self.tasks) - 1):
            print('Please enter existing task number')
            # self.view_tasks()
            task = int(input('Enter the task number to mark as completed: '))
        self.tasks[task].mark_completed()



test = ToDoList()
test.add_task()
test.complete_task
