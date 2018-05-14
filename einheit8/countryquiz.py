import random

from askyesno import ask_yes_or_no_question


def main():
    countries = ['Slovenia', 'Croatia', 'Austria']
    country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna"}

    while True:
        selected_country = random.choice(countries)

        guess = raw_input("What is the capital of %s? " % selected_country)

        check_guess(guess, selected_country, country_capital_dict)

        again = ask_yes_or_no_question("Would you like to continue this game? (yes/no) ")
        if again == False:
            break

    print "END"
    print "_________________________"


def check_guess(user_guess, country, cc_dict):
    capital = cc_dict[country]

    if user_guess == cc_dict[country]:
        print "Correct! The capital of %s is indeed %s." % (country, capital)
        return True
    else:
        print "Sorry, you are wrong. The capital of %s is %s." % (country, capital)
        return False

if __name__ == "__main__":
    # Erkenne, ob diese Datei direkt ausgefuehrt wurde
    # oder ob sie importiert wurde
    main()