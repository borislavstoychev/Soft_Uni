from collections import deque


def lets_cross(free_light, c):
    counts = 0
    while counts < free_light:
        if not c:
            return free_light - counts, c
        c.popleft()
        counts += 1
    return 0, c


green_light = int(input())
green_copy = [green_light].copy()
free_window = int(input())
is_crash = False
count = 0
letter_hit = ""
car = []
cars_deq = deque()
command = input()
while not command == "END":
    if is_crash:
        break
    elif command == "green":
        green_light = green_copy[0]
        while green_light and cars_deq:
            if cars_deq:
                cars = deque(cars_deq.popleft())
                car = cars.copy()
                green_light, cars = lets_cross(green_light, cars)
                count += 1
                if cars:
                    free_window, cars = lets_cross(free_window, cars)
                    if cars:
                        is_crash = True
                        letter_hit = cars.popleft()
                        break
    else:
        cars_deq.append(command)

    command = input()

if not is_crash:
    print("Everyone is safe.")
    print(f"{count} total cars passed the crossroads.")
else:
    print("A crash happened!")
    print(f"{''.join(car)} was hit at {letter_hit}.")