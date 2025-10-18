#1

from collections import deque

potions = {
    "Draught of Wisdom": 90,
    "Essence of Resilience": 100,
    "Potion of Agility": 80,
    "Elixir of Strength": 70,
    "Brew of Immortality": 110,
}

substances = list(map(int, input().split(", ")))
crystals = deque(map(int, input().split(", ")))

crafted = []

while substances and crystals and len(crafted) < len(potions):
    substance = substances.pop()
    crystal = crystals.popleft()
    total = substance + crystal

    available = {k: v for k, v in potions.items() if k not in crafted}
    crafted_now = None

    for name, energy in available.items():
        if total == energy:
            crafted_now = name
            break

    if not crafted_now:
        lower_potions = sorted(
            [(n, e) for n, e in available.items() if e < total],
            key=lambda x: x[1],
            reverse=True
        )
        for name, energy in lower_potions:
            crafted_now = name
            break

        if lower_potions:
            crystal -= 20
            if crystal > 0:
                crystals.append(crystal)
        else:
            crystal -= 5
            if crystal > 0:
                crystals.append(crystal)
            

    if crafted_now and crafted_now not in crafted:
        crafted.append(crafted_now)

if len(crafted) == len(potions):
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted:
    print(f"Crafted potions: {', '.join(crafted)}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if crystals:
    print(f"Crystals: {', '.join(map(str, crystals))}")

#2 

from sys import stdin

n = int(stdin.readline().strip())
grid = [list(stdin.readline().strip()) for _ in range(n)]

pr = pc = None
stars = 0
for r in range(n):
    for c in range(n):
        if grid[r][c] == 'P':
            pr, pc = r, c
        elif grid[r][c] == '*':
            stars += 1

health = 100
frozen_immunity = False
moved = False

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

def wrap(r, c):
    return r % n, c % n

game_over = False
won = False

for line in stdin:
    cmd = line.strip()
    if cmd == 'end' or game_over or won:
        break
    dr, dc = moves[cmd]
    if not moved:
        grid[pr][pc] = '-'
        moved = True
    pr, pc = wrap(pr + dr, pc + dc)
    cell = grid[pr][pc]

    if cell == '-':
        pass
    elif cell == '*':
        stars -= 1
        grid[pr][pc] = '-'
        if stars == 0:
            won = True
            break
    elif cell == 'G':
        grid[pr][pc] = '-'
        if frozen_immunity:
            frozen_immunity = False
        else:
            health -= 50
            if health <= 0:
                game_over = True
                break
    elif cell == 'F':
        frozen_immunity = True
        grid[pr][pc] = '-'

if game_over:
    print(f"Game over! Pacman last coordinates [{pr},{pc}]")
elif won:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if stars > 0:
    print(f"Uncollected stars: {stars}")

grid[pr][pc] = 'P'
for row in grid:
    print(''.join(row))


# 3 

def classify_books(*args, **kwargs):
    title_to_isbn = {title: isbn for isbn, title in kwargs.items()}
    fiction = []
    non_fiction = []

    for genre, title in args:
        isbn = title_to_isbn.get(title)
        if not isbn:
            continue
        if genre == "fiction":
            fiction.append((isbn, title))
        elif genre == "non_fiction":
            non_fiction.append((isbn, title))

    fiction.sort(key=lambda x: x[0])               
    non_fiction.sort(key=lambda x: x[0], reverse=True) 

    lines = []
    if fiction:
        lines.append("Fiction Books:")
        for isbn, title in fiction:
            lines.append(f"~~~{isbn}#{title}")
    if non_fiction:
        lines.append("Non-Fiction Books:")
        for isbn, title in non_fiction:
            lines.append(f"***{isbn}#{title}")

    return "\n".join(lines)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))