import sqlite3
from config import DB_NAME


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currency_cache (
            currency TEXT PRIMARY KEY,
            response TEXT,
            timestamp INTEGER
        )
    """)
    conn.commit()

    cursor.execute("""
           CREATE TABLE IF NOT EXISTS subscriptions (
               chat_id INTEGER,
               currency_code TEXT,
               UNIQUE(chat_id, currency_code)
           )
       """)
    conn.commit()

    conn.close()
