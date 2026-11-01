prompt = "\nTopping apa yang mau kamu tambah? "
prompt += "Ketik 'quit' kalau sudah selesai: "

active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("Tiket kamu gratis.")
        elif age <= 12:
            print("Harga tiket kamu $10.")
        else:
            print("Harga tiket kamu $15.")
