my_pizza = ["pepperoni", "keju", "daging sapi asap", "jamur"]
friend_pizza = my_pizza

my_pizza.append("sosis")
friend_pizza.append("paprika")

print("Pizza favoritku adalah:")
for pizza in my_pizza:
    print(pizza)
    
print("\nPizza favorit temanku adalah:")
for pizza in friend_pizza:
    print(pizza)