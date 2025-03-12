# # #Zad 1 Sum Seconds
time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second + time_third
minutes = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
 
# # #Zad 2 Bonus Score
number = int(input())
bonus_score = 0
if number <= 100:
    bonus_score = 5
elif number > 1000:
    bonus_score = number * 0.1
elif number > 100:
    bonus_score = number * 0.2
if number % 2 == 0:
    bonus_score += 1
elif number % 10 == 5:
    bonus_score += 2
print(bonus_score)
print(number + bonus_score)

# # #Zad 3 Time + 15 Minutes
hours = int(input())
minutes = int(input())
total_minutes = hours * 60 + minutes + 15
hours = total_minutes // 60
minutes = total_minutes % 60
if hours == 24:
    hours = 0
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")

# # #Zad 4 Toy Shop
price_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
total_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2
total_price = number_puzzles * price_puzzle + number_dolls * price_doll + number_bears * price_bear + number_minions * price_minion + number_trucks * price_truck
discount = 0
if total_toys >= 50:
    discount = total_price * 0.25
total = total_price - discount
rent = total * 0.1
profit = total - rent
if profit >= price_excursion:
    print(f"Yes! {profit - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - profit:.2f} lv needed.")  

# #Zad 5 Godzila vs. Kong
budget = float(input())
number_statists = int(input())
price_clothes_for_one = float(input())
decor = budget * 0.1
price_clothes = number_statists * price_clothes_for_one
discount = 0
if number_statists > 150:
    discount = price_clothes *0.1 
total_clothes = price_clothes - discount
total_price = decor + total_clothes
if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")

# #Zad 6 World Swimming Record
record = float(input())
distance = float(input())
time_per_meter = float(input())
time = distance * time_per_meter
delay = distance // 15
delay_time = delay * 12.5
total_time = time + delay_time
if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")

# #Zad 7 Shopping
budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())
video_card = 250
total_video_cards = number_video_cards * video_card
proccesor = total_video_cards * 0.35
ram = total_video_cards * 0.1
discount = 0
total = number_video_cards * video_card + number_processors * proccesor + number_ram * ram
if number_video_cards > number_processors:
    discount = total * 0.15
total -= discount
if total <= budget:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")

#Zad 8 Lunch Break
import math
series_name = input()
episode_time = float(input())
break_time = float(input())
lunch_time = break_time / 8
rest_time = break_time / 4
free_time = break_time - lunch_time - rest_time
if free_time >= episode_time:
    remaining_time = math.ceil(free_time - episode_time)
    print(f"You have enough time to watch {series_name} and left with {remaining_time} minutes free time.")
else:
    needed_time = math.ceil(episode_time - free_time)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")