import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

# Insert values into table
# cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
# ( 'Thunderstruck', 20 ) )
# cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
# ( 'My Way', 15 ) )
# conn.commit()

print('Tracks:')
# Fetch values from the table
cur.execute('SELECT title, plays FROM Tracks')
# Iterate through the result to print table contents
for row in cur :
    print(row)

# Delete tracks where plays is less than 20
cur.execute('DELETE FROM Tracks WHERE plays < 20')

conn.commit()
cur.close()