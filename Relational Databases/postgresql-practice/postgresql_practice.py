import psycopg2
import os

PASSWORD = os.environ.get('PASSWORD')
# PostgreSQL is an RDBMS
# Data organized into tables, with columns and rows
# PostgreSQL is also an object-relational database
# it includes features like table inheritance and function overloading
# PostgreSQL interacts with python using python db api , sqlalchemy, sqlalchemy-orm, postgres-shell  or postgres-GUI
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user="postgres",
                              host="localhost",
                              password=PASSWORD,
                              port="5432",
                              database="red30"
                              )
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Creating a database
# cursor.execute('''CREATE database red30;''')
# cursor.execute('''DROP TABLE  if exists Sales;''')
# cursor.execute('''create table Sales( ORDER_NUM INT PRIMARY KEY,ORDER_TYPE TEXT, CUST_NAME TEXT, PROD_NUMBER TEXT,
#                                       PROD_NAME TEXT, QUANTITY INT, PRICE REAL, DISCOUNT REAL, ORDER_TOTAL REAL);
#                                       ''')

# view data in the table :
# cursor.execute("SELECT * FROM Sales LIMIT 10")
# print(cursor.fetchall())


# to insert a new sale into the database :
# cursor.execute('''INSERT INTO Sales (ORDER_NUM,ORDER_TYPE,CUST_NAME,PROD_NUMBER,PROD_NAME,QUANTITY,PRICE,DISCOUNT,
# ORDER_TOTAL)
#                VALUES(1105910, 'Retail', 'Syman Mapstone', 'EB521', 'Understanding Artificial Intelligence', 3, 19.5,
#                 0, 58.5)''')
# commit changes
connection.commit()


# select the recently inserted record using the order_num
# cursor.execute("SELECT CUST_NAME, ORDER_TOTAL from SALES WHERE ORDER_NUM=1105910")
# records = cursor.fetchall()
# for record in records:
#     print("CUST_NAME=", record[0])  # CUST_NAME= Syman Mapstone
#     print("ORDER_TOTAL=", record[1])  # ORDER_TOTAL= 58.5

# inserting a sale using a function :
def insert_sale(db_connection: psycopg2, order_num: int, order_type: str, cust_name: str, prod_number: str,
                prod_name: str, quantity: int, price: float, discount: float = 0):
    # calculating the order_total using the price, discount and quantity
    order_total = calculate_order_total(discount, price, quantity)
    sale_data = (order_num, order_type, cust_name, prod_number,
                 prod_name, quantity, price, discount, order_total)
    # create a cursor  object using the connection
    cursor = db_connection.cursor()
    # to overwrite/update existing data with the new data, delete the existing entry
    delete_existing_record(cursor, order_num)

    cursor.execute('''INSERT INTO Sales (ORDER_NUM,ORDER_TYPE,CUST_NAME,PROD_NUMBER,PROD_NAME,QUANTITY,PRICE,DISCOUNT,
    ORDER_TOTAL)VALUES(%s, %s, %s, %s, %s, %s, %s,%s,%s);''', sale_data)
    db_connection.commit()
    view_entry_data(cursor, order_num)


def view_entry_data(cursor, order_num):
    """prints some order information such ad ORDER_NUM, CUST_NAME,ORDER_TOTAL given an order number."""
    cursor.execute("SELECT ORDER_NUM, CUST_NAME, ORDER_TOTAL from SALES WHERE ORDER_NUM=%s;", (order_num,))
    data = cursor.fetchall()
    for record in data:
        print("ORDER_NUM=", record[0])
        print("CUST_NAME=", record[1])
        print("ORDER_TOTAL=", record[2])


def delete_existing_record(cursor, order_num):
    """deletes an existing record of a given order number from the database."""
    cursor.execute('''DELETE FROM SALES WHERE ORDER_NUM=%s;''', (order_num,))


def calculate_order_total(discount: float, price: float, quantity: int) -> float:
    """returns the total price of an order given  price of the item, the quantity, and the discount."""
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount
    return order_total


# test the insert_sale method
insert_sale(connection, 1105910, 'Retail', 'Syman Mapstone', 'EB521', 'Understanding Artificial Intelligence', 3, 19.5)

connection.close()
