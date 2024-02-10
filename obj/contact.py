class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class MailSender:
    pass


class EmailableContact(Contact, MailSender):
    pass


if __name__ == "__main__":
    c1 = Contact("John A", "johna@example.net")
    c2 = Contact("John B", "johnb@example.net")
    c3 = Contact("Jenna C", "jenna@example.net")
    print([c.name for c in Contact.all_contacts.search("John")])
