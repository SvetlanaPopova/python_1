__author__ = 'User'
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    app.contact.delete_first_contact()

def test_delete_first_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    app.contact.delete_first_contact_edit()