import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # Store the plain text password
        print(f"Debug: Created user with username {self.username} and password {self.password}")

    def save_to_db(self):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
            conn.commit()
            print("Debug: User saved to database")
        except sqlite3.IntegrityError:
            print(f"User {self.username} already exists.")
        conn.close()

    @staticmethod
    def authenticate(username, password):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        record = cursor.fetchone()
        conn.close()

        print(f"Debug: Retrieved password from database: {record}")
        print(f"Debug: Input password: {password}")

        if record and record[0] == password:
            return True
        else:
            return False
