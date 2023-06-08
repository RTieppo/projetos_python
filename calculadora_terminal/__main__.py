import sys
import os

from funcoes import print_terminal as p
from funcoes import calcular as cal
from funcoes import perguntas as pt


cores = ('\033[m', #0 - sem cor
        '\033[0;31m', #1 - vermelho
        '\033[0;32m', #2 - verde
        '\033[0;33m', #3 - amarelo
        )

def inicia():

    p.inicial()

    opbasicas = cal.OpBasicas

    while True:
        try:
            print(cores[2],'Escolha uma das opções acima [1,2,3,4,9,0]',cores[0], end='')

            escolha_user = int(input(': '))

            if escolha_user > 9:
                print(cores[1],'Erro entrada invalida!',cores[0])
            
            elif escolha_user == 1:
                resultado_soma = opbasicas.soma()
                print(cores[2],f'O resultado da sua Adição é {resultado_soma}',cores[0])

                perguntar = pt.psoma()
                
                if perguntar == True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    p.inicial()
                
                else:
                    p.fim()
                    sys.exit()

            elif escolha_user == 9:
                os.system('cls' if os.name == 'nt' else 'clear')
                p.inicial()

            elif escolha_user == 0:
                p.fim()
                sys.exit()

        
        except ValueError:
            print(cores[1],'Erro entrada invalida!',cores[0])

if __name__ == '__main__':
    inicia() 