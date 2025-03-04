#Zad 1 Hello SoftUni
print("Hello SoftUni")

#Zad 2 Nums 1...10
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
print("8")
print("9")
print("10")

#Zad 3 Rectangle Area
a = int(input())
b = int(input())
area = a * b
print(area)

#Zad 4 Inches to Centimeters
sm = float(input())
inch = sm * 2.54
print(f"Inches = {inch}")

#Zad 5 Greeting by Name
name = input()
print(f"Hello, {name}!")

#Zad 6 Concatenate Data
name = input()
lastName = input()
age = int(input())
town = input()
print(f"You are {name} {lastName}, a {age}-years old person from {town}.")

#Zad 7 Projects Creation
name = input()
projects = int(input())
time = projects * 3
print(f"The architect {name} will need {time} hours to complete {projects} project/s.")

#Zad 8 Pet Shop
dogs = int(input())
otherAnimals = int(input())
dogsPrice = dogs * 2.50
otherAnimalsPrice = otherAnimals * 4
total = dogsPrice + otherAnimalsPrice
print(f"{total} lv.")

#Zad 9 Yard Greening
squareMeters = float(input())
price = squareMeters * 7.61
discount = price * 0.18
finalPrice = price - discount
print(f"The final price is: {finalPrice} lv.")
print(f"The discount is: {discount} lv.")
