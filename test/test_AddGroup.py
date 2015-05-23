# -*- coding: utf-8 -*-
from model.group import Group


def test_TestAddGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group1", header="Common_Croup", footer="for all"))
    app.session.logout()


def test_TestAddEmptyGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
