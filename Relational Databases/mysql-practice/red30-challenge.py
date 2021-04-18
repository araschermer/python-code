import pandas as pandas
from mysql.connector import Error
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector as mysql
import os

from sqlalchemy.orm import sessionmaker

ROOT_PASSWORD = os.environ.get('ROOT_PASSWORD')


# create database
def connect():
    try:
        return mysql.connect(
            host="127.0.0.1", port="3306", user="root", password=ROOT_PASSWORD, auth_plugin='mysql_native_password')
    except Error as e:
        print(e)


landon_db = connect()
cursor = landon_db.cursor()
# create database
# cursor.execute("CREATE DATABASE red30")

# connect with the database
engine = create_engine(f'mysql+mysqlconnector://root:{ROOT_PASSWORD}@localhost:3306/red30',
                       echo=True)
Base = declarative_base()


class Sales(Base):
    __tablename__ = 'sales'
    __table_args__ = {"schema": "red30"}
    order_num = Column(Integer, primary_key=True, unique=True)
    order_type = Column(String(250))
    cust_name = Column(String(250))
    # cust_state = Column(String(250))
    # prod_category = Column(String(250))
    prod_number = Column(String(250))
    prod_name = Column(String(250))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return f'''<Purchase(order_num='{self.order_num}', order_type='{self.order_type}',
         prod_number='{self.prod_number}', product_name='{self.prod_name}', quantity='{self.quantity}', 
        product_price='{self.price}',discount='{self.discount}', order_total='{self.order_total}')>'''



Base.metadata.create_all(engine)

# import data from landon.csv file using panda and insert the data into the table
filename = "data/red30.csv"


def load_data_into_sales_using_pandas(path):
    file_dataframe = pandas.read_csv(path)
    file_dataframe.to_sql(con=engine, name=Sales.__tablename__, if_exists="replace", index=False)


# load the data into the file using method call
load_data_into_sales_using_pandas(filename)
session = sessionmaker()
session.configure(bind=engine)
session = session()
data = session.query(Sales).all()
for entry in data:
    print(entry)
# get the available information on the biggest purchase
# approach 01
biggest_purchase = session.query(func.max(Sales.order_total)).scalar()
print(f" biggest purchase is:{biggest_purchase} ")
# approach 02 : providing more information on the biggest purchase
data = session.query(Sales).order_by(Sales.order_total.desc())
print(f" biggest purchase is:{data[0]}")
