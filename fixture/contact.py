__author__ = 'User'
from model.contact import Contact


class ContactHelper:
    
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_id("maintable"))>0):
            wd.find_element_by_link_text("home").click()

    def add_new(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
         # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cash = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_first_contact_edit(self):
        wd = self.app.wd
        self.open_home_page()
        # init contact editing
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cash = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname",contact.lastname)
        self.change_field_value("nickname",contact.nickname)
        self.change_field_value("title",contact.title)
        self.change_field_value("company",contact.company)
        self.change_field_value("address",contact.address)
        self.change_field_value("home",contact.telhome)
        self.change_field_value("mobile",contact.telmobile)
        self.change_field_value("work",contact.telwork)
        self.change_field_value("fax",contact.telfax)
        self.change_field_value("homepage",contact.homepage)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # init contact editing
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cash = []
            IndRow = 2 # row index
            for element in wd.find_elements_by_name("entry"):
                text = []
                for IndClm in range(2,4): # IndClm - column index; 2 - Last name, 3 - First name
                    # text:[0] - Last name, [1] - First name
                    text.append(wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(IndRow)+"]/td["+str(IndClm)+"]").text)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cash.append(Contact(firstname=text[1], lastname=text[0], id=id))
                IndRow = IndRow + 1
        return list(self.contact_cash)