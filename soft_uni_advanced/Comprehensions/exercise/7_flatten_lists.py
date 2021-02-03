numbers = [x for x in input().split('|')]
nums = reversed([n.split() for n in numbers])
num = [val for sublist in nums for val in sublist]
print(*num, sep=" ")

