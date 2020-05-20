# Creates table in sqlite db

import sqlite3
import pandas as pd

conn = sqlite3.connect('pythonsqlite.db')
cur = conn.cursor()
#cur.execute('INSERT INTO test (name, description) values ("Aquiles", "My experiment description")')

sql_command = """
DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id INTEGER,
    name VARCHAR,
    description VARCHAR,
    PRIMARY KEY (id));
INSERT INTO test (name, description) values ("Aquiles", "My experiment description");
INSERT INTO test (name, description) values ("Aquiles 2", "My experiment description 2");
"""
cur.executescript(sql_command)
conn.commit()
cur.execute('SELECT * FROM test')
data = cur.fetchall()
for d in data:
     print(d)
conn.close()

