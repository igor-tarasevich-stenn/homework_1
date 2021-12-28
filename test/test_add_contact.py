# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_contact(Contact(name="name1", lastname="lastname1", company="test1", home_tel="1231",
                                 email="test1@mail.com", bday="11", bmonth="September", byear="1992"))
    app.session.logout()

