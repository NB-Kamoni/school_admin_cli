import getpass
from colorama import init, Fore, Style
from db import initialize_db
from user import User

init(autoreset=True)

def main():
    initialize_db()

    # Adding a test user directly for debugging purposes
    test_user = User(username="testuser", password="testpassword")
    test_user.save_to_db()

    while True:
        print(Fore.YELLOW + "Login:")
        username = input(Fore.YELLOW + "Username: ")
        password = getpass.getpass(Fore.YELLOW + "Password: ")

        if User.authenticate(username, password):
            print(Fore.GREEN + "Successfully logged in")
            while True:
                print(Fore.YELLOW + "\nMenu:")
                print("1. Enroll New Students")
                print("2. Logout")
                choice = input(Fore.YELLOW + "Choose an option: ")
                if choice == '1':
                    print(Fore.YELLOW + "Enrolling new students...")
                    # Implement enrollment functionality here
                elif choice == '2':
                    print(Fore.GREEN + "Goodbye!")
                    break
                else:
                    print(Fore.RED + "Invalid choice, please try again.")
            break
        else:
            print(Fore.RED + "Wrong username or password")

if __name__ == "__main__":
    main()
