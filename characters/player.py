from time import sleep
from narrator import narrate
from items import inventory

class player:
    def __init__(self, name, attack, defense, hp):
        self.name = str(name)
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.baseHP = hp
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.inventory = inventory(self.name, capacity=20)
        #self.intelligence = intelligence

    def exp_to_level_up(self, exp_to_next_level):
        exp_to_next_level = self.exp_to_next_level * (1 + ((self.level - 1) * ((1/100 * 15))))
        return exp_to_next_level

    def ganhoXP(self, battle_exp):
        self.exp += battle_exp
        necessary_exp = self.exp_to_level_up()
        if self.exp >= necessary_exp:
            extra_exp = self.exp - necessary_exp
            self.LevelUp(extra_exp, necessary_exp)

    def LevelUp(self, extra_exp):
        self.level += 1
        self.exp = extra_exp
        self.statsUp(self.name)
        self.exp_to_next_level = self.exp_to_level_up()

        narrate(f'You character Leveled UP!\nHP is now fully recovered!\nAttack is now {self.attack}\nDefense is now {self.defense}.\nHP is now {self.hp}.')
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

if __name__ == '__main__':

#Playable classes

classWarrior = player('Warrior', 4, 2, 20)
classKnight = player('Knight', 2, 5, 20)
classAssassin = player('Assassin', 6, 1, 15)

list_classes = [classWarrior, classKnight, classAssassin]

classAssassin.inventory.add_item('ITEM 1', qtd=2)

classAssassin.inventory.show_inventory()