import re
import os

from pygame import mixer
from PySimpleGUI import PySimpleGUI as sg

#Definindo tema geral
tema_g = 'DarkBlue2'
tema_erro = 'DarkRed2'

#Base de comparação
analise_caminho = re.compile(r'^[A-Za-z]:(?:/|\\)(?:[\w.-]+(?:/|\\))*[\w.-]+(?:\.\w+)?$')

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

def dir_img():
    lista_img = os.listdir(r'.\play_musica\img\display')
    return lista_img

def altera_display(window,img):

    altera = f'.\play_musica\img\display\{img}'
    window['-display_img-'].update(altera)



def caminho_music(caminho_geral):
    musicas = list()

    for (root, dirs, files) in os.walk(caminho_geral):
        for file in files:
            musicas.append(root + os.sep + file)
    return musicas

def info_display(window,musica,posicao):
    nome_base = os.path.basename(musica[posicao])
    convert = nome_base.split('-')
    artista = convert[1].split('.')
    window['-name_music-'].update(convert[0])
    window['-artista-'].update(artista[0])

def tempo_music(window,musica):
    
    musica = mixer.Sound(musica)

    duracao_musica = int(musica.get_length())
    minuto = duracao_musica//60
    segundos = duracao_musica%60

    if segundos < 10:
        segundos = f'0{segundos}'

    window['-tempo_total-'].update(f'{minuto}:{segundos}')

def ajuste_barra(window,tempo):

    musica = mixer.Sound(tempo)

    duracao_musica = int(musica.get_length())
    
    window['-progress-'].update(current_count= 0, max=duracao_musica)

def tocando():
    if mixer.music.get_busy() == True:
        return True
    return False

def play_music(pasta_sound):
    mixer.music.load(pasta_sound)
    mixer.music.play()

def pause_music():
    mixer.music.pause()
