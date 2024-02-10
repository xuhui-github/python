class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(
        self, name="", email="", street="", city="", state="", code="", **kwargs
    ):
        Contact.__init__(self, name, email, **kwargs)
        AddressHolder.__init__(self, street, city, state, code, **kwargs)


if __name__ == "__main__":
    f = Friend("unknown", "unknow", "unknown", "unknown", "unknown", "unknown")
    print(f.all_contacts)
    c = Contact("", "")
    a = AddressHolder()
    print(f.all_contacts)
    print(c.all_contacts)
