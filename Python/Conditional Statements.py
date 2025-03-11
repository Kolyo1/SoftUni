# # Zad 1 Excellent Result
grade = float(input())
if grade >= 5.50:
    print("Excellent!")

# # Zad 2 Greater Number
first_number = int(input())
second_number = int(input())
if first_number > second_number:
    print(first_number)
else:
    print(second_number)
# Zad 3 Even or Odd
number = int(input())
if number % 2 == 0:
    print("even")
else:
    print("odd")

# # Zad 4 Password Guess
password = input()
if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")

# #Zad 5 Number 100...200
number = int(input())
if number < 100:
    print("Less than 100")
elif number <= 200 and number >= 100:
    print("Between 100 and 200")
else:
    print("Greater than 200")

# #Zad 6 Speed Info
speed = float(input())
if speed <= 10:
    print("slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("fast")
elif speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")

# #Zad 7 Area of Figures
import math
figure = input()
if figure == "square":
    side = float(input())
    print(f"{side * side:.3f}")
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print(f"{side1 * side2:.3f}")
elif figure == "circle":
    radius = float(input())
    print(f"{math.pi * radius * radius:.3f}")
elif figure == "triangle":
    side = float(input())
    height = float(input())
    print(f"{side * height / 2:.3f}")