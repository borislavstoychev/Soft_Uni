even_set = set()
odd_set = set()
for line in range(int(input())):
    name = sum(map(ord, input()))
    result = name // (line + 1)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
sum_even = sum(even_set)
sum_odd = sum(odd_set)
if sum_even == sum_odd:
    print(*even_set | odd_set, sep=", ")
elif sum_odd > sum_even:
    print(*odd_set - even_set, sep=", ")
elif sum_odd < sum_even:
    print(*even_set ^ odd_set, sep=", ")