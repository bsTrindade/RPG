import random, os, character, enemys
from time import sleep


#from character import player, list_classes

#FUNÇÃO PARA MOSTRAR TEXTO DE FORMA NARRATIVA
def narrarTexto (texto):
    texto_1 = ''
    n = 0
    while n <= 2:
        print('\033[7m \033[m')
        sleep(.3)
        os.system("cls")
        print(' \033[m')
        sleep(.3)
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
        sleep(.3)
        os.system("cls")
        print(texto_1, end='')
        print(' \033[m')
        sleep(.3)
        os.system("cls")
        n = n + 1

#FUNÇÃO PARA CALCULAR O DANO DOS ATAQUES
def calculateDamage(atkValue, defValue):
    return atkValue - defValue

#FUNÇÃO PARA ENCONTRAR UM INIMIGO PARA LUTAR
def enemyEncounter():
    return random.choice(enemys.list_enemys)

def luta(pc, enem):

    print('\nThe battle begins!')
    print('\n\033[1mBATTLE LOG\033[m')

    player_baseAtk = pc.attack
    player_baseDef = pc.defense
    #player_baseHP = pc.hp

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
            print('\033[1mBattle over!\033[m The enemy has fallen and {} won the battle.'.format(player_name))
            pc.ganhoXP(enem.expMonstro())
            
            break

        sleep(1.5)

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

            print('\033[1mBattle over!\033[m {} has fallen and {} won the battle.'.format(player_name, enemy_name.title().split()[1]))
            break
        sleep(1.5)
    

#ESCOLHA DO PERSONAGEM / CLASSE
player_name = str(input("Adventurer's name: "))
player_character_input = int(input("Which class you'll begin your journey?: \n[1] Warrior [2] Knight [3] Assassin\n"))
player_character = character.list_classes[player_character_input - 1]

# if player_class.level == 1:
#     lvlSys.expPool = 20

os.system("cls")

# narrarTexto('\033[1m{}\033[m is an {}, in search for a great treasure, hidden ages ago.
            
while player_character.hp > 0:
    enemy = enemyEncounter()
    
    narrarTexto('\033[1m{}\033[m is an {}, in search for a great treasure, hidden ages ago. Passing through a cave, he was attacked by {}.'.format(player_name, player_character.name, enemy.name))
    luta(player_character, enemy)
    
    print(f'{player_name} is level {player_character.level}.\nHe has {player_character.hp} HP left and has {player_character.exp:.0f} exp points')

    sleep(2)

print('YOU DIED')