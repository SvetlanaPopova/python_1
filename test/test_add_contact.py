# -*- coding: utf-8 -*-


def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    app.contact.check_add_new_success(contact, old_contacts)

