from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.session.logout()
