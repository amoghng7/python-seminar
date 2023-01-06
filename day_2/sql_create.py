import sqlite3

# Connect to music.sqlite3 if exists otherwise create a new DB
conn = sqlite3.connect('music.sqlite3')
# Create a cursor to perform operations
cur = conn.cursor()

# Drop the table if already exists
cur.execute('DROP TABLE IF EXISTS Tracks ')
# Create a table tracks with title as TEXT and plays as INTEGER
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

cur.execute('''CREATE TABLE IF NOT EXISTS Follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')