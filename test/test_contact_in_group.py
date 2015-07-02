__author__ = 'User'

from model.contact import Contact
from model.group import Group
import random


def get_group_list(app, orm):
    group_list = orm.get_group_list()
    if group_list == []:
        app.group.create(Group(name="Group_Contact"))
        group_list = orm.get_group_list()
    return group_list


def choice_some_group(group_list):
    group = random.choice(group_list)
    group_list_with_same_name = list(filter(lambda x: x.name == group.name, group_list))
    if len(group_list_with_same_name) > 1:
        group = group_list_with_same_name[0]
    return group


def choice_some_contact_not_group(app, group, old_contacts_not_in_group, orm):
    if old_contacts_not_in_group == []:
        app.contact.add_new(Contact(firstname="Contact_Group"))
        old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(old_contacts_not_in_group)
    return contact, old_contacts_not_in_group

def choice_some_contact_in_group(app, group, old_contacts_in_group, old_contacts_not_in_group, orm):
    if old_contacts_in_group == []:
        contact, old_contacts_not_in_group = choice_some_contact_not_group(app, group, old_contacts_not_in_group, orm)
        app.contact.add_in_group(contact, group)
        old_contacts_in_group = orm.get_contacts_in_group(group)
        old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(old_contacts_in_group)
    return contact, old_contacts_in_group, old_contacts_not_in_group

def check_add_or_delete_contact_in_group_success(app, check_ui, group, new_contacts_in_group, new_contacts_not_in_group,
                                       old_contacts_in_group, old_contacts_not_in_group):
    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == \
           sorted(old_contacts_in_group, key=Contact.id_or_max)
    assert sorted(new_contacts_not_in_group, key=Contact.id_or_max) == \
           sorted(old_contacts_not_in_group, key=Contact.id_or_max)
    # check_ui
    if check_ui:
        contacts_from_home_page = app.contact.get_contact_list_filter_group(group)
        db_contacts = list(
            map(lambda contact: Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname,
                                        address=contact.address,
                                        all_phones_from_home_page=app.contact.merge_phones_like_on_home_page(contact),
                                        all_emails_from_home_page=app.contact.merge_emails_like_on_home_page(contact)),
                                        new_contacts_in_group))
        assert sorted(list(map(app.contact.clean, contacts_from_home_page)),
                      key=Contact.id_or_max) == \
               sorted(list(map(app.contact.clean, db_contacts)), key=Contact.id_or_max)


def test_add_some_contact_in_some_group(app, orm, check_ui):
    #choice some group
    group_list = get_group_list(app, orm)
    group = choice_some_group(group_list)
    #get old lists
    old_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    #choice contact and perhaps update old_contacts_not_in_group
    contact, old_contacts_not_in_group = choice_some_contact_not_group(app, group, old_contacts_not_in_group, orm)
    #add contact in group
    app.contact.add_in_group(contact, group)
    #old lists like new lists
    old_contacts_in_group.append(contact)
    old_contacts_not_in_group.remove(contact)
    #new lists
    new_contacts_in_group = orm.get_contacts_in_group(group)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    #compare old lists with new lists
    check_add_or_delete_contact_in_group_success(app, check_ui, group, new_contacts_in_group, new_contacts_not_in_group,
                                       old_contacts_in_group, old_contacts_not_in_group)

def test_delete_some_contact_from_some_group(app, orm, check_ui):
    #choice some group
    group_list = get_group_list(app, orm)
    group = choice_some_group(group_list)
    #get old lists
    old_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    #choice contact and perhaps update old_contacts_not_in_group, old_contacts_not_in_group
    contact, old_contacts_in_group, old_contacts_not_in_group = \
        choice_some_contact_in_group(app, group, old_contacts_in_group, old_contacts_not_in_group, orm)
    #delete contact from group
    app.contact.delete_from_group(contact, group)
    #old lists like new lists
    old_contacts_in_group.remove(contact)
    old_contacts_not_in_group.append(contact)
    #new lists
    new_contacts_in_group = orm.get_contacts_in_group(group)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    #compare old lists with new lists
    check_add_or_delete_contact_in_group_success(app, check_ui, group, new_contacts_in_group, new_contacts_not_in_group,
                                       old_contacts_in_group, old_contacts_not_in_group)