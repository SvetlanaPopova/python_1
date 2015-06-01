__author__ = 'User'

from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="GroupNew"))

def test_modify__first_contact_fax(app):
    app.contact.modify_first_contact(Contact(telfax="77777"))

def test_modify_first_contact_all(app):
    app.contact.modify_first_contact(Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                                           title="NewTitle", company="NewCompany", address="-", telhome="1234",
                                           telmobile="4567",
                                           telwork="7890", telfax="1234567890", homepage="contactnew.homepage"))