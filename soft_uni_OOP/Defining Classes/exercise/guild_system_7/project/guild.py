# from player import *


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != self.name and player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        self.list_of_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_names = [p.name for p in self.list_of_players]
        if player_name not in player_names:
            return f"Player {player_name} is not in the guild."
        else:
            del self.list_of_players[player_name.index(player_name)]
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self,):
        data = f"Guild: {self.name}\n"
        resources = [player.player_info() for player in self.list_of_players]
        return data + "\n".join(resources)





# player = Player("Pesho", 90, 90)
# expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n"
# print(player.player_info())
#
#
# player = Player("Pesho", 90, 90)
# message = player.add_skill("A", 3)
# expected = "Skill A added to the collection of the player Pesho"
# print(message)
#
# player = Player("Pesho", 90, 90)
# player.add_skill("A", 3)
# message = player.add_skill("A", 3)
# expected = "Skill already added"
# print(message)
#
# player = Player("Pesho", 90, 90)
# player.add_skill("A", 3)
# message = player.player_info()
# expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3\n"
# print(message)
#
# guild = Guild("GGXrd")
# message = guild.guild_info()
# expeted = "Guild: GGXrd\n"
# print(message)
#
# #
# guild = Guild("GGXrd")
# player = Player("Pesho", 90, 90)
# player.add_skill("A", 3)
# player.add_skill("B", 3)
# message = guild.assign_player(player)
# expected = "Welcome player Pesho to the guild GGXrd"
# print(guild.guild_info())
#
# guild = Guild("GGXrd")
# player = Player("Pesho", 90, 90)
# guild.assign_player(player)
# message = guild.assign_player(player)
# expected = "Player Pesho is already in the guild."
# print(message)
#
#
