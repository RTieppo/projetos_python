
from extras import cores

def inicial():
    print(f"{'Bem-vindo!':-^60}")
    print(f"{'Sou o Calculon o senhor das calculadoras':^60}")
    print('-'*60)
    print('[1] Adição | Subtração | Multiplicação | Divisão | Potência\n[2] Conversor de metros para MM | CM | DM | DAM | HM | KM\n[3] Fatorial de um número\n[4] Números Complexos\n[5] Raiz quadrada\n[6] Tabuada')
    print('-'*60)
    print('[8] Historico\n[9] Limpar\n[0] Exit')
    print('-'*60)

def fim():
    print('-'*60)
    print(f"{'Até a Proxima...':^60}")

def basicas():
    print(f"{'Calculando Fórmulas Básicas':-^60}")
    print('Exemplo de formula Básica:')
    print(cores[3],f"{'4/2*3+(4+6*2)+18/3-8':^60}",cores[0])
    print('Exemplo de formula Com Potência:')
    print(cores[3],f"{'4/2*3+(4+6*2)+18/3**2-8':>43}",cores[0])
    print('-'*60)

def factori():
    print(f"{'Calculando o fatorial':-^60}")
    print(f'Os valores a serem fatorados devem ser inteiros!')
    print('-'*60)

def ptabuada():
    print(f"{'Gerador de Tabuada':-^60}")
    print('Escolhar qualquer número interio para gerar a tabuada.')
    print('-'*60)

def praiz():
    print(f"{'Calculando a Raiz quadrada':-^60}")
    print('Lembrando que só podemos obter a raiz quadrada de um número\npositivo.')
    print('-'*60)

def conversor():
    print(f"{'Conversor de metros':-^60}")
    print('Exemplos de entradas:')
    print(cores[3],f"{'Para metros inteiro: 2':^60}",cores[0])
    print(cores[3],f"{'Para metros fracionados: 1.5 ou 0.5':>54}",cores[0])
    print('-'*60)

def numcomplexo():
    print(f"{'Números complexos':-^60}")
    print('Qual operação vai ser realizada?')
    print('[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potência')
    print('-'*60)
