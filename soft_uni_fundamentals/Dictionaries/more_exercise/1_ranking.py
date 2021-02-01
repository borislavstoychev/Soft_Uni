lines = input()
contests = {}
while not lines == "end of contests":
    contest, password = lines.split(":")
    contests[contest] = password
    lines = input()

user_result = input()
users_results = {}
while not user_result == "end of submissions":
    contest, password, username,  points = user_result.split("=>")
    points = int(points)
    if contest in contests and contests[contest] == password:
        if username not in users_results:
            users_results[username] = {contest: points}
        else:
            if contest in users_results[username]:
                if users_results[username][contest] < points:
                    users_results[username][contest] = points
            else:
                users_results[username][contest] = points
    user_result = input()

best_score = {}
for (key, value) in users_results.items():
    score = 0
    for k, v in value.items():
        score += v
    best_score[key] = score

max_score = max(best_score, key=lambda x: best_score[x])
print(f"Best candidate is {max_score} with total {best_score[max_score]} points.")
print("Ranking:")
for (user, data) in sorted(users_results.items()):
    print(user)
    for contest_n, result in dict(sorted(data.items(), key=lambda x: (-x[1]))).items():
        print(f"#  {contest_n} -> {result}")