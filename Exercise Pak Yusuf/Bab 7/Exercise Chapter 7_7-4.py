prompt = "\nTopping apa yang mau kamu tambah? "
prompt += "Ketik 'quit' kalau sudah selesai: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Oke, saya tambahkan {topping} ke pizza kamu.")
    else:
        break
