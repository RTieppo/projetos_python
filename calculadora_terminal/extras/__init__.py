cores = ['\033[m', #0 - sem cor
        '\033[0;31m', #1 - vermelho
        '\033[0;32m', #2 - verde
        '\033[0;33m', #3 - amarelo
        ]

def criatxt():

        try:
                with open(r'C:\Users\Public\hist.txt', 'w', encoding='utf8') as cria_txt:
                        cria_txt.write('')
                        return True

        except Exception:
                return False

def gravahist(text):
        
        try:
                with open(r'C:\Users\Public\hist.txt', 'a', encoding='utf8') as txt:
                        txt.write(text)

        
        except Exception as erro:
                print(erro)