people = int(input())
wagons = list(map(int, input().split()))
index = - 1
for wagon in wagons:
    index += 1
    if wagon < 4:
        people -= 4 - wagon
        wagon += 4 - wagon
        if people <= 0:
            wagon = people + wagon
            people = 0
    wagons.pop(index)
    wagons.insert(index, wagon)
    if people == 0:
        break

if not sum(wagons) / 4 == len(wagons):
    print("The lift has empty spots!")
    print(" ".join(list(map(str, wagons))))
elif not people == 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(list(map(str, wagons))))
else:
    print(" ".join(list(map(str, wagons))))

