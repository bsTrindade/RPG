import os, sys
from time import sleep

def __init__():
    pass

#LIMPA O CONSOLE
##SE WINDOWS CLS, SENÃO CLEAR

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#ESCREVE A NARRAÇÃO DE LETRA EM LETRA
def print_message_and_sleep(message):
    print(message, end='')
    sys.stdout.flush()
    sleep(.012)

#QUADRADO QUE PISCA IMITANDO CONSOLE
def blink_square(times):
    n = 0
    while n < times:
        print('\033[7m \b', end='')
        sys.stdout.flush()
        sleep(.4)
        print('\033[m \b', end='')
        sys.stdout.flush()
        sleep(.4)
        n += 1


#CHAMA A NARRAÇÃO
def narrate(message, _should_clear=True, speaker=False, blink=False, *args, **kwargs):
    
    if _should_clear:
        cls()

    if speaker:
        print(f'\033[1;34m{speaker}:\033[m')
        sys.stdout.flush()
        
    composed_message = f'{message.format(*args, **kwargs)}' 
    for letter in composed_message:
        print_message_and_sleep(letter)

    if blink:
        blink_square(blink)

#ESPAÇO PARA TESTES
if __name__ == '__main__':

    # narrate('teste teste teste', speaker="Lola", blink=2)

    text = 'TESTANDO A PARADA AQUI'
    text_to_draw = str()
    for l in range(len(text)):
        cls()
        text_to_draw = text_to_draw + text[l]

        print(text_to_draw)