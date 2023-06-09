#Definir stats
class stats:
    def __init__(self, name, attack, defense, hp, level, exp):
        self.name = str(name)
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.level = level
        self.exp = exp
        #self.intelligence = intelligence
    pass

#Playable classes
classWarrior = stats('Warrior', 4, 2, 20, 1, 0)
classKnight = stats('Knight', 2, 5, 20, 1, 0)
classAssassin = stats('Assassin', 6, 1, 15, 1, 0)

list_classes = [classWarrior, classKnight, classAssassin]

#Enemys ------> enemy_name = ['a Rat', 'a Bat', 'a Slime', 'a Skeleton', 'an Orc', 'a Troll']
enemyRat = stats('a Rat', 1, 2, 6, 1, 3)
enemyBat = stats('a Bat', 2, 2, 8, 1, 4)
enemySlime = stats('a Slime', 1, 6, 10, 1, 5)
enemySkeleton = stats('a Skeleton', 3, 1, 10, 1, 5)
enemyOrc = stats('an Orc', 3, 3, 15, 1, 8)
enemyTroll = stats('a Troll', 5, 3, 10, 1, 12)

list_enemys = [enemyRat, enemyBat, enemySlime, enemySkeleton, enemyOrc, enemyTroll]