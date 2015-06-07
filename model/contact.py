__author__ = 'User'
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 telhome=None, telmobile=None, telwork=None, telfax=None, homepage=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.telhome = telhome
        self.telmobile = telmobile
        self.telwork = telwork
        self.telfax = telfax
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.firstname == other.firstname)\
               and (self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize