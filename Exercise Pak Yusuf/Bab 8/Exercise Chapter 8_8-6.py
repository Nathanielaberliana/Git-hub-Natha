def city_country(city, country):
    return f"{city.title()}, {country.title()}"

location = city_country('santiago', 'chili')
print(location)

location = city_country('jakarta', 'indonesia')
print(location)

location = city_country('kyoto', 'jepang')
print(location)