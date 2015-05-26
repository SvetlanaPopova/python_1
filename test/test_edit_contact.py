__author__ = 'User'
from model.contact import Contact


def test_edit_first_contact_top_button_update(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                                           title="NewTitle", company="NewCompany", address="-", telhome="1234",
                                           telmobile="4567",
                                           telwork="7890", telfax="1234567890", homepage="contactnew.homepage"),
                                   locator_button_update="//*[@id='content']/form[1]/input[1]")
    app.session.logout()


def test_edit_first_contact_bottom_button_update(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                                           title="NewTitle", company="NewCompany", address="-", telhome="1234",
                                           telmobile="4567",
                                           telwork="7890", telfax="1234567890", homepage="contactnew.homepage"),
                                   locator_button_update="//*[@value='Update'][2]")
    app.session.logout()