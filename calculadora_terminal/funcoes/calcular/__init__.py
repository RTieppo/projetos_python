import os
from math import factorial, sqrt
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
                    limpeza = perguntas.limp()

                    if limpeza == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.basicas()
                        continue
                    
                    else:

                        print('-'*60)
                        continue

            
            except SyntaxError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)

            except TypeError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)
            
            except ZeroDivisionError:
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
                                    limpeza = perguntas.limp()

                                    if limpeza == True:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        p.factori()
                                        break
                                    
                                    else:
                                        print('-'*60)
                                        break

                            else:
                                print(cores[2],f'O resultado da sua conta é {factorial(entrada)}',cores[0])
                                print('-'*60)
                                perguntar = perguntas.pbasicas()

                                if perguntar == False:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    return True
                                
                                else:
                                    limpeza = perguntas.limp()

                                    if limpeza == True:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        p.factori()
                                        break
                                    
                                    else:
                                        print('-'*60)
                                        break
                        
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
        p.ptabuada()

        while True:

            try:
                entrada = int(input('Qual tabuada você deseja gerar? '))

                for num in range(11):
                    print(f"{entrada:^2} x {num:^4} = ", end='')
                    print(cores[2],f"{entrada*num}",cores[0])
                
                print('-'*60)
                perguntar = perguntas.pbasicas()

                if perguntar == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True
                
                else:
                    limpeza = perguntas.limp()
                    if limpeza == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.ptabuada()
                        continue
                    
                    else:

                        print('-'*60)
                        continue

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def raiz():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.praiz()

        while True:

            try:
                entrada = float(input("Vamos calcular a raiz de qual número? "))
                print(cores[2],f"A Raiz quadrada de {entrada} é {sqrt(entrada)}",cores[0])
                print('-'*60)

                perguntar = perguntas.pbasicas()

                if perguntar == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True
                
                else:
                    limpeza = perguntas.limp()
                    if limpeza == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.praiz()
                        continue
                    else:
                        print('-'*60)
                        continue


            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def convert():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.conversor()

        while True:
            try:
                entrada = float(input('Quantos metros gostaria de converter? '))
                print(cores[2],end='')
                print(f"A conversão de {entrada}M para mm é {entrada*1000};")
                print(f"A conversão de {entrada}M para cm é {entrada*100};")
                print(f"A conversão de {entrada}M para dm é {entrada*10};")
                print(f"A conversão de {entrada}M para dam é {entrada/10};")
                print(f"A conversão de {entrada}M para hm é {entrada/100};")
                print(f"A conversão de {entrada}M para km é {entrada/1000}.",cores[0])
                print('-'*60)

                perguntar = perguntas.pbasicas()

                if perguntar == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True
                
                else:
                    limpeza = perguntas.limp()
                    if limpeza == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.conversor()
                    
                    else:
                        print('-'*60)
                        continue

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def numcomplex():
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            try:
                p.numcomplexo()
                print(cores[2],'Escolha uma das opções acima [1,2,3,4,5]',cores[0], end='')
                escolha_user = int(input(': '))

                if escolha_user > 5:
                    print(cores[1],'Erro entrada invalida!',cores[0])
                    print('-'*60)
                
                else:
                    while True:
                        try:
                            print('-'*60)
                            print('Exemplos de entradas:')
                            print(cores[3],f"{'3+5j':>24}",cores[0])
                            print('-'*60)
                            
                            num1 = complex(input('Primeira entrada:'))

                            while True:
                                try:
                                    num2 = complex(input('Segunda entrada:'))
                                    break

                                except ValueError:
                                    print(cores[1],'Erro entrada invalida!',cores[0])
                                    print('-'*60)

                            if escolha_user == 1:

                                print(cores[2],f"O resultado da sua soma é {str(num1 + num2)[1:-1]}",cores[0])
                                print('-'*60)
                                break
                            
                            elif escolha_user == 2:

                                print(cores[2],f"O resultado da sua Subtração é {str(num1 - num2)[1:-1]}",cores[0])
                                print('-'*60)
                                break
                            elif escolha_user == 3:

                                print(cores[2],f"O resultado da sua Multiplicação é {str(num1 * num2)[1:-1]}",cores[0])
                                print('-'*60)
                                break

                            elif escolha_user == 4:

                                print(cores[2],f"O resultado da sua Divisão é {str(num1 / num2)[1:-1]}",cores[0])
                                print('-'*60)
                                break

                            elif escolha_user == 5:

                                print(cores[2],f"O resultado da sua Potência é {str(num1 ** num2)[1:-1]}",cores[0])
                                print('-'*60)
                                break
                        
                        except ValueError:
                            print(cores[1],'Erro entrada invalida!',cores[0])

                    perguntar = perguntas.pbasicas()
                    
                    if perguntar == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True
                    
                    else:
                        limpeza = perguntas.limp()
                        if limpeza == True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            continue
                        
                        else:
                            print('-'*60)
                            continue

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
