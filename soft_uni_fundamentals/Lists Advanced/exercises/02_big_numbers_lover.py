number = input().split()
number = int("".join(sorted(number, reverse=True)))
print(number)
