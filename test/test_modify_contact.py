__author__ = 'User'

from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="ModifyFirstName")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0].firstname = contact.firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_fax(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(telfax="77777")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0].telfax = contact.telfax
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_all(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                                           title="NewTitle", company="NewCompany", address="-", telhome="1234",
                                           telmobile="4567",
                                           telwork="7890", telfax="1234567890", homepage="contactnew.homepage")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)