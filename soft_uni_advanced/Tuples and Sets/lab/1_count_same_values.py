numbers = list(map(float, input().split()))
set_numbers = []
for number in numbers:
    if number not in set_numbers:
        set_numbers.append(number)
for n in set_numbers:
    print(f"{n} - {numbers.count(n)} times")