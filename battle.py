import random
from characters.hero import Hero
from characters.enemy import Enemy
from time import sleep
from narrator import cls, narrate

class Battle:

    def __init__(self, hero: Hero, enemy: Enemy):

        self.hero = hero

        self.enemy = enemy

        self.log = []

    # DISPLAY THE STATUS
    def show_battle_status(self):

        print(f'Hero: {self.hero.name}\t\t\tEnemy: {self.enemy.name}')

        print(f'Level: {self.hero.level}\t\t\tLevel: {self.enemy.level}')

        print(f'HP: {self.hero.hp}/{self.hero.max_hp}\t\t\tHP: {self.enemy.hp}/{self.enemy.max_hp}')

        print(f'Attack: {self.hero.attack}\t\t\tAttack: {self.enemy.attack}')

        print(f'Defense: {self.hero.defense}\t\t\tDefense: {self.enemy.defense}')

    # DISPLAY THE LOG OF THE ACTIONS
    def write_battle(self, message):

        cls()

        self.show_battle_status()

        print('\n\033[1mBATTLE LOG\033[m')
        
        for l in self.log[-5:]:

            print(l)

        narrate(message, _should_clear=False)

        self.log.append(message)
    
    # LETS THE PLAYER CHOOSE THE ACTION
    def choose_action(self):

        cls()

        self.show_battle_status()

        action = int(input('\nPLAYER TURN:\n|1| ATTACK\n|2| ITENS \n|3| FLEE\n'))

        if action > 3 or action <= 0:

              self.choose_action()

        return action

    # CALCULATES THE DAMAGE BETWEEN ATTACK AND DEFENSE VALUES
    def calculate_damage(self, attacker, defender):

        attack_value = attacker.attack + random.randint(0, 6)

        defense_value = defender.defense + random.randint(0, 3)

        damage = max(attack_value - defense_value, 0)

        return damage

    #FUNCTION THAT DETERMINES IF THE ATTEMPT TO FLEE WAS SUCCESFULL
    def try_to_flee(self, attacker, defender):
        
        flee_chance = attacker.attack - defender.attack

        flee_number = random.randint(0, 30) + flee_chance

        if flee_number > 20:

            fled_from_battle = f'{attacker.name} fled succesfully!'

            narrate(fled_from_battle)

            sleep(1.5)

            return fled_from_battle
        
        else:

            fled_from_battle = "Couldn't flee from the battle."

            narrate(fled_from_battle)

            sleep(1.5)

            return fled_from_battle

    # PLAY THE TURN
    def play_turn(self, attacker, defender):
        
        damage = 0

        if attacker.__module__ == 'characters.hero':
            
            action = self.choose_action()

            if action == 1:

                damage = self.calculate_damage(attacker, defender)

                sleep(.4)

            elif action == 2:

                is_inventory_not_empty = attacker.inventory.check_if_inventory_is_not_empty()

                if is_inventory_not_empty:

                    attacker.inventory.show_inventory(use_item=True)

                else:

                    narrate('Inventory is Empty', blink = True)

                    self.play_turn(attacker, defender)
                
            else:
                
                fled_from_battle = self.try_to_flee(attacker, defender)

                return fled_from_battle
                
        if attacker.__module__ == 'characters.enemy':
            
                damage = self.calculate_damage(attacker, defender)

                sleep(.4)

        if not damage:
            
            message = f"\033[1;31m{attacker.name.upper()}'S ATTACK MISSED\033[m"

            self.write_battle(message)

            sleep(0.5)

            return
        
        message = f'{attacker.name} attacked {defender.name} and inflicted {damage} damage.'

        self.write_battle(message)

        defender.hp = max(defender.hp - damage, 0)

        if defender.hp == 0:

            attacker.earn_xp(defender.calculate_fight_xp())

        sleep(0.5)

    # THE FIGHT ITSELF
    def fight(self, player):

        narrate('The battle begins!', blink=True)

        cls()
        
        attacker, defender = self.hero, self.enemy

        while self.hero.hp and self.enemy.hp:

            turn = self.play_turn(attacker, defender)

            if turn == f'{player.name} fled succesfully!':

                break

            attacker, defender = defender, attacker

        if self.enemy.hp == 0:

            self.hero.earn_xp(self.enemy.calculate_fight_xp())

            item_droped = self.enemy.drop_items()

            narrate(f'\033[1mBattle over!\033[m\nThe enemy has fallen and {self.hero.name} won the battle.', blink=3)

            sleep(0.3)

            narrate(f'{self.hero.name} is level {self.hero.level}.\nHe has {self.hero.hp} HP left and has {self.hero.xp:.0f} exp points', blink=3)

            sleep(0.3)

            self.hero.inventory.add_item(item_droped, item_droped.get_quantity())

        if self.hero.hp == 0:

            narrate(f'\033[1mBattle over!\033[m\n{self.hero.name} has fallen and {self.enemy.name} won the battle.', blink=3)

            sleep(0.3)


if __name__ == "__main__":

    from time import sleep

    import choose_action
    class Player():
        def __init__(self, atk, deffense, hp):
            self.atk = atk
            self.deffense = deffense
            self.hp = hp
            self.name = "Lulu"

    class Enemy():
        def __init__(self, atk, deffense, hp):
            self.atk = atk
            self.deffense = deffense
            self.hp = hp
            self.name = "Bat"

    def choose_action():

        action = int(input(('|1| Attack\t|2| Flee: ')))
        return action

    player = Player(10, 9, 20)

    def battle_(player):

        enemy = Enemy(10, 9, 20)

        attacker, defender = player, enemy

        while defender.hp > 0:
            print(f'Attacker HP = {attacker.hp}\nDefender HP = {defender.hp}')
            sleep(1)

            if type(attacker).__name__ == 'Player':

                action = choose_action()
                if action == 1:

                    damage = attacker.atk - defender.deffense
                    defender.hp -= damage
                    print(f"{attacker.name} hit for {damage} damage.")
                    sleep(.5)
                    
                    attacker, defender = defender, attacker
                
                else:
                    break

            else:
                damage = attacker.atk - defender.deffense
                defender.hp -= damage
                print(f"{attacker.name} hit for {damage} damage.")
                sleep(.5)
                attacker, defender = defender, attacker

    while True:

        battle_(player)

        x = input('Batalhar novamente? Sim Não\n')
        
        if x[0].upper() == "N":
            break

