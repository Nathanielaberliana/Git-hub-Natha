usernames = ['admin', 'Natha', 'Kayla', 'Nayla', 'Kennard', 'Briliant']

for username in usernames:
    if username == 'admin':
        print("Halo admin, mau lihat laporan status?")
    else:
        print(f"Halo {username.title()}, terima kasih sudah login lagi.")
        