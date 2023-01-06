import json
import sqlite3
import twitter_following_lookup

conn = sqlite3.connect('spider.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Twitter
(id INTEGER, username TEXT, name TEXT)''')

response = twitter_following_lookup.get_following_for("drchuck")
for data in response['data']:
    cur.execute("INSERT OR IGNORE INTO Twitter (id, username, name) VALUES (?,?,?)", 
    (data['id'], data['username'], data['name']))

conn.commit()
cur.close()