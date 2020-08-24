import pokemon_functions, pokemon_characters
from random import randrange

class Pokemon:
    def __init__(self, name):
        if not name in pokemon_characters.characters:
            raise ValueError("The Character you have summoned does not exist. Check your spelling and try again")
        self.name = name
        self.level = 1
        self.xp = 0
        self.type = pokemon_characters.characters[name]['type']
        self.current_health = 0
        self.ko = False
        self.max_health = (
            (((pokemon_characters.characters[self.name]['base_hp'] + 7) * 2
            + ((pokemon_characters.characters[self.name]['effort_value'] **.5) / 4) * self.level) / 100)
            + self.level + 10
            )
        self.attack = 0
        self.defense = 0

    def __repr__(self):
        return "You have initialized {name} of the {type} type as your Pokemon! Good Luck! It has {health} health.".format(name=self.name, type=self.type, health=int(self.max_health))

    # Function to reducing Pokemon health
    def lose_hp(self, health):
        new_hp = 0
        return new_hp
    # Function for increasing Pokemon health
    def add_hp(self, health):
        new_hp = 0
        return new_hp
    # Function for knocking out a Pokemon
    def knock_out(self):
        pass
    # Function to revive a Pokemon
    def revive(self):
        pass
    '''
    All of these methods had print statements to let the user know what was happening.
    For example, we might print something like "Charmander now has 30 health" when healing.
    '''
    # Attack Method
    def attack(self, opponent, damage):
        ((2 * level) / (5 + 2) * )

# Debug Statements
print(Pokemon('Pikachu'))