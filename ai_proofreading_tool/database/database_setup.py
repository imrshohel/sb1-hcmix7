import sqlite3
import os

def create_database():
    db_path = os.path.join('resources', 'proofreading_tool.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create user_prompts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_prompts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt_name TEXT UNIQUE NOT NULL,
        prompt_content TEXT NOT NULL
    )
    ''')

    # Create documents table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
    ''')

    # Create user_settings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
    ''')

    # Insert default settings
    cursor.execute("INSERT OR IGNORE INTO user_settings (key, value) VALUES (?, ?)", 
                   ('current_ai_service', 'OpenAI'))
    cursor.execute("INSERT OR IGNORE INTO user_settings (key, value) VALUES (?, ?)", 
                   ('api_key', ''))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()