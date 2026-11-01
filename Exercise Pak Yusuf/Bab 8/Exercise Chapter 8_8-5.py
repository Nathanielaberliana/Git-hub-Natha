def describe_city(city, country='indonesia'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city('surakarta')
describe_city('yogyakarta')
describe_city('kyoto', 'japan')
