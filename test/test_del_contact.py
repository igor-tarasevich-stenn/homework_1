from random import randrange

from model.contact import Contact


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(name="name1", lastname="lastname12", company="test1", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

