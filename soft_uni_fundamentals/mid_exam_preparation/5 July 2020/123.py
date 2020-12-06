targets = [int(el) for el in input().split()]

command = input()


while command != 'End':
    count = -1
    index = int(command)
    if index in range(len(targets)):
        current_index_value = targets[index]
        targets[index] = -1
        for el in targets:
            count += 1
            if el > current_index_value and not current_index_value == -1:
                targets[count] = el - current_index_value
            else:
                if not el == -1:
                    targets[count] = el + current_index_value

    command = input()

print(f'Shot targets: {len([_ for _ in targets if _ == -1])} -> {" ".join(list(map(str, targets)))}')