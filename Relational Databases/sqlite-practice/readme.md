<br />
<p align="center">

  <h3 align="center">SQLLite-practice</h3>

  <p align="center">
    project_description
    <br />
In this project I provide the implementation and documentation of my first experience working on of examples, challenges and practice of SQLite, one of the most popular open-source relational database management systems .<br />
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
* [Sqlite](https://www.sqlite.org/index.html)
### Modules used:
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [sqlalchemy](https://docs.sqlalchemy.org/en/14/)

######Example: 
```py
# 1- CREATE AND CONNECT TO THE DATABASE
connection = sqlite3.connect("movies.db")
# 2-  CREATE CURSOR OBJECT TO MANIPULATE THE DATABASE
cursor = connection.cursor()
#  CREATE TABLE named Movies IN THE DATABASE, AND SPECIFY THE NAME AND THE TYPE OF EACH COLUMN
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies(Title TEXT, Director TEXT, Year INT)''')
# adding entries to the movies DB
cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

