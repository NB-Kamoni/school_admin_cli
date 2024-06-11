import getpass
from colorama import Fore
from rich.console import Console
from db import initialize_db
from user import User

console = Console()

def main():
    initialize_db()
    attempts = 0

    while attempts < 3:
        console.print("\n" * 3)
        console.print("KAMONI-SCHOOL ADMIN CLI", justify="center", style="bold green underline")
        print(Fore.LIGHTMAGENTA_EX + "An admin tool for managing student enrollment, schoolfees, exams, teacher allocation and inventory.")
        print("")
        print("Please try again" if attempts > 0 else "Please Login")
        username = input(Fore.LIGHTGREEN_EX + "Username: ")
        password = getpass.getpass(Fore.LIGHTGREEN_EX + "Password: ")

        if User.authenticate(username, password):
            print(Fore.LIGHTGREEN_EX + "Successfully logged in")
            while True:
                print(Fore.LIGHTMAGENTA_EX + "\nMenu:")
                print("1. Enroll New Students")
                print("2. Deregister Student")
                print("3. School Fees")
                print("4. Budget")
                print("5. Inventory")
                print("6. Summary")
                print("7. Logout")
                print("")
                choice = input(Fore.LIGHTGREEN_EX + "Choose an option: ")
                if choice == '1':
                    print(Fore.LIGHTGREEN_EX + "Enrolling new students...")
                    # Implement enrollment functionality here
                elif choice == '2':
                    print(Fore.LIGHTGREEN_EX  + "Deregistering student...")
                elif choice == '3':
                    print(Fore.LIGHTGREEN_EX  + "School Fees...")
                elif choice == '4':
                    print(Fore.LIGHTGREEN_EX  + "Budget")
                elif choice == '2':
                    print(Fore.LIGHTGREEN_EX  + "Inventory")
                elif choice == '6':
                    print(Fore.LIGHTGREEN_EX  + "Generating summary...")
                    # Implement summary functionality here
                elif choice == '7':
                    print(Fore.GREEN + "Goodbye!")
                    break
                else:
                    print(Fore.RED + "Invalid choice, please try again.")
            break
        else:
            attempts += 1
            if attempts == 3:
                print(Fore.RED + "Blocked")
            else:
                print(Fore.RED + "Wrong username or password")

if __name__ == "__main__":
    main()
