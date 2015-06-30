__author__ = 'User'
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name="TestGroup"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    app.group.check_delete_success(db, group, old_groups, check_ui)
