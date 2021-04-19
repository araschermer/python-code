from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

password = os.environ.get("PASSWORD")
engine = create_engine(f'postgres://postgres:{password}@localhost/red30')
Base = declarative_base(engine)
# base object reflects the metadata in the database
Base.metadata.reflect(engine)


class Sales(Base):
    __table__ = Base.metadata.tables['sales']

    def __repr__(self):
        return f'''<Sale(order_num='{self.order_num}', order_type'{self.order_type}', cust_name='{self.cust_name}', 
            prod_name='{self.prod_name}', quantity='{self.quantity}', order_total='{self.order_total}')>'''


def load_session():
    session_ = sessionmaker(bind=engine)
    session_ = session_()
    return session_


def insert_sale(session_, order_num, order_type, cust_name,
                prod_number, prod_name, quantity, price, discount, order_total):
    recent_sale = Sales(order_num, order_type, cust_name,
                        prod_number, prod_name, quantity, price, discount, order_total)
    print(recent_sale)
    session_.add(recent_sale)
    session_.commit()
    return recent_sale


if __name__ == "__main__":
    session = load_session()

    # Read the smallest sale
    smallest_sales = session.query(Sales).order_by(Sales.order_total).limit(1)
    print(smallest_sales[0].cust_name)

    # Insert
    recent_sale = insert_sale(session, order_num=1105910, order_type='Retail', cust_name='Syman Mapstone',
                              prod_number='EB521',
                              prod_name='Understanding Artificial Intelligence', quantity=3, price=19.5, discount=0,
                              order_total=58.5)

    # Update the objects inmemory and  with that make changes to the database with the first commit
    sale = session.query(Sales).filter(Sales.order_num == 1105910).first()

    sale.quantity = 2
    sale.order_total = 39
    session.commit()
    updated_sale = session.query(Sales).filter(Sales.order_num == 1105910).first()
    print(updated_sale)

    # Delete
    returned_sale = session.query(Sales).filter(Sales.order_num == 1105910).first()
    session.delete(returned_sale)
    session.commit()
