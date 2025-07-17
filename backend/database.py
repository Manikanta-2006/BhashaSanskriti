# backend/database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    language TEXT,
                    category TEXT,
                    text_data TEXT,
                    audio_path TEXT,
                    image_path TEXT,
                    video_path TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def save_submission(name, language, category, text_data, audio_path, image_path, video_path):
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('''INSERT INTO submissions 
                 (name, language, category, text_data, audio_path, image_path, video_path)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (name, language, category, text_data, audio_path, image_path, video_path))
    conn.commit()
    conn.close()
