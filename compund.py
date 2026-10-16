principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter your principal amount: "))
    if principal <= 0:
        print("Principal must not less than.")

while rate <= 0:
    rate = float(input("Enter your interest rate: "))
    if principal <= 0:
        print("Rate must not less than.")

while time <= 0:
    time = float(input("Enter your time in year: "))
    if time <= 0:
        print("Time must not less than.")        


print(principal)
print(rate)
print(time)