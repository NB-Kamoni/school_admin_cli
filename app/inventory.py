import sqlite3

class Inventory:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

    def save_to_db(self):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO inventory (item_name, quantity) VALUES (?, ?)', 
                       (self.item_name, self.quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_item(item_id):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_items():
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM inventory')
        items = cursor.fetchall()
        conn.close()
        return items
