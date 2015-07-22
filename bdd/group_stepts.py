__author__ = 'User'

from pytest_bdd import given, when, then
from model.group import Group
import random


@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>')
def new_group(app, name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group, app, check_ui):
    app.group.check_add_or_modify_success(db, new_group, group_list, check_ui)
    

@given ('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_group_list()) < 0:
      app.group.create(Group(name='some name'))
    return db.get_group_list()

@given ('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when ('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then ('the new group list is equal to the old list without the added group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    app.group.check_delete_success(db, random_group, non_empty_group_list, check_ui)
