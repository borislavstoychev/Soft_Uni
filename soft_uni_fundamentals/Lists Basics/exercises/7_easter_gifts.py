line = input().split()

place = ''

commands = input()

try:
    command, gift, place = commands.split()
except:
    command, gift = commands.split()

while not command == 'No':
    if command == 'OutOfStock':
        for index in range(len(line)):
            if gift == line[index]:
                line[index] = 'None'

    elif command == 'Required':
        position = int(place)
        for index in range(len(line)):
            if position >= len(line) or position < 0:
                continue
            else:
                line[position] = gift
                break

    elif command == 'JustInCase':
        line[-1] = gift

    commands = input()
    try:
        command, gift, place = commands.split()
    except:
        command, gift = commands.split()

for removing in line:
    if "None" in line:
        line.remove("None")

print(' '.join(line))
