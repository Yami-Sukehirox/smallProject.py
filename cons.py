# concession 

menu = {"pizza": 1.21,
        "burger": 2.34,
        "spag": 4.67,
        "soda": 10.3,
        "lemonade": 3.4,
        "fries": 25.4,
        "chips": 5.6}

cart =[]
total = 0

print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")    

while True:
    food = input("Enter an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("--------------YOUR TOTAl----------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")


print()
print(f"The total is: ${total:.2f}")