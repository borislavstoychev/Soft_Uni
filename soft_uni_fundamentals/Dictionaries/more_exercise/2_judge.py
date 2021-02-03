line = input()
judge = {}
individual_standings = {}
while not line == "no more time":
    username, contest, points = line.split(" -> ")
    points = int(points)
    if contest not in judge:
        judge[contest] = {username: points}
    else:
        if username in judge[contest]:
            if judge[contest][username] < points:
                judge[contest][username] = points
        else:
            judge[contest].update({username: points})

    line = input()
for key, value in judge.items():
    print(f"{key}: {len(value)} participants")
    count = 0
    for name, result in dict(sorted(value.items(), key=lambda x: (-x[1], x[0]))).items():
        count += 1
        print(f"{count}. {name} <::> {result}")
        if name not in individual_standings:
            individual_standings[name] = result
        else:
            individual_standings[name] += result
print("Individual standings:")
count2 = 0
for user, total_result in dict(sorted(individual_standings.items(), key=lambda x: (-x[1], x[0]))).items():
    count2 += 1
    print(f"{count2}. {user} -> {total_result}")