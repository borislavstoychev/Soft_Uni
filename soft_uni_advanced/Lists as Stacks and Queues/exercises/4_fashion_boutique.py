numbers = list(map(int, input().split()))
capacity = int(input())
summary = 0
racks = []
while numbers:
    dress = numbers.pop()
    summary += dress
    if summary > capacity:
        numbers.append(dress)
        racks.append(summary)
        summary = 0
    elif summary == capacity:
        racks.append(summary)
        summary = 0
if not summary == 0:
    racks.append(summary)
    summary = 0
print(len(racks))
