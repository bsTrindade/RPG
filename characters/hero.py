from characters import Character

class Hero(Character):

    @classmethod
    def create_hero(cls, char_type, name):
        heroes = {c.__name__[0].lower(): c for c in cls.__subclasses__()}
        hero_class = heroes[char_type[0].lower()]
        return hero_class(name)

class Warrior(Hero):
    base_attack = 4
    base_defense = 2
    base_hp = 20

class Knight(Hero):
    base_attack = 2
    base_defense = 5
    base_hp = 20

class Assassin(Hero):
    base_attack = 6
    base_defense = 1
    base_hp = 15