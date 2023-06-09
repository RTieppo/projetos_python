import sys
import os

from extras import cores
from funcoes import print_terminal as p
from funcoes import calcular

def inicia():

    p.inicial()

    while True:
        try:

            print(cores[2],'Escolha uma das opções acima [1,2,9,0]',cores[0], end='')

            escolha_user = int(input(': '))

            if escolha_user > 9:
                print(cores[1],'Erro entrada invalida!',cores[0])
            
            elif escolha_user == 1:
                
                opbasica = calcular.OpBasicas.basicas()
                if opbasica == True:
                    p.inicial()
            
            elif escolha_user == 2:
                opfact = calcular.OpBasicas.factor()

                if opfact == True:
                    p.inicial()

            elif escolha_user == 9:
                os.system('cls' if os.name == 'nt' else 'clear')
                p.inicial()

            elif escolha_user == 0:
                p.fim()
                sys.exit()

        
        except ValueError:
            print(cores[1],'Erro entrada invalida!',cores[0])
            print('-'*60)

if __name__ == '__main__':
    inicia()