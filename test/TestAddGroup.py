# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_TestAddGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group1", header="Common_Croup", footer="for all"))
    app.session.logout()


def test_TestAddEmptyGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
