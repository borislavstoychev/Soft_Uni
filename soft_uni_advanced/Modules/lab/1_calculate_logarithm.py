from math import log


num = int(input())
base = input()

if base == "natural":
    print(f"{log(num):.2f}")
else:
    base = float(base)
    print(f"{log(num, base):.2f}")
