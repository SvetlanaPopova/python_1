__author__ = 'User'
from model.group import Group


def clean(group):
    return Group(id=group.id, name=group.name.strip())


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name",group.name)
        self.change_field_value("group_header",group.header)
        self.change_field_value("group_footer",group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_xpath("//*[@id='content']//*[@name='new'][1]").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//*[@id='content']//*[@name='delete'][1]").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//*[@id='content']//*[@name='delete'][1]").click()
        self.return_to_groups_page()
        self.group_cash = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification group
        wd.find_element_by_xpath("//*[@id='content']//*[@name='edit'][1]").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cash = None

    def modify_group_by_id(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group.id)
        # open modification group
        wd.find_element_by_xpath("//*[@id='content']//*[@name='edit'][1]").click()
        # fill group form
        self.fill_group_form(group)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cash = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cash = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cash.append(Group(name=text, id=id))
        return list(self.group_cash)

    def check_add_or_modify_success(self, db, group, old_groups, check_ui):
        new_groups = db.get_group_list()
        old_groups.append(group)
        self.compare_group_lists(new_groups, old_groups, check_ui)

    def check_delete_success(self, db, group, old_groups, check_ui):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        self.compare_group_lists(new_groups, old_groups, check_ui)

    def compare_group_lists(self, new_groups, old_groups, check_ui):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == \
                   sorted(list(map(clean, self.get_group_list())), key=Group.id_or_max)
