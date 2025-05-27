import sqlite3


def init_db():
    conn = sqlite3.connect('db/cache.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currency_cache (
            currency TEXT PRIMARY KEY,
            response TEXT,
            timestamp INTEGER
        )
    """)
    conn.commit()
    conn.close()
