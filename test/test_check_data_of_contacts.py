__author__ = 'User'

from model.contact import Contact
from random import randrange



def test_check_data_of_some_contact_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list_all()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_check_data_of_all_contacts_on_home_page(app, db):
    db_contacts = db.get_contact_list()
    home_page_contacts = app.contact.get_contact_list_all()
    db_contacts_like_on_home_page = list(map(lambda contact: Contact(id=contact.id, firstname=contact.firstname,
                                        lastname=contact.lastname, address=contact.address,
                                        all_phones_from_home_page=app.contact.merge_phones_like_on_home_page(contact),
                                        all_emails_from_home_page=app.contact.merge_emails_like_on_home_page(contact)),
                                             db_contacts))
    assert sorted(list(map(app.contact.clean, home_page_contacts)), key=Contact.id_or_max) == \
               sorted(list(map(app.contact.clean, db_contacts_like_on_home_page)), key=Contact.id_or_max)
