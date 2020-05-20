# Creates table in sqlite db

import sqlite3

conn = sqlite3.connect('pythonsqlite.db')
cur = conn.cursor()
cur.execute('CREATE TABLE test (name VARCHAR, description VARCHAR)')
conn.commit()

conn.close()