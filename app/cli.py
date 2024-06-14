#!/usr/bin/env python3

import getpass
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import subprocess
import csv
import webbrowser
from colorama import Fore
from rich.console import Console
from rich.table import Table
from db import initialize_db
from user import User
from student import Student
from inventory import Inventory
from teacher import Teacher


console = Console()

################################students############
# Select student photo
def select_student_photo():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    file_path = filedialog.askopenfilename()  # Open file dialog window
    
    return file_path
# enroll students
def enroll_new_student():
    name = input(Fore.LIGHTGREEN_EX + "Enter student name: ")
    age = int(input(Fore.LIGHTGREEN_EX + "Enter student age: "))
    parent_name = input(Fore.LIGHTGREEN_EX + "Enter parent name: ")
    level = input(Fore.LIGHTGREEN_EX + "Enter student level: ")
    phone_number = input(Fore.LIGHTGREEN_EX + "Enter parent's phone number: ")

    student = Student(name, age, parent_name, level, phone_number)

     # Select student photo
    print(Fore.LIGHTGREEN_EX + "Please select student photo...")
    student_photo_path = select_student_photo()
    
    # Ensure a photo is selected
    if not student_photo_path:
        print(Fore.RED + "No photo selected. Student enrollment aborted.")
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
    print("")
    print(Fore.LIGHTGREEN_EX + "Student enrolled successfully!")
    print("")

#Student search functionality

def search_student_by_id():
    print("")
    id = input(Fore.LIGHTGREEN_EX + "Enter student ID: ")
    students = Student.get_by_id(id)

    if not students:
        print(Fore.RED + f"No students found at level '{id}'")
    else:
        table = Table(show_header=True, header_style="bold green", show_lines=False, style="magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", style="bold magenta")
        table.add_column("Age", style="magenta")
        table.add_column("Parent Name", style=" magenta")
        table.add_column("Level", style=" bold magenta")
        table.add_column("Phone Number", style="magenta")

        for student in students:
            table.add_row(str(student[0]), student[1], str(student[2]), student[3], student[4], student[5])

            

        console.print(table)

         # Display the student's image
        image_path = f"./photos/{id}.jpg"
    if os.path.exists(image_path):
        print("\033[92m" + f"Opening image for student ID '{id}':")
        webbrowser.open(image_path)

         # Define the desired dimensions for resizing
        width = 800
        height = 600
    
           # Command to display the resized image with specific window geometry
        command = ["display", "-resize", f"{width}x{height}", "-geometry", f"{width}x{height}+100+40", image_path]
    
          # Open the image using subprocess
        subprocess.Popen(command)
    
            
    else:
         print("\033[91m" + f"Image not found for student ID '{id}'")






def search_student_by_level():
    level = input(Fore.LIGHTGREEN_EX + "Enter student level: ")
    students = Student.get_by_level(level)
    
    if not students:
        console.print(Fore.RED + f"No students found at level '{level}'")
    else:
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

################################STUDENTS END#######
################################TEACHERS START#####
# Select teacher photo
def select_teacher_photo():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    file_path = filedialog.askopenfilename()  # Open file dialog window
    
    return file_path
# enroll teacher
def enroll_new_teacher():
    name = input(Fore.LIGHTGREEN_EX + "Enter teacher name: ")
    age = int(input(Fore.LIGHTGREEN_EX + "Enter teacher age: "))
    subject = input(Fore.LIGHTGREEN_EX + "Enter teacher subject: ")
    phone_number = input(Fore.LIGHTGREEN_EX + "Enter teacher's phone number: ")

    teacher = Teacher(name, age, subject, phone_number)

     # Select teacher photo
    print("")
    print(Fore.YELLOW + "Please select teacher photo...")
    teacher_photo_path = select_teacher_photo()
    
    # Ensure a photo is selected
    if not teacher_photo_path:
        print(Fore.RED + "No photo selected. Teacher onboarding aborted.")
        return

    # Save teacher photo with an incrementing integer as filename
    photos_directory = 'teacher_photos'
    os.makedirs(photos_directory, exist_ok=True)

    # Find the next available filename by iterating over existing files
    next_filename = 1
    while os.path.exists(os.path.join(photos_directory, f"{next_filename}.jpg")):
        next_filename += 1

    new_photo_path = os.path.join(photos_directory, f"{next_filename}.jpg")
    shutil.copy(teacher_photo_path, new_photo_path)

    # Update teacher object with photo path
    teacher.photo_path = new_photo_path


    teacher.save_to_db()
    print("")
    print(Fore.LIGHTMAGENTA_EX + "Teacher Onboarded successfully!")
    print("")

#Teacher search functionality

def search_teacher_by_id():
    print("")
    id = input(Fore.LIGHTGREEN_EX + "Enter teacher ID: ")
    teachers = Teacher.get_teachers_by_id(id)

    if not teachers:
        print(Fore.RED + f"No teacher found")
    else:
        table = Table(show_header=True, header_style="bold green", show_lines=False, style="magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", style="bold magenta")
        table.add_column("Age", style="magenta")
        table.add_column("Subject", style=" bold magenta")
        table.add_column("Phone Number", style="magenta")

        for teacher in teachers:
            table.add_row(str(teacher[0]), teacher[1], str(teacher[2]), teacher[3], teacher[4])

            

        console.print(table)

         # Display the teacher's image
        image_path = f"/home/bennie/Development/phase3/school_admin_cli/teacher_photos/{id}.jpg"
    if os.path.exists(image_path):
        print("\033[92m" + f"Opening image for teacher ID '{id}':")
        webbrowser.open(image_path)

         # Define the desired dimensions for resizing
        width = 800
        height = 600
    
           # Command to display the resized image with specific window geometry
        command = ["display", "-resize", f"{width}x{height}", "-geometry", f"{width}x{height}+100+40", image_path]
    
          # Open the image using subprocess
        subprocess.Popen(command)
    
            
    else:
         print("\033[91m" + f"Image not found for teacher ID '{id}'")






def search_teacher_by_subject():
    subject = input(Fore.LIGHTGREEN_EX + "Enter teacher subject: ")
    teachers = Teacher.get_teachers_by_subject(subject)
    
    if not teachers:
        console.print(Fore.RED + f"No teachers found for subject '{subject}'")
    else:
        table = Table(show_header=True, header_style="bold green", show_lines=False, style="magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", style="magenta")
        table.add_column("Age", style="magenta")
        table.add_column("Subject", style="magenta")
        table.add_column("Phone Number", style="magenta")

        for teacher in teachers:
            table.add_row(str(teacher[0]), teacher[1], str(teacher[2]), teacher[3], teacher[5])

        console.print(table)

# delete students
def delete_teacher():
    student_id = int(input(Fore.LIGHTGREEN_EX + "Enter teacher ID to delete: "))
    Teacher.delete_teacher(student_id)
    print(Fore.LIGHTGREEN_EX + "Teacher deleted successfully!")

# show student tables
def display_teachers_table():
    teachers = Teacher.get_all_teachers()
    if not teachers:
        print(Fore.RED + "No teachers found.")
    else:
        print("")
        print("")
        print(Fore.LIGHTGREEN_EX + "Teacher Records")
        print("")
        table = Table(show_header=True, header_style="bold green", show_lines=False, style="magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", style="magenta")
        table.add_column("Age", style="magenta")
        table.add_column("Subject", style="magenta")
        table.add_column("Phone Number", style="magenta")

        for teacher in teachers:
            table.add_row(str(teacher[0]), teacher[1], str(teacher[2]), teacher[3], teacher[4])

        console.print(table)

# Download students data
def export_teachers_to_csv():
    teachers = Teacher.get_all_teacher()
    if not teachers:
        console.print(Fore.RED + "No teachers found.")
        return

    filename = "teachers.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing headers
        writer.writerow(["ID", "Name", "Age", "Subject", "Phone Number"])
        # Writing student data
        writer.writerows(teachers)

    console.print(Fore.GREEN + f"Teacher data has been exported to {filename}")
################################TEACHERS END#######
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

##---------------Teacher allocation----------------
def allocate_teacher_to_student():
    teachers = Teacher.get_all_teachers()
    students = Student.get_all_students()

    if not teachers:
        console.print(Fore.RED + "No teachers available.")
        return

    if not students:
        console.print(Fore.RED + "No students available.")
        return

    console.print("Teachers:")
    for teacher in teachers:
        print(Fore.LIGHTMAGENTA_EX + f"{teacher[0]}. {teacher[1]} - {teacher[2]}")

    teacher_id = int(input(Fore.LIGHTGREEN_EX + "Enter teacher ID to allocate: "))

    # console.print("Students:")
    # for student in students:
    #     console.print(f"{student[0]}. {student[1]}")

    student_ids = input(Fore.LIGHTGREEN_EX + "Enter student IDs to allocate (comma-separated): ")
    student_ids = [int(id.strip()) for id in student_ids.split(',')]

    for student_id in student_ids:
        Student.allocate_teacher_to_student(teacher_id, student_id)

    print(Fore.LIGHTGREEN_EX + "Teacher allocated to students successfully!")
## Search by teacher
def view_students_by_teacher():
    teachers = Teacher.get_all_teachers()

    if not teachers:
        console.print(Fore.RED + "No teachers available.")
        return

    print(Fore.LIGHTMAGENTA_EX + "Teachers:")
    for teacher in teachers:
        print(Fore.LIGHTMAGENTA_EX + f"{teacher[0]}. {teacher[1]} - {teacher[2]}")

    teacher_id = int(input(Fore.LIGHTGREEN_EX + "Enter teacher ID to view students: "))
    students = Student.get_students_by_teacher(teacher_id)

    if not students:
        console.print(Fore.RED + "No students allocated to this teacher.")
    else:
        print("")
        table = Table(show_header=True, header_style="bold green", show_lines=False, style="magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", style="magenta")
        table.add_column("Level", style="magenta")
        print("")


        for student in students:
            table.add_row(str(student[0]), student[1], str(student[4]))

        console.print(table)
        print(Fore.LIGHTMAGENTA_EX + "")
####################################CLI CONTENT STARTS HERE############################
def main():
    initialize_db()
    attempts = 0



    while attempts < 3:
        console.print("\n" * 3)
        console.print("KAMONI-SCHOOL CLI ADMIN  TOOL", justify="center", style="bold green underline")
        print(Fore.LIGHTMAGENTA_EX + "An admin tool for managing student enrollment, schoolfees, exams, teacher allocation and inventory.")
        print("")
        print("Please try again" if attempts > 0 else "Please Login")
        username = input(Fore.LIGHTGREEN_EX + "Username: ")
        password = getpass.getpass(Fore.LIGHTGREEN_EX + "Password: ")

        if User.authenticate(username, password):
            print(Fore.LIGHTGREEN_EX + "Successfully logged in")
            while True:
                print(Fore.LIGHTMAGENTA_EX + "\nAdmin Panel:")
                print("")
                print("1. Student Records")
                print("2. Teacher Records")
                print("3. School Fees")
                print("4. Budget")
                print("5. Inventory")
                print("6. Exam Records")
                print("7. Logout")
                print("")
                choice = input(Fore.LIGHTGREEN_EX + "Choose an option: ")
                print("")
                if choice == '1':
                    print(Fore.LIGHTMAGENTA_EX + "Managing Student Records")
                    print("")
                    while True:
                        print("e :Enroll New Student")
                        print("d :Deregister Student")
                        print("s :Show Student Data")
                        print("g :Get csv data")
                        print("a :Allocate Teacher to Student")
                        print("f :find")
                        print("b :Back")
                        print("")
                        choice = input(Fore.LIGHTGREEN_EX + "Choose action:")
                        print("")
                        if choice == 'e':
                           enroll_new_student()
                        elif choice == 'd':
                            delete_student()
                        elif choice == 's':
                            display_students_table()
                        elif choice == 'g':
                            export_students_to_csv()
                        elif choice == 'a':
                            allocate_teacher_to_student()

                        elif choice == 'f':
                            print("")
                            print(Fore.LIGHTMAGENTA_EX + "Searching Student Records")
                            print("")
                            print("1 :Search by ID")
                            print("2 :Search by Level")
                            print("3 :Search by teacher")
                            print("4 :Back")
                            print("")
                            search_choice = input(Fore.LIGHTGREEN_EX + "Choose search option: ")
                            
                            if search_choice == '1':
                                search_student_by_id()
                            elif search_choice == '2':
                                search_student_by_level()
                            elif search_choice == '3': view_students_by_teacher()
                            elif choice == '4':
                                break
                            else:
                                print(Fore.RED + "Invalid choice, please try again.")
                            
                        elif choice == 'g':
                            export_students_to_csv()
            
                        elif choice == 'b':
                            break
                    #---------teacher records-------
                elif choice == '2':
                    print(Fore.LIGHTMAGENTA_EX  + "Managing Teacher Records")
                    print("")
                    if choice == '1':
                        print("")
                    while True:
                        print("e :Enroll New Teacher")
                        print("d :Deregister Teacher")
                        print("s :Show Teacher Data")
                        print("g :Get csv data")
                        print("f :find")
                        print("b :Back")
                        print("")
                        choice = input(Fore.LIGHTGREEN_EX + "Choose action:")
                        print("")
                        if choice == 'e':
                           enroll_new_teacher()
                        elif choice == 'd':
                            delete_teacher()
                        elif choice == 's':
                            display_teachers_table()
                        elif choice == 'g':
                            export_teachers_to_csv()

                        elif choice == 'f':
                            print("")
                            print(Fore.LIGHTMAGENTA_EX + "Searching Teacher Records")
                            print("")
                            print("1 :Search by ID")
                            print("2 :Search by Subject")
                            print("3 :Back")
                            print("")
                            search_choice = input(Fore.LIGHTGREEN_EX + "Choose search option: ")
                            
                            if search_choice == '1':
                                search_teacher_by_id()
                            elif search_choice == '2':
                                search_teacher_by_subject()
                            elif choice == '3':
                                break
                            else:
                                console.print(Fore.RED + "Invalid choice, please try again.")
                            
                        elif choice == 'g':
                            export_teachers_to_csv()
            
                        elif choice == 'b':
                            break
                    #---------end-teacher records----
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
                    print(Fore.LIGHTGREEN_EX  + "Exam Records")
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
