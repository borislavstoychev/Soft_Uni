commands = input()
while not commands == "end":
    print(f"{commands} = {commands[::-1]}")
    commands = input()