import sqlite3

db = sqlite3.connect("connect.sqlite")
db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 5459828, 'tim@email.com')")
db.close()