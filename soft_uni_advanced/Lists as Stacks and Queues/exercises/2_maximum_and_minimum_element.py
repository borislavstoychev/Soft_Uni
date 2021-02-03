n = int(input())
numbers = []
for _ in range(n):
    nums = input().split()
    num = nums[0]
    if num == "1":
        num = nums[1]
        numbers.append(int(num))
    elif num == "2" and len(numbers) > 0:
        numbers.pop()
    elif num == "3" and len(numbers) > 0:
        print(max(numbers))
    elif num == "4" and len(numbers) > 0:
        print(min(numbers))
print(", ".join(reversed(list(map(str, numbers)))))
