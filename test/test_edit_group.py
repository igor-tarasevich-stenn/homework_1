from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="zxczxc", header="zxczxc", footer="zxczxc"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

