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
            print("2. WITHDRAW MONEY\n")
            print("3. DEPOSIT MONEY\n")
            print("4. MINI STATEMENTS\n")
            print("5. CHANGE PIN\n")
            print("6. EXIT\n")


            choice = input("Enter your chouce: ")

            if choice == 1:
                print (f"\nYour Balance is {balance:^.2f}")

            elif choice == 2:
                withdraw = float(input("Enter amount of withdraw: $"))

                


