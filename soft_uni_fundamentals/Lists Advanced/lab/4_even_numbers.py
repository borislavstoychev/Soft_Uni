line = [int(nums) for nums in input().split(", ")]

print(list(num for num in range(len(line)) if line[num] % 2 == 0))
