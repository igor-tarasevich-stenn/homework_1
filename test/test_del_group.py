

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.group.delete_first_group()
