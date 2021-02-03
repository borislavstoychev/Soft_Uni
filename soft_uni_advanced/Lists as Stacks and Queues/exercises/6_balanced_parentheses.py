line = input()
matches = []
is_yes = False
mirrors = {"{": "}", "[": "]", "(": ")"}

for index in range(len(line)):
    if line[index] in "({[":
        matches.append(line[index])
    else:
        if not matches:
            is_yes = False
            break
        match = matches.pop()
        if mirrors[match] == line[index]:
            is_yes = True
        else:
            is_yes = False
            break
if is_yes:
    print("YES")
else:
    print("NO")
