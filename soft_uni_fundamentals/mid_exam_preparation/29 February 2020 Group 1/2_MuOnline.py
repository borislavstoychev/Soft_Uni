health = 100
bitcoins = 0
is_dead = False
count_room = 0
rooms = input().split("|")
for room in rooms:
    count_room += 1
    command, number = room.split()
    number = int(number)
    if command == "potion":
        health += number
        if health > 100:
            print(f"You healed for {100 - (health - number)} hp.")
            health = 100
        else:
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health <= 0:
            is_dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_room}")
            break
        else:
            print(f"You slayed {command}.")

if not is_dead:
    print(f"You've made it!\n" f"Bitcoins: {bitcoins}\n" f"Health: {health}")

