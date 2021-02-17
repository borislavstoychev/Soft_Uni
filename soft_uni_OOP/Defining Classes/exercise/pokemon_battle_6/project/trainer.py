class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name not in pokemon_names:
            return "Pokemon is not caught"
        del self.pokemon[pokemon_name.index(pokemon_name)]
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        data =  f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        pokemons = [f"- {pokemon.pokemon_details()}" for pokemon in self.pokemon]
        return data + "\n".join(pokemons) + "\n"


