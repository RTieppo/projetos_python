
from extras import cores

def inicial():
    print(f"{'Bem-vindo!':-^60}")
    print(f"{'Sou o Calculon o senhor das calculadoras':^60}")
    print('-'*60)
    print(f"{'Operações Basicas:'}")
    print('[1] Adição | Subtração | Multiplicação | Divisão | Potência\n[2] Fatorial de um número\n[3] Raiz quadrada\n[4] Tabuada')
    print('-'*60)
    print('[9] Limpar\n[0] Exit')
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