import time 

print("=" * 42)
print("         STUDENT GRADE MANAGEMENT")
print("=" * 42)

student_name = str(input("Enter the full-name: "))

pre_Cal = -1
programming = -1
science = -1


while pre_Cal < 0 or pre_Cal > 100:
    try:
        pre_Cal = float(input("Enter Pre-Calculus grades (1-100): "))
        if pre_Cal < 0 or pre_Cal > 100:
            print("Invalid grade!: (1-100)")
    except ValueError:
        print("Enter valid grade.")
        pre_Cal = -1        

while programming < 0 or programming > 100:
    try:
        programming = float(input("Enter Programming grades (1-100): "))
        if programming < 0 or programming > 100:
            print("Invalid grade!: (1-100)")
    except ValueError:
        print("Enter valid number.")
        programming = -1

while science < 0 or science > 100:
    try:
        science = float(input("Enter Science grades (1-100): "))
        if science < 0 or science >100:
            print("Invalid grade!: (1-100)")
    except ValueError:
        print("Enter valid number.")
        science = -1

    average = (pre_Cal + programming + science) / 3

    print("\nCalculating grades", end=".")
    for idx in range(3):
        time.sleep(0.5)
        print(idx, end=".", flush=True)

    print("\n\n" + "=" * 42)
    print("        STUDENT REPORT")
    print("=" * 42)

    print(f"\nSTUDENT NAME: {student_name}")
    print("-" * 30)
    print(f"Pre-calculus: {pre_Cal:^.2f}")
    print(f"Programming: {programming:^.2f}")
    print(f"Science: {science:^.2f}")
    print("=" * 20)
    print(f"AVERAGE: {average:^.2f}")

    if average >= 95:
        remark = "WOW GREAT JOB!"
    elif average >= 90:
        remark = "WOW GOOD JOB!"
    elif average >= 85:
        remark = "GOOD JOB"
    elif average >= 80:
        remark = "GOOD"
    elif average >= 75:
        remark = "NICE"
    else:
        remark = "haymako!"

    print(f"REMARK: {remark}")

    if average >= 75:
        print("STATUS: PASSED")
    else:
        print("STATUS: FAILED")

    print("=" * 42)
    print("      REPORT GENERATED SUCCESSFULLY")
    print("=" * 42)    