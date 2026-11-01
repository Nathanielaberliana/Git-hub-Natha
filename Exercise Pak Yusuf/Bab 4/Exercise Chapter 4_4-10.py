pizza = ["pepperoni", "keju", "daging sapi asap", "jamur", "sosis", "paprika", "bawang"]

print("Tiga item pertama dalam list adalah:")
for cube in pizza[:3]:
    print(cube)

print("Tiga item dari tengah list adalah:")
for cube in pizza[3:6]:
    print(cube)

print("Tiga item terakhir dalam list adalah:")
for cube in pizza[-3:]:
    print(cube)