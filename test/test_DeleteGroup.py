__author__ = 'User'


def test_TestDeleteFirstGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
