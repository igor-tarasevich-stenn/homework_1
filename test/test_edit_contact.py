from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(name="test_edit", lastname="test_edit", company="test_edit", home_tel="1231",
                            email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    app.session.logout()
