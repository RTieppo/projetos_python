import os
from extras import cores
from funcoes import perguntas
from funcoes import print_terminal as p


class OpBasicas:
    
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

            except TypeError:
                print(cores[1],'Erro formula invalida!',cores[0])
    
    