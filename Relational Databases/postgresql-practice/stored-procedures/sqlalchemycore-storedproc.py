from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
import os

password = os.environ.get("PASSWORD")

engine = create_engine(f'postgres://postgres:{password}@localhost/red30')

with engine.connect() as connection:
	meta = MetaData(engine)
	sales_table = Table('sales', meta, autoload=True, autoload_with=engine)
	#  to end the current transaction and start a new one
	connection.execute('COMMIT')
	# alternatively:
	# add  isolation_level = "AUTO_COMMIT" to the create_engine  parameters
	connection.execute('CALL return_nondiscounted_item (%s, %s)', (1105910, 1))
