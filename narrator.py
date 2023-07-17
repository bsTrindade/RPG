import os, sys
from time import sleep

#LIMPA O CONSOLE
##SE WINDOWS CLS, SENÃO CLEAR
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#ESCREVE A NARRAÇÃO DE LETRA EM LETRA
def print_message_and_sleep(message):
    print(message, end='')
    sys.stdout.flush()
    sleep(.015)

#QUADRADO QUE PISCA IMITANDO CONSOLE
def blink_square():
    n = 0
    while n < 4:
        print('\033[7m \b', end='')
        sys.stdout.flush()
        sleep(.48)
        print('\033[m \b', end='')
        sys.stdout.flush()
        sleep(.48)
        n += 1


#CHAMA A NARRAÇÃO
def narrate(message, _should_clear=True, speaker=False, *args, **kwargs):
    if _should_clear:
        cls()

    if speaker:
        print(f'\033[1;34m{speaker}:\033[m')
        sys.stdout.flush()
        
    composed_message = f'{message.format(*args, **kwargs)}' 
    for letter in composed_message:
        print_message_and_sleep(letter)

    sleep(.15)

def narrate_combat_message(message, hero, enemy):
    pass

#ESPAÇO PARA TESTES
if __name__ == '__main__':

    narrate('teste teste teste', speaker="Lola")
    blink_square()