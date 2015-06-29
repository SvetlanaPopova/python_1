__author__ = 'User'


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    app.group.compare_group_lists(ui_list, db_list)