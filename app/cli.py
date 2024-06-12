#!/usr/bin/env python3

import getpass
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import csv
from colorama import Fore
from rich.console import Console
from rich.table import Table
from db import initialize_db
from user import User
from student import Student
from inventory import Inventory


console = Console()


# Select student photo
def select_student_photo():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    file_path = filedialog.askopenfilename()  # Open file dialog window
    
    return file_path
# enroll students
def enroll_new_student():
    name = input(Fore.YELLOW + "Enter student name: ")
    age = int(input(Fore.YELLOW + "Enter student age: "))
    parent_name = input(Fore.YELLOW + "Enter parent name: ")
    level = input(Fore.YELLOW + "Enter student level: ")
    phone_number = input(Fore.LIGHTMAGENTA_EX + "Enter parent's phone number: ")

    student = Student(name, age, parent_name, level, phone_number)

     # Select student photo
    console.print(Fore.YELLOW + "Please select student photo...")
    student_photo_path = select_student_photo()
    
    # Ensure a photo is selected
    if not student_photo_path:
        console.print(Fore.RED + "No photo selected. Student enrollment aborted.")
        return

    # Save student photo with an incrementing integer as filename
    photos_directory = 'photos'
    os.makedirs(photos_directory, exist_ok=True)

    # Find the next available filename by iterating over existing files
    next_filename = 1
    while os.path.exists(os.path.join(photos_directory, f"{next_filename}.jpg")):
        next_filename += 1

    new_photo_path = os.path.join(photos_directory, f"{next_filename}.jpg")
    shutil.copy(student_photo_path, new_photo_path)

    # Update student object with photo path
    student.photo_path = new_photo_path


    student.save_to_db()
    console.print(Fore.GREEN + "Student enrolled successfully!")
  

# Student search functionality
def display_student_details(student_id):
    # Retrieve student details from the database based on student_id
    student = Student.get_by_id(student_id)
    
    if student:
        # Display student details
        console.print(f"Student ID: {student.id}")
        console.print(f"Name: {student.name}")
        console.print(f"Level: {student.level}")
        
        # Display student photo
        if student.photo_path:
            console.print(Fore.YELLOW + "Displaying student photo...")
            os.system(f"xdg-open {student.photo_path}")  # Open photo using default image viewer
        else:
            console.print(Fore.RED + "No photo available for this student.")
    else:
        console.print(Fore.RED + f"No student found with ID '{student_id}'")

def search_student_by_id():
    id = input(Fore.YELLOW + "Enter student ID: ")
    students = Student.get_by_id(id)

    if not students:
        print(Fore.RED + f"No students found at level '{id}'")
    else:
        table = Table(show_header=True, header_style="bold green")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name")
        table.add_column("Age")
        table.add_column("Parent Name")
        table.add_column("Level")
        table.add_column("Phone Number")

        for student in students:
            table.add_row(str(student[0]), student[1], str(student[2]), student[3], student[4], student[5])

        console.print(table)

def search_student_by_level():
    level = input(Fore.YELLOW + "Enter student level: ")
    students = Student.get_by_level(level)
    
    if not students:
        console.print(Fore.RED + f"No students found at level '{level}'")
    else:
        table = Table(show_header=True, header_style="bold green")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name")
        table.add_column("Age")
        table.add_column("Parent Name")
        table.add_column("Level")
        table.add_column("Phone Number")

        for student in students:
            table.add_row(str(student[0]), student[1], str(student[2]), student[3], student[4], student[5])

        console.print(table)

# delete students
def delete_student():
    student_id = int(input(Fore.YELLOW + "Enter student ID to delete: "))
    Student.delete_student(student_id)
    console.print(Fore.GREEN + "Student deleted successfully!")

# show student tables
def display_students_table():
    students = Student.get_all_students()
    if not students:
        print(Fore.RED + "No students found.")
    else:
        print("")
        print("")
        print(Fore.LIGHTGREEN_EX + "Student Records")
        print("")
        table = Table(show_header=True, header_style="bold green", show_lines=False, style="magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", style="magenta")
        table.add_column("Age", style="magenta")
        table.add_column("Parent Name", style=" magenta")
        table.add_column("Level", style="magenta")
        table.add_column("Phone Number", style="magenta")

        for student in students:
            table.add_row(str(student[0]), student[1], str(student[2]), student[3], student[4], student[5])

        console.print(table)

# Download students data
def export_students_to_csv():
    students = Student.get_all_students()
    if not students:
        console.print(Fore.RED + "No students found.")
        return

    filename = "students.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing headers
        writer.writerow(["ID", "Name", "Age", "Parent Name", "Level", "Phone Number"])
        # Writing student data
        writer.writerows(students)

    console.print(Fore.GREEN + f"Student data has been exported to {filename}")


# inventory
def add_inventory_item():
    item_name = input(Fore.YELLOW + "Enter item name: ")
    quantity = int(input(Fore.YELLOW + "Enter quantity: "))

    item = Inventory(item_name, quantity)
    item.save_to_db()
    console.print(Fore.GREEN + "Item added successfully!")

def delete_inventory_item():
    item_id = int(input(Fore.YELLOW + "Enter item ID to delete: "))
    Inventory.delete_item(item_id)
    console.print(Fore.GREEN + "Item deleted successfully!")

def display_inventory():
    items = Inventory.get_all_items()
    table = Table(title="Inventory")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Item Name", style="magenta")
    table.add_column("Quantity", style="green")

    for item in items:
        table.add_row(str(item[0]), item[1], str(item[2]))

    console.print(table)

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
                print("1. Students")
                print("2. Grades")
                print("3. School Fees")
                print("4. Budget")
                print("5. Inventory")
                print("6. Summary")
                print("7. Logout")
                print("")
                choice = input(Fore.LIGHTGREEN_EX + "Choose an option: ")
                if choice == '1':
                    print("Managing Students")
                    print("")
                    while True:
                        print("e :Enroll New Student")
                        print("d :Deregister Student")
                        print("s :Show Student Data")
                        print("g :Get csv data")
                        print("f :find")
                        print("b :Back")
                        choice = input(Fore.LIGHTGREEN_EX + "Choose action:")
                        if choice == 'e':
                           enroll_new_student()
                        elif choice == 'd':
                            delete_student()
                        elif choice == 's':
                            display_students_table()
                        elif choice == 'f':
                            print("1 :Search by ID")
                            print("2 :Search by Level")
                            print("3 :Back")
                            search_choice = input(Fore.LIGHTGREEN_EX + "Choose search option: ")
                            if search_choice == '1':
                                search_student_by_id()
                            elif search_choice == '2':
                                search_student_by_level()
                            elif choice == '3':
                                break
                            else:
                                console.print(Fore.RED + "Invalid choice, please try again.")
                            
                        elif choice == 'g':
                            export_students_to_csv()
            
                        elif choice == 'b':
                            break
                    
                elif choice == '2':
                    print(Fore.LIGHTGREEN_EX  + "Deregistering student...")
                    delete_student()
                elif choice == '3':
                    print(Fore.LIGHTGREEN_EX  + "School Fees...")
                elif choice == '4':
                    print(Fore.LIGHTGREEN_EX  + "Budget")
                elif choice == '5':
                    print(Fore.LIGHTGREEN_EX  + "Inventory")
                    print("")                
                    while True:
                        print("a :Add Item")
                        print("d :Delete Item")
                        print("s :Show Table")
                        print("b :Back")

                        choice = input("Choose an action:")
                        if choice == 'a':
                            add_inventory_item()
                        elif choice == 'd':
                            delete_inventory_item()
                        elif choice == 's':
                            display_inventory()
                        elif choice == 'b':
                            break
                        else:
                            console.print(Fore.RED + "Invalid choice, please try again.")
                            
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
