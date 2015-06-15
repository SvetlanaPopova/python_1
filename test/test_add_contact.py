# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    #wd = app.wd
    old_contacts = app.contact.get_contact_list()
    #wd.find_element_by_link_text("add new").click()
    contact = Contact(firstname="ContactName", lastname="ContactLastName", nickname="Contact1",
                        title="ContactTitle", company="NewCompany", address="Moscow", homephone="123", mobilephone="456",
                        workphone="789", fax="123456789", homepage="contact.homepage", secondaryphone="secondary123")
    app.contact.add_new(contact)
    app.contact.check_add_new_success(contact, old_contacts)
    #assert len(old_contacts) + 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="", lastname="", nickname="",
                        #title="", company="", address="", homephone="", mobilephone="",
                        #workphone="", fax="", homepage="")
    #app.contact.add_new(contact)
    #app.contact.check_add_new_success(contact, old_contacts)
