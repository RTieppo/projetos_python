import sys
import os

from extras import cores,criatxt
from funcoes import print_terminal as p
from funcoes import calcular

def inicia():

    p.inicial()
    cria_txt = criatxt()

    while True:
        try:

            print('\033[0;31mEscolha uma das opções acima [1,2,3,4,5,8,9,0]\033[m', end='')
            escolha_user = int(input(': '))

            if escolha_user > 9:
                print(cores[1],'Erro entrada invalida!',cores[0])
            
            elif escolha_user == 1:
                opbasica = calcular.OpMatematicas.basicas()
                if opbasica == True:
                    p.inicial()
            
            elif escolha_user == 2:
                opconvert = calcular.OpMatematicas.convert()

                if opconvert == True:
                    p.inicial()

            elif escolha_user == 3:
                opfact = calcular.OpMatematicas.factor()

                if opfact == True:
                    p.inicial()
            
            elif escolha_user == 4:
                numcomplex = calcular.OpMatematicas.numcomplex()

                if numcomplex == True:
                    p.inicial()

            elif escolha_user == 5:
                opraiz = calcular.OpMatematicas.raiz()

                if opraiz == True:
                    p.inicial()

            elif escolha_user == 6:
                optabuada = calcular.OpMatematicas.tabuada()

                if optabuada == True:
                    p.inicial()

            
            elif escolha_user == 7:
                pass


            elif escolha_user == 8:
                
                if cria_txt == True:
                    abre_txt = open(r'C:\Users\Public\hist.txt', 'r', encoding='utf8').read()

                    if len(abre_txt) > 5:
                        print(f"{'Histórico':-^60}")
                        print(abre_txt)
                    
                    else:
                        print(cores[1],'Sem Histórico!',cores[0])
                        print('-'*60)

                else:
                    print(cores[1],'Sem Histórico!',cores[0])
                    print('-'*60)

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