class ForceBook:
    def __init__(self):
        self.force_book = {}
        self.all_users = []

    def side_user(self, side, user):
        self.all_users = [person for users in self.force_book.values() for person in users]
        if user not in self.all_users:
            if side in self.force_book:
                self.force_book[side].append(user)
            else:
                self.force_book[side] = [user]

    def user_side(self, user, side):
        for (k, v) in self.force_book.items():
            if user in v:
                self.force_book[k].remove(user)
                if len(self.force_book[k]) == 0:
                    self.force_book.pop(k)
                    break
        if side in self.force_book:
            self.force_book[side] += [user]
            print(f"{user} joins the {side} side!")
        else:
            self.force_book[side] = [user]
            print(f"{user} joins the {side} side!")

    def get_info(self):
        for (key, value) in dict(sorted(self.force_book.items(), key=lambda el: (-len(el[1]), el[0]))).items():
            if not len(value) == 0:
                print(f"Side: {key}, Members: {len(value)}")
                print('!' + ' ' + "\n! ".join(sorted(value)))
        return exit()


f_b = ForceBook()
while True:
    line = input()
    if line == "Lumpawaroo":
        f_b.get_info()
    if "|" in line:
        side, user = line.split(" | ")
        f_b.side_user(side, user)
    elif "->" in line:
        user, side = line.split(" -> ")
        f_b.user_side(user, side)
