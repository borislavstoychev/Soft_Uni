information = {}

while True:
    line = input()
    if line == "End":
        for (key, value) in dict(sorted(information.items(), key=lambda el: el[0])).items():
            print(f'{key}')
            print('--' + ' ' + "\n-- ".join(value))
        exit()
    name, id_employ = line.split(" -> ")
    if name not in information:
        information[name] = [id_employ]
    else:
        if id_employ not in information[name]:
            information[name] += [id_employ]
