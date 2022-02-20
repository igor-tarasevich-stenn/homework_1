from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.group.edit_first_group(Group(name="zxczxc", header="zxczxc", footer="zxczxc"))
