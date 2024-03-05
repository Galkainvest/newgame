# Python code for a simple to-do list application

class ToDoList:
    def __init__(self):
        # Initialize the to-do list from a file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # Load tasks from a file
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
            return [task.strip() for task in tasks]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        # Save tasks to a file
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        # Add a new task to the list
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_number):
        # Delete a task from the list
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
            self.save_tasks()
            return True
        return False

    def modify_task(self, task_number, new_task):
        # Modify an existing task
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number] = new_task
            self.save_tasks()
            return True
        return False

    def display_tasks(self):
        # Display the list of tasks
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

def main():
    # Main function to run the to-do list application
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        todo_list.display_tasks()
        print("\nOptions: add <task>, del <task number>, mod <task number> <new task>, exit")
        command = input("Enter command: ").split()

        if command[0] == "add":
            todo_list.add_task(" ".join(command[1:]))

        elif command[0] == "del":
            if todo_list.delete_task(int(command[1])):
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif command[0] == "mod":
            if todo_list.modify_task(int(command[1]), " ".join(command[2:])):
                print("Task modified.")
            else:
                print("Invalid task number.")

        elif command[0] == "exit":
            break

        else:
            print("Invalid command.")

# Uncomment this to run the program
# main()
