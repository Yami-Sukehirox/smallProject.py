import time
brand = [["Tesla", "Toyota", "Nissan", "Ferrari"],
         [ "Samsung", "Apple", "Oppo", "Asus"],  
         ["Orange", "Pineapple", "Strawberry", ]]

for collections in brand:
    time.sleep(0.5)
    for brands in collections:
        print(brands, end = ", ")
    print()
