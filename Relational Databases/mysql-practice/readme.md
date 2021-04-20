<br />
<p align="center">

  <h3 align="center">Mysql-practice</h3>

  <p align="center">
    project_description
    <br />
In this project I provide the implementation and documentation of my first experience working on of examples, challenges and practice of Mysql, one of the most popular open-source relational database management systems.<br />
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
* [mysql](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)

### Modules used:
* [mysql](https://pypi.org/project/MySQL-python/)
* [sqlalchemy](https://docs.sqlalchemy.org/en/14/)
* [sqlalchemy.orm ](https://docs.sqlalchemy.org/en/14/orm/)
* [pandas](https://pandas.pydata.org/)

###### Example: 
```py
# connecting to a database  projects and using a connection on the localhost
def connect():
    try:
        return mysql.connect(
            host="127.0.0.1", port="3306", user="root", password=ROOT_PASSWORD, auth_plugin='mysql_native_password',
            database="projects")
    except Error as e:
        print(e)
```
###### Example using command line:
1-navigate to : C:\Program Files\MySQL\MySQL Server 8.0\bin\
1-open shell or command prompt:'
```sh
#type: 
 > mysql -u root -p 
#enter the password of the database: 
# to create a database named "projects":
 > CREATE DATABASE projects;  
# to create a table:
 > CREATE TABLE projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR (255), PRIMARY KEY(project_id));
# to view the tables:
 SHOW TABLES;
 
# create a second table :
 CREATE TABLE tasks(task_id int (11) not null auto_increment, project_id int (11) not null, description varchar (255), primary key (task_id), foreign key(project_id) references projects(project_id));
# to insert a record in a table :
insert into projects (title, description) values ("Organize Photos", "Organize old photos by year");
insert into tasks (description, project_id) values ("Organize 2021 photos", 1);
insert into tasks (description, project_id) values ("Organize 2020 photos", 1);
insert into projects (title, description) values ("Read more", "Read a book every month this year");
insert into tasks (description, project_id) values ("Read nytimes best seller book ", 2);

# Since tasks are reference the projects by their ids, no task can be inserted without a project id
#projects can not be deleted if they have relevant tasks standing  (tasks must be deleted first)


#Viewing the projects in the database:
mysql> select * from projects;
+------------+-----------------+-----------------------------------+
| project_id | title           | description                       |
+------------+-----------------+-----------------------------------+
|          1 | Organize Photos | Organize old photos by year       |
|          2 | Read more       | Read a book every month this year |
+------------+-----------------+-----------------------------------+
2 rows in set (0.01 sec)

# view the tasks table
mysql> select * from tasks;
+---------+------------+--------------------------------------+
| task_id | project_id | description                          |
+---------+------------+--------------------------------------+
|       1 |          1 | Organize 2021 photos                 |
|       2 |          1 | Organize 2020 photos                 |
|       3 |          2 | Read ny times best seller book  |
+---------+------------+--------------------------------------+
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

