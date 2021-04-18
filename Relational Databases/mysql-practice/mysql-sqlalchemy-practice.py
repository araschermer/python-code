import mysql.connector as mysql
from mysqlx import Error
from sqlalchemy import Column, String, ForeignKey, create_engine, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

# Since sqlalchemy does not initialize database, it just connects to it,
# mysql-connector is used to initialize the database
# create a database and connect to it
ROOT_PASSWORD = os.environ.get('ROOT_PASSWORD')


def connect():
    try:
        return mysql.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password=ROOT_PASSWORD
            , auth_plugin='mysql_native_password')
    except Error as e:
        print(e)


household_db = connect()
cursor = household_db.cursor()
# create a database called household
# cursor.execute("CREATE DATABASE household")

# -----Working with sqlalchemy---------#
engine = create_engine(f"mysql+mysqlconnector://root:{ROOT_PASSWORD}@localhost:3306/household", echo=True)
# the parameter for the engine creation are:
# type of the db, driver( since it is on the server), username, password,
# host of the db, database name, echo=True to print the executed command

# --Object relational mapping--#
#  create a base, since all models in the ORM are based on the declarative base
Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'
    __tableargs__ = {"schema": "household"}
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        """ shows a printable representation of the object"""
        return f"<Project(title={self.title}, description={self.description})>"


class Task(Base):
    __tablename__ = 'tasks'
    __tableargs__ = {"schema": "household"}
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    description = Column(String(length=50))
    project = relationship("Project")

    # Project here is the name of the class, so the relationship is between objects of classes( between two models)

    def __repr__(self):
        """ shows a printable representation of the object"""
        return f"<Task(description={self.description})>"


Base.metadata.create_all(engine)
# create a session to query the database
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()
# adding a project in the session into the database
learn_rdbms_project = Project(title="Learn RDBMS", description="learn relational database management systems")
session.add(learn_rdbms_project)
# commit project addition
session.commit()
# adding tasks for the first project
tasks = [Task(project_id=learn_rdbms_project.project_id, description=" learn Mysql"),
         Task(project_id=learn_rdbms_project.project_id, description=" learn SQLite"),
         Task(project_id=learn_rdbms_project.project_id, description=" learn POSTGRESQL")]
session.bulk_save_objects(tasks)
session.commit()

# Retrieve the committed project in this session
project = session.query(Project).filter_by(title="Learn RDBMS").first()
print(project)
# to retrieve the committed tasks in this project
project_tasks = session.query(Task).all()
print(project_tasks)
