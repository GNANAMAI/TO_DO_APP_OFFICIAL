import uvicorn
import sqlite3
import datetime
from database import engine
import models

def run_migrations():
    print("Ensuring database tables exist...")
    # This creates the database and tables if they don't exist
    models.Base.metadata.create_all(bind=engine)
    
    print("Checking for required schema updates...")
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    
    # Try adding columns. If they already exist, it raises OperationalError which we ignore.
    try:
        c.execute('ALTER TABLE todos ADD COLUMN category VARCHAR DEFAULT "Personal"')
        print(" -> Added 'category' column.")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute('ALTER TABLE todos ADD COLUMN priority VARCHAR DEFAULT "medium"')
        print(" -> Added 'priority' column.")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute('ALTER TABLE todos ADD COLUMN due_date VARCHAR')
        print(" -> Added 'due_date' column.")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute('ALTER TABLE todos ADD COLUMN created_at VARCHAR')
        c.execute('UPDATE todos SET created_at = ? WHERE created_at IS NULL', (datetime.datetime.utcnow().isoformat(),))
        print(" -> Added 'created_at' column.")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()
    print("Database initialization complete and migrations applied!")

if __name__ == "__main__":
    run_migrations()
    print("Starting FastAPI server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
