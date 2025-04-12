#Zad 1 Numbers Ending in 7
for i in range(1, 1001):
    if i %10 == 7:
        print(i)

#Zad 2 Half Sum Element
import sys

n = int(input())
sum = 0
max_num = -sys.maxsize
for i in range(n):
    a = int(input())
    if a > max_num:
        max_num = a
    sum += a
if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (sum - max_num))
    print("No")
    print(f"Diff = {diff}")

#Zad 3 Histogram
n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(n):
    a = int(input())
    if a < 200:
        p1 += 1
    elif a < 400:
        p2 += 1
    elif a < 600:
        p3 += 1
    elif a < 800:
        p4 += 1
    else:
        p5 += 1
print(f"{p1/n*100:.2f}%")
print(f"{p2/n*100:.2f}%")
print(f"{p3/n*100:.2f}%")
print(f"{p4/n*100:.2f}%")
print(f"{p5/n*100:.2f}%")

#Zad 4 Clever Lily
age = int(input())
price_washing_machine = float(input())
toy_price = int(input())

money_saved = 0
money_received = 0
toy_count = 0
brother_cut = 0
    
for year in range(1, age + 1):
    if year % 2 == 0:
        money_received += (year // 2) * 10
        brother_cut += 1
    else:
        toy_count += 1

money_saved = money_received - brother_cut + (toy_count * toy_price)
    
if money_saved >= price_washing_machine:
    print(f"Yes! {money_saved - price_washing_machine:.2f}")
else:
    print (f"No! {price_washing_machine - money_saved:.2f}")

#Zad 5 Salary
n5 = int(input())
salary = int(input())
for i in range(n5):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)

#Zad 6 Oscars
actor_name = input()
academy_points = float(input())
n6 = int(input())

for _ in range(n6):
    judge_name = input()
    judge_points = float(input())
    academy_points += (len(judge_name) * judge_points) / 2
        
    if academy_points >= 1250.5:
        print (f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    print (f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")

#Zad 7 Trekking Mania
groups_count = int(input())
musala_count = 0
montblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(groups_count):
    group_size = int(input())
    if group_size <= 5:
        musala_count += group_size
    elif 6 <= group_size <= 12:
        montblan_count += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro_count += group_size
    elif 26 <= group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size
total_climbers = musala_count + montblan_count + kilimanjaro_count + k2_count + everest_count
musala_percent = (musala_count / total_climbers) * 100
montblan_percent = (montblan_count / total_climbers) * 100
kilimanjaro_percent = (kilimanjaro_count / total_climbers) * 100
k2_percent = (k2_count / total_climbers) * 100
everest_percent = (everest_count / total_climbers) * 100
print(f'{musala_percent:.2f}%')
print(f'{montblan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')

#Zad 8 Tennis Ranklist
tournaments = int(input())
starting_points = int(input())
total_points = starting_points
won_tournaments = 0

total_earned_points = 0

for _ in range(tournaments):
    stage = input()
    if stage == "W":
        total_points += 2000
        total_earned_points += 2000
        won_tournaments += 1
    elif stage == "F":
        total_points += 1200
        total_earned_points += 1200
    elif stage == "SF":
        total_points += 720
        total_earned_points += 720

average_points = total_earned_points // tournaments
win_percentage = (won_tournaments / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
