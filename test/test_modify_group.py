__author__ = 'User'

from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="GroupNew"))

def test_modify_group_headr(app):
    app.group.modify_first_group(Group(header="Common_Croup_new"))

