import sqlite3

# 1- CREATE AND CONNECT TO THE DATABASE
connection = sqlite3.connect("movies.db")
# 2-  CREATE CURSOR OBJECT TO MANIPULATE THE DATABASE
cursor = connection.cursor()
#  CREATE TABLE named Movies IN THE DATABASE, AND SPECIFY THE NAME AND THE TYPE OF EACH COLUMN
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies(Title TEXT, Director TEXT, Year INT)''')

# adding entries to the movies DB
cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

# RETRIEVING A SINGLE RECORD/ENTRY
cursor.execute("SELECT * FROM Movies")  # select all columns in the movies table
print(cursor.fetchone())  # from all columns, view the first row

# adding multiple entries
famous_movies = [('Pulp Fiction', 'Quentin Tarantino', 1994),
                 ('Back to the Future', 'Steven Spielberg', 1985),
                 ('Moonrise Kingdom', ' Wes Anderson', 2012)]
# cursor.executemany('INSERT INTO movies VALUES (?,?,?)', famous_movies)

# viewing all records:
records = cursor.execute("SELECT * FROM Movies")


def fetch_records():
    return cursor.execute("SELECT * FROM Movies")


# approach 01
print("approach 01")
print(cursor.fetchall())
# approach 02
print("approach 02")
# the cursor acts as a pointer from the beginning to the end of the records
# it can only be iterated though once, otherwise it resets by every call
# here , the iteration happens over the records variable not the cursor, therefore multiple iterations are possible
for record in records:
    print(record)
# selecting entries with specific properties:
release_year = (1985,)
cursor.execute("SELECT * from Movies where year =?", release_year)
print(cursor.fetchall())


# deleting entries from the db:
def delete(value):
    cursor.execute(f"DELETE FROM Movies WHERE year ={value}")
    connection.commit()


# updating entries with specific properties
def update(column, old_value, new_value):
    cursor.execute(f"UPDATE Movies SET {column} ={new_value} WHERE {column} ={old_value}")
    connection.commit()


# Testing
print("Testing database")
# adding a new testing entry and viewing  the  database
cursor.execute("INSERT INTO Movies VALUES ('TESTING', 'TESTING', 1999)")
fetch_records()
print(cursor.fetchall())
# Updating the new testing entry and viewing  the database
update("year", 1999, 2020)
fetch_records()
print(cursor.fetchall())
#  deleting the new testing entry and viewing the DB
delete(2020)
fetch_records()

print(cursor.fetchall())

# SAVE THE CHANGES
connection.commit()
# CLOSE CONNECTION
connection.close()
