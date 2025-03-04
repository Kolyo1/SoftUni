#Zad 1 USD to BGN
usd = float(input())
bgn = usd * 1.79549
print(bgn)

#Zad 2 Radians to Degrees
import math
radians = float(input())
degrees = radians * 180 / math.pi
print(degrees)

#Zad 3 Deposit Calculator
deposit = float(input())
months = int(input())
interest = float(input())
interest = deposit * interest / 100
interest = interest / 12
total = deposit + months * interest
print(total)

#Zad 4 Vacation Books List
pages = int(input())
pagesPerHour = int(input())
days = int(input())
hours = int(pages / pagesPerHour)
total = int(hours / days)
print(total)

#Zad 5 Supplies for School
pens = int(input())
markers = int(input())
cleaner = float(input())
discount = int(input())
pens = pens * 5.80
markers = markers * 7.20
cleaner = cleaner * 1.20
total = pens + markers + cleaner
total = total - total * discount / 100
print(total)

#Zad 6 Repainting
nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())
nylon = (nylon + 2) * 1.50
paint = (paint + paint * 0.10)*14.50
diluent = diluent * 5.00
total = nylon + paint + diluent + 0.40
totalmaistori = (total* 0.30) * hours
totaltotal = total + totalmaistori
print(totaltotal)

#Zad 7 Food Delivery
delivery = 2.50
pilMenu = float(input())
fishMenu = float(input())
vegiMenu = float(input())
pilMenu = pilMenu * 10.35
fishMenu = fishMenu * 12.40
vegiMenu = vegiMenu * 8.15
total = fishMenu + vegiMenu + pilMenu
desert = total * 0.20
totaltotal = total + desert + delivery
print(totaltotal)

#Zad 8 Basketball Equipment
yearPrice = float(input())
shoes = yearPrice - 0.40 * yearPrice
clothes = shoes - 0.20 * shoes
ball = clothes / 4
accessories = ball / 5
total = yearPrice + shoes + clothes + ball + accessories
print(total)

#Zad 9 Fish Tank
length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volumeLiter = volume * 0.001
percent = percent * 0.01
neededLiters = volumeLiter * (1 - percent)
print(neededLiters)