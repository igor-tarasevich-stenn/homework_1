from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(Contact(name="name2", lastname="lastname2", company="test1", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

