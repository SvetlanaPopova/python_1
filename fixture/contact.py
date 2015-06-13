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
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_first_contact_edit(self):
        self.delete_contact_edit_by_index(0)

    def init_contact_editing_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img").click()

    def delete_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.init_contact_editing_by_index(index)
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
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.init_contact_editing_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    #def get_contact_list(self):
        #if self.contact_cash is None:
            #wd = self.app.wd
            #self.open_home_page()
            #self.contact_cash = []
            #for row in wd.find_elements_by_name("entry"):
                #contact_data = []
                #for column in row.find_elements_by_xpath("//td"):
                    #if len(column.find_elements_by_name("selected[]")) > 0:
                        #contact_data.append(column.find_element_by_name("selected[]").get_attribute("value")) #id
                    #else:
                        #contact_data.append(column.text)
            #self.contact_cash.append(Contact(firstname=contact_data[2], lastname=contact_data[1], id=contact_data[0]))
        #return list(self.contact_cash)


    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cash = []
            IndRow = 2 # row index
            for element in wd.find_elements_by_name("entry"):
                contact_data = []
                for IndClm in range(2,4): # IndClm - column index; 2 - Last name, 3 - First name
                # text:[0] - Last name, [1] - First name
                    contact_data.append(wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(IndRow)+"]/td["+str(IndClm)+"]").text)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                IndRow = IndRow + 1
                self.contact_cash.append(Contact(firstname=contact_data[1], lastname=contact_data[0], id=id))
        return list(self.contact_cash)

    def compare_contact_lists(self, new_contacts, old_contacts):
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def check_add_new_success(self, contact, old_contacts):
        assert len(old_contacts) + 1 == self.count()
        new_contacts = self.get_contact_list()
        old_contacts.append(contact)
        self.compare_contact_lists(new_contacts, old_contacts)

    def check_delete_success(self, index, old_contacts):
        assert len(old_contacts) - 1 == self.count()
        new_contacts = self.get_contact_list()
        old_contacts[index:index + 1] = []
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def check_modify_success(self, contact, index, old_contacts):
        assert len(old_contacts) == self.count()
        new_contacts = self.get_contact_list()
        old_contacts[index].firstname = contact.firstname
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)