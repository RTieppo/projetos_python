cores = ('\033[m', #0 - sem cor
        '\033[0;31m', #1 - vermelho
        '\033[0;32m', #2 - verde
        '\033[0;33m', #3 - amarelo
        )

def psoma():
    
    while True:
        try:
            continua = str(input('Realizar outra operação? [S/N]: ')).upper().strip()[0]

            if continua in 'SN':
                if continua == 'S':
                    return True

                else:
                    return False

            else:
                print(cores[1],'Erro entrada invalida!',cores[0])

        except ValueError:
            print(cores[1],'Erro entrada invalida!',cores[0])

        except IndexError:
            print(cores[1],'Erro entrada invalida!',cores[0])

        except TypeError:
            print(cores[1],'Erro entrada invalida!',cores[0])