__author__ = 'User'

from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <lastname>, <address> and <mobilephone>')
def new_contact(firstname, lastname, address, mobilephone):
    return Contact(firstname=firstname, lastname=lastname, address=address, mobilephone=mobilephone)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.add_new(new_contact)

@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, new_contact, app, check_ui):
    app.contact.check_add_new_success(db, new_contact, contact_list, check_ui)

@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) < 0:
        app.group.create(Contact(firstname='some firstname'))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old contact list without the contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    app.contact.check_delete_success(db, random_contact, non_empty_contact_list, check_ui)

@when('I modify the contact from the list')
def modify_contact(app, new_contact, random_contact):
    new_contact.id = random_contact.id
    app.contact.modify_contact_by_id(new_contact)

@then('the new contact list is equal to the old contact list with the modified contact')
def verify_contact_deleted(db, non_empty_contact_list, new_contact, random_contact ,app, check_ui):
    non_empty_contact_list.remove(random_contact)
    random_contact.firstname = new_contact.firstname
    random_contact.lastname = new_contact.lastname
    random_contact.address = new_contact.address
    random_contact.mobilephone =new_contact.mobilephone
    non_empty_contact_list.append(random_contact)
    app.contact.check_modify_contact_success(db, non_empty_contact_list, check_ui)
