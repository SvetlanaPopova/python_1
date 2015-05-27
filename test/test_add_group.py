# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_top_button_new(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="GroupTop", header="Common_Croup", footer="for all"), locator_button_new="//*[@id='content']//*[@name='new'][1]")
    app.session.logout()


def test_add_group_bottom_button_new(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="GroupBottom", header="Common_Croup", footer="for all"), locator_button_new="//*[@id='content']//*[@name='new'][2]")
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""), locator_button_new="//*[@id='content']//*[@name='new'][1]")
    app.session.logout()
