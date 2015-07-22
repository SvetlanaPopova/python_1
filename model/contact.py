__author__ = 'User'
from sys import maxsize
import re


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, fax=None, homepage=None, id=None,
                 all_phones_from_home_page=None, email_1=None, email_2=None, email_3=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.fax = fax
        self.homepage = homepage
        self.id = id
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.company, self.address,
                                               self.homephone, self.mobilephone, self.workphone, self.email_1)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.firstname == other.firstname)\
               and (self.lastname == other.lastname)\
               and (self.address == other.address)\
               #and (self.homephone == other.homephone)\
               #and (self.mobilephone == other.mobilephone)\
               #and (self.workphone == other.workphone)\
               #and (self.secondaryphone == other.secondaryphone)\
               #and (self.all_phones_from_home_page == other.all_phones_from_home_page)\
               #and (self.email_1 == other.email_1)\
               #and (self.email_2 == other.email_2)\
               #and (self.email_3 == other.email_3)\
              # and (self.all_emails_from_home_page == other.all_emails_from_home_page)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize