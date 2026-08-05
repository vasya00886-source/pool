import sqlite3

class ArkadyMemory:
    def __init__(self):
        self.db = sqlite3.connect('.arkady/memory.db')
        self.init_db()

    def init_db(self):
        cursor = self.db.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    FOREIGN KEY (session_id) REFERENCES sessions(id)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS skills (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    code TEXT NOT NULL,
                    lang TEXT NOT NULL
                )
            ''')
            self.db.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
            self.db.rollback()

    def save_session(self, name):
        cursor = self.db.cursor()
        try:
            cursor.execute('INSERT INTO sessions (name) VALUES (?)', (name,))
            self.db.commit()
        except sqlite3.Error as e:
            print(f"Error saving session: {e}")
            self.db.rollback()

    def load_session(self, name):
        cursor = self.db.cursor()
        try:
            cursor.execute('SELECT * FROM sessions WHERE name = ?', (name,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error loading session: {e}")
            return None

    def save_message(self, session_id, role, content):
        cursor = self.db.cursor()
        try:
            cursor.execute('INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)', (session_id, role, content))
            self.db.commit()
        except sqlite3.Error as e:
            print(f"Error saving message: {e}")
            self.db.rollback()

    def search_sessions(self, query):
        cursor = self.db.cursor()
        try:
            cursor.execute('SELECT * FROM sessions WHERE name LIKE ?', (f'%{query}%',))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching sessions: {e}")
            return []

    def register_skill(self, name, code, lang):
        cursor = self.db.cursor()
        try:
            cursor.execute('INSERT INTO skills (name, code, lang) VALUES (?, ?, ?)', (name, code, lang))
            self.db.commit()
        except sqlite3.Error as e:
            print(f"Error registering skill: {e}")
            self.db.rollback()

    def get_skill(self, query):
        cursor = self.db.cursor()
        try:
            cursor.execute('SELECT * FROM skills WHERE name LIKE ?', (f'%{query}%',))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting skill: {e}")
            return []

    def close(self):
        try:
            self.db.commit()
            self.db.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")