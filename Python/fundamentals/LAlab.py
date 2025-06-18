#Zad 1 Which are in?
import sys
first_line = sys.stdin.readline().strip()
second_line = sys.stdin.readline().strip()
fList = first_line.split(", ")
sList = second_line.split(", ")
result = [w for w in fList if any(w in s for s in sList)]
print(result)

#Zad 2 Next Version
import sys
def next_version(n):
    parts = [int(x) for x in n.split('.')]
    idx = len(parts) - 1
    while idx >= 0:
        parts[idx] += 1
        if parts[idx] > 9:
            parts[idx] = 0
            idx -= 1
        else:
            break
    return '.'.join(str(x) for x in parts)
n1 = sys.stdin.readline().strip()
n2 = sys.stdin.readline().strip()
n3 = sys.stdin.readline().strip()
print(next_version(n1))
print(next_version(n2))
print(next_version(n3))

# Zad 3 WordFilter
str = input().split(" ")
word_filt = [x for x in str if len(x) %2 == 0]
print("\n".join(word_filt))

# Zad 4 Num Clasif
num = input().split(", ")
posiv = [x for x in num if int(x) >= 0]
negat = [x for x in num if int(x) < 0]
even = [x for x in num if int(x) % 2 == 0]
odd = [x for x in num if int(x) % 2 != 0]
print("Positive:",", ".join(posiv))
print("Negative:",", ".join(negat))
print("Even:" ,", ".join(even))
print("Odd:",", ".join(odd))

# Zad 5 
n = int(input())
total_chair = 0
enough_chair = True
for i in range(1,n+1):
    line = input().split()
    chairs = len(line[0])
    visitors = int(line[1])
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        enough_chair = False
    else:
        total_chair += chairs - visitors
if enough_chair:
    print(f"Game On, {total_chair} free chairs left")

# Zad 6 El Distribution
el = int(input())
shells = []
n = 1
while el > 0:
    capacity = 2*n**2
    el_shell = min(el, capacity)
    shells.append(el_shell)
    el -= el_shell
    n += 1
print(shells)

# Zad 7 Group of 10's
gr = [int(x) for x in input().split(", ")]
max_value = max(gr)
count = 10
while count <= max_value+10:
    gr_list = [x for x in gr if count - 10 <x <= count]
    if gr_list:
        print(f"Group of {count}'s: {gr_list}")
    count += 10

# Zad 8 Decipher
message = input().split()
deciphered = []
for word in message:
    num = ''
    i = 0 
    while i < len(word) and word[i].isdigit():
        num += word[i]
        i += 1
    if num:
        fLetter = chr(int(num))
        rest = word[i:]
        if len(rest) > 1:
            rest = rest[-1] + rest[1:-1] + rest[0]
        deciphered.append(fLetter + rest)
    else:
        deciphered.append(word)
print(" ".join(deciphered))