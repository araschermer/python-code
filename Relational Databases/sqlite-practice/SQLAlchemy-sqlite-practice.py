import sqlalchemy as db

# SQLAlchemy is a large SQL toolkit
# 1- SQLAlchemy core
# create engine and connect to database
# it the db does not exist, then it will be created
# an engine allows and manages multiple database connections
engine = db.create_engine("sqlite:///movies.db")
connection = engine.connect()
# Get the METADATA  of the DB table content
metadata = db.MetaData()
# Load the DB content into SQLAlchemy
movies = db.Table("Movies", metadata, autoload=True, autoload_with=engine)
movies_query = db.select([movies])

# view db records
# approach 01:
result_proxy = connection.execute(movies_query)
print(result_proxy.fetchall())


# approach 02:


def view_records():
    query = db.select([movies])
    res_proxy = connection.execute(query)
    res_set = res_proxy.fetchall()
    for entry in res_set:
        print(entry)


# adding conditions to the query
query = db.select([movies]).where(movies.columns.Director == "Martin Scorsese")
result_proxy = connection.execute(query)
print(result_proxy.fetchall())

# Inserting entries into the table
# query = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", Year="1960")
connection.execute(query)

# viewing the records in the database
view_records()
