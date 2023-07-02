import re
from PySimpleGUI import PySimpleGUI as sg


#Definindo tema geral
tema_g = 'DarkBlue2'
tema_erro = 'DarkRed2'

#Define fonte


#Base de comparação
analise_caminho = re.compile(r'^[A-Za-z]:(?:/|\\)(?:[\w-]+(?:/|\\))*[\w-]+(?:\.\w+)?$')

def dir_music(tema=None,titulo = 'Escolha o local das Musicas.'):
    
    try:
        if tema == None:
            sg.theme(tema_g)
        
        else:
            sg.theme(tema_erro)

        dir = sg.popup_get_folder(titulo,icon=r'play_musica\img\icon\botoes.ico')

        if dir == '':
            return False
        
        elif dir == None:
            return '-break-'
        
        elif analise_caminho.match(dir):
            return dir 
        
        else:
            return False

    except Exception as erro:
        print(erro)

