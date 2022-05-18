# Function accepts city and country as arguments.
#   Country is specified by default to 'Italy'
def describe_city(city, country='Italy'):
    print(f"{city.title()} is in {country.title()}.")


# Call twice the function with default country value.
describe_city('Florence')
describe_city('Rome')
# Call the function using different country value.
describe_city('Paris', 'France')
