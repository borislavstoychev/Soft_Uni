line = input()
matches = []
is_yes = False
if len(line) % 2 == 0:
    for index in range(len(line)):
        if line[index] == "(" or line[index] == "{" or line[index] == "[":
            matches.append(line[index])
        elif line[index] == ")" and len(matches) > 0 or line[index] == "}" and len(matches) > 0 or line[
            index] == "]" and len(matches) > 0:
            match = matches.pop()
            if match == "(" and line[index] == ")" or match == "{" and line[index] == "}" or match == "[" and line[
                index] == "]":
                is_yes = True
            else:
                is_yes = False
                break

if is_yes:
    print("YES")
else:
    print("NO")
