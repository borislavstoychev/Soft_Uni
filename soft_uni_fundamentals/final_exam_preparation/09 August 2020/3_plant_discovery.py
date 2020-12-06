class Plant:
    def __init__(self):
        self.plant_rarity = {}
        self.plant_rating = {}

    def plants(self, plant, rarity):
        self.plant_rarity[plant] = [rarity]
        self.plant_rating[plant] = []

    def rate_plant(self, plant_r, rating):
        if plant_r in self.plant_rarity:
            if plant_r not in self.plant_rating:
                self.plant_rating[plant_r].
            else:
                self.plant_rating[plant_r].append(rating)
        else:
            print("error")

    def update(self, plant_u, new_rarity):
        if plant_u in self.plant_rarity:
            self.plant_rarity[plant_u] = [int(new_rarity)]
        else:
            print("error")

    def reset(self, plant_to_reset):
        if plant_to_reset in self.plant_rating:
            self.plant_rating[plant_to_reset] = [0]
        else:
            print("error")

    def get_info(self, ):
        for (kay, value) in self.plant_rating.items():
            if not len(value) == 0:
                self.plant_rating[kay] = (sum(value) / len(value))


        # print("Plants for the exhibition:")
        # for (key, value) in dict(sorted(self.plant_rarity.items(), key=lambda el: (-el[1][0], -el[1][1]))).items():
        #     print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
        return exit()


n = int(input())
p = Plant()
for _ in range(n):
    line = input().split("<->")
    plant, rarity = line[::]
    rarity = int(rarity)
    p.plants(plant, rarity)

while True:
    commands = input()
    if commands == "Exhibition":
        p.get_info()
    command, token = commands.split(": ")[::]
    token = str(token)
    if command == "Rate":
        plant_r, rating = token.split(" - ")
        rating = int(rating)
        p.rate_plant(plant_r, rating)
    elif command == "Update":
        plant_u, new_rarity = token.split(" - ")
        p.update(plant_u, new_rarity)
    elif command == "Reset":
        plant_to_reset = token
        p.reset(plant_to_reset)

