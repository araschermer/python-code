import sqlalchemy

# Create and query a SQLite database
# create a Users' table
# Table Users has 4 columns: user_id, first_name, last_name,email
# insert multiple entries in each column
# Query the database to retrieve users email addresses
# solution using SQLAlchemy

engine = sqlalchemy.create_engine("sqlite:///users-sqlite_sqlalchemy.db")
metadata = sqlalchemy.MetaData()
connection = engine.connect()
users = sqlalchemy.Table("Users", metadata, sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("first_name", sqlalchemy.Text),
                         sqlalchemy.Column("last_name", sqlalchemy.Text),
                         sqlalchemy.Column("email", sqlalchemy.Text))
metadata.create_all(engine)
# Insertion query
insertion_query = users.insert().values([
    {"first_name": "fname1", "last_name": "lname1", "email": "email1@email.com"},
    {"first_name": "fname2", "last_name": "lname2", "email": "email2@email.com"},
    {"first_name": "fname3", "last_name": "lname3", "email": "email3@email.com"},
    {"first_name": "fname4", "last_name": "lname4", "email": "email4@email.com"},
])
connection.execute(insertion_query)
# selection query
selection_query = sqlalchemy.select([users.columns.email])
query_result = connection.execute(selection_query)
print(query_result.fetchall())
connection.commit()
connection.close()
