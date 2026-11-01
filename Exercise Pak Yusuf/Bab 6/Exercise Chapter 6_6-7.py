people = []
person = {
    'first_name': 'Nathaniela',
    'last_name': 'Berliana',
    'age': 18,
    'city': 'Surakarta',
    }
people.append(person)

person = {
    'first_name': 'Kayla',
    'last_name': 'Hani',
    'age': 18,
    'city': 'Semarang',
    }
people.append(person)

person = {
    'first_name': 'Nayla',
    'last_name': 'Azka',
    'age': 18,
    'city': 'Surakarta',
    }
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")