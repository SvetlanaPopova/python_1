# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_TestAddGroup(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Group1", header="Common_Croup", footer="for all"))
    app.logout()


def test_TestAddEmptyGroup(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
