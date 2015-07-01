__author__ = 'User'

from model.contact import Contact
import random


def test_modify_some_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(firstname="ModifyFirstName")
    contact.id = old_contact.id
    old_contacts.remove(old_contact)
    old_contact.firstname = contact.firstname
    old_contacts.append(old_contact)
    app.contact.modify_contact_by_id(contact)
    app.contact.check_modify_contact_success(db, old_contacts, check_ui)


#def test_modify_first_contact_fax(app):
    #if app.contact.count() == 0:
        #app.contact.add_new(Contact(firstname="TestContact"))
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(fax="77777")
    #contact.id = old_contacts[0].id
    #app.contact.modify_first_contact(contact)
    #app.contact.check_modify_success(contact, index, old_contacts)


#def test_modify_first_contact_all(app):
    #if app.contact.count() == 0:
        #app.contact.add_new(Contact(firstname="TestContact"))
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                                           #title="NewTitle", company="NewCompany", address="-", homephone="1234",
                                           #mobilephone="4567",
                                           #workphone="7890", fax="1234567890", homepage="contactnew.homepage")
    #contact.id = old_contacts[0].id
    #app.contact.modify_first_contact(contact)
    #app.contact.check_modify_success(contact, index, old_contacts)