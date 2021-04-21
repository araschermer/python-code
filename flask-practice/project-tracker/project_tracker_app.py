from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for
import os

from sqlalchemy import String, Integer, ForeignKey

# get the stored  password for the postgresql database from the environment variables
password = os.environ.get('PASSWORD')

# get the stored flask application secret key from the environment variables, which is set to use flask-wtforms
secret_key = os.environ.get("SECRET_KEY")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://postgres:{password}@localhost:5432/project_tracker'
app.config['SECRET_KEY'] = secret_key

# create database object
project_tracker_db = SQLAlchemy(app)


# create an orm for the projects and tasks tables
class Project(project_tracker_db.Model):
    __tablename__ = 'projects'

    project_id = project_tracker_db.Column(project_tracker_db.Integer, primary_key=True)
    title = project_tracker_db.Column(project_tracker_db.String(length=50))
    task = project_tracker_db.relationship("Task", cascade="all, delete-orphan")


class Task(project_tracker_db.Model):
    __tablename__ = 'tasks'

    task_id = project_tracker_db.Column(project_tracker_db.Integer, primary_key=True)
    project_id = project_tracker_db.Column(project_tracker_db.Integer,
                                           project_tracker_db.ForeignKey('projects.project_id'))
    description = project_tracker_db.Column(project_tracker_db.String(length=50))

    project = project_tracker_db.relationship("Project", backref="project")


@app.route("/")
def show_projects():
    """Shows the stored projects in the database"""
    # Project.query.all() to retrieve all projects from the DB
    return render_template("index.html", projects=Project.query.all())


@app.route("/project/<project_id>")
def show_task(project_id):
    """shows the tasks of a project that are stored in the database, given the project_id"""
    return render_template("project_tasks.html", project=Project.query.filter_by(project_id=project_id).first(),
                           tasks=Task.query.filter_by(project_id=project_id).all())


@app.route("/add/project", methods=["POST"])
def add_project():
    """adds a new project to the database"""
    # if title of new project is empty
    if not request.form['project-title']:
        flash("Enter a title for the project", "red")
    else:
        project = Project(title=request.form['project-title'])
        project_tracker_db.session.add(project)
        project_tracker_db.session.commit()
        flash("Project added successfully", "green")
    return redirect(url_for('show_projects'))


@app.route("/add/task/<project_id>", methods=["POST"])
def add_task(project_id):
    """add a new task to a project given the project id"""
    # task description is empty
    if not request.form['task-description']:
        flash("Enter a task description for the new task", "red")
    else:
        task = Task(description=request.form['task-description'], project_id=project_id)
        project_tracker_db.session.add(task)
        project_tracker_db.session.commit()
        flash("Task added successfully.", "green")
    return redirect(url_for("show_task", project_id=project_id))


# if a user deletes a task, remove it form the database
# if a user deletes a project without tasks, remove the project form the database
# if a user deletes a project that still contains tasks, remove the project and all its tasks form the database
@app.route("/delete/task/<task_id>", methods=['POST'])
def delete_task(task_id):
    """deletes a task from a project and removes it from the database"""
    task_to_delete = Task.query.filter_by(task_id=task_id).first()
    project_id = task_to_delete.project.project_id
    project_tracker_db.session.delete(task_to_delete)
    project_tracker_db.session.commit()
    return redirect(url_for('show_task', project_id=project_id))


@app.route("/delete/project/<project_id>", methods=['POST'])
def delete_project(project_id):
    """deletes a project from the database"""
    project_to_delete = Project.query.filter_by(project_id=project_id).first()
    project_tracker_db.session.delete(project_to_delete)
    project_tracker_db.session.commit()
    return redirect(url_for('show_projects', project_id=project_id))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=3000)
