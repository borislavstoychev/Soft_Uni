lower = 'abcdefghijklmnopqrstuvwxyz'
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lines = input().split()
action = 0
total = 0
for line in lines:
    first_letter = line[0]
    last_letter = line[-1]
    action = int(line[1:-1])
    if first_letter in upper:
        action /= (upper.index(first_letter) + 1)
    elif first_letter in lower:
        action *= (lower.index(first_letter) + 1)
    if last_letter in upper:
        action -= upper.index(last_letter) + 1
    elif last_letter in lower:
        action += lower.index(last_letter) + 1
    total += action

print(f"{total:.2f}")
