__author__ = 'User'
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="NewName", lastname="NewLastName", nickname="NewContact1",
                        title="NewTitle", company="NewCompany", address="-", telhome="1234", telmobile="4567",
                        telwork="7890", telfax="1234567890", homepage="contactnew.homepage"))
    app.session.logout()