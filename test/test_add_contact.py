# -*- coding: utf-8 -*-


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new(contact)
    app.contact.check_add_new_success(db, contact, old_contacts)

