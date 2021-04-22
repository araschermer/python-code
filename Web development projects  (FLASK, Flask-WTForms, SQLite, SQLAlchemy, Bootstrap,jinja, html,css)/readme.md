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
        <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20development%20projects%20%20(FLASK%2C%20Flask-WTForms%2C%20SQLite%2C%20SQLAlchemy%2C%20Bootstrap%2Cjinja%2C%20html%2Ccss)/basic_blog">Basic Blog</a></li>
        <ul><b>About the project</b>: this project is implemented  to practice the basic functionality of flask, jinja2, flask-wtforms  
            <li> Used modules: <em> flask</em>, <em> flask_wtf</em>, <em> wtforms</em> 
      </ul></ul> 
<ul>
        <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20development%20projects%20%20(FLASK%2C%20Flask-WTForms%2C%20SQLite%2C%20SQLAlchemy%2C%20Bootstrap%2Cjinja%2C%20html%2Ccss)/blog">Simple Blog</a></li>
        <ul>about the project: Simple Blog  with a number of blog posts that are retrieved through requests from the <a href="https://api.npoint.io"> npoint api</a> and render the  different post content in simple html template structure.
            <li> Used modules: <em> flask</em>, <em> requests</em> 
</li>
</ul>
</ul>
 <ul>
        <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20development%20projects%20%20(FLASK%2C%20Flask-WTForms%2C%20SQLite%2C%20SQLAlchemy%2C%20Bootstrap%2Cjinja%2C%20html%2Ccss)/project-tracker">Project Tracker</a></li>
        <ul>about the project: <em><b>Project Tracker</b></em> is designed to record projects and the associated tasks in a database using PostgreSQL as RDBMS
it  has the functionality to add, delete and view projects or tasks that can be stored in a database "project_tracker"</ul>
      </ul>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
These projects were developed, documented and tested to improve one's skills  mainly in the following programming languages and frameworks
* [Python](https://www.python.org/)
* [html5](html5)
* [CSS](CSS)
* [Javascript](Javascript)
* [flask](https://flask.palletsprojects.com/en/1.1.x/)
* [jinja2](https://jinja.palletsprojects.com/)
* [flask_sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) 
* [SQLalchemy](SQLalchemy)
* [SQLite](SQLite)
* [PostgreSQL](PostgreSQL)
* [requests](https://pypi.org/project/requests/)


<!-- GETTING STARTED -->
## Installation 
Install the following modules 
* `flask ` 
* `psycopg2` 
* `sqlalchemy` 
* `flask_sqlalchemy`
* `requests`


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