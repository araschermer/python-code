import psycopg2
import os

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

password = os.environ.get('PASSWORD')
print(password)


def create_database(database_name):
    # establish connection
    connection = psycopg2.connect(user="postgres",
                                  host="localhost",
                                  password=password,
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    # Creating a database
    cursor.execute(f'''CREATE database {database_name};''')


engine = create_engine(f'postgres://postgres:{password}@localhost:5432/project_tracker')

Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))

    def __repr__(self):
        return f"<Project(project_id='{self.project_id}', title='{self.title}')>"


class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))
    project = relationship("Project")

    def __repr__(self):
        return f"<Task(description='{self.description}')>"


Base.metadata.create_all(engine)


def create_session():
    session = sessionmaker(bind=engine)
    return session()


if __name__ == "__main__":
    # create_database("project_tracker")
    session = create_session()
    new_project = Project(title="New Project3")
    session.add(new_project)
    session.commit()
    task = Task(description="New Task3", project_id=new_project.project_id)
    session.add(task)
    session.commit()
