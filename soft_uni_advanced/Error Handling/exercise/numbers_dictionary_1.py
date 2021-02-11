numbers_dictionary = {}
line = input()
while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

commands = input()
while not commands == "Remove":
    try:
        print(numbers_dictionary[commands])
    except KeyError:
        print("Number does not exist in dictionary")
    commands = input()

command = input()
while not command == "End":
    try:
        del numbers_dictionary[command]
    except KeyError:
        print("Number does not exist in dictionary")
    command = input()
print(numbers_dictionary)