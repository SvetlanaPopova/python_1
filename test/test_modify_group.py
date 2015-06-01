__author__ = 'User'

from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="TestGroupName"))
    app.group.modify_first_group(Group(name="GroupNew"))

def test_modify_group_headr(app):
    if app.group.count() == 0:
        app.group.create(Group(name="TestGroupHeader"))
    app.group.modify_first_group(Group(header="Common_Croup_new"))

