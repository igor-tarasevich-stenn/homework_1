from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(name="name1", lastname="lastname12", company="test1", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    app.contact.edit_first_contact(Contact(name="test_edit", lastname="test_edit", company="test_edit", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
