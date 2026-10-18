print ("=" * 42)
print("         ATM SYSTEM")
print ("=" * 42) 

correct_pin = 12345
attempts = 3

balance = 5000.00
last_withdraw = 0
last_deposit = 0

while attempts < 3:
    pin = int(input("\nEnter your pin: "))

    if pin == correct_pin:
        print("\nAccess Granted!")
        break
    else:
        attempts += 1
        print("\nIncorrect PIN")

    if attempts == 3:
        print("Too many incorrecr attempts")

    else:
        choice = "0"

        while choice != "6":

            print("\n------ ATM MENU --------\n")
            print("1. CHECK BALANCE\n")
            print("2. WITHDRAW MONEY")


