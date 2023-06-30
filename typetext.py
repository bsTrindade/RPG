#FUNÇÃO PARA MOSTRAR TEXTO DE FORMA NARRATIVA
import os
from time import sleep

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