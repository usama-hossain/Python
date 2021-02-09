class ContactList(list):

    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)

        return matching_contacts


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.email = email
        self.name = name
        Contact.all_contacts.append(self)


class Supplier(Contact):

    def order(self, msg):
        print(str(msg))
