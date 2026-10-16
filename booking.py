# while loop airport calculator

again = "Y"

while again.upper() == "Y":
    travelClass = input("Enter your travel class (E-conomy / B-usiness): ")

    if travelClass.upper() == "E":
        baseFare = 2500.00
        allowance = 20

    elif travelClass.upper() == "B":
        baseFare = 6500.00
        allowance = 40
    else:
        print("Invalid travel class")
        break

    while True:
        baggageWeight = float(input("Enter the Baggage Weight (kg): "))

        if baggageWeight < 0:
            print("Invalid baggage weight")
        else:
            break
    if baggageWeight > allowance:
        excessBaggage = (baggageWeight - allowance) * 150
    else:
        excessBaggage = 0            

    totalFare = baseFare + excessBaggage

    print("\n-------------BOARDING SUMMARY--------------\n")

    if travelClass.upper() == "E":
        print("Travel Class: Economoy")
    else:
        print("Travel Class: Bussiness")
    print(f"Base Fare: PHP {baseFare:.2f}")
    print(f"Baggage Weight: {baggageWeight:.1f}kg ({allowance:.0f})kg")
    print(f"Excess Baggage Fee: PHP {excessBaggage:.2f}")
    print(f"Total Fare: PHP {totalFare:.2f}")

    again = input (
        "Do you want to calculate another passenger? (Y/N): "
    )    

    print("------------THANK YOU---------------")


