elements = input().split()
move = 0
is_win = False
while True:
    move += 1
    line = input()
    if line == "end":
        break
    index1, index2 = line.split()
    index1 = int(index1)
    index2 = int(index2)
    if index1 == index2 or index1 not in range(len(elements)) or index2 not in range(len(elements)):
        print("Invalid input! Adding additional elements to the board")
        elements.insert(len(elements)//2, f"-{move}a")
        elements.insert(len(elements)//2, f"-{move}a")
    elif elements[index1] == elements[index2]:
        element_to_remove = elements[index1]
        elements.remove(element_to_remove)
        elements.remove(element_to_remove)
        print(f"Congrats! You have found matching elements - {element_to_remove}!")

    elif not elements[index1] == elements[index2]:
        print("Try again!")
    if len(elements) == 0:
        is_win = True
        print(f"You have won in {move} turns!")
        break

if not is_win:
    print(f"Sorry you lose :(")
    print(f"{' '.join(elements)}")
