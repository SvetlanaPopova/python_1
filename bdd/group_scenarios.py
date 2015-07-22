__author__ = 'User'

from pytest_bdd import scenario
from .group_stepts import *

@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass

@scenario('groups.feature', 'Delete a group')
def test_delete_some_group():
    pass