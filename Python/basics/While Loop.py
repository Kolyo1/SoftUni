#Zad 1 Read Text
while True:
    text = input()
    if text == 'Stop':
        break
    print(text)

#Zad 2 Password
user = input()
password = input()
data = input()
while data!= password:
    data = input()
print(f'Welcome {user}!')

#Zad 3 Sum of Numbers
start = int(input())
sum = 0
while sum < start:
    num = int(input())
    sum += num
print(sum)

#Zad 4 Sequence 2k+1
n = int(input())
count = 1
while count <= n:
    print(count)
    count = 2 * count + 1

#Zad 5 Account Balance
comm = input()
balance = 0
while comm != 'NoMoreMoney':
    comm = float(comm)
    if comm < 0:
        print('Invalid operation!')
        break
    balance += comm
    print(f'Increase: {comm:.2f}')
    comm = input()
print(f'Total: {balance:.2f}')

#Zad 6 Max Number
import sys
cm = input()
max = -sys.maxsize
while cm != 'Stop':
    cm = int(cm)
    if cm > max:
        max = cm
    cm = input()
print(max)

#Zad 7 Min Number
cmm = input()
min = sys.maxsize
while cmm != 'Stop':
    cmm = int(cmm)
    if cmm < min:
        min = cmm
    cmm = input()
print(min)

#Zad 8 Graduation
name = input()
year = 1
sum = 0
failed = 0
while year <= 12:
    grade = float(input())
    if grade < 4:
        failed += 1
        if failed > 1:
            year -= 1
            print(f'{name} has been excluded at {year} grade')
            break
    sum += grade
    year += 1
if year > 12:
    average = sum / 12  
    print(f'{name} graduated. Average grade: {average:.2f}')