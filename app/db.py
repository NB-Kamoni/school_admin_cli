import sqlite3

#Initializes db and creates user table
def initialize_db():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    #Create students table/enroll
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        parent_name TEXT NOT NULL,
        level TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        photo_path TEXT                      
    )
    ''')
     #Create teachers table/enroll
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        subject TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        photo_path TEXT                      
    )
    ''')

    #Create teacher_students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teacher_student (
        teacher_id INTEGER,
        student_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        PRIMARY KEY (teacher_id, student_id)
    )
    ''')
     # Create inventory table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')



    conn.commit()
    conn.close()

