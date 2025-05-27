import json
import time
import sqlite3


def get_cached_currency(code: str, max_age: int = 3600):
    conn = sqlite3.connect("db/cache.db")
    cursor = conn.cursor()
    cursor.execute("SELECT response, timestamp FROM currency_cache WHERE currency = ?", (code,))
    row = cursor.fetchone()
    conn.close()

    print_all_cached()

    if row:
        response, timestamp = row
        if time.time() - timestamp < max_age:
            return json.loads(response)

    return None


def set_cached_currency(code: str, data: dict):
    conn = sqlite3.connect("db/cache.db")
    cursor = conn.cursor()
    cursor.execute(
        "REPLACE INTO currency_cache (currency, response, timestamp) VALUES (?, ?, ?)",
        (code, json.dumps(data), int(time.time()))
    )
    conn.commit()
    conn.close()



def print_all_cached():
    conn = sqlite3.connect("db/cache.db")
    cursor = conn.cursor()

    cursor.execute("SELECT currency, response, timestamp FROM currency_cache")
    rows = cursor.fetchall()

    for currency, response, timestamp in rows:
        print(f"{currency}:")
        print("  Данные:", json.loads(response))
        print("  Время:", timestamp)
        print()

    conn.close()

