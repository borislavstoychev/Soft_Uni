with open("numbers.txt") as file:
    print(sum([int(el.strip())for el in file.readlines()]))