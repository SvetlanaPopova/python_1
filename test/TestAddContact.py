# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_TestAddContact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="ContactName", lastname="ContactLastName", nickname="Contact1",
                        title="ContactTitle", company="NewCompany", address="Moscow", telhome="123", telmobile="456",
                        telwork="789", telfax="123456789", homepage="contact.homepage"))
    app.logout()


def test_TestAddEmptyContact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="", lastname="", nickname="",
                        title="", company="", address="", telhome="", telmobile="",
                        telwork="", telfax="", homepage=""))
    app.logout()
