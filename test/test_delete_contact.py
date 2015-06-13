__author__ = 'User'
from model.contact import Contact
from random import randrange



def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.contact.check_delete_success(index, old_contacts)


def test_delete_some_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_edit_by_index(index)
    app.contact.check_delete_success(index, old_contacts)
