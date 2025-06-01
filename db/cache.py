import json
import time
import sqlite3
from config import DB_NAME


def get_cached_currency(code: str, max_age: int = 3600):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT response, timestamp FROM currency_cache WHERE currency = ?", (code,))
    row = cursor.fetchone()
    conn.close()

    if row:
        response, timestamp = row
        if time.time() - timestamp < max_age:
            return json.loads(response)

    return None


def set_cached_currency(code: str, data: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "REPLACE INTO currency_cache (currency, response, timestamp) VALUES (?, ?, ?)",
        (code, json.dumps(data), int(time.time()))
    )
    conn.commit()
    conn.close()
