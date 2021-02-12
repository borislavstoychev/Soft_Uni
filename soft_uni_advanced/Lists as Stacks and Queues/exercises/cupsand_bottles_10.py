from collections import deque


cups = deque(int(c) for c in input().split())
bottles = deque(int(c) for c in input().split())

wasted_watter = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    result = bottle - cup
    if result < 0:
        cups.appendleft(cup - bottle)
    elif result > 0:
        wasted_watter += result
if bottles:
    print(f"Bottles: ", end="")
    print(*bottles, sep=" ")
else:
    print(f"Cups: ", end="")
    print(*cups, sep=" ")
print(f"Wasted litters of water: {wasted_watter}")