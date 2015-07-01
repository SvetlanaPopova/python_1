__author__ = 'User'
from model.contact import Contact
import random



def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.contact.check_delete_success(db, contact, old_contacts, check_ui)



def test_delete_some_contact_edit(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TestContact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_edit_by_id(contact.id)
    app.contact.check_delete_success(db, contact, old_contacts, check_ui)
