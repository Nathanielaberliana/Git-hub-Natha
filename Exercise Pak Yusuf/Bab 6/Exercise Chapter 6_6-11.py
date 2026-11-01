cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': 520000,
        'fact': 'Juga dikenal sebagai Solo, terkenal dengan batik.',
    },
    'yogyakarta': {
        'country': 'indonesia',
        'population': 370000,
        'fact': 'Pusat budaya dan pendidikan, punya keraton yang masih aktif.',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': 10600000,
        'fact': 'Kota terbesar di Indonesia.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tNegara: {info['country'].title()}")
    print(f"\tPopulasi: sekitar {info['population']:,} jiwa")
    print(f"\tFakta: {info['fact']}")