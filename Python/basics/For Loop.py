#Zad 1 Numbers from 1 to 100
for i in range(1,101):
    print(i)

#Zad 2 Numbers 1...N with Step 3
n2 = int(input())
for i in range(1,n2+1,3):
    print(i)

#Zad 3 Even Powers of 2
n3 = int(input())
for i in range(0,n3+1,2):
    print(2**i)

#Zad 4 Numbers N...1
n4 = int(input())
for i in range(n4,0,-1):
    print(i)

#Zad 5 Character Sequence
str = input()
for i in range(0, len(str)):
    print(str[i])

#Zad 6 Vowels Sum
text = input()
sum = 0
for i in range(0, len(text)):
    if text[i] == 'a':
        sum += 1
    elif text[i] == 'e':
        sum += 2
    elif text[i] == 'i':
        sum += 3
    elif text[i] == 'o':
        sum += 4
    elif text[i] == 'u':
        sum += 5
print(sum)

#Zad 7 Sum Numbers
n7 = int(input())
sum = 0
for i in range(1, n7+1):
    a = int(input())
    sum += a
print(sum)

#Zad 8 Number sequence
n8 = int(input())
max = -9999999999
min = 9999999999
for i in range(1, n8+1):
    a = int(input())
    if a > max:
        max = a
    if a < min:
        min = a
print(f"Max number: {max}")
print(f"Min number: {min}")

#Zad 9 Left and Right Sum
n9 = int(input())
left_sum = 0
right_sum = 0
for i in range(n9):
    left_sum += int(input())
for i in range(n9):
    right_sum += int(input())
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")

#Zad 10 Odd Even Sum
n10 = int(input())
odd_sum = 0
even_sum = 0
for i in range(n10):
    a = int(input())
    if i % 2 == 0:
        even_sum += a
    else:
        odd_sum += a
if odd_sum == even_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    print(f"No\nDiff = {abs(odd_sum - even_sum)}")