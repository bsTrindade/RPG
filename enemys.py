class enemy:
    def __init__(self, name, attack, defense, hp):
        self.name = str(name)
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.level = 1
        self.exp = 0
        #self.intelligence = intelligence

    def expMonstro(self):
        return 50 + (self.level - 1) * ((1/100 * 10))
    
    pass

#Enemys ------> enemy_name = ['a Rat', 'a Bat', 'a Slime', 'a Skeleton', 'an Orc', 'a Troll']
enemyRat = enemy('a Rat', 1, 2, 6)
enemyBat = enemy('a Bat', 2, 2, 8)
enemySlime = enemy('a Slime', 1, 6, 10)
enemySkeleton = enemy('a Skeleton', 3, 1, 10)
enemyOrc = enemy('an Orc', 3, 3, 15)
enemyTroll = enemy('a Troll', 5, 3, 10)

list_enemys = [enemyRat, enemyBat, enemySlime, enemySkeleton, enemyOrc, enemyTroll]