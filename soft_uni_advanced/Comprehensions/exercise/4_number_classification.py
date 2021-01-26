numbers = [int(n) for n in input().split(", ")]
print("Positive: ", end="")
print(*[p for p in numbers if p >= 0], sep=", ")
print("Negative: ", end="")
print(*[n for n in numbers if n < 0], sep=", ")
print("Even: ", end="")
print(*[e for e in numbers if e % 2 == 0], sep=", ")
print("Odd: ", end="")
print(*[o for o in numbers if not o % 2 == 0], sep=", ")