# Zad 1 Cinema
screening_type = input()
rows = int(input())
columns = int(input())
income = 0
cinema_capacity = rows * columns
if screening_type == "Premiere":
    income = cinema_capacity * 12
elif screening_type == "Normal":
    income = cinema_capacity * 7.5
elif screening_type == "Discount":
    income = cinema_capacity * 5.0

print(f"{income:.2f} leva")

# Zad 2 Summer Outfit
degrees = int(input())
time_of_day = input()
outfit = ""
shoes = ""
if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# Zad 3 New House
flower = input()
quantity = int(input())
budget = int(input())
price = 0
if flower == "Roses":
    price = quantity * 5
    if quantity > 80:
        price *= 0.9
elif flower == "Dahlias":
    price = quantity * 3.8
    if quantity > 90:
        price *= 0.85
elif flower == "Tulips":
    price = quantity * 2.8
    if quantity > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = quantity * 3
    if quantity < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = quantity * 2.5
    if quantity < 80:
        price *= 1.2
if budget >= price:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")

# Zad 4 Fishing Boat
budget = int(input())
season = input()
fishermen = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if fishermen <= 6:
    price *= 0.9
elif 7 <= fishermen <= 11:
    price *= 0.85
else:
    price *= 0.75
if fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95
if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")

# Zad 5 Journey
budget = float(input())
season = input()
destination = ""
place = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        budget *= 0.3
    elif season == "winter":
        place = "Hotel"
        budget *= 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        budget *= 0.4
    elif season == "winter":
        place = "Hotel"
        budget *= 0.8
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    budget *= 0.9
print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")

# Zad 6 Operations Between Numbers
n1 = int(input())
n2 = int(input())
operation = input()
result = 0
if operation == "+":
    result = n1 + n2
    if result % 2 == 0:
        print(f"{n1} {operation} {n2} = {result} - even")
    else:
        print(f"{n1} {operation} {n2} = {result} - odd")
elif operation == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f"{n1} {operation} {n2} = {result} - even")
    else:
        print(f"{n1} {operation} {n2} = {result} - odd")
elif operation == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f"{n1} {operation} {n2} = {result} - even")
    else:
        print(f"{n1} {operation} {n2} = {result} - odd")
elif operation == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operation == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")

# Zad 7 Hotel Room
month = input()
nights = int(input())
studio = 0 
apartment = 0
if month == "May" or month == "October":
    studio = 50 * nights
    apartment = 65 * nights
    if 7 < nights <= 14:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.7
        apartment *= 0.9
elif month == "June" or month == "September":
    studio = 75.2 * nights
    apartment = 68.7 * nights
    if nights > 14:
        studio *= 0.8
        apartment *= 0.9
elif month == "July" or month == "August":
    studio = 76 * nights
    apartment = 77 * nights
    if nights > 14:
        apartment *= 0.9
print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")

# Zad 8 On Time for the Exam
exam_hour = int(input())
exam_minute = int(input())
arival_hour = int(input())
arival_minute = int(input())
exam_time = exam_hour * 60 + exam_minute
arival_time = arival_hour * 60 + arival_minute
difference = abs(exam_time - arival_time)
difference_hour = difference // 60
difference_minute = difference % 60
if exam_time < arival_time:
    print("Late")
    if difference_hour == 0:
        print(f"{difference_minute} minutes after the start")
    else:
        print(f"{difference_hour}:{difference_minute:02d} hours after the start")
elif exam_time == arival_time or exam_time - arival_time <= 30:
    print("On time")
    if difference_hour == 0:
        print(f"{difference_minute} minutes before the start")
    else:
        print(f"{difference_hour}:{difference_minute:02d} hours before the start")
else:
    print("Early")
    if difference_hour == 0:
        print(f"{difference_minute} minutes before the start")
    else:
        print(f"{difference_hour}:{difference_minute:02d} hours before the start")

#Zad 9 Ski Trip
day = int(input())
room = input()
rating = input()
nights = day - 1
price = 0
if room == "room for one person":
    price = 18.00 * nights
elif room == "apartment":
    price = 25.00 * nights
    if nights < 10 :
       price *= 0.70
    elif 10 <= nights <= 15:
        price *= 0.65
    elif nights > 15:
       price *= 0.50
elif room == "president apartment":
    price = 35.00 * nights
    if nights < 10 :
        price *= 0.90
    elif 10 <= nights <= 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.80

if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.90

print(f"{price:.2f}")