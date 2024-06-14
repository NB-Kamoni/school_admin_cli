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
        - [Find Student](#find-student)
    - [Teacher Allocation](#teacher-allocation)
        - [Allocate Teacher to Student](#allocate-teacher-to-student)
        - [View Students by Teacher](#view-students-by-teacher)
    - [Inventory Management](#inventory-management)
        - [Add Inventory Item](#add-inventory-item)
        - [Delete Inventory Item](#delete-inventory-item)
        - [Show Inventory](#show-inventory)
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

test username: test
test password: pw

## Student management

1. **Enroll new student**
2. **Deregister student**
3. **Show student data**
4. **Get CSV data**
5. **Allocate teacher to students**
6. **Find**

## Teacher records

1. **Enroll new teacher**
2. **Deregister teacher**
3. **Show teacher data**
4. **Get CSV data**
5. **Find**
## Logout
