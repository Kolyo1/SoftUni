# Zad 1 Day of Week
day = int(input())
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3: 
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Error")

# Zad 2 Weekend or Working Day
day = input()
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")

# Zad 3 Animal Type
animal = input()
if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")

# Zad 4 Personal Titles
age = float(input())
gender = input()
if gender == "m":
    if age < 16:
        print("Master")
    else:
        print("Mr.")
else:
    if age < 16:
        print("Miss")
    else:
        print("Ms.")

# Zad 5 Small Shop
product = input()
city = input()
quantity = float(input())
price = 0
if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50
elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55
print(f"Price: {price * quantity}")

# Zad 6 Number in Range
n = int(input())
if n >= -100 and n <= 100 and n != 0:
    print("Yes")
else:
    print("No")

# Zad 7 Working Hours
time = int(input())
day = input()
if time >= 10 and time <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")

# Zad 8 Cinema Ticket
day = input()
if day == "Monday" or day == "Tuesday" or day == "Friday":
    print(12)
elif day == "Wednesday" or day == "Thursday":
    print(14)
else:
    print(16)

# Zad 9 Fruit or Vegetable
product = input()
if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
    print("fruit")
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    print("vegetable")
else:
    print("unknown")

# Zad 10 Invalid Number
n = int(input())
if n >= 100 and n <= 200 or n == 0:
    pass
else:
    print("invalid")

# Zad 11 Fruit Shop
product = input("banana / apple / orange / grapefruit / kiwi / pineapple / grapes: ")
day = input("Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday: ")
quantity = float(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        price = 2.50
    elif product == "apple":
        price = 1.20
    elif product == "orange":
        price = 0.85
    elif product == "grapefruit":
        price = 1.45
    elif product == "kiwi":
        price = 2.70
    elif product == "pineapple":
        price = 5.50
    elif product == "grapes":
        price = 3.85
elif day == "Saturday" or day == "Sunday":
    if product == "banana":
        price = 2.70
    elif product == "apple":
        price = 1.25
    elif product == "orange":
        price = 0.90
    elif product == "grapefruit":
        price = 1.60
    elif product == "kiwi":
        price = 3.00
    elif product == "pineapple":
        price = 5.60
    elif product == "grapes":
        price = 4.20
else:
    print("error")
    exit()

if price == 0:
    print("error")
else:
    print(f"{price * quantity:.2f}")

#Zad 12 Trade Commissions
city = input()
sales = float(input())
if sales < 0:
    print("error")
    exit()
elif city == "Sofia":
    if 0 <= sales <= 500:
        sales *= 0.05
    elif 500 < sales <= 1000:
        sales *= 0.07
    elif 1000 < sales <= 10000:
        sales *= 0.08
    elif sales > 10000:
        sales *= 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        sales *= 0.045
    elif 500 < sales <= 1000:
        sales *= 0.075
    elif 1000 < sales <= 10000:
        sales *= 0.10
    elif sales > 10000:
        sales *= 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        sales *= 0.055
    elif 500 < sales <= 1000:
        sales *= 0.08
    elif 1000 < sales <= 10000:
        sales *= 0.12
    elif sales > 10000:
        sales *= 0.145
else:
    print("error")
    exit()
if sales == 0:
    print("error")
else:
    print(f"{sales:.2f}")