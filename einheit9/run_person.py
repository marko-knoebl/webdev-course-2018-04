from person import Person

marko = Person('Marko', 'Knoebl', 1988)
john = Person(year_of_birth=2000, first_name='John',
              last_name='Doe')

print marko.first_name
print john.year_of_birth

print john.get_age()

print john.get_full_name()

# ohne Klassen
jane = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'year_of_birth': 1996
}

print jane['last_name']
