import random, os

from time import sleep

from characters.hero import Hero
from characters.enemy import Enemy
from battle import Battle

from narrator import cls, narrate
from texts import introduction, name_selection


def boot_screen():
    cls()
    print("""\
      _______   _           _           _        _____  _____   _____ 
     |__   __| (_)         | |         | |      |  __ \|  __ \ / ____|
        | |_ __ _ _ __   __| | __ _  __| | ___  | |__) | |__) | |  __ 
        | | '__| | '_ \ / _` |/ _` |/ _` |/ _ \ |  _  /|  ___/| | |_ |
        | | |  | | | | | (_| | (_| | (_| |  __/ | | \ \| |    | |__| |
        |_|_|  |_|_| |_|\__,_|\__,_|\__,_|\___| |_|  \_\_|     \_____|
                                                                    
    v0.1                                                              
    """)


def select_character():
    narrate(introduction, _should_clear=False)
    player_name = input("\nWhat is your name, adventurer? ")
    char_type = input("Which class will you begin your journey?\n[W] Warrior | [K] Knight | [A] Assassin ")
    narrate(name_selection, _should_clear=False, player_name=player_name)
    return Hero.create_hero(char_type, player_name)
 

if __name__ == "__main__":
    boot_screen()

    hero = select_character()

    while hero.hp > 0:
        enemy = Enemy.encounter(hero.level)
        
        narrate(f'\033[1m{hero.name}\033[m is an {hero.char_name}, in search for a great treasure, hidden ages ago. Passing through a cave, he was attacked by one {enemy.name}.')
        Battle(hero, enemy).fight()
        narrate(f'{hero.name} is level {hero.level}.\nHe has {hero.hp} HP left and has {hero.xp:.0f} exp points')

        sleep(3)

    narrate('YOU DIED')
