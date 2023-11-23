import sqlite3
from sqlite3 import Error


db_filename = r"/home/jayson/PycharmProjects/FoS/db/pythonsqlite.db"
def create_database(db_files):
    conn = None
    try:
        conn = sqlite3.connect(db_files)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_database(db_filename)