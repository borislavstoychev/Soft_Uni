class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        data = f"Name: {self.name}\nGuild: {self.guild}\n HP: {self.hp}\n MP: {self.mp}\n"
        skills = {f"==={key} – {value}" for key, value in self.skills.items()}
        return data + "\n".join(skills) + "\n"


