from extras import cores

def pbasicas():
    
    while True:
        try:
            continua = str(input('Gostaria de fazer outra? [S/N]: ')).upper().strip()[0]

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

def limp():

    while True:
        try:
            limpar = str(input('Gostaria de limpar o terminal? [S/N]: ')).upper().strip()[0]

            if limpar in 'SN':
                if limpar == 'S':
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