from collections import deque
n = int(input())
stations = deque()
for _ in range(n):
    station = list(map(int, input().split()))
    stations.append(station)
for i in range(n):
    is_valid = True
    gasoline = 0
    for s in range(n):
        current = stations.popleft()
        gasoline += current[0] - current[1]
        if gasoline < 0:
            is_valid = False
        stations.append(current)
    if is_valid:
        print(i)
        break
    stations.append(stations.popleft())

