import psycopg2
import os

password = os.environ.get("PASSWORD")
# create a connection to the database
connection = psycopg2.connect(database="red30", user="postgres", password=password, host="localhost", port="5432")
# to automatically commit changes
connection.autocommit = True
cursor = connection.cursor()
# to call an existing procedure return_nondiscounted_items
cursor.execute('''CALL return_nondiscounted_items (%s,%s)''', (1105910, 1))
# cursor.callproc('CALL return_nondiscounted_items' (1105910, 1)) #is used for postgres functions not procedures
connection.close()
