collect = {}
count = 0
key = ""
while True:
    count += 1
    line = input()
    if line == "stop":
        break
    if count % 2 == 0:
        value = int(line)
        if key not in collect:
            collect[key] = value
        else:
            collect[key] += value
    else:
        key = line
for (key, value) in collect.items():
    print(f"{key} -> {value}")
