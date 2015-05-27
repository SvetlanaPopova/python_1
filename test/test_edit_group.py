__author__ = 'User'
from model.group import Group


def test_edit_first_group_top_button_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="GroupNew", header="Common_Croup_new", footer="aaaaa"), locator_button_edit="//*[@id='content']//*[@name='edit'][1]")
    app.session.logout()

def test_edit_first_group_bottom_button_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="GroupNew", header="Common_Croup_new", footer="aaaaa"), locator_button_edit="//*[@id='content']//*[@name='edit'][2]")
    app.session.logout()