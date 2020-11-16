animals = input()

animal = animals.split(", ")

for i in range(len(animal) - 1, -1, -1):
    if animal[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animal[i] == "wolf":
        print(f"Oi! Sheep number {len(animal) - 1 - i}! You are about to be eaten by a wolf!")