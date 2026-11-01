favorite_places = {
    'natha': ['Bali', 'Yogyakarta'],
    'kayla': ['Raja Ampat', 'Bandung', 'Lombok'],
    'nayla': ['Surakarta'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"\t{place}")