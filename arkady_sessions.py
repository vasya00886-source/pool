import json
from pathlib import Path
import sqlite3

class SessionManager:
    def __init__(self):
        self.dir = Path('.arkady/sessions')
        if not self.dir.exists():
            self.dir.mkdir(parents=True)

    def import_zcode(self, db_path):
        try:
            if not Path(db_path).exists():
                raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT sid, messages FROM sessions")
            rows = cursor.fetchall()

            for row in rows:
                sid, messages_json = row
                messages = json.loads(messages_json)
                self.save(sid, messages)

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        except FileNotFoundError as e:
            print(e)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
        finally:
            if conn:
                conn.close()