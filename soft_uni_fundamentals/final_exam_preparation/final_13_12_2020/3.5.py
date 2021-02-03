n = int(input())
lines = input()
users = {}
while not lines == "Statistics":
    commands = lines.split("=")[0]
    if commands == "Add":
        user, sent, received = lines.split("=")[1:]
        sent, received = int(sent), int(received)
        if user not in users and sent + received < n:
            users[user] = {"Sent": sent, "Received": received}
    elif commands == "Message":
        sender, receiver = lines.split("=")[1:]
        if sender in users and receiver in users:
            users[sender]["Sent"] += 1
            users[receiver]["Received"] += 1
            if users[sender]["Sent"] + users[sender]["Received"] >= n:
                print(f"{sender} reached the capacity!")
                del users[sender]
            if users[receiver]["Received"] + users[receiver]["Sent"] >= n:
                print(f"{receiver} reached the capacity!")
                del users[receiver]
    elif commands == "Empty":
        name = lines.split("=")[1]
        if name in users:
            del users[name]
        elif name == "All":
            users.clear()
    lines = input()
print(f"Users count: {len(users)}")
for key, value in dict(sorted(users.items(), key=lambda el: (-el[1]["Received"], el[0]))).items():
    print(f"{key} - {value['Sent'] + value['Received']}")
