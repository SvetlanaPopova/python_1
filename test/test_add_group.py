# -*- coding: utf-8 -*-

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    app.group.check_add_or_modify_success(db, group, old_groups, check_ui)


