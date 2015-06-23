# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string (prefix, maxlen):
    symbols = string.ascii_letters*3 + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phones (prefix, maxlen):
    symbols = string.ascii_letters + string.digits*15 + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", company="", address="", homephone="", mobilephone="",
                        workphone="", email_1="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            company=random_string("company", 10), address=random_string("address", 30),
            homephone=random_string_for_phones("homephone", 20), mobilephone=random_string_for_phones("mobilephone", 20),
            workphone=random_string_for_phones("workphone", 20), email_1=random_string("email", 15))
    for i in range(5)
]


@pytest.mark.parametrize ("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    app.contact.check_add_new_success(contact, old_contacts)


#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="", lastname="", nickname="",
                        #title="", company="", address="", homephone="", mobilephone="",
                        #workphone="", fax="", homepage="")
    #app.contact.add_new(contact)
    #app.contact.check_add_new_success(contact, old_contacts)
