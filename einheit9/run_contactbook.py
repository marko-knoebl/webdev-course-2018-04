from contactbook import ContactBook

cb1 = ContactBook()

cb1.add_contact()
cb1.add_contact()

print '---'

cb1.find_by_name()
# Ausgabe: John Doe

cb1.remove()
# fragt nach einem index,
# entfernt den entsprechenden Kontakt

print '---'

cb1.list_contacts()