__author__ = 'User'
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a


def random_string (prefix, maxlen):
    symbols = string.ascii_letters*3 + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phones (prefix, maxlen):
    symbols = string.ascii_letters + string.digits*15 + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", company="", address="", homephone="", mobilephone="",
                        workphone="", secondaryphone="", email_1="", email_2="", email_3="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            company=random_string("company", 10), address=random_string("address", 30),
            homephone=random_string_for_phones("homephone", 20), mobilephone=random_string_for_phones("mobilephone", 20),
            workphone=random_string_for_phones("workphone", 20), secondaryphone=random_string_for_phones("secondaryphone", 20),
            email_1=random_string("email", 15), email_2=random_string("email", 15) ,email_3=random_string("email", 15))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))