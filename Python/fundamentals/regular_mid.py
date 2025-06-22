# Zad 1 
import math
budget = float(input())
students = int(input())
flour_price = float(input())
eggs_price = float(input())
apron_price = float(input())
free_package = students // 5
needed_flout = flour_price * (students - free_package)
needed_eggs = eggs_price * 10 * students
needed_apron = apron_price * math.ceil(students * 1.2)
total = needed_flout + needed_eggs + needed_apron
if total <= budget:
    print(f'Items purchased for {total:.2f}$.')
else:
    print(f"{total - budget:.2f}$ more needed.")

# Zad 2 

name = input().split(", ")
while True:
    command = input()
    if command == "Report":
        break

    parts = command.split()
    action = parts[0]
    if action == "Blacklist":
        black = parts[1]
        if black in name:
            index = name.index(black)
            name[index] = "Blacklisted"
            print(f"{black} was blacklisted.")
        else:
            print(f"{black} was not found.")
    
    elif action == "Error":
        index = int(parts[1])
        if 0 <= index < len(name):
            lost = name[index]
            if lost != "Blacklisted" and lost != "Lost":
                name[index] = "Lost"
                print(f"{lost} was lost due to an error.")
    
    elif action == "Change":
        index = int(parts[1])
        new_name = parts[2]
        if 0 <= index < len(name):
            current_name = name[index]
            name[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

print(f"Blacklisted names: {name.count('Blacklisted')}")
print(f"Lost names: {name.count('Lost')}")
print(" ".join(name))

# Zad 3
chat = []
while True:
    command = input()
    if command == "end":
        break

    parts = command.split()
    action = parts[0]
    if action == "Chat":
        message = " ".join(parts[1:])
        chat.append(message)
    if action == "Delete":
        message = " ".join(parts[1:])
        if message in chat:
            chat.remove(message)
    if action == "Edit":
        message = parts[1]
        edited = " ".join(parts[2:])
        if message in chat:
            index = chat.index(message)
            chat[index] = edited
    if action == "Pin":
        message = " ".join(parts[1:])
        if message in chat:
            chat.remove(message)
            chat.append(message)
    if action == "Spam":
        messages = parts[1:]
        for msg in messages:
            chat.append(msg)  
for msg in chat:
    print(msg)