read = list(map(int, input().split()))

read = [number for number in read if number > sum(read) / len(read)]
read = sorted(read, reverse=True)

if len(read) == 0:
    print("No")
else:
    print(" ".join(list(map(str, read[:5]))))
