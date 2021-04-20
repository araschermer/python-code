<br />
<p align="center">

  <h3 align="center">PostgreSQL-practice</h3>

  <p align="center">
    project_description
    <br />
In this project I provide the implementation and documentation of my first experience working on of examples, challenges and practice of PostgreSQL, one of the most popular open-source relational database management systems.
PostgreSQL is an RDBMS, that manages databases,  where data organized into tables, with columns and rows.PostgreSQL is also an object-relational database. it includes features like table inheritance and function overloading.

PostgreSQL interacts with python using python db api , sqlalchemy, sqlalchemy-orm, postgres-shell  or postgres-GUI
<br />
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

###### Example: 
```py

connection = psycopg2.connect(user="postgres",
                              host="localhost",
                              password=PASSWORD,
                              port="5432",
                              database="red30"
                              )
cursor = connection.cursor()

# Creating a database
cursor.execute('''CREATE database red30;''')
# delete a table "Sales"
cursor.execute('''DROP TABLE  if exists Sales;''')
# creating a new table "Sales"
cursor.execute('''create table Sales( ORDER_NUM INT PRIMARY KEY,ORDER_TYPE TEXT, CUST_NAME TEXT, PROD_NUMBER TEXT,
                                      PROD_NAME TEXT, QUANTITY INT, PRICE REAL, DISCOUNT REAL, ORDER_TOTAL REAL);
                                      ''')

# view all data in the table :
cursor.execute("SELECT * FROM Sales ")
print(cursor.fetchall())

# to insert a new sale into the database :
cursor.execute('''INSERT INTO Sales (ORDER_NUM,ORDER_TYPE,CUST_NAME,PROD_NUMBER,PROD_NAME,QUANTITY,PRICE,DISCOUNT,
ORDER_TOTAL)
               VALUES(1105910, 'Retail', 'Syman Mapstone', 'EB521', 'Understanding Artificial Intelligence', 3, 19.5,
                0, 58.5)''')
# commit changes
connection.commit()
```
###### Example using command line:
in the ```SQL shell```

```sh
#USE SQL SHELL TO RUN THIS COMMANDS 
# log into he shell using user the set username and password 
# to view all the databases: 
	\l
# to quit 
	\q
# to create database 
	CREATE DATABASE db_name
# to delete database
	DROP DATABASE db_name 
# to connect to a database :
	\c db_name 
# to view the table in the db:
	\dt 
# view data in tables :
	SELECT * FROM table_name;
# to view information about the table :
	 \d table_name
# to delete a table:
	DROP TABLE IF EXISTS table_name

# to read  data from a csv file into  a table :
\copy sales from '/path/to/file/red30-postgres.csv' WITH DELIMITER ',' CSV HEADER;


# call help function
  \help 
 Available help:
  ABORT                            CREATE USER
  ALTER AGGREGATE                  CREATE USER MAPPING
  ALTER COLLATION                  CREATE VIEW
  ALTER CONVERSION                 DEALLOCATE
  ALTER DATABASE                   DECLARE
  ALTER DEFAULT PRIVILEGES         DELETE
  ALTER DOMAIN                     DISCARD
  ALTER EVENT TRIGGER              DO
  ALTER EXTENSION                  DROP ACCESS METHOD
  ALTER FOREIGN DATA WRAPPER       DROP AGGREGATE
  ALTER FOREIGN TABLE              DROP CAST
  ALTER FUNCTION                   DROP COLLATION
  ALTER GROUP                      DROP CONVERSION
  ALTER INDEX                      DROP DATABASE
  ALTER LANGUAGE                   DROP DOMAIN
  ALTER LARGE OBJECT               DROP EVENT TRIGGER
  ALTER MATERIALIZED VIEW          DROP EXTENSION
  ALTER OPERATOR                   DROP FOREIGN DATA WRAPPER
  ALTER OPERATOR CLASS             DROP FOREIGN TABLE
  ALTER OPERATOR FAMILY            DROP FUNCTION
  ALTER POLICY                     DROP GROUP
  ALTER PROCEDURE                  DROP INDEX
  ALTER PUBLICATION                DROP LANGUAGE
  ALTER ROLE                       DROP MATERIALIZED VIEW
  ALTER ROUTINE                    DROP OPERATOR
  ALTER RULE                       DROP OPERATOR CLASS
  ALTER SCHEMA                     DROP OPERATOR FAMILY
  ALTER SEQUENCE                   DROP OWNED
  ALTER SERVER                     DROP POLICY
  ALTER STATISTICS                 DROP PROCEDURE
  ALTER SUBSCRIPTION               DROP PUBLICATION
  ALTER SYSTEM                     DROP ROLE
  ALTER TABLE                      DROP ROUTINE
  ALTER TABLESPACE                 DROP RULE
  ALTER TEXT SEARCH CONFIGURATION  DROP SCHEMA
  ALTER TEXT SEARCH DICTIONARY     DROP SEQUENCE
  ALTER TEXT SEARCH PARSER         DROP SERVER
  ALTER TEXT SEARCH TEMPLATE       DROP STATISTICS
  ALTER TRIGGER                    DROP SUBSCRIPTION
  ALTER TYPE                       DROP TABLE
  ALTER USER                       DROP TABLESPACE
  ALTER USER MAPPING               DROP TEXT SEARCH CONFIGURATION
  ALTER VIEW                       DROP TEXT SEARCH DICTIONARY
  ANALYZE                          DROP TEXT SEARCH PARSER
  BEGIN                            DROP TEXT SEARCH TEMPLATE
  CALL                             DROP TRANSFORM
  CHECKPOINT                       DROP TRIGGER
  CLOSE                            DROP TYPE
  CLUSTER                          DROP USER
  COMMENT                          DROP USER MAPPING
  COMMIT                           DROP VIEW
  COMMIT PREPARED                  END
  COPY                             EXECUTE
  CREATE ACCESS METHOD             EXPLAIN
  CREATE AGGREGATE                 FETCH
  CREATE CAST                      GRANT
  CREATE COLLATION                 IMPORT FOREIGN SCHEMA
  CREATE CONVERSION                INSERT
  CREATE DATABASE                  LISTEN
  CREATE DOMAIN                    LOAD
  CREATE EVENT TRIGGER             LOCK
  CREATE EXTENSION                 MOVE
  CREATE FOREIGN DATA WRAPPER      NOTIFY
  CREATE FOREIGN TABLE             PREPARE
  CREATE FUNCTION                  PREPARE TRANSACTION
  CREATE GROUP                     REASSIGN OWNED
  CREATE INDEX                     REFRESH MATERIALIZED VIEW
  CREATE LANGUAGE                  REINDEX
  CREATE MATERIALIZED VIEW         RELEASE SAVEPOINT
  CREATE OPERATOR                  RESET
  CREATE OPERATOR CLASS            REVOKE
  CREATE OPERATOR FAMILY           ROLLBACK
  CREATE POLICY                    ROLLBACK PREPARED
  CREATE PROCEDURE                 ROLLBACK TO SAVEPOINT
  CREATE PUBLICATION               SAVEPOINT
  CREATE ROLE                      SECURITY LABEL
  CREATE RULE                      SELECT
  CREATE SCHEMA                    SELECT INTO
  CREATE SEQUENCE                  SET
  CREATE SERVER                    SET CONSTRAINTS
  CREATE STATISTICS                SET ROLE
  CREATE SUBSCRIPTION              SET SESSION AUTHORIZATION
  CREATE TABLE                     SET TRANSACTION
  CREATE TABLE AS                  SHOW
  CREATE TABLESPACE                START TRANSACTION
  CREATE TEXT SEARCH CONFIGURATION TABLE
  CREATE TEXT SEARCH DICTIONARY    TRUNCATE
  CREATE TEXT SEARCH PARSER        UNLISTEN
  CREATE TEXT SEARCH TEMPLATE      UPDATE
  CREATE TRANSFORM                 VACUUM
  CREATE TRIGGER                   VALUES
  CREATE TYPE                      WITH
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

