import sys
import os

from extras import cores
from funcoes import print_terminal as p
from funcoes import calcular
from funcoes import perguntas 

def inicia():

    p.inicial()

    while True:
        try:
            print(cores[2],'Escolha uma das opções acima [1,9,0]',cores[0], end='')

            escolha_user = int(input(': '))

            if escolha_user > 9:
                print(cores[1],'Erro entrada invalida!',cores[0])
            
            elif escolha_user == 1:
                resultado_soma = calcular.OpBasicas.basicas()

                print(cores[2],f'O resultado da sua conta é {resultado_soma}',cores[0])

                perguntar = perguntas.pbasicas()
                
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