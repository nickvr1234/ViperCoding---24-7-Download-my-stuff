import os
import sys
import time

def clear():
    os.system("cls")

def pause():
    input("\nPress Enter to continue...")

def open_cmd():
    os.system("start cmd")

def open_taskmgr():
    os.system("start taskmgr")

def open_notepad():
    os.system("start notepad")

def open_calc():
    os.system("start calc")

def open_explorer():
    os.system("start explorer")

def system_tools_menu():
    while True:
        clear()
        print("=== SYSTEM TOOLS ===")
        print("1) Open CMD")
        print("2) Open Task Manager")
        print("3) Open File Explorer")
        print("4) Back to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            open_cmd()
        elif choice == "2":
            open_taskmgr()
        elif choice == "3":
            open_explorer()
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
            time.sleep(1)

def utility_tools_menu():
    while True:
        clear()
        print("=== UTILITY TOOLS ===")
        print("1) Open Notepad")
        print("2) Open Calculator")
        print("3) Back to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            open_notepad()
        elif choice == "2":
            open_calc()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")
            time.sleep(1)

def main_menu():
    while True:
        clear()
        print("=== MINI TOOL LAUNCHER ===")
        print("1) System Tools")
        print("2) Utility Tools")
        print("3) Shortcuts")
        print("4) Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            system_tools_menu()
        elif choice == "2":
            utility_tools_menu()
        elif choice == "3":
            shortcuts_menu()
        elif choice == "4":
            print("Closing launcher...")
            time.sleep(0.5)
            sys.exit()
        else:
            print("Invalid choice.")
            time.sleep(1)

def shortcuts_menu():
    while True:
        clear()
        print("=== SHORTCUTS ===")
        print("Type these anytime in the main menu:")
        print("cmd  - Open Command Prompt")
        print("tm   - Open Task Manager")
        print("np   - Open Notepad")
        print("calc - Open Calculator")
        print("back - Return to Main Menu")

        cmd = input("\nShortcut: ").strip().lower()

        if cmd == "cmd":
            open_cmd()
        elif cmd == "tm":
            open_taskmgr()
        elif cmd == "np":
            open_notepad()
        elif cmd == "calc":
            open_calc()
        elif cmd == "back":
            return
        else:
            print("Unknown shortcut.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
