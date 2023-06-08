
from extras import cores

class OpBasicas:
    
    def basicas():
        while True:
            try:
                entrada = input('Digite a sua conta ou formula: ')
                return eval(entrada)
            
            except SyntaxError:
                print(cores[1],'Erro formula invalida!',cores[0])

            except TypeError:
                print(cores[1],'Erro formula invalida!',cores[0])