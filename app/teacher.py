import sqlite3

class Teacher:
    def __init__(self, name, age, subject, phone_number):
        self.name = name
        self.age = age
        self.subject = subject
        self.phone_number = phone_number

    def save_to_db(self):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO teachers (name, age, subject, phone_number) VALUES (?, ?, ?, ?)', 
                       (self.name, self.age, self.subject, self.phone_number))
        conn.commit()
        conn.close()

    #Delete student
    @staticmethod
    def delete_teacher(teacher_id):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM teachers WHERE id = ?', (teacher_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_teachers():
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teachers')
        teachers = cursor.fetchall()
        conn.close()
        return teachers
    @staticmethod
    def get_teachers_by_id(id):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teachers WHERE id = ?', (id,))
        teachers = cursor.fetchall()
        conn.close()
        return teachers

    @staticmethod
    def get_teachers_by_subject(subject):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teachers WHERE subject = ?', (subject,))
        teachers = cursor.fetchall()
        conn.close()
        return teachers
