from math import ceil

numbers = list(map(int, input().split(', ')))

for i in range(1, ceil(max(numbers) / 10) + 1):
    result = [nums for nums in numbers if nums in range(i * 10 - 9, i * 10 + 1)]
    print(f"Group of {i * 10}'s: {result}")
