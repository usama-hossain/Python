class AddressHolder:

    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


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
        self.email = email
        self.name = name
        Contact.all_contacts.append(self)


class Supplier(Contact):

    def order(self, msg):
        print(str(msg))


class Friend(Contact):

    # Example of overriding a method.
    # super() returns an instance of the parent class.
    # This way, we don't need to repeat code for getting
    # name and email in our overidden method
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
