def make_sandwich(*items):
    print("\nSaya akan membuatkan sandwich spesial untukmu:")
    for item in items:
        print(f"  ...menambahkan {item} ke sandwichmu.")
    print("Sandwichmu sudah siap!")


make_sandwich('daging sapi panggang', 'keju', 'selada', 'madu dijon')
make_sandwich('kalkun', 'apel', 'mustard')
make_sandwich('selai kacang', 'selai stroberi')