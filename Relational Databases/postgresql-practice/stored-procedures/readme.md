<br />
<p align="center">

  <h3 align="center">Stored procedures</h3>

  <p align="center">
    project_description
    <br />
A stored procedure is a group of SQL statements that has been created and stored in the database. A stored procedure will accept input parameters so that a single procedure can be used over the network by several clients using different input data.
Stored procedures are associated with the database not the application, therefore  it is more practical to create the procedure in the shell before using it in the python application<br />
    <br />
  </p>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <ul><li><a href="#modules">modules used</a></ul>
      </ul>
    </li>
    <li>
      <a href="#example">Example</a>
    </li>
        <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
### Built With:
* [Python](Python)
* [PostgreSQL](https://www.postgresql.org/)

### Modules used:
* [psycopg2](https://pypi.org/project/psycopg2/)
* [sqlalchemy](https://docs.sqlalchemy.org/en/14/)
* [sqlalchemy.orm ](https://docs.sqlalchemy.org/en/14/orm/)
* [sqlalchemy.core ](https://docs.sqlalchemy.org/en/14/core/)

###### Example using command line:
in the ```SQL shell```

```
# activate/connect to a database 
[comment]: <> (    \c database_name )
[comment]: <> (     example:)
     \c red30
[comment]: <> (# to create a stored procedure:)
	 \h CREATE PROCEDURE
[comment]: <> (# $$  double dollar sign indicates the start of the body procedure)
[comment]: <> (# BEGIN : use begin and end for consistancy, so a procedure is treated as a transaction)
[comment]: <> (# use $ before numbers )
[comment]: <> (## example of creating a procedure that updates the  database when an item is returned &#40;for an item without any discounts applied&#41;)
red30=# \h CREATE PROCEDURE
Command:     CREATE PROCEDURE
Description: define a new procedure
Syntax:
CREATE [ OR REPLACE ] PROCEDURE
    name ( [ [ argmode ] [ argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] )
  { LANGUAGE lang_name
    | TRANSFORM { FOR TYPE type_name } [, ... ]
    | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
    | SET configuration_parameter { TO value | = value | FROM CURRENT }
    | AS 'definition'
    | AS 'obj_file', 'link_symbol'
  } ...
URL: https://www.postgresql.org/docs/13/sql-createprocedure.html

red30=# CREATE OR REPLACE PROCEDURE return_nondiscounted_items(INT,INT)
red30-# LANGUAGE plpgsql
red30-# AS $$
red30$# BEGIN
red30$# UPDATE sales
red30$# SET quantity=quantity- $2, order_total=order_total-price * $2
red30$# WHERE order_num=$1 AND discount=0;
red30$# commit;
red30$# end;
red30$# $$;
CREATE PROCEDURE
red30=#

[comment]: <> (# to call a procedure :)
	CALL return_nondiscounted_items(1105910,1);
```
The stored procedure can be used later in the application as shown in examples in ```sqlalchemycore-storedproc.py``` and ```sqlalchemyorm_storedproc.py```

###### Example: 
```py
engine = create_engine(f'postgres://postgres:{password}@localhost/red30')

with engine.connect() as connection:
	meta = MetaData(engine)
	sales_table = Table('sales', meta, autoload=True, autoload_with=engine)
	#  to end the current transaction and start a new one
	connection.execute('COMMIT')
	# alternatively:
	# add isolation_level = "AUTO_COMMIT" to the create_engine parameters
    # Call the stored procedure "return_nondiscounted_item" with the parameters (1105910, 1)
	connection.execute('CALL return_nondiscounted_item (%s, %s)', (1105910, 1))
```
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

