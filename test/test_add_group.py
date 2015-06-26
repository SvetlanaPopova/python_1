# -*- coding: utf-8 -*-

def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    app.group.check_add_group_success(group, old_groups)


