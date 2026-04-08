# Handle app business logic

from core import storage
from core import validators
from core import services
import ui_items as ui


class Todo_System:

    def __init__(self):
        """
        Initialize the Todo System."""
        self.todos = storage.load_from_json()

    def add_a_todo(self, todo_data):
        # Generate unique todo ID
        # Find max existing ID and increment
        todo_id = 1 if not self.todos else max(todo['id'] for todo in self.todos) + 1

        # Create new todo object
        new_todo = {
            "id": todo_id,
            "todo": todo_data,
            "completed": False,
            "status": "pending"
        }

        # Add todo to list
        self.todos.append(new_todo)
        # Persist data to JSON storage
        storage.save_in_json(self.todos)
        return True

    def view_all_todos(self):
        """
        Display all todos and optionally mark one as completed.
        """

        # Validate if todos exist
        validators.validate_todos_existence(self.todos)

        # Loop through todos and display them
        for index, todo in enumerate(self.todos):
            ui.green()
            print("Your todo:")

            ui.white()
            print(f"Todo ID: {todo['id']}, Task: {todo['todo']}")

            # Show status based on completion
            if not todo['completed']:
                print(f"Status: {todo['status']}")
            else:
                # Update status if completed
                todo['status'] = "completed"
                storage.save_in_json(self.todos)
                print(f"Status: {todo['status']}")

        # Ask user if they want to complete a todo
        ui.green()
        ask_user = input("Do you want to complete a todo? (y/n): ").strip().lower()

        if ask_user == "y":
            try:
                todo_id = validators.validate_int_input(input("Enter Todo ID: "))

                # Find and update the selected todo
                for todo in self.todos:
                    if todo_id == todo['id']:
                        todo['completed'] = True

                        # Save updated data
                        storage.save_in_json(self.todos)

                        ui.green()
                        print("Todo completed successfully!")
                        return

                # If ID not found
                print("Invalid Todo ID!")

            except ValueError:
                print("Please enter a valid number!")

        else:
            print("Thanks for using the app!")

    def update_a_todo(self):
        """
        #show all todos using services show_todos()
        #take todo id then match with the todo['id'], if not matched the return error
        #take updated todo from user
        #update todo['todo'] = todo in todos (dictionary)
        #save in json (todos)
        #show success message to user
        """
        todos = services.show_todos(self.todos)
        ui.green()
        todo_id = validators.validate_int_input(input("Enter todo id: "))

        if todo_id is None:
            return

        todo_found = False
        for todo in todos:
            if todo_id == todo['id']:
                new_todo = input("Enter new todo: ")
                #updating todo
                todo['todo'] = new_todo
                #saving todo in json
                storage.save_in_json(self.todos)
                #showing success message
                ui.green()
                print("Your todo updated successfully!")
                todo_found = True
                break
        
        if not todo_found:
            ui.red()
            print("Sorry, We got and error, Please try again.")     

    def delete_a_todo(self):
        todos = services.show_todos(self.todos)
        ui.green()
        todo_id = validators.validate_int_input(input("Enter todo id: "))

        if todo_id is None:
            return

        todo_found = False

        for i, todo in enumerate(todos):
          if todo_id == todo['id']:
          # deleting from list (correct way)
           del todos[i]

          # saving updated list
          storage.save_in_json(todos)

          ui.green()
          print("Your todo deleted successfully!")

          todo_found = True
          break

        if not todo_found:
          ui.red()
          print("Sorry, We got an error, Please try again.")