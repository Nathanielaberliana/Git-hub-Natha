favorite_languages = {
    'Nathaniela': 'python',
    'Kayla': 'inggris',
    'Nayla': 'mandarin',
    'Renai': 'arab',
}

for name, language in favorite_languages.items():
    print(f"Bahasa favorit {name.title()} adalah {language.title()}.")

print()

coders = ['Nathaniela', 'Kayla', 'Nayla', 'Renai', 'Berliana']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Terima kasih sudah ikut polling, {coder.title()}!")
    else:
        print(f"{coder.title()}, apa bahasa favoritmu?")