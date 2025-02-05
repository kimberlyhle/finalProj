# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:24:00 2025

@author: kimbe
"""

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_id = 1

    def add_task(self, task):
        self.tasks[self.task_id] = {'task': task, 'completed': False}
        print(f"Task added with ID: {self.task_id}")
        self.task_id += 1

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_id, task_info in self.tasks.items():
                status = "Completed" if task_info['completed'] else "Pending"
                print(f"{task_id}: {task_info['task']} - {status}")

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f"Task {task_id} marked as completed.")
        else:
            print("Invalid Task ID.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted.")
        else:
            print("Invalid Task ID.")


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter Task ID to mark as completed: "))
            todo_list.mark_completed(task_id)
        elif choice == "4":
            task_id = int(input("Enter Task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
