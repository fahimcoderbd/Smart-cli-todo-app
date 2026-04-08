#handle app ui components

import os

#app.py ui components
app_info = {
    "app_name": "Smart Todo app",
    "app_version": 1.0,
    "app_dev": "Fahim Abrar"
}

#color functions
def green(): print("\033[92m", end="")
def cyan(): print("\033[96m", end="")
def white(): print("\033[97m", end="")
def red(): print("\033[91m", end="")
def reset(): print("\033[0m", end="")

#banners
#app banner
def show_banner():
    green()  # Set text color to green
    print("=" * 50)
    print(app_info['app_name'].center(50))   # Center app name
    print(f"Version {app_info['app_version']}".center(50))  # Center version
    print(f"Developed by {app_info['app_dev']}".center(50))  # Center developer name
    print("=" * 50)
    reset()  # Reset color

#options banner
def show_options_banner(option_name):
     print("=="*20)
     print(f"{option_name}.....")
     print("=="*20)

#app menu
def show_menu():
    show_banner()
    cyan()
    print("==" * 20)
    print("1️⃣  ➕ Add a todo")
    print("2️⃣  📋 View Todos")
    print("3️⃣  ✅ update a Todo")
    print("4️⃣  ❌ Delete a Todo")
    print("0️⃣  🚪 Exit")
    print("==" * 20)

#pause mechanism
def pause_menu():
    reset()
    input("\nPress Enter to continue...")

#clear console
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")




