import json
import os

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load()
        
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename) as file:
                self.tasks = json.load(file)
    
    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add(self, task):
        self.tasks.append(task)
        self.save()
        print("Task added successfully.")
        
    def show(self):
        print("Your tasks:")
        for number, task in enumerate(self.tasks, start=1):
            print(f"{number}. {task}") 
            
    def delete(self, number):
        if 1 <= number <= len(self.tasks):
             self.tasks.pop(number - 1)
             self.save()
             print("Task deleted successfully.")
        else:
             print("Invalid task number.")
             

todo = TodoList("tasks.json")

while True:
    choice = input("=============\n1. Add task\n2. Show tasks\n3. Delete task\n4. Quit\nChoose your choice: ")
    
    if choice == "1" :
        new_task = input("Enter a new task: ")
        todo.add(new_task)
    elif choice == "2" :
        todo.show()
    elif choice == "3" :
        todo.show()
        try:
            delete_number = int(input("Enter the number of the task you want to delete: "))
            todo.delete(delete_number)
        except ValueError:
            print("Please enter a valid task number.")
    elif choice == "4" :
        break
    else:
        print("Please enter a valid choice.")
        
        