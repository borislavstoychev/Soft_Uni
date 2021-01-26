def get_result(commands, nums):
    if commands == "Odd":
        result = sum([n for n in nums if not n % 2 == 0])
    else:
        result = sum([e for e in nums if e % 2 == 0])
    return result * len(nums)


command = input()
numbers = [int(n) for n in input().split()]
print(get_result(command, numbers))