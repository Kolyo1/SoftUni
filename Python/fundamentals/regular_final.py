# Zad 1
str = input()
while True:
    command = input()
    if command == "Done":
        break

    parts = command.split()
    action = parts[0]
    if action == "Change":
        old_char = parts[1]
        new_char = parts[2]
        str = str.replace(old_char, new_char)
        print(str)

    elif action == "Includes":
        substring = parts[1]
        print(substring in str)

    elif action == "End":
        substring = parts[1]
        print(str.endswith(substring))

    elif action == "Uppercase":
        str = str.upper()
        print(str)

    elif action == "FindIndex":
        char = parts[1]
        print(str.index(char))

    elif action == "Cut":
        start_index = int(parts[1])
        count = int(parts[2])
        end_index = start_index + count
        str = str[start_index:end_index]
        print(str)

# zad 2
import re
n = int(input())
pattern =  r'^\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#$'
for _ in range(n):
    st = input()
    match = re.match(pattern, st)
    if match:
        boss_name = match.group(1)
        boss_title = match.group(2)
        print(f"{boss_name}, The {boss_title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(boss_title)}")
    else:
        print("Access denied!")

# Zad 3
capacity = int(input())
users = {}

while True:
    command = input()
    if command == "Statistics":
        break

    parts = command.split("=")
    action = parts[0]

    if action == "Add":
        username, sent, received = parts[1], int(parts[2]), int(parts[3])
        if username not in users:
            users[username] = {"sent": sent, "received": received}

    elif action == "Message":
        sender, receiver = parts[1], parts[2]
        if sender in users and receiver in users:
            users[sender]["sent"] += 1
            users[receiver]["received"] += 1

            if users[sender]["sent"] + users[sender]["received"] >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]

            if receiver in users and users[receiver]["sent"] + users[receiver]["received"] >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif action == "Empty":
        username = parts[1]
        if username == "All":
            users.clear()
        else:
            users.pop(username, None)

print(f"Users count: {len(users)}")
for username, data in users.items():
    total_messages = data["sent"] + data["received"]
    print(f"{username} - {total_messages}")
