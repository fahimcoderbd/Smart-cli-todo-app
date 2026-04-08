from core import storage
from core import validators
import ui_items as ui

#show all todos service
def show_todos(todos):
     # Validate if todos exist
     validators.validate_todos_existence(todos)
     #viewing all todos
      # Loop through todos and display them
     for todo in todos:
          ui.green()
          print("Your todo:")
          ui.white()
          print(f"Todo ID: {todo['id']}, Task: {todo['todo']}")

     return todos