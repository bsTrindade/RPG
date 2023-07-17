from time import sleep
from narrator import narrate

class player:
    def __init__(self, name, attack, defense, hp):
        self.name = str(name)
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.baseHP = hp
        self.level = 1
        self.exp = 0
        #self.intelligence = intelligence

    def expLevelUp(self):
        return 100 * (1 + ((self.level - 1) * ((1/100 * 15))))

    def ganhoXP(self, exp):
        self.exp += exp
        necessary_exp = self.expLevelUp()
        if self.exp >= necessary_exp:
            extra_exp = self.exp - necessary_exp
            self.LevelUp(extra_exp)

    def LevelUp(self, extra_exp):
        self.level += 1
        self.exp = extra_exp
        self.statsUp(self.name)

        narrate(f'You character Leveled UP!\nYour HP is now fully recovered!\nAttack is now {self.attack}\nDefense is now {self.defense}.\nHP is now {self.hp}.')
        sleep(3)

    def statsUp(self, name):
        match name:
            case 'Warrior':
                self.attack += 2
                self.defense += 1
                self.hp = self.baseHP + 4 * (self.level - 1)
            case 'Knight':
                self.attack += 1
                self.defense += 3
                self.hp = self.baseHP + 5 * (self.level - 1)
            case 'Assassin':
                self.attack += 4
                self.defense += 1
                self.hp = self.baseHP + 3 * (self.level - 1)


#Playable classes
classWarrior = player('Warrior', 4, 2, 20)
classKnight = player('Knight', 2, 5, 20)
classAssassin = player('Assassin', 6, 1, 15)

list_classes = [classWarrior, classKnight, classAssassin]