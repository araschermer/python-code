import pandas as pandas
from mysql.connector import Error
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
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
cursor.execute("CREATE DATABASE landon")

# connect with the database
engine = create_engine(f'mysql+mysqlconnector://root:{ROOT_PASSWORD}@localhost:3306/landon',
                       echo=True)
Base = declarative_base()


class Purchase(Base):
    __tablename__ = 'purchases'
    __table_args__ = {"schema": "landon"}

    order_id = Column(Integer, primary_key=True)
    property_id = Column(Integer)
    property_city = Column(String(250))
    property_state = Column(String(250))
    product_id = Column(Integer)
    product_category = Column(String(250))
    product_name = Column(String(250))
    quantity = Column(Integer)
    product_price = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return f'''<Purchase(order_id='{self.order_id}', property_id='{self.property_id}',
        property_city='{self.property_city}', property_state='{self.property_state}', product_id='{self.product_id}',
        product_category='{self.product_category}', product_name='{self.product_name}', quantity='{self.quantity}',
        product_price='{self.product_price}', order_total='{self.order_total}')>'''


Base.metadata.create_all(engine)

# import data from landon.csv file using panda and insert the data into the table
filename = "data/landon.csv"


def load_data_into_purchases_using_pandas(path):
    file_dataframe = pandas.read_csv(path)
    file_dataframe.to_sql(con=engine, name=Purchase.__tablename__, if_exists="append", index=False)


# load the data into the file using method call
# load_data_into_purchases_using_pandas(filename)
session = sessionmaker()
session.configure(bind=engine)
session = session()
data = session.query(Purchase).limit(10).all()
for entry in data:
    print(entry)
