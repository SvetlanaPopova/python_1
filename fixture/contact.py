__author__ = 'User'
from model.contact import Contact
import re






class ContactHelper:
    
    def __init__(self, app):
        self.app = app

    def clean(self, contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(),
                   lastname=contact.lastname.strip(), address=contact.address.strip(),
                   all_phones_from_home_page=contact.all_phones_from_home_page,
                   all_emails_from_home_page=contact.all_emails_from_home_page)

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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_first_contact_edit(self):
        self.delete_contact_edit_by_index(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        for row in wd.find_elements_by_name("entry"):
            if row.find_elements_by_tag_name("td")[0].find_element_by_tag_name("input").get_attribute("value") == id:
                row.find_elements_by_tag_name("td")[7].find_element_by_tag_name("a").click()
                break

    #def open_contact_view_by_index(self, id):
        #wd = self.app.wd
        #self.open_home_page()
        #for row in wd.find_elements_by_name("entry"):
            #if row.find_elements_by_tag_name("td")[0].find_element_by_tag_name("input").get_attribute("value") == id:
                #row.find_elements_by_tag_name("td")[6].find_element_by_tag_name("a").click()

    def delete_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cash = None

    def delete_contact_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
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
        self.change_field_value("email",contact.email_1)
        self.change_field_value("email2",contact.email_2)
        self.change_field_value("email3",contact.email_3)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def modify_contact_by_id(self, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(contact.id)
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        #self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        wd = self.app.wd
        if self.contact_cash is None:
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cash.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cash)

    def get_contact_list_all(self):
        wd = self.app.wd
        #self.open_home_page()
        self.contacts_filter_by_all()
        return self.get_contact_list()

    def contacts_filter_by_group(self, name):
        wd = self.app.wd
        self.open_home_page()
        field = wd.find_element_by_name("group")
        field.click()
        for element in field.find_elements_by_tag_name("option"):
            if element.text == name:
                element.click()
                break

    def contacts_filter_by_all(self):
        wd = self.app.wd
        self.contacts_filter_by_group(name="[all]")

    def get_contact_list_filter_group(self, group):
        wd = self.app.wd
        self.contacts_filter_by_group(group.name)
        return self.get_contact_list()

    def clear(self, s):
        return re.sub("[() -]","",s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                            map(lambda s: self.clear(s),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email_1, contact.email_2, contact.email_3])))


    def compare_contact_lists(self, new_contacts, old_contacts, check_ui):
        wd = self.app.wd
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            db_contacts = list(map(lambda contact: Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname,
                                        address=contact.address,
                                        all_phones_from_home_page=self.merge_phones_like_on_home_page(contact),
                                        homephone=None, workphone=None, mobilephone=None, secondaryphone=None,
                                        all_emails_from_home_page=self.merge_emails_like_on_home_page(contact),
                                        email_1=None, email_2=None, email_3=None), new_contacts))
            assert sorted(list(map(self.clean, self.get_contact_list_all())), key=Contact.id_or_max) == \
               sorted(list(map(self.clean, db_contacts)), key=Contact.id_or_max)

    def check_add_new_success(self, db, contact, old_contacts, check_ui):
        wd = self.app.wd
        self.open_home_page()
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        self.compare_contact_lists(new_contacts, old_contacts, check_ui)

    def check_modify_contact_success(self, db, old_contacts, check_ui):
        wd = self.app.wd
        self.open_home_page()
        new_contacts = db.get_contact_list()
        self.compare_contact_lists(new_contacts, old_contacts, check_ui)

    def check_delete_success(self, db, contact, old_contacts, check_ui):
        wd = self.app.wd
        self.open_home_page()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        self.compare_contact_lists(new_contacts, old_contacts, check_ui)

    def add_in_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact.id)
        field = wd.find_element_by_name("to_group")
        field.click()
        for element in field.find_elements_by_tag_name("option"):
            if element.text == group.name:
                element.click()
                break
        wd.find_element_by_name("add").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        #self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workhome = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workhome,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, address=address,
                       email_1=email_1, email_2=email_2, email_3=email_3)

    def get_contact_info_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)