guests = set(input()for _ in range(int(input())))
all_guest = set()
line = input()
while not line == "END":
    all_guest.add(line)
    line = input()
undefined = guests - all_guest
print(len(undefined))
print(*sorted(undefined), sep="\n")
