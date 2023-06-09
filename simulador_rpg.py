import random, os, classes
import lvlSys 
from time import sleep

def narrarTexto (texto):
    texto_1 = ''
    n = 0
    while n <= 2:
        print('\033[7m \033[m')
        sleep(.6)
        os.system("cls")
        print(' \033[m')
        sleep(.6)
        os.system("cls")
        n = n + 1
    n = 0
    while n < len(texto):
        texto_1 = texto_1 + texto[n]
        os.system("cls")
        
        print('{}\033[7m \033[m'.format(texto_1))

        n = n + 1
    
        sleep(.005)
    n = 0
    os.system("cls")
    while n <= 2:
        print(texto_1, end='')
        print('\033[7m \033[m')
        sleep(.6)
        os.system("cls")
        print(texto_1, end='')
        print(' \033[m')
        sleep(.6)
        os.system("cls")
        n = n + 1

def calculateDamage(atkValue, defValue):
    return atkValue - defValue


player_name = str(input("Adventurer's name: "))
player_class = int(input("Which class you'll begin your journey?: \n[1] Warrior [2] Knight [3] Assassin\n"))
player_class = classes.list_classes[player_class - 1]

player_baseAtk = player_class.attack
player_baseDef = player_class.defense
player_baseHP = player_class.hp

enemy = random.choice(classes.list_enemys)
enemy_name = enemy.name

enemy_baseAtk = enemy.attack
enemy_baseDef = enemy.defense
enemy_baseHP = enemy.hp

if player_class.level == 1:
    lvlSys.expPool = 20

os.system("cls")

narrarTexto('\033[1m{}\033[m is an {}, in search for a great treasure, hidden ages ago. Passing through a cave, he was attacked by {}.'.format(player_name, player_class.name, enemy_name))

print('\nThe battle begins!')
print('\n\033[1mBATTLE LOG\033[m')

while True:
    
    player_baseAtk = player_baseAtk + random.randint(0, 6)
    enemy_baseDef = enemy_baseDef + random.randint(0, 4)
    damage = calculateDamage(player_baseAtk, enemy_baseDef)
    if damage <= 0:
        damage = 0
        print("\033[1;31m{}'S ATTACK MISSED\033[m".format(player_name.upper()))
    else:
        enemy_baseHP = enemy_baseHP - damage
        print('{} attacked {} and inflicted {} damage. {} HP is now {}.'.format(player_name, (enemy_name.title().split())[1], damage, enemy_name, enemy_baseHP))
    if enemy_baseHP <= 0:
        enemy_baseHP = 0
        print('\033[1mBattle over!\033[m The enemy has fallen and {} won the battle.'.format(player_name))

        lvlSys.expWon(enemy, player_class)

        break

    sleep(1.5)

    enemy_baseAtk = enemy_baseAtk + random.randint(0, 6)
    player_baseDef = player_baseDef + random.randint(0, 4)
    damage = calculateDamage(enemy_baseAtk, player_baseDef)
    if damage <= 0:
        damage = 0
        print("\033[1;31m{}'S ATTACK MISSED\033[m".format((enemy_name.title().split())[1].upper()))
        
    else:
        player_baseHP = player_baseHP - damage
        print('{} attacked {} and inflicted {} damage. {} HP is now {}.'.format((enemy_name.title().split())[1], player_name, damage, player_name, player_baseHP))
    if player_baseHP <= 0:

        print('\033[1mBattle over!\033[m {} has fallen and {} won the battle.'.format(player_name, enemy_name.title().split()[1]))
        break
    sleep(1.5)