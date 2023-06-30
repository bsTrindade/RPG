import random, os, character, enemys
from time import sleep
from typetext import narrarTexto as narrar

#from character import player, list_classes

#FUNÇÃO PARA CALCULAR O DANO DOS ATAQUES
def calculateDamage(atkValue, defValue):
    return atkValue - defValue

#FUNÇÃO PARA ENCONTRAR UM INIMIGO PARA LUTAR
def enemyEncounter():
    return random.choice(enemys.list_enemys)

def luta(pc, enem):

    narrar('\nThe battle begins!')
    print('\n\033[1mBATTLE LOG\033[m')

    player_baseAtk = pc.attack
    player_baseDef = pc.defense

    enemy_name = enem.name
    enemy_baseAtk = enem.attack
    enemy_baseDef = enem.defense
    enemy_baseHP = enem.hp

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
            pc.ganhoXP(enem.expMonstro(pc.level))
            narrar('\033[1mBattle over!\033[m\nThe enemy has fallen and {} won the battle.'.format(player_name))
            narrar(f'{player_name} won {enem.exp:.0f} experience points.')

            sleep(3)

            break

        sleep(2)

        enemy_baseAtk = enemy_baseAtk + random.randint(0, 6)
        player_baseDef = player_baseDef + random.randint(0, 4)
        damage = calculateDamage(enemy_baseAtk, player_baseDef)
        if damage <= 0:
            damage = 0
            print("\033[1;31m{}'S ATTACK MISSED\033[m".format((enemy_name.title().split())[1].upper()))
            
        else:
            pc.hp = pc.hp - damage
            print('{} attacked {} and inflicted {} damage. {} HP is now {}.'.format((enemy_name.title().split())[1], player_name, damage, player_name, pc.hp))
        if pc.hp <= 0:

            narrar('\033[1mBattle over!\033[m\n{} has fallen and {} won the battle.'.format(player_name, enemy_name.title().split()[1]))

            sleep(3)

            break
        sleep(2)
    

#ESCOLHA DO PERSONAGEM / CLASSE
player_name = str(input("Adventurer's name: "))
player_character_input = int(input("Which class you'll begin your journey?: \n[1] Warrior [2] Knight [3] Assassin\n"))
player_character = character.list_classes[player_character_input - 1]

# if player_class.level == 1:
#     lvlSys.expPool = 20

os.system("cls")

# narrar('\033[1m{}\033[m is an {}, in search for a great treasure, hidden ages ago.
            
while player_character.hp > 0:
    enemy = enemyEncounter()
    
    narrar('\033[1m{}\033[m is an {}, in search for a great treasure, hidden ages ago. Passing through a cave, he was attacked by {}.'.format(player_name, player_character.name, enemy.name))
    luta(player_character, enemy)
    
    narrar(f'{player_name} is level {player_character.level}.\nHe has {player_character.hp} HP left and has {player_character.exp:.0f} exp points')

    sleep(3)

narrar('YOU DIED')