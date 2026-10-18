foods = []
prices = []
total = 0

while True:
    food = str(input("Enter the your food to buy (q to quit): "))
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a{food}: $"))
        foods.append(food)
        prices.append(price)

print("=" * 20)
print("   SHOOPING CART")
print("=" * 20)        

for food in foods:
    print(food, end=", ")

for price in prices:
    total += price

print(f"Your total is ${total:.2f}")