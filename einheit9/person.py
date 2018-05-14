# definiere eine Person-Klasse
class Person():

    # Initialisiere die Klasse mit Daten
    def __init__(self, first_name, last_name, year_of_birth):
        # speichere die uebergebenen parameter ab
        # (self ist das aktuelle Objekt - also das Objekt, das
        # gerade initialisiert wird)
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def get_age(self):
        age = 2018 - self.year_of_birth
        return age

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name