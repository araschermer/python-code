<br />
<p align="center">

  <h3 align="center">Flask-Practice</h3>

  <p align="center">
    project_description
    <br />
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.<br />

In this Flask-Practice, I provide my implementation and documentation of projects using Flask framework

   <br />
    <br />
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Projects</h2></summary>
  <ol>
      <ul>
        <li><a href="https://github.com/amgad01/python-code/tree/main/flask-practice/project-tracker">Project-Tracker</a></li>
        <ul>about the project:  project tracker is  designed to record projects and the associated tasks in a database using PostgreSQL as RDBMS
it  has the functionality to add, delete and view projects or tasks that can be stored in a database "project_tracker"</ul>
      </ul>


  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
These projects were developed, documented and tested to improve one's skills  mainly in the following programming languages and frameworks
* [Python](https://www.python.org/)
* [flask_sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) 
* [SQLalchemy / PostgreSQL](PostgreSQL) 
* [flask](https://flask.palletsprojects.com/en/1.1.x/)
* [jinja2](https://jinja.palletsprojects.com/)


<!-- GETTING STARTED -->
## Installation 
Install the following modules 
* `flask ` 
* `psycopg2` 
* `sqlalchemy` 
* `flask_sqlalchemy`


## example of a simple flask project
```py
from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
	return "Hello World!"
if __name__=='__main__':
	app.run()
```