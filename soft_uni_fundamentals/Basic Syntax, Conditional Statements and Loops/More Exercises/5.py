activity = input()

coffee = 0

events = ["coding", "dog", "cat", "movie"]
while activity != "END":
    for i in range(len(events)):
        if activity == events[i]:
            coffee += 1
        elif activity == events[i].upper():
            coffee += 2
    activity = input()

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")