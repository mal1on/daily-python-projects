class Task:
    '''
    Console-based task manager app where users can add, complete,
    and view tasks
    '''

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
        print(f'Task "{description}" added to the To-Do list.\n')

    def complete_task(self):

        self.view_tasks()
        task = None

        while True:
            try:
                task = int(
                    input('Enter the task number to mark as completed: '))
                if task in range(1, len(self.tasks) + 1):
                    break
                else:
                    print('Please enter valid task number')
            except ValueError:
                print('Please enter valid task number')

        self.tasks[task - 1].mark_completed()
        print(
            f'Task {self.tasks[task - 1].description} marked as completed.\n')

    def view_tasks(self):

        print('To-Do List:')
        for n, task in enumerate(self.tasks):
            if task.is_completed:
                print(f'{n + 1}. {task.description} [✔]')
            else:
                print(f'{n + 1}. {task.description} [❌]')
        print('\n')

    def run(self):

        print('1. Add Task\n2. Complete Task\n3. View Tasks\n4. Exit')
        choice = None

        while True:
            try:
                choice = int(input('Enter choice: '))
                if choice in range(1, 5):
                    break
                else:
                    print('Please enter valid choice')
            except ValueError:
                print('Please enter valid choice')

        match choice:
            case 1:
                self.add_task()
                self.run()
            case 2:
                self.complete_task()
                self.run()
            case 3:
                self.view_tasks()
                self.run()
            case 4:
                return


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
