n = int(input())
cars = {}
for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage, fuel = int(mileage), int(fuel)
    cars[car] = [mileage, fuel]
commands = input()
while not commands == "Stop":
    command = commands.split(" : ")[0]
    if command == "Drive":
        car, distance, fuel = commands.split(" : ")[1:]
        distance, fuel = int(distance), int(fuel)
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif command == "Refuel":
        car, fuel = commands.split(" : ")[1:]
        fuel = int(fuel)
        cars[car][1] += fuel
        if cars[car][1] > 75:
            cars[car][1] -= fuel
            fuel = 75 - cars[car][1]
            cars[car][1] = 75
        print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        car, kilometers = commands.split(" : ")[1:]
        kilometers = int(kilometers)
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    commands = input()
for (key, value) in dict(sorted(cars.items(), key=lambda el: (-el[1][0], el[0]))).items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")