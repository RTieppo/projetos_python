import os
from math import factorial
from extras import cores
from funcoes import perguntas
from funcoes import print_terminal as p


class OpMatematicas:
    
    def basicas():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.basicas()

        while True:
            try:
                entrada = input('Digite a sua conta ou fórmula: ')

                print(cores[2],f'O resultado da sua conta é {eval(entrada)}',cores[0])
                print('-'*60)
                perguntar = perguntas.pbasicas()

                if perguntar == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True
                
                else:
                    print('-'*60)
                    continue

            
            except SyntaxError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)

            except TypeError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)
    
    def factor():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.factori()

        while True:
            try:
                entrada = int(input('Qual Nº você quer fatorar? '))

                while True:
                    try:
                        calculo = str(input('Gostaria de ver o calculo? [S/N] ')).upper().strip()[0]

                        if calculo in 'SN':

                            if calculo == 'S':
                                multiplicador = 1
                                for num in range(entrada, 0, -1):
                                    print(cores[2],f'{num}', end=' ')
                                    if num != 1:
                                        print('x', end='')
                                    multiplicador *= num
                                print(f'= {multiplicador}',cores[0])
                                print('-'*60)

                                perguntar = perguntas.pbasicas()

                                if perguntar == False:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    return True
                                
                                else:
                                    print('-'*60)
                                    continue

                            else:
                                print(cores[2],f'O resultado da sua conta é {factorial(entrada)}',cores[0])
                                print('-'*60)
                                perguntar = perguntas.pbasicas()

                                if perguntar == False:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    return True
                                
                                else:
                                    print('-'*60)
                                    continue
                        
                        else:
                            print(cores[1],'Erro entradas invalidas!',cores[0])
                            print('-'*60)

                    except IndexError:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)


            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)
    
    def tabuada():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.tabuada()

        while True:

            try:
                entrada = int(input('Qual tabuada você deseja gerar? '))

                for num in range(11):
                    print(f"{entrada:^2} x {num:^4} = ", end='')
                    print(cores[2],f"{entrada*num}",cores[0])
                
                perguntar = perguntas.pbasicas()

                if perguntar == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True
                
                else:
                    print('-'*60)
                    continue

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

