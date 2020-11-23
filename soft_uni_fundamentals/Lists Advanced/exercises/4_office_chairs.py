rooms = int(input())
left_chairs = 0
is_free_chairs = True
for el in range(1, rooms + 1):
    information = input().split()
    chairs = information[0]
    persons = int(information[1])
    if len(chairs) < persons:
        is_free_chairs = False
        print(f'{persons - len(chairs)} more chairs needed in room {el}')
    else:
        left_chairs += len(chairs) - persons
if is_free_chairs:
    print(f'Game On, {left_chairs} free chairs left')

