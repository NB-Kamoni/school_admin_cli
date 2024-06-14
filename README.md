# Kamoni School Admin CLI Tool

Welcome to the Kamoni School Admin CLI Tool! This tool is designed to help school administrators manage student enrollment, school fees, exams, teacher allocation, and inventory efficiently.

## Table of Contents
1. [Installation](#installation)
2. [Initialization](#initialization)
3. [Usage](#usage)
    - [Login](#login)
    - [Student Management](#student-management)
        - [Enroll New Student](#enroll-new-student)
        - [Deregister Student](#deregister-student)
        - [Show Student Data](#show-student-data)
        - [Get CSV Data](#get-csv-data)
        - [Allocate Teacher to Students](#allocate-teacher-to-students)
        - [Find Student](#find-student)
    - [Teacher Allocation](#teacher-allocation)
         - [Enroll New Teacher](#enroll-new-teacher)
        - [Deregister Teacher](#deregister-teacher)
        - [Show Teacher Data](#show-teacher-data)
        - [Get CSV Data](#get-csv-data)
        - [Find Teacher](#find-teacher)
    - [Logout](#logout)

---

## Installation

1. **Clone the repository**:
   
  ```
   git clone git@github.com:NB-Kamoni/school_admin_cli.git

  ```
move into the working directory

  ```
  cd .../school_admin_cli

  ```

2. **Install dependensies**

```
pip install -r requirements.txt

```
ensure that Tkinter is installed...

```
sudo apt-get install python3-tk

```

## Initialization

1. **Activate the virtual env**

```
source venv/bin/activate

```
2. **Initialize the database**

```
app/cli.py

```
## Usage

1. **Run CLI tool**

```
app/cli.py

```
## Login
You will be prompted to log in. Enter your username and password to access the tool. If you fail to log in three times, you will be blocked.

test username: **test**
password: **pw**

## Student management

1. **Enroll new student**

Choose the "Students" option from the main menu.
Select 'e' to enroll a new student.
Follow the prompts to enter the student's details (name, age, parent name, level, phone number).
You will be asked to select a student photo from your file system.
The student's details and photo will be saved to the database.

2. **Deregister student**

Choose the "Students" option from the main menu.
Select 'd' to deregister a student.
Enter the student ID of the student you wish to deregister.
The student will be removed from the database.

3. **Show student data**

Choose the "Students" option from the main menu.
Select 's' to show student the student record.

4. **Get CSV data**

Choose the "Students" option from the main menu.
Select 'g' to export student data to a CSV file.

5. **Allocate teacher to students**

Choose the "Students" option from the main menu.
Select 'a' to allocate a teacher to a student.
Follow the prompts to select a teacher and assign them to many students.

6. **Find**

Choose the "Students" option from the main menu.
Select 'f' to find a student.
Choose 1 to search by ID, 2 to search by level and 3 to search by teacher.
Follow the prompts to enter the search criteria.
The student details will be displayed, including the student photo if available.

## Teacher records

1. **Enroll new teacher**
2. **Deregister teacher**
3. **Show teacher data**
4. **Get CSV data**
5. **Find**
## Logout
