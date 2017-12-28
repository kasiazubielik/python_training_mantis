from model.project import Project


def test_add_project(app, db):
    project = Project(name="name3", description="description3")
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    if project.name != "" and project.name not in [x.name for x in old_projects]:
        old_projects.append(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
