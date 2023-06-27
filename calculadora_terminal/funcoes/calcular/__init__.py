import os
import re
from math import factorial, sqrt
from extras import cores,gravahist
from funcoes import perguntas
from funcoes import print_terminal as p

analise = re.compile(r"(-?(?:0|[1-9]\d*)(?:\.\d+)?)")

class OpMatematicas:

    def basicas():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.basicas()

        while True:
            try:
                entrada = input('Digite a sua conta ou fórmula: ')

                if entrada in "ls":
                    
                    if entrada == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.basicas()
                        continue

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True

                else:
                    resultado = eval(entrada)

                    print(cores[2],f'O resultado da sua conta é {resultado}',cores[0])
                    print('-'*60)

                    gravahist(f'A sua conta foi: {entrada}\n')
                    gravahist(f'O resultado da sua conta é {resultado}\n')
                    gravahist(f"{'-'*60}\n")

            
            except SyntaxError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)

            except TypeError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)
            
            except ZeroDivisionError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)
            
            except NameError:
                print(cores[1],'Erro formula invalida!',cores[0])
                print('-'*60)
    
    def factor():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.factori()

        while True:
            try:
                entrada = input('Qual Nº você quer fatorar? ')

                if entrada in "ls":
                    
                    if entrada == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.factori()

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True
                
                else:
                    if entrada.isnumeric():
                        while True:
                            try:
                                calculo = str(input('Gostaria de ver o calculo? [S/N] ')).upper().strip()[0]

                                if calculo in 'SN':
                                    gravahist(f'Nº fatorado: {entrada}\n')

                                    if calculo == 'S':
                                        multiplicador = 1
                                        print('-'*60)
                                        print('O resultado da sua fatoração é:')
                                        gravahist('O resultado da sua fatoração é:')

                                        for num in range(int(entrada), 0, -1):
                                            print(cores[2],f'{num}', end=' ')
                                            gravahist(f'{num}')
                                            if num != 1:
                                                print('x', end='')
                                                gravahist('x')
                                            multiplicador *= num
                                        
                                        gravahist(f'={multiplicador}\n')
                                        gravahist(f"{'-'*60}\n")

                                        print(f'= {multiplicador}',cores[0])
                                        print('-'*60)
                                        break

                                    else:
                                        gravahist(f'O resultado da sua conta é {factorial(int(entrada))}\n')
                                        gravahist(f"{'-'*60}\n")

                                        print(cores[2],f'O resultado da sua conta é {factorial(int(entrada))}',cores[0])
                                        print('-'*60)
                                        break
                                
                                else:
                                    print(cores[1],'Erro entradas invalidas!',cores[0])
                                    print('-'*60)

                            except IndexError:
                                print(cores[1],'Erro entrada invalida!',cores[0])
                                print('-'*60)
                    else:
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

                entrada = input('Qual tabuada você deseja gerar? ')

                if analise.match(entrada):
                    
                    gravahist(f'Tabuada do {entrada}\n')

                    for num in range(11):

                        gravahist(f"{entrada:^2} x {num:^4} = ")
                        gravahist(f"{float(entrada)*num}\n")

                        print(f"{entrada:^2} x {num:^4} = ", end='')
                        print(cores[2],f"{float(entrada)*num}",cores[0])
                    
                    gravahist(f"{'-'*60}\n")
                    print('-'*60)

                elif entrada in "ls ":
                    
                    if entrada == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.ptabuada()
                    
                    elif entrada == 's':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True

                    else:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)
                
                else:
                    print(cores[1],'Erro entrada invalida!',cores[0])
                    print('-'*60)

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def raiz():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.praiz()

        while True:
            try:

                entrada = input("Vamos calcular a raiz de qual número? ")

                if entrada in "ls":
                    
                    if entrada == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.praiz()

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True
                
                else:

                    convert = entrada.split('.')
                    if convert[0].isnumeric():

                        gravahist(f"A Raiz quadrada de {entrada} é {sqrt(float(entrada))}\n")
                        gravahist(f"{'-'*60}\n")
                        
                        print(cores[2],f"A Raiz quadrada de {entrada} é {sqrt(float(entrada))}",cores[0])
                        print('-'*60)
                    
                    else:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)


            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def convert():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.conversor()

        while True:
            try:
                entrada = input('Quantos metros gostaria de converter? ')

                if entrada in "ls":
                    
                    if entrada == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.conversor()

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True
                
                else:
                    convert = entrada.split('.')
                    if convert[0].isnumeric():
                        gravahist(f"A conversão de {entrada}M para mm é {float(entrada)*1000};\n")
                        gravahist(f"A conversão de {entrada}M para cm é {float(entrada)*100};\n")
                        gravahist(f"A conversão de {entrada}M para dm é {float(entrada)*10};\n")
                        gravahist(f"A conversão de {entrada}M para dam é {float(entrada)/10};\n")
                        gravahist(f"A conversão de {entrada}M para hm é {float(entrada)/100};\n")
                        gravahist(f"A conversão de {entrada}M para km é {float(entrada)/1000}.\n")
                        gravahist(f"{'-'*60}\n")

                        print(cores[2],end='')
                        print(f"A conversão de {entrada}M para mm é {float(entrada)*1000};")
                        print(f"A conversão de {entrada}M para cm é {float(entrada)*100};")
                        print(f"A conversão de {entrada}M para dm é {float(entrada)*10};")
                        print(f"A conversão de {entrada}M para dam é {float(entrada)/10};")
                        print(f"A conversão de {entrada}M para hm é {float(entrada)/100};")
                        print(f"A conversão de {entrada}M para km é {float(entrada)/1000}.",cores[0])
                        print('-'*60)
                    
                    else:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)


            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def numcomplexpt2(escolha_user):
        
        while True:

            num1 = input('Primeira entrada:')
                
            if num1 in 'ls ':

                if num1 == 'l':
                    return '-limpa-'
                
                elif num1 == 's':
                    return '-sair-'
                                
                else:
                    print(cores[1],'Erro entrada invalida!',cores[0])
                    print('-'*60)
            
            elif analise.match(num1):
                while True:

                    try:
                        num2 = input('Segunda entrada:')

                        if num2 in 'ls ':

                            if num2 == 'l':
                                return '-limpa-'
                            
                            elif num2 == 's':
                                return '-sair-'
                            
                            else:
                                print(cores[1],'Erro entrada invalida!',cores[0])
                                print('-'*60)
                            
                        elif analise.match(num2):

                            num1 = complex(num1)
                            num2 = complex(num2)

                            if escolha_user == 1:

                                gravahist(f"Números somados {num1} + {num2}:\n")
                                gravahist(f"O resultado da sua soma é {str(num1 + num2)[1:-1]}\n")
                                gravahist(f"{'-'*60}\n")

                                print(cores[2],f"O resultado da sua soma é {str(num1 + num2)[1:-1]}",cores[0])
                                print('-'*60)
                                return True
                            
                            elif escolha_user == 2:

                                gravahist(f"Números subtraídos {num1} - {num2}:\n")
                                gravahist(f"O resultado da sua Subtração é {str(num1 - num2)[1:-1]}\n")
                                gravahist(f"{'-'*60}\n")

                                print(cores[2],f"O resultado da sua Subtração é {str(num1 - num2)[1:-1]}",cores[0])
                                print('-'*60)
                                return True

                            elif escolha_user == 3:
                                
                                gravahist(f"Números Multiplicados {num1} * {num2}:\n")
                                gravahist(f"O resultado da sua Multiplicação é {str(num1 * num2)[1:-1]}\n")
                                gravahist(f"{'-'*60}\n")

                                print(cores[2],f"O resultado da sua Multiplicação é {str(num1 * num2)[1:-1]}",cores[0])
                                print('-'*60)
                                return True

                            elif escolha_user == 4:

                                gravahist(f"Números Divididos {num1} + {num2}:\n")
                                gravahist(f"O resultado da sua Divisão é {str(num1 / num2)[1:-1]}\n")
                                gravahist(f"{'-'*60}\n")

                                print(cores[2],f"O resultado da sua Divisão é {str(num1 / num2)[1:-1]}",cores[0])
                                print('-'*60)
                                return True

                            elif escolha_user == 5:

                                gravahist(f"Potência dos números {num1} + {num2}:\n")
                                gravahist(f"O resultado da sua Potência é {str(num1 ** num2)[1:-1]}\n")
                                gravahist(f"{'-'*60}\n")

                                print(cores[2],f"O resultado da sua Potência é {str(num1 ** num2)[1:-1]}",cores[0])
                                print('-'*60)
                                return True
                        
                        else:
                            print(cores[1],'Erro entrada invalida!',cores[0])
                            print('-'*60)
                    
                    except ValueError:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)

    def numcomplex():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.numcomplexo()

        while True:
            try:
                print(cores[2],'Escolha uma das opções acima [1,2,3,4,5]',cores[0], end='')
                escolha_user = input(': ')

                if escolha_user in 'ls ':

                    if escolha_user == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.numcomplexo()

                    elif escolha_user == 's':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True
                    
                    else:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)
                    
                
                elif escolha_user.isnumeric():
                    escolha_user = int(escolha_user)

                    if escolha_user > 5:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)
                    
                    else:
                        print('Exemplos de entradas:')
                        print(cores[3],f"{'3+5j':>24}",cores[0])
                        print('-'*60)

                        opera_pt2 = OpMatematicas.numcomplexpt2(escolha_user=escolha_user)

                        if opera_pt2 == '-limpa-':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            p.numcomplexo()
                        
                        elif opera_pt2 == '-sair-':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            return True
                        
                        else:
                            p.numcomplexo()
                            continue
                        
            
                else:
                    print(cores[1],'Erro entrada invalida!',cores[0])
                    print('-'*60)

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)

    def hipot():
        os.system('cls' if os.name == 'nt' else 'clear')
        p.hipotnu()

        while True:
            try:
                co = input('Entre com o valor do cateto oposto: ')

                if co in 'ls ':
                    if co == 'l':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        p.hipotnu()

                    elif co == 's':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return True
                    
                    else:
                        print(cores[1],'Erro entrada invalida!',cores[0])
                        print('-'*60)
                    
                elif co[0].isnumeric():

                    while True:
                        ca = input('Entre com o valor do cateto adjacente: ')

                        if ca in 'ls ':

                            if ca == 'l':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                p.hipotnu()
                                break

                            elif ca == 's':
                                
                                os.system('cls' if os.name == 'nt' else 'clear')
                                return True
                            
                            else:
                                print(cores[1],'Erro entrada invalida!',cores[0])
                                print('-'*60)
                    
                        elif ca[0].isnumeric():
                                
                                gravahist(f"cateto oposto:{co}\ncateto adjacente:{ca}\n")
                                gravahist(f'A hipotenusa é {(float(ca)**2 + float(co)**2)**(1/2)}\n')
                                gravahist(f"{'-'*60}\n")


                                print(cores[2],f'A hipotenusa é {(float(ca)**2 + float(co)**2)**(1/2)}',cores[0])
                                print('-'*60)
                                break
                        

                        else:
                            print(cores[1],'Erro entrada invalida!',cores[0])
                            print('-'*60)
                    
                else:
                    print(cores[1],'Erro entrada invalida!',cores[0])
                    print('-'*60)


            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)
            
            except UnboundLocalError:
                print(cores[1],'Erro entrada invalida!',cores[0])
                print('-'*60)