import mysql.connector as mysql
import csv
from mysqlx import Error
import os

ROOT_PASSWORD = os.environ.get('ROOT_PASSWORD')


def connect():
    """initialize a connection to a mysql db on a local host server """
    try:
        return mysql.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password=ROOT_PASSWORD
            , auth_plugin='mysql_native_password',
            database="sales",
        )
    except Error as e:
        print(e)


sales_db = connect()
cursor = sales_db.cursor()


# create a database sales
# cursor.execute("CREATE DATABASE sales")

def create_salesperson_table(cursor):
    create_table_query = f'''CREATE TABLE salesperson (id INT(255) NOT NULL AUTO_INCREMENT,	
    first_name VARCHAR(255) NOT NULL,last_name VARCHAR(255) NOT NULL,
     email_address VARCHAR(255) NOT NULL, city VARCHAR(255) NOT NULL,
     state VARCHAR(255) NOT NULL,PRIMARY KEY (id))'''
    # drop table if it exists
    cursor.execute(f"DROP TABLE IF EXISTS salesperson")
    cursor.execute(create_table_query)


# create table salesperson
# create_salesperson_table(salesperson,cursor)


def insert_data_into_salesperson(new_data, cursor_):
    cursor_.execute('INSERT INTO salesperson(first_name, last_name, email_address, city, state) '
                    'VALUES("%s", "%s", "%s", "%s","%s")', new_data)
    return sales_db.commit()


# Two ways to read dataa from a local file
# 1- using the csv module
def read_csv_and_insert_into_sales_person(path):
    with open(path, "r") as salesperson_file:
        salesperson_data = csv.reader(salesperson_file)
        for entry in salesperson_data:
            print(entry)
            entry = tuple(entry)
            print(f" entry after formatting{entry}")
            insert_data_into_salesperson(entry, cursor)


# read data from a csv file and insert into salesperson table
# read_csv_and_insert_into_sales_person(path="data/salespeople.csv")
# sales_db.close()


# 2- using sql query
def load_local_salesperson_file(path, cursor):
    q = f'''LOAD DATA LOCAL INFILE  '{path}' INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
    (first_name, last_name, email_address, city, state);'''
    cursor.execute(q)


#  initialize  server with local infile allowed
def connect_with_local_infile_allowed():
    """initialize a connection to a mysql db on a local host server """
    try:
        return mysql.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password=ROOT_PASSWORD,
            auth_plugin='mysql_native_password',
            database="sales",
            allow_local_infile=True
        )
    except Error as e:
        print(e)


def view_table_data(cursor):
    """view the data frm the table given as a parameter"""
    cursor.execute(f"SELECT * FROM salesperson")
    data = cursor.fetchall()
    print(data)


db = connect_with_local_infile_allowed()
cursor = db.cursor()

create_salesperson_table(cursor=cursor)
load_local_salesperson_file("data/salespeople.csv",
                            cursor=cursor)
view_table_data(cursor=cursor)
