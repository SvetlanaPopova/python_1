__author__ = 'User'


def test_delete_first_group_top_button_delete(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group(locator_button_delete="//*[@id='content']//*[@name='delete'][1]")
    app.session.logout()

def test_delete_first_group_bottom_button_delete(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group(locator_button_delete="//*[@id='content']//*[@name='delete'][2]")
    app.session.logout()
