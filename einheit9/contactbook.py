from person import Person

class ContactBook():
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        first_name = raw_input('Enter the first name: ')
        last_name = raw_input('Enter the last name: ')
        year_of_birth = int(raw_input('Enter the year of birth: '))

        new_contact = Person(first_name, last_name,
                             year_of_birth)
        self.contacts.append(new_contact)

    def list_contacts(self):
        for contact in self.contacts:
            print contact.get_full_name()

    def find_by_name(self):
        name = raw_input('enter search text to find contact: ')
        for contact in self.contacts:
            if name == contact.first_name:
                print contact.get_full_name(), contact.get_age()

    def remove(self):
        index = int(raw_input('enter the index you want to remove: '))
        self.contacts.pop(index)