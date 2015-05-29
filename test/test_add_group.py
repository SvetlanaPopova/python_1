# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="GroupTop", header="Common_Croup", footer="for all"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
