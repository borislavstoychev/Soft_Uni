def get_info(my_dict):
    for (key, value) in dict(sorted(my_dict.items(), key=lambda el: -len(el[1]))).items():
        print(f'{key}: {len(value)}')
        print('--' + ' ' + "\n-- ".join(sorted(value)))
    return exit()


curses = {}
while True:
    line = input()
    if line == "end":
        get_info(curses)
    curse_name, user_name = line.split(" : ")
    if curse_name not in curses:
        curses[curse_name] = [user_name]
    else:
        curses[curse_name] += [user_name]
