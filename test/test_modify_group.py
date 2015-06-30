__author__ = 'User'

from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="TestGroupName"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = Group(name="ModifyGroup")
    group.id = old_group.id
    old_groups.remove(old_group)
    app.group.modify_group_by_id(group)
    app.group.check_add_or_modify_success(db, group, old_groups, check_ui)


#def test_modify_group_headr(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="TestGroupHeader"))
    #old_groups = app.group.get_group_list()
    #group = Group(name="Common_Croup_new")
    #group.id = old_groups[0].id
    #app.group.modify_first_group(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)

