pets = []

pet = {
    'animal type': 'kucing',
    'name': 'cebret',
    'owner': 'natha',
    'weight': 6,
    'eats': 'wetfood',
}
pets.append(pet)

pet = {
    'animal type': 'sugar glider',
    'name': 'gula',
    'owner': 'Kayla',
    'weight': 1,
    'eats': 'kacang'
}
pets.append(pet)

for pet in pets:
    print(f"\nBerikut adalah apa yang saya ketahui tentang {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")