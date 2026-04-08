#handle running the application
import ui_items as ui
from core import todos

#adding todo_system as my_app
my_app = todos.Todo_System()

def run_app():
    while True:
        ui.clear_screen()
        ui.show_menu()

        #taking menu choice
        try:
            menu_choice = int(input("Enter your choice: ")) 

            #handling menu choice

            #exit from application
            if menu_choice == 0:
                ui.green()
                print("Exiting the program. Goodbye!")
                ui.reset()
                break

            if menu_choice == 1:
                ui.clear_screen()
                ui.cyan()
                ui.show_options_banner("1️⃣  ➕ Add a todo")
                #taking new todo from user
                ui.green()
                new_todo = input("Enter the new todo: ")
                success = my_app.add_a_todo(new_todo)
                if success:
                    ui.green()
                    print("Your todo added successfully!")
                ui.pause_menu()

            elif menu_choice == 2:
                ui.clear_screen()
                ui.cyan()
                ui.show_options_banner("2️⃣  📋 View todos")
                my_app.view_all_todos()
                ui.pause_menu()

            elif menu_choice == 3:
                ui.clear_screen()
                ui.cyan()
                ui.show_options_banner("3️⃣  ✅ Update a todo")
                ui.green()
                my_app.update_a_todo()
                ui.pause_menu()

            elif menu_choice == 4:
                ui.clear_screen()
                ui.cyan()
                ui.show_options_banner("4️⃣  ❌ Delete a todo")
                my_app.delete_a_todo()
                ui.pause_menu()


        except ValueError:
            ui.red()
            print("Invalid input. Please enter a valid number.")
            ui.reset()
            ui.pause_menu()

        except KeyboardInterrupt:
            ui.green()
            print("\nExiting the application. Goodbye!")
            ui.reset()
            break

if __name__ == "__main__":
    run_app()