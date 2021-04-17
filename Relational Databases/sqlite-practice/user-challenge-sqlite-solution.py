import sqlite3

# Create and query a SQLite database
# create a Users' table
# Table Users has 4 columns: user_id, first_name, last_name,email
# insert multiple entries in each column
# Query the database to retrieve users email addresses
# solution using Sqlite 3 module with sql statements
connection = sqlite3.connect("users-sqlite.db")
cursor = connection.cursor()
cursor.execute("""create table if not exists Users
(user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email TEXT)""")
users_to_insert = [("fname1", "lname1", "email1@email.com"),
                   ("fname2", "lname2", "email2@email.com"),
                   ("fname3", "lname3", "email3@email.com"),
                   ("fname4", "lname4", "email4@email.com")]
cursor.executemany('''INSERT INTO Users (first_name, last_name,email)
 VALUES(?,?,?)''', users_to_insert)
# to print all email addresses in the users table
cursor.execute("SELECT  email FROM Users")
print(cursor.fetchall())
# print all records in the users table
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())
connection.commit()
connection.close()
