__author__ = 'User'
import mysql.connector
from model.group import Group
from model.contact import Contact

class Dbfixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, nickname, title, company, address, "
                           "home, mobile, work, fax, email, email2, email3, homepage, phone2 from addressbook")
            for row in cursor:
                (id, firstname, lastname, nickname, title, company, address, homephone, mobilephone, workphone,
                 fax, email_1, email_2, email_3, homepage, secondaryphone) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, nickname=nickname, title=title,
                                    company=company, address=address, homephone=homephone, mobilephone=mobilephone,
                                    workphone=workphone, fax=fax, email_1=email_1, email_2=email_2, email_3=email_3,
                                    homepage=homepage, secondaryphone=secondaryphone))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()