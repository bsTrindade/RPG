import random

from characters.hero import Hero
from characters.enemy import Enemy

from narrator import cls, narrate

class Battle:
    def __init__(self, hero: Hero, enemy: Enemy):
        self.hero = hero
        self.enemy = enemy
        self.log = []

    def write_battle(self, message):
        cls()
        print(f'Hero: {self.hero.name}\t\t\tEnemy: {self.enemy.name}')
        print(f'Level: {self.hero.level}\t\t\tLevel: {self.enemy.level}')
        print(f'HP: {self.hero.hp}\t\t\t\tHP: {self.enemy.hp}')
        print(f'Attack: {self.hero.attack}\t\t\tAttack: {self.enemy.attack}')
        print(f'Defense: {self.hero.defense}\t\t\tDefense: {self.enemy.defense}')

        print('\n\033[1mBATTLE LOG\033[m')
        for l in self.log:
            print(l)

        narrate(message, _should_clear=False)
        self.log.append(message)

    def play_turn(self, attacker, defender):
        attack_value = attacker.attack + random.randint(0,6)
        defense_value = defender.defense + random.randint(0,6)
        damage = max(attack_value - defense_value, 0)

        if not damage:
            message = f"\033[1;31m{attacker.name.upper()}'S ATTACK MISSED\033[m"
            self.write_battle(message)
            return
        
        message = f'{attacker.name} attacked {defender.name} and inflicted {damage} damage.'
        self.write_battle(message)
        defender.hp = max(defender.hp - damage, 0)

        if defender.hp == 0:
            attacker.earn_xp(defender.calculate_fight_xp())


    def fight(self):
        narrate('The battle begins!')
        cls()
        
        attacker, defender = self.hero, self.enemy
        while self.hero.hp and self.enemy.hp:
            self.play_turn(attacker, defender)
            attacker, defender = defender, attacker
        
        if self.enemy.hp == 0:
            self.hero.earn_xp(self.enemy.calculate_fight_xp())
            narrate(f'\033[1mBattle over!\033[m\nThe enemy has fallen and {self.hero.name} won the battle.')
            return

        if self.hero.hp == 0:
            narrate(f'\033[1mBattle over!\033[m\n{self.hero.name} has fallen and {self.enemy.name} won the battle.')
