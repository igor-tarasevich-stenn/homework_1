# -*- coding: utf-8 -*-
import pytest
from group import Group
from application_group import ApplicationGroup


@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_hw_1_add_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.logout()
