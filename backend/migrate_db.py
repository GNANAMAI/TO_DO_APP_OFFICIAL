import sqlite3
import datetime

conn = sqlite3.connect('todos.db')
c = conn.cursor()

try:
    c.execute('ALTER TABLE todos ADD COLUMN category VARCHAR DEFAULT "Personal"')
except sqlite3.OperationalError:
    print("Column category exists")
    pass

try:
    c.execute('ALTER TABLE todos ADD COLUMN priority VARCHAR DEFAULT "medium"')
except sqlite3.OperationalError:
    print("Column priority exists")
    pass

try:
    c.execute('ALTER TABLE todos ADD COLUMN due_date VARCHAR')
except sqlite3.OperationalError:
    print("Column due_date exists")
    pass

try:
    c.execute('ALTER TABLE todos ADD COLUMN created_at VARCHAR')
    # Update existing rows
    c.execute('UPDATE todos SET created_at = ? WHERE created_at IS NULL', (datetime.datetime.utcnow().isoformat(),))
except sqlite3.OperationalError:
    print("Column created_at exists")
    pass

conn.commit()
print("Migration completed successfully.")
