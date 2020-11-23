n = int(input())

total = 0

for i in range(n):
    quantity = int(input())
    total += quantity
    if total > 255:
        total -= quantity
        print("Insufficient capacity!")

print(total)


