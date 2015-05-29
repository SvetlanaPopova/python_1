# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new(Contact(firstname="ContactName", lastname="ContactLastName", nickname="Contact1",
                        title="ContactTitle", company="NewCompany", address="Moscow", telhome="123", telmobile="456",
                        telwork="789", telfax="123456789", homepage="contact.homepage"))


def test_add_empty_contact(app):
    app.contact.add_new(Contact(firstname="", lastname="", nickname="",
                        title="", company="", address="", telhome="", telmobile="",
                        telwork="", telfax="", homepage=""))
