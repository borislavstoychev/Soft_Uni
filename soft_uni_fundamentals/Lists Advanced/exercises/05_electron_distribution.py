electrons = int(input())
list_el = []
for index in range(1, electrons + 1):
    electron = 2 * index ** 2
    if electron <= electrons:
        electrons -= electron
        list_el.append(electron)
    else:
        electron = electrons
        list_el.append(electron)
        break

print(list(el for el in list_el if not el <= 0))
