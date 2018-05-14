# teste die Funktion check_guess:
from countryquiz import check_guess

country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna"}

assert check_guess('Vienna', 'Austria', country_capital_dict) == True

assert check_guess('Viena', 'Austria', country_capital_dict) == False

print 'All tests passed successfully'