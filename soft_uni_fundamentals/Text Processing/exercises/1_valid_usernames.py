users = input().split(", ")
for user in users:
    if 3 <= len(user) <= 16:
        for i in user:
            if not (i.isalpha() or i.isdigit() or i == chr(45) or i == chr(95)):
                break
        else:
            print(user)
