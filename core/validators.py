#handle app input validation and error handling
import ui_items as ui

#todos exist validator

def validate_todos_existence(todos):
    if not todos:
       ui.red() #red color for error
       print("Todos not exists! create a new sir.")
       ui.pause_menu()

def validate_int_input(user_input):
    try:
        return int(user_input)
    except ValueError:
        ui.red()
        print("Invalid input. Please enter a valid number.")
        ui.pause_menu()
        return None