"""A library module so you can start talking with databases"""

import sqlite3

DATABASE = "coffee_shop.db"

def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()