from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(name="name1", lastname="lastname12", company="test1", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(name="test_edit1", bday="11", bmonth="September"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(name="name1", lastname="lastname12", company="test1", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname="test_edit1", bday="11", bmonth="September"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

