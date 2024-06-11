import sqlite3

class Student:
    def __init__(self, name, age, parent_name, level):
        self.name = name
        self.age = age
        self.parent_name = parent_name
        self.level = level

    def save_to_db(self):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, age, parent_name, level) VALUES (?, ?, ?, ?)', 
                       (self.name, self.age, self.parent_name, self.level))
        conn.commit()
        conn.close()

    #Delete student
    @staticmethod
    def delete_student(student_id):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_students():
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        conn.close()
        return students
