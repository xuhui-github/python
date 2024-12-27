class Person(object):
    """"""

    def __init__(self, firstname, lastname):
        """Constructor"""
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        """
        Return the full name
        """
        return "%s %s" % (self.firstname, self.lastname)


if __name__ == "__main__":
    person = Person("Mike", "Driscoll")
    print(person.full_name)
    print(person.firstname)
    print(person.lastname)

    """person.full_name = 'Jackalope'"""

    person.firstname = "Dan"
    print(person.full_name)
