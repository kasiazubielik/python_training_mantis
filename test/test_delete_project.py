from model.project import Project
import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects

def test_delete_project_with_soap(app):
    username = "administrator"
    password = "root"
    if len(app.soap.get_projects(username, password)) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.soap.get_projects(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_projects(username, password)
    old_projects.remove(project)
    assert old_projects == new_projects
