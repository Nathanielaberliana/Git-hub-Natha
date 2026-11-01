favorite_numbers = {
    'natha': [7, 21],
    'kayla': [12, 3, 9],
    'nayla': [3],
    'renai': [21, 8],
    'rara': [8, 34, 44],
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(f"\t{number}")