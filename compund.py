

again = "Y"
principal = 0
        rate = 0
        time = 0

while again.upper() == "Y":

    while principal <= 0:
        principal = float(input("Enter your principal amount: "))
    if principal <= 0:
        print("Principal must not less than.")

while rate <= 0:
    rate = float(input("Enter your interest rate: "))
    if rate <= 0:
        print("Rate must not less than.")

while time <= 0:
    time = int(input("Enter your time in year: "))
    if time <= 0:
        print("Time must not less than.")        


amount = principal * pow((1  + rate / 100), time) 

print("-----------SUMMARY---------")

print (f"Your principal is{principal:^,.2f}")
print (f"Your rate is {rate:^,.2f}")
print (f"Your year is {time:^}")

print (f"The balance after {time} year/s: ${amount:.2f}")


again = input("Do you want to calculate again (Y/N)? ")

print("--------------END-----------")