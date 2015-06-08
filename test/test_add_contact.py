# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="ContactName", lastname="ContactLastName", nickname="Contact1",
                        title="ContactTitle", company="NewCompany", address="Moscow", telhome="123", telmobile="456",
                        telwork="789", telfax="123456789", homepage="contact.homepage")
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)


#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="", lastname="", nickname="",
                        #title="", company="", address="", telhome="", telmobile="",
                        #telwork="", telfax="", homepage="")
    #app.contact.add_new(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)
