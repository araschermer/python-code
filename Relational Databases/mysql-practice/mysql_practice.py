import mysql.connector as mysql
import os

from mysql.connector import Error

ROOT_PASSWORD = os.environ.get('ROOT_PASSWORD')


def connect(db_name=""):
    try:
        if db_name != "":
            return mysql.connect(
                host="127.0.0.1",
                port="3306",
                user="root",
                password=ROOT_PASSWORD
                , auth_plugin='mysql_native_password',
                database=db_name)
        else:
            return mysql.connect(
                host="127.0.0.1",
                port="3306",
                user="root",
                password=ROOT_PASSWORD
                , auth_plugin='mysql_native_password')
    except Error as e:
        print(e)


def add_new_project(cursor, project_title, project_description, task_descriptions):
    # insert project's data into database
    cursor.execute('''INSERT INTO projects( title, description) VALUES(%s,%s)''', (project_title, project_description))
    # Get the id of the recently added project
    project_id = cursor.lastrowid
    # define task data assigned too the project id
    task_data = [(project_id, task_description) for task_description in task_descriptions]  # task data
    # insert task data into the database
    cursor.executemany('''INSERT INTO tasks(  project_id,description) VALUES(%s,%s)''', task_data)


if __name__ == '__main__':
    # connect to the projects db
    projects_db = connect("projects")
    # create a cursor  for the projects_db
    cursor = projects_db.cursor()
    # insert data into the database using add_new_project method
    task_descriptions = ["learn Mysql", "learn POSTGRESQL", "learn SQLite"]
    project_title, project_description = project_data = ("learn RDBMS", "Study Mysql, POSTGRESQL, SQLite")
    # add_new_project(cursor=cursor, project_title=project_title,
    #                 project_description=project_description, task_descriptions=task_descriptions)

    # commit changes
    projects_db.commit()
    # view the db content
    cursor.execute("SELECT * FROM projects")
    projects_records = cursor.fetchall()
    print(projects_records)
    # close the db
    projects_db.close()
