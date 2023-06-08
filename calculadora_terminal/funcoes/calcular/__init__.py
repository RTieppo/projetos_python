
cores = ('\033[m', #0 - sem cor
        '\033[0;31m', #1 - vermelho
        '\033[0;32m', #2 - verde
        '\033[0;33m', #3 - amarelo
        )

class OpBasicas:
    def soma():
        valores = 0
        print('Informe a quantidade de números que deseja somar.\nPara finalizar a soma digite [0]')
        while True:
            try:
                entrada_user = float(input('Número: '))

                if entrada_user == 0:
                    return valores
                else:
                    valores += entrada_user

            except ValueError:
                print(cores[1],'Erro entrada invalida!',cores[0])