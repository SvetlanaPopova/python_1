# -*- coding: utf-8 -*-


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    app.contact.check_add_new_success(contact, old_contacts)

