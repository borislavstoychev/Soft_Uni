line = input().split(">")
explode = 0
after_explode = []
for l in line:
    if l[0].isdigit():
        explode += int(l[0])
        if len(l) <= explode:
            explode -= len(l)
            l = ">"
        else:
            l = ">"+"".join(list(l[explode::]))
            explode = 0
    after_explode.append(l)
print("".join(after_explode))


