from sys import maxsize


class Contact:

    def __init__(self, name=None, lastname=None, company=None, home_tel=None,
                 email=None, bday=None, bmonth=None, byear=None, id=None):
        self.name = name
        self.lastname = lastname
        self.company = company
        self.home_tel = home_tel
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.name is None or other.name is None or self.name == other.name) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
