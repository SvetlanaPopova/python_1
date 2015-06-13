__author__ = 'User'

from model.contact import Contact
from random import randrange


def test_modify_some_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="ModifyFirstName")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    app.contact.check_modify_success(contact, index, old_contacts)


#def test_modify_first_contact_fax(app):
    #if app.contact.count() == 0:
        #app.contact.add_new(Contact(firstname="TestContact"))
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(telfax="77777")
    #contact.id = old_contacts[0].id
    #app.contact.modify_first_contact(contact)
    #app.contact.check_modify_success(contact, index, old_contacts)


#def test_modify_first_contact_all(app):
    #if app.contact.count() == 0:
        #app.contact.add_new(Contact(firstname="TestContact"))
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                                           #title="NewTitle", company="NewCompany", address="-", telhome="1234",
                                           #telmobile="4567",
                                           #telwork="7890", telfax="1234567890", homepage="contactnew.homepage")
    #contact.id = old_contacts[0].id
    #app.contact.modify_first_contact(contact)
    #app.contact.check_modify_success(contact, index, old_contacts)