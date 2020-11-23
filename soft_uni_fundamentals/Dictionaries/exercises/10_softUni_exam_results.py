class Statistics:
    def __init__(self):
        self.languages = {}
        self.points = {}

    def store(self, name, language, points):
        if language not in self.languages:
            self.languages[language] = [name]
        else:
            self.languages[language] += [name]
        if name not in self.points:
            self.points[name] = [points]
        else:
            self.points[name] += [points]

    def ban(self, name):
        if name in self.points:
            self.points.pop(name)

    def max_points(self):
        for (k, v) in self.points.items():
            self.points[k] = max(v)
        return self.points

    def get_info(self):
        print("Results:")
        for (k, v) in dict(sorted(self.points.items(), key=lambda el: (-el[1], el[0]))).items():
            print(f"{k} | {v}")
        print("Submissions:")
        for (k, v) in dict(sorted(self.languages.items(), key=lambda el: (-len(el[1]), el[0]))).items():
            print(f"{k} - {len(v)}")
        return exit()


soft_uni = Statistics()

while True:
    commands = input()
    if commands == "exam finished":
        soft_uni.max_points()
        soft_uni.get_info()
    try:
        name, language, points = commands.split("-")
        points = int(points)
    except ValueError:
        name, command = commands.split("-")
        if command == "banned":
            soft_uni.ban(name)
    else:
        soft_uni.store(name, language, points)
