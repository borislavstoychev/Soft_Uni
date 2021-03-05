class Team:
    name: str
    rating: int
    players: []

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    @name.setter
    def name(self, value):
        self.__name = value

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        player_to_remove = [player for player in self.__players if player.name == player_name]
        if player_to_remove:
            self.__players.remove(player_to_remove[0])
            return player_to_remove[0]
        return f"Player {player_name} not found"

