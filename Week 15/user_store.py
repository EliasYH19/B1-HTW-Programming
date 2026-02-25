import sqlite3

class UserStore:
    def __init__(self, db_path):
     #Constructor accepts db_path and initializes the database
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        #Creates the users table if it does not already exist
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def load(self):
        # Returns a list of all user dictionaries from the database
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        users = [dict(row) for row in rows]
        conn.close()
        return users

    def save(self, user_data):
        # Inserts a new user into the database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user_data['name'], user_data['email'])
        )
        conn.commit()
        conn.close()

    def find_by_id(self, user_id):
        # Returns a specific user dict or None using an SQL queryy
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def update_user(self, user_id, updated_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (updated_data['name'], updated_data['email'], user_id)
        )
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    def delete_user(self, user_id):
        # Removes a user by ID using an SQL DELETE statement
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return success
