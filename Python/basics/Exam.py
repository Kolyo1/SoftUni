# Zad 1 Pc Strore
processor_price = float(input()) * 1.57
video_card_price = float(input()) * 1.57
ram_price = float(input()) * 1.57
ram_count = int(input())
discount = float(input())
real_proccesor_price = processor_price - (processor_price * discount)
print(real_proccesor_price)
real_video_card_price = video_card_price - (video_card_price * discount)
print(real_video_card_price)
real_ram_price = ram_price * ram_count
print(real_ram_price)
total_price = real_proccesor_price + real_video_card_price + real_ram_price
print(f"Money needed - {total_price:.2f} leva.")

# Zad 2 Bracelet Stand]
days = 5
day_money = float(input()) * days
sales_money = float(input()) * days
razhodi = float(input())
gift_price = float(input())
total_price = day_money + sales_money - razhodi
if total_price >= gift_price:
    print(f"Profit: {total_price:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - total_price:.2f} BGN.")

# Zad 3 Courier Express
kg = float(input())
usluga = input()
km = int(input())
price_per_km = 0
if kg < 1:
    price_per_km = 0.03
    express_percent = 0.80
elif kg < 10:
    price_per_km = 0.05
    express_percent = 0.40
elif kg < 40:
    price_per_km = 0.10
    express_percent = 0.05
elif kg < 90:
    price_per_km = 0.15
    express_percent = 0.02
else:
    price_per_km = 0.20
    express_percent = 0.01

standard_price = price_per_km * km
if usluga == "standard":
    price = standard_price
elif usluga == "express":
    express_price = express_percent * kg * price_per_km * km
    price = standard_price + express_price
print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price:.2f} lv.")

# Zad 4 Computer Firm
n = int(input())
total_sales = 0
total_rating = 0
for i in range (1, n+1):
    num = int(input())
    rating = num % 10
    possible_sales = num // 10
    if rating == 2:
        sales = 0
    elif rating == 3:
        sales = possible_sales * 0.5
    elif rating == 4:
        sales = possible_sales * 0.7
    elif rating == 5:
        sales = possible_sales * 0.85
    elif rating == 6:
        sales = possible_sales * 1.0
    else:
        sales = 0  


    total_sales += sales
    total_rating += rating

print(f"{total_sales:.2f}")
print(f"{(total_rating/n):.2f}")

# Zad 5 Hair Salon
target = int(input())
earned = 0

while earned < target:
    service = input()

    if service == "closed":
        break

    if service == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            earned += 15
        elif haircut_type == "ladies":
            earned += 20
        elif haircut_type == "kids":
            earned += 10

    elif service == "color":
        color_type = input()
        if color_type == "touch up":
            earned += 20
        elif color_type == "full color":
            earned += 30

if earned >= target:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target - earned}lv. more.")

print(f"Earned money: {earned}lv.")

#Zad 6 Multiply Table
number = int(input())
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
if hundreds == 0 or tens == 0 or ones == 0:
    print("Invalid number!")
else:
    for i in range(1, ones + 1):
        for j in range(1, tens + 1):
            for k in range(1, hundreds + 1):
                result = i * j * k
                print(f"{i} * {j} * {k} = {result};")

