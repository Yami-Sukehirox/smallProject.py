import time

set = int(input("Enter the time: "))
for idx in reversed(range(0, set)):
    seconds = idx % 60
    minutes = int(idx / 60) % 60
    hours = int(idx /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("HELLO WORLD")