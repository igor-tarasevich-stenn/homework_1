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
        return self.id == other.id and self.name == other.name and self.lastname == other.lastname
