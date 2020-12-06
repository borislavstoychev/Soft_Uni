energy = int(input())
count_of_battle = 0
is_win = True
while True:
    commands = input()
    if commands == "End of battle":
        break
    distance = int(commands)
    if energy < distance:
        print(f"Not enough energy! Game ends with {count_of_battle} won battles and {energy} energy")
        is_win = False
        break
    count_of_battle += 1
    if count_of_battle % 3 == 0:
        energy += count_of_battle
    energy -= distance

if is_win:
    print(f"Won battles: {count_of_battle}. Energy left: {energy}")
