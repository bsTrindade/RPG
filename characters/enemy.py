import random

from characters import Character

class Enemy(Character):

    def __init__(self, name="", level=1):
        name = self.__class__.__name__
        super().__init__(name, level)

    @classmethod
    def encounter(cls, level):
        enemies = cls.__subclasses__()
        enemy_cls = random.choice(enemies)
        return enemy_cls(level=level)

class Rat(Enemy):
    base_attack = 1
    base_defense = 2
    base_hp = 6

class Bat(Enemy):
    base_attack = 2
    base_defense = 2
    base_hp = 8

class Slime(Enemy):
    base_attack = 1
    base_defense = 6
    base_hp = 10

class Skeleton(Enemy):
    base_attack = 3
    base_defense = 1
    base_hp = 10

class Orc(Enemy):
    base_attack = 3
    base_defense = 3
    base_hp = 15

class Troll(Enemy):
    base_attack = 5
    base_defense = 3
    base_hp = 10
