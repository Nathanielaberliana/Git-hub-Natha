guests = ["Albert Einstein", "R.A. Kartini", "Soekarno"]

print("Yth.", guests[0], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[1], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[2], "saya mengundang Anda untuk makan malam bersama.")

print("\nMohon maaf", guests[2], "tidak bisa hadir di acara makan malam.")
guests[2] = "B.J. Habibie"
print("Yth.", guests[0], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[1], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[2], "saya mengundang Anda untuk makan malam bersama.")

print("\nKabar baik! Saya menemukan meja makan yang lebih besar untuk kita, jika kalian tidak keberatan, saya ingin mengundang 3 orang lagi.")
guests.insert(0, "Ibu Fatmawati")
guests.insert(2, "Najwa Shihab")
guests.append("Jokowi")
print("Yth.", guests[0], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[1], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[2], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[3], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[4], "saya mengundang Anda untuk makan malam bersama.")
print("Yth.", guests[5], "saya mengundang Anda untuk makan malam bersama.")

print("\nMohon maaf, ternyata meja makan yang lebih besar tidak bisa digunakan. Saya hanya bisa mengundang 2 orang saja.")
removed_guest1 = guests.pop(5)
print("Mohon maaf", removed_guest1, "tidak bisa hadir di acara makan malam.")
removed_guest2 = guests.pop(1)
print("Mohon maaf", removed_guest2, "tidak bisa hadir di acara makan malam.")
removed_guest3 = guests.pop(3)
print("Mohon maaf", removed_guest3, "tidak bisa hadir di acara makan malam.")
removed_guest4 = guests.pop(2)
print("Mohon maaf", removed_guest4, "tidak bisa hadir di acara makan malam.")

print("Hello", guests[0], "Anda masih diundang untuk makan malam bersama.")
print("Hello", guests[1], "Anda masih diundang untuk makan malam bersama.") 

del guests[0]
del guests[0]
print(guests)