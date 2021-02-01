n = int(input())
cars = set()
for _ in range(n):
    direction, reg_num = input().split(", ")
    operation = {
        "IN": cars.add,
        "OUT": cars.remove,
    }
    operation[direction](reg_num)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")

