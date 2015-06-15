__author__ = 'User'
from model.contact import Contact


class ContactHelper:
    
    def __init__(self, app):
        self.app = app

    #def open_home_page(self):
        #wd = self.app.wd
        #if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_id("maintable"))>0):
            #wd.find_element_by_link_text("home").click()

    def add_new(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
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
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_first_contact_edit(self):
        self.delete_contact_edit_by_index(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def delete_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
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
        self.change_field_value("home",contact.homephone)
        self.change_field_value("mobile",contact.mobilephone)
        self.change_field_value("work",contact.workphone)
        self.change_field_value("fax",contact.fax)
        self.change_field_value("homepage",contact.homepage)
        self.change_field_value("phone2",contact.secondaryphone)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2]
                lastname = cells[1]
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                if len(all_phones) < 4:
                    for i in range(0,4):
                        if len(all_phones) < i+1:
                            all_phones.append('')
                self.contact_cash.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                 homephone=all_phones[0], mobilephone=all_phones[1],
                                                 workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cash)

    def compare_contact_lists(self, new_contacts, old_contacts):
        wd = self.app.wd
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def check_add_new_success(self, contact, old_contacts):
        wd = self.app.wd
        assert len(old_contacts) + 1 == self.count()
        new_contacts = self.get_contact_list()
        old_contacts.append(contact)
        self.compare_contact_lists(new_contacts, old_contacts)

    def check_delete_success(self, index, old_contacts):
        wd = self.app.wd
        assert len(old_contacts) - 1 == self.count()
        new_contacts = self.get_contact_list()
        old_contacts[index:index + 1] = []
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def check_modify_success(self, contact, index, old_contacts):
        wd = self.app.wd
        assert len(old_contacts) == self.count()
        new_contacts = self.get_contact_list()
        old_contacts[index].firstname = contact.firstname
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname ").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workhome = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workhome,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)